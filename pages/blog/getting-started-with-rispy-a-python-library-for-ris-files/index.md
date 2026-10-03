# Blog Post: Getting Started with rispy - A Python Library for RIS Files

## Introduction

In the world of academic research and literature management, dealing with bibliographic data is a common task. One of the formats used for exporting and handling such data is RIS (Research Information System Format), which is a standardized tag format used by digital libraries. Managing these RIS files can be a daunting task, but thanks to Python libraries like Rispy, this process becomes much more manageable. In this blog post, we'll explore how to use rispy to handle RIS files effectively.

Note: The pronunciation is rispee, like "crispy", but without the c.

## What is rispy?

Rispy is a Python library designed to parse and handle bibliographic data in RIS format. Developed by MrTango, it simplifies the process of reading and writing RIS files, making it an indispensable tool for researchers and developers working in academic environments. *rispy* is open-source and can be found on GitHub: [rispy on GitHub](https://github.com/MrTango/rispy).

## Installation

Before we dive into the usage of Rispy, the first step is to install the library. This can be easily done using pip, Python's package installer. Open your terminal or command prompt and run the following command:


```python
!pip install -q rispy
```

## Downloading samples

In order to run the commands in this blog post, let's download some data sample with data from three different sources: EMBASE, Rayyan, and Web Of Science.


```python
!wget https://gist.github.com/xmnlab/edbca465fc6151e87ac5aaa6b0b8837d/raw/6f8bd30362c737565c6530732f1edeb882c8e879/sample_embase.ris -O /tmp/embase.ris
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
--2024-01-31 23:57:04--  https://gist.github.com/xmnlab/edbca465fc6151e87ac5aaa6b0b8837d/raw/6f8bd30362c737565c6530732f1edeb882c8e879/sample_embase.ris
Resolving gist.github.com (gist.github.com)... 140.82.113.3
Connecting to gist.github.com (gist.github.com)|140.82.113.3|:443... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://gist.githubusercontent.com/xmnlab/edbca465fc6151e87ac5aaa6b0b8837d/raw/6f8bd30362c737565c6530732f1edeb882c8e879/sample_embase.ris [following]
--2024-01-31 23:57:04--  https://gist.githubusercontent.com/xmnlab/edbca465fc6151e87ac5aaa6b0b8837d/raw/6f8bd30362c737565c6530732f1edeb882c8e879/sample_embase.ris
Resolving gist.githubusercontent.com (gist.githubusercontent.com)... 185.199.110.133, 185.199.109.133, 185.199.108.133, ...
Connecting to gist.githubusercontent.com (gist.githubusercontent.com)|185.199.110.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 30718 (30K) [text/plain]
Saving to: ‘/tmp/embase.ris’

/tmp/embase.ris     100%[===================>]  30.00K  --.-KB/s    in 0.003s

2024-01-31 23:57:05 (11.3 MB/s) - ‘/tmp/embase.ris’ saved [30718/30718]


</span></code>
</pre>
</div>


```python
!wget https://gist.github.com/xmnlab/edbca465fc6151e87ac5aaa6b0b8837d/raw/6f8bd30362c737565c6530732f1edeb882c8e879/sample_rayyan.ris -O /tmp/rayyan.ris
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
--2024-01-31 23:57:07--  https://gist.github.com/xmnlab/edbca465fc6151e87ac5aaa6b0b8837d/raw/6f8bd30362c737565c6530732f1edeb882c8e879/sample_rayyan.ris
Resolving gist.github.com (gist.github.com)... 140.82.113.3
Connecting to gist.github.com (gist.github.com)|140.82.113.3|:443... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://gist.githubusercontent.com/xmnlab/edbca465fc6151e87ac5aaa6b0b8837d/raw/6f8bd30362c737565c6530732f1edeb882c8e879/sample_rayyan.ris [following]
--2024-01-31 23:57:08--  https://gist.githubusercontent.com/xmnlab/edbca465fc6151e87ac5aaa6b0b8837d/raw/6f8bd30362c737565c6530732f1edeb882c8e879/sample_rayyan.ris
Resolving gist.githubusercontent.com (gist.githubusercontent.com)... 185.199.111.133, 185.199.108.133, 185.199.109.133, ...
Connecting to gist.githubusercontent.com (gist.githubusercontent.com)|185.199.111.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 10817 (11K) [text/plain]
Saving to: ‘/tmp/rayyan.ris’

/tmp/rayyan.ris     100%[===================>]  10.56K  --.-KB/s    in 0.001s

2024-01-31 23:57:08 (8.81 MB/s) - ‘/tmp/rayyan.ris’ saved [10817/10817]


</span></code>
</pre>
</div>


```python
!wget https://gist.github.com/xmnlab/edbca465fc6151e87ac5aaa6b0b8837d/raw/6f8bd30362c737565c6530732f1edeb882c8e879/sample_wos.ris -O /tmp/wos.ris
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
--2024-01-31 23:57:10--  https://gist.github.com/xmnlab/edbca465fc6151e87ac5aaa6b0b8837d/raw/6f8bd30362c737565c6530732f1edeb882c8e879/sample_wos.ris
Resolving gist.github.com (gist.github.com)... 140.82.113.3
Connecting to gist.github.com (gist.github.com)|140.82.113.3|:443... connected.
HTTP request sent, awaiting response... 301 Moved Permanently
Location: https://gist.githubusercontent.com/xmnlab/edbca465fc6151e87ac5aaa6b0b8837d/raw/6f8bd30362c737565c6530732f1edeb882c8e879/sample_wos.ris [following]
--2024-01-31 23:57:11--  https://gist.githubusercontent.com/xmnlab/edbca465fc6151e87ac5aaa6b0b8837d/raw/6f8bd30362c737565c6530732f1edeb882c8e879/sample_wos.ris
Resolving gist.githubusercontent.com (gist.githubusercontent.com)... 185.199.108.133, 185.199.111.133, 185.199.109.133, ...
Connecting to gist.githubusercontent.com (gist.githubusercontent.com)|185.199.108.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 9526 (9.3K) [text/plain]
Saving to: ‘/tmp/wos.ris’

/tmp/wos.ris        100%[===================>]   9.30K  --.-KB/s    in 0.001s

2024-01-31 23:57:11 (15.5 MB/s) - ‘/tmp/wos.ris’ saved [9526/9526]


</span></code>
</pre>
</div>

## Using rispy to Read RIS Files

Once you have rispy installed and a sample RIS file downloaded, it's time to start coding. 
Here's some examples about how to read a RIS file.


```python
import rispy
```

### Read from EMBASE RIS


```python
# Path to your downloaded RIS file
embase_path = '/tmp/embase.ris'

# Read the RIS file
with open(embase_path, 'r') as bibliography_file:
    embase_data = rispy.load(bibliography_file)
```


```python
pprint(list(embase_data[0].keys()))
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
Pretty printing has been turned OFF

</span></code>
</pre>
</div>

Let's check if the result correspond to the data we created:


```python
assert len(embase_data) == 2
assert embase_data[0]["primary_title"] == "Author Correction: Federated learning enables big data for rare cancer boundary detection (Nature Communications, (2022), 13, 1, (7346), 10.1038/s41467-022-33407-5)"
assert embase_data[0]["doi"] == "10.1038/s41467-023-36188-7"
assert embase_data[0]["notes_abstract"] == "In this article the author name Carmen Balaña was incorrectly written as Carmen Balaña Quintero. The original article has been corrected."
```

One attribute that calls the attention is `unknown_tag`, that probably means that they are EMBASE specific fields. Let's check that:


```python
embase_data[0]["unknown_tag"].keys()
```




<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
dict_keys(['U2', 'U4', 'LK'])
</span></code>
</pre>
</div>



### Read from Rayyan RIS


```python
# Path to your downloaded RIS file
rayyan_path = '/tmp/rayyan.ris'

# Read the RIS file
with open(rayyan_path, 'r') as bibliography_file:
    rayyan_data = rispy.load(bibliography_file)
```


```python
pprint(list(rayyan_data[0].keys()))
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
Pretty printing has been turned ON

</span></code>
</pre>
</div>


```python
assert len(rayyan_data) == 3
assert rayyan_data[0]["title"] == "Organic fertilization and alternative products in the control of powdery mildew"
assert rayyan_data[0]["doi"] == "10.1590/2447-536x.v26i1.2109"
assert rayyan_data[0]["abstract"] == "Abstract Rose is a plant of high nutritional requirement, susceptible to powdery mildew disease caused by fungus Oidium leucoconium, which causes leaf fall and losses in flower production. The objective of this study was to evaluate powdery mildew severity in rose cultivar ‘Grand Gala’ in response to organic fertilization and the application of alternative products to disease control. The first experiment was set in a factorial arrangement, with 5 alternative products: spraying with water as a control (PA), lime sulfur (CS), neem oil (ON), mixture of sodium bicarbonate and canola oil (BC) and coffee pyroligneous acid (APC) and 2 organic fertilizers: chicken manure (EA) and biofertilizer based on banana stalk (B). Disease severity was assessed at 0, 15, 30 and 45 days after the treatments. In the second experiment, asymptomatic leaves or with different powdery mildew severity levels were sprayed only once with the same alternative products mentioned above. Severity was assessed at 0, 7 and 14 days. The organic fertilizations did not influence the reduction in powdery mildew severity in rose. At 45 days, APC yielded a greater reduction in disease severity (81.6%), followed by treatments based on BC, ON and CS. Greater reduction in disease severity in experiment 2 occurred in the treatments of BC and CS, followed by APC. Therefore, it is possible to conclude that APC and the BC have the potential to control rose powdery mildew in an organic cultivation system."
```

### Read from Web Of Science RIS


```python
# Path to your downloaded RIS file
wos_path = '/tmp/wos.ris'

# Read the RIS file
with open(wos_path, 'r') as bibliography_file:
    wos_data = rispy.load(bibliography_file)
```


```python
pprint(list(wos_data[0].keys()))
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
Pretty printing has been turned OFF

</span></code>
</pre>
</div>


```python
assert len(wos_data) == 3
assert wos_data[0]["title"] == "A Survey on Computer Vision for Assistive Medical Diagnosis From Faces"
assert wos_data[0]["doi"] == "10.1109/JBHI.2017.2754861"
assert wos_data[0]["abstract"] == "Automatic medical diagnosis is an emerging center of interest in computer vision as it provides unobtrusive objective information on a patient's condition. The face, as a mirror of health status, can reveal symptomatic indications of specific diseases. Thus, the detection of facial abnormalities or atypical features is at up most importance when it comes to medical diagnostics. This survey aims to give an overview of the recent developments in medical diagnostics from facial images based on computer vision methods. Various approaches have been considered to assess facial symptoms and to eventually provide further help to the practitioners. However, the developed tools are still seldom used in clinical practice, since their reliability is still a concern due to the lack of clinical validation of the methodologies and their inadequate applicability. Nonetheless, efforts are being made to provide robust solutions suitable for healthcare environments, by dealing with practical issues such as real-time assessment or patients positioning. This survey provides an updated collection of the most relevant and innovative solutions in facial images analysis. The findings show that with the help of computer vision methods, over 30 medical conditions can be preliminarily diagnosed from the automatic detection of some of their symptoms. Furthermore, future perspectives, such as the need for interdisciplinary collaboration and collecting publicly available databases, are highlighted."
```

Again, the attribute `unknown_tag` appears, that probably means that they are WoS specific fields. Let's check that:


```python
wos_data[0]["unknown_tag"].keys()
```




<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
dict_keys(['PU', 'PI', 'PA', 'J9', 'JI', 'WE'])
</span></code>
</pre>
</div>



### Consistency of fields across the sources

Some sources uses different fields, so it is important to pay attention to some fields like title, abstract, etc.

So let's first check all the fields across the sources.


```python
fields = set()

for dataset in [embase_data, rayyan_data, wos_data]:
    for row in dataset:
        fields |= set(row.keys())

fields
```




<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
{'urls', 'first_authors', 'notes', 'custom3', 'date', 'alternate_title1', 'accession_number', 'type_of_work', 'publication_year', 'journal_name', 'custom7', 'custom5', 'language', 'number', 'primary_title', 'type_of_reference', 'issn', 'name_of_database', 'start_page', 'alternate_title3', 'note', 'year', 'doi', 'title', 'end_page', 'file_attachments2', 'abstract', 'access_date', 'keywords', 'volume', 'secondary_title', 'unknown_tag', 'author_address', 'custom6', 'notes_abstract', 'authors'}
</span></code>
</pre>
</div>



Now, let's check all the fields about title:


```python
[field for field in fields if "title" in field]
```




<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
['alternate_title1', 'primary_title', 'alternate_title3', 'title', 'secondary_title']
</span></code>
</pre>
</div>



Let's also check the fields about abstract:


```python
[field for field in fields if "abstract" in field]
```




<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
['abstract', 'notes_abstract']
</span></code>
</pre>
</div>



So, if we are planning to use rispy inside a pipeline, we need to be very careful to get the field we want from all possible values.

## Writing RIS Files with Rispy

In addition to reading RIS files, Rispy also provides functionality for writing RIS files. This feature is particularly useful for creating your bibliographic data programmatically and exporting it in the RIS format, which is widely accepted in academic and research circles. Let's delve into how to use Rispy for writing RIS files.

For this example, it will use the data from Rayyan that was just loaded.

### Writing to a RIS File

Once your data is structured correctly, you can proceed to write it to a RIS file. Rispy simplifies this process significantly. Here’s how you can do it:


```python
# Path for the new RIS file
output_file_path = '/tmp/output.ris'

# Write the data to a RIS file
with open(output_file_path, 'w') as output_file:
    rispy.dump(rayyan_data, output_file)
```

Now, let's check the first 10 lines of this new file created.


```python
!head -n 10 /tmp/output.ris
```

<div class="language-text highlight">
<h3 class="code-label">
  OUTPUT<i aria-hidden="true" data-feather="chevron-left"></i>
  <i aria-hidden="true" data-feather="chevron-right"></i>
</h3>
<pre class="output">
  <code><span>
1.
TY  - JOUR
AN  - rayyan-536206336
TI  - Organic fertilization and alternative products in the control of powdery mildew
Y1  - 2020
Y2  - 3
T2  - Ornamental Horticulture
SN  - 2447-536X
J2  - Ornamental Horticulture
VL  - 26

</span></code>
</pre>
</div>

Writing RIS files with rispy is straightforward and efficient. Whether you are generating bibliographic data from another source or manually creating your entries for research purposes, rispy's writing functionality makes the process seamless.

## Conclusion

By mastering both reading and writing of RIS files using rispy, you can automate and streamline your bibliographic management tasks, saving time and reducing the potential for manual errors. This makes rispy a valuable tool in any researcher's toolkit. 

**rispy** is a powerful and easy-to-use library for anyone dealing with RIS files in Python. Its simplicity in installation and usage makes it an excellent choice for managing bibliographic data. Whether you're a researcher, academic, or developer working with bibliographic information, Rispy is definitely worth exploring.
