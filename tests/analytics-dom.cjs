/* Minimal DOM harness for behavior tests, NOT browser/layout verification. */
const vm = require("node:vm");
const fs = require("node:fs");
const model = require("../theme/js/analytics-model.js");
function setup(fixture = "tests/fixtures/analytics-explorer.json") {
  let document;
  class Node {
    constructor(tag, attrs = {}, nodes = []) {
      this.tagName = tag;
      this.attrs = attrs;
      this.nodes = [];
      this.listeners = {};
      this.style = {};
      this.dataset = new Proxy(
        {},
        {
          get: (_, key) =>
            this.attrs[
              "data-" + key.replace(/[A-Z]/g, (x) => "-" + x.toLowerCase())
            ],
          set: (_, key, value) => {
            this.attrs[
              "data-" + key.replace(/[A-Z]/g, (x) => "-" + x.toLowerCase())
            ] = String(value);
            return true;
          },
        },
      );
      this.classList = {
        add: (name) => {
          this.attrs.class = [this.attrs.class || "", name].join(" ");
        },
      };
      this.append(...nodes);
    }
    append(...nodes) {
      nodes.forEach((node) => {
        if (node instanceof Node) node.parentElement = this;
        this.nodes.push(node);
      });
    }
    replaceChildren(...nodes) {
      this.nodes = [];
      this.append(...nodes);
    }
    remove() {
      this.parentElement.nodes = this.parentElement.nodes.filter(
        (node) => node !== this,
      );
    }
    get textContent() {
      return this.nodes
        .map((node) => (node instanceof Node ? node.textContent : node))
        .join("");
    }
    set textContent(value) {
      this.nodes = [String(value)];
    }
    get className() {
      return this.attrs.class || "";
    }
    set className(value) {
      this.attrs.class = value;
    }
    get dateTime() {
      return this.attrs.datetime;
    }
    get value() {
      return this._value ?? this.attrs.value ?? "";
    }
    set value(value) {
      this._value = String(value);
    }
    get hidden() {
      return Object.hasOwn(this.attrs, "hidden");
    }
    set hidden(value) {
      if (value) this.attrs.hidden = "";
      else delete this.attrs.hidden;
    }
    get disabled() {
      return Object.hasOwn(this.attrs, "disabled");
    }
    set disabled(value) {
      if (value) this.attrs.disabled = "";
      else delete this.attrs.disabled;
    }
    get checked() {
      return Object.hasOwn(this.attrs, "checked");
    }
    set checked(value) {
      if (value) this.attrs.checked = "";
      else delete this.attrs.checked;
    }
    get options() {
      return this.querySelectorAll("option");
    }
    setAttribute(key, value) {
      this.attrs[key] = String(value);
    }
    getAttribute(key) {
      return this.attrs[key] ?? null;
    }
    removeAttribute(key) {
      delete this.attrs[key];
    }
    matches(selector) {
      const tag = selector.match(/^[\w-]+/);
      if (tag && tag[0] !== this.tagName) return false;
      const id = selector.match(/#([\w-]+)/);
      if (id && this.attrs.id !== id[1]) return false;
      const cls = selector.match(/\.([\w-]+)/);
      if (cls && !this.className.split(" ").includes(cls[1])) return false;
      for (const match of selector.matchAll(/\[([\w-]+)(?:="([^"]*)")?\]/g))
        if (
          !Object.hasOwn(this.attrs, match[1]) ||
          (match[2] != null && this.attrs[match[1]] !== match[2])
        )
          return false;
      return true;
    }
    querySelectorAll(selector) {
      const tokens = selector.split(/\s+/);
      let scopes = [this];
      for (const token of tokens) {
        const results = [];
        function walk(node) {
          for (const child of node.nodes)
            if (child instanceof Node) {
              if (child.matches(token)) results.push(child);
              walk(child);
            }
        }
        scopes.forEach(walk);
        scopes = [...new Set(results)];
      }
      return scopes;
    }
    querySelector(selector) {
      return this.querySelectorAll(selector)[0] || null;
    }
    closest(selector) {
      return this.matches(selector)
        ? this
        : this.parentElement?.closest(selector);
    }
    addEventListener(type, fn) {
      (this.listeners[type] ||= []).push(fn);
    }
    dispatch(type, extras = {}) {
      const event = { target: this, preventDefault() {}, ...extras };
      let node = this;
      while (node) {
        (node.listeners[type] || []).forEach((fn) => fn(event));
        node = node.parentElement;
      }
      this["on" + type]?.(event);
    }
    click() {
      if (!this.disabled) this.dispatch("click");
    }
    focus() {
      document.activeElement = this;
    }
    getBoundingClientRect() {
      return { left: 0, width: 900 };
    }
  }
  const raw = JSON.parse(
    fs.readFileSync(".cache/analytics-dom-fixtures.json", "utf8"),
  )[fixture];
  if (!raw) throw new Error("Run python tests/render_analytics_dom.py first");
  const make = (raw) =>
    typeof raw === "string"
      ? raw
      : new Node(raw.tag, raw.attrs, raw.nodes.map(make));
  document = make(raw);
  document.createElement = (tag) => new Node(tag);
  document.createElementNS = (_, tag) => new Node(tag);
  document.getElementById = (id) => document.querySelector("#" + id);
  const blobs = [],
    timers = [],
    events = {};
  const context = {
    OSLAnalytics: model,
    document,
    Date,
    Intl,
    Object,
    JSON,
    String,
    Number,
    Math,
    Blob,
    URL: {
      createObjectURL: (blob) => {
        blobs.push(blob);
        return "blob:fixture";
      },
      revokeObjectURL() {},
    },
    window: {
      setInterval: (fn) => timers.push(fn),
      addEventListener: (key, fn) => {
        events[key] = fn;
      },
    },
    history: { replaceState() {} },
    location: { hash: "" },
    setTimeout: (fn) => fn(),
  };
  vm.runInNewContext(fs.readFileSync("theme/js/analytics.js", "utf8"), context);
  return {
    document,
    blobs,
    timers,
    events,
    $: (selector) => document.querySelector(selector),
    $$: (selector) => document.querySelectorAll(selector),
  };
}
module.exports = setup;
