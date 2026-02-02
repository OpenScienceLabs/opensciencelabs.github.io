---
title: "Working with Boolean Expressions in Python"
slug: "working-with-boolean-expressions-in-python"
date: 2024-01-31
authors: ["Ivan Ogasawara"]
tags: ["boolean expressions", "boolean", "python"]
categories: ["devops", "automation", "python"]
description: |
  Boolean logic is a crucial component in many programming tasks, especially
  in searching and querying data. In this tutorial, we'll explore how to use boolean.py,
  a Python library, for handling Boolean expressions. 
  We'll apply it to medical symptom data as an illustrative example.
thumbnail: "/header.png"
template: "blog-post.html"
---
# Working with Boolean Expressions in Python

Boolean logic is a crucial component in many programming tasks, especially in searching and querying data. In this tutorial, we'll explore how to use `boolean.py`, a Python library, for handling Boolean expressions. We'll apply it to medical symptom data as an illustrative example.

## Introduction to `boolean.py`

`boolean.py` is a Python library for creating, manipulating, and evaluating Boolean expressions. It's particularly useful in scenarios where you need to parse and evaluate expressions that represent conditions or filters, such as searching for specific symptoms in a medical database.

## Installation

First and foremost, you need to have `boolean.py` installed in your Python environment. You can easily install it using pip. Run the following command:


```python
!pip install -q boolean.py
```

## Basic Usage

We begin with basic Boolean operations, which are the foundation of working with this library.

### Creating Boolean Variables


```python
import boolean

from boolean.boolean import BooleanAlgebra

# Create a Boolean algebra system
algebra = BooleanAlgebra()

# Define some symptoms as variables
fever = algebra.Symbol('fever')
cough = algebra.Symbol('cough')

fever, cough
```




<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
(Symbol('fever'), Symbol('cough'))
</span></code>
</pre>
</div>



In this code, we import `BooleanAlgebra` from `boolean.py` and create an instance of it. We then define Boolean variables (symbols) for common symptoms. These symbols act as the basic units for our Boolean expressions.


### Basic Boolean Operations


```python
# AND operation
symptoms_and = fever & cough
print(symptoms_and)

# OR operation
symptoms_or = fever | cough
print(symptoms_or)

# NOT operation
no_fever = ~fever
print(no_fever)
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
fever&cough
fever|cough
~fever

</span></code>
</pre>
</div>

Here, we demonstrate basic Boolean operations: AND, OR, and NOT. These operations are essential in constructing more complex Boolean expressions. For example, `symptoms_and` represents a scenario where a patient has both fever and cough.

## Advanced Expressions

Now, let's create more complex expressions that could simulate queries for medical symptoms.

### Complex Expressions


```python
headache = algebra.Symbol('headache')
fatigue = algebra.Symbol('fatigue')

# Complex expression
complex_symptoms = (fever | cough) & ~headache & fatigue
print(complex_symptoms)
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
((fever|cough)&~headache)&fatigue

</span></code>
</pre>
</div>

This complex expression can represent a more specific medical query. For instance, it could be used to find patients who have either fever or cough, do not have a headache, but are experiencing fatigue.

### Evaluating Expressions

We can evaluate these expressions with specific values to simulate checking a patient's symptoms against our criteria.


```python
# Define truthy and falsy symbols
true = algebra.TRUE
false = algebra.FALSE

# Define complex expression
complex_symptoms = (fever | cough) & ~headache & fatigue

# Define a patient's symptoms using truthy and falsy symbols
patient_symptoms = {fever: true, cough: false, headache: false, fatigue: true}

# Substitute symbols in the expression with the corresponding patient symptoms
substituted_expression = complex_symptoms.subs(patient_symptoms)

# Evaluate the expression
# The expression itself is the result since boolean.py does not evaluate to Python booleans
result = substituted_expression

print("Does the patient match the criteria?", result, "=", result.simplify() == true)

```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
Does the patient match the criteria? (((1)|(0))&(~(0)))&(1) = True

</span></code>
</pre>
</div>

In this example, we demonstrate how to evaluate a Boolean expression against a set of patient symptoms. We use `.subs()` to replace each symbol in our expression with the corresponding value (symptom presence) from `patient_symptoms`. The `.simplify()` method then evaluates this substituted expression to a Boolean value, indicating whether the patient's symptoms match our query criteria.


## Parsing Expressions from Strings

Lastly, we explore parsing Boolean expressions from strings, a powerful feature for dynamic expression construction.

### Parsing Example


```python
expression_string = "(fever | cough) & ~headache & fatigue"

# Parse the expression from string
parsed_expression = algebra.parse(expression_string)

# Display the parsed expression
print("parsed expression:", parsed_expression)

# Evaluate with the same patient symptoms
result = parsed_expression.subs(patient_symptoms)
print(f"Does the patient match the criteria? {result.simplify() == true}")
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
parsed expression: (fever|cough)&~headache&fatigue
Does the patient match the criteria? True

</span></code>
</pre>
</div>

Parsing expressions from strings is extremely useful when you need to construct Boolean expressions dynamically, such as from user inputs or configuration files. In this example, we parse a string representing a Boolean expression and then evaluate it as before.


```python
expression_string = '(fever | "blood cough") & ~headache & fatigue'

# Parse the expression from string
try:
    parsed_expression = algebra.parse(expression_string)
except boolean.ParseError as e:
    print("[EE]", str(e))
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
[EE] Unknown token for token: """ at position: 9

</span></code>
</pre>
</div>

The string parser doesn't work with complex strings directly, but creating a manual symbol for the disease works fine.


```python
blood_cough = boolean.Symbol("blood cough")

chest_infection = blood_cough & fever

print("=" * 80)
print("patient without fever")
chest_infection_patient_symptoms = {blood_cough: true, fever: false}
result = chest_infection.subs(chest_infection_patient_symptoms)
print(f"Does the patient match the criteria? {result.simplify() == true}")

print("=" * 80)
print("patient with all symptoms")
chest_infection_patient_symptoms = {blood_cough: true, fever: true}
result = chest_infection.subs(chest_infection_patient_symptoms)
print(f"Does the patient match the criteria? {result.simplify() == true}")
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
================================================================================
patient without fever
Does the patient match the criteria? False
================================================================================
patient with all symptoms
Does the patient match the criteria? True

</span></code>
</pre>
</div>

## Conclusion

Throughout this tutorial, we have explored how to use `boolean.py` for handling and evaluating Boolean expressions in Python. By starting from basic operations and moving to parsing expressions from strings, we've covered a range of functionalities provided by this library. While we focused on a medical context, the principles and methods are broadly applicable across different domains.
