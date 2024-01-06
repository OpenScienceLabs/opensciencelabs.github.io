{% extends 'markdown/index.md.j2'%}
{% block data_text %}
<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>{{ super().split('\n') | map('trim') | join('\n') }}</span></code>
</pre>
</div>
{% endblock data_text %}

{% block data_html %}
{{ super().split('\n') | map('trim') | join('\n') }}
{% endblock data_html %}


{% block stream %}
<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>{{ super().split('\n') | map('trim') | join('\n') }}</span></code>
</pre>
</div>
{% endblock stream %}
