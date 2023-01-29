"""
From a csv file and the files directory path as arguments, modify the metadata according the new metadata assigned from 
the csv file.

Example
if the file exist in the csv file modify its metadata according to

filename, slug, author, date, tags, category
...
filtrar-datos-r.md, filtrar-datos-r, John Vino, 2022-09-25, "Word Cloud, r, DataViz", ciencia de datos https://opensciencelabs.org/blog/filtrar-datos-r/filtrar-datos-r/
...

filename=filtrar-datos-r.md
---
title: "Crea tu nube de palabras en R a partir de un documento de texto"
author: John Vino
slug: filtrar-datos-r
category: ciencia de datos
date: 2022-09-25
draft: false
usePageBundles: true
thumbnail: '/header.png'
featureImage: '/header.png' 
tags: ["Word Cloud, r, DataViz"]
alias: ["https://opensciencelabs.org/blog/filtrar-datos-r/filtrar-datos-r/"]
---
Note that in the alias key in the metadata is equal to a list containing the url 
"""
import csv
import re
# Para la nube de palabras
import numpy as np
from PIL import Image 
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib as mpl

# Separando ingles y español
def separate_files(csv_file):
    lst = []
    with open(csv_file) as f:
        reader = csv.DictReader(f)
        for a in reader:
            lst.append(a)
    for e in lst:
        e["tags"] = e["tags"].replace("][", "]\n[").replace("] [", "]\n[")
        e["category"] = e["category"].replace("][", "]\n[").replace("] [", "]\n[")

    es_cat = []
    es_tags = []
    for e in lst:
        partial = e["tags"].split("\n")[1]
        es_tags.append(partial)
        print(e["category"])
        partial_cat = e["category"].split("\n")[1]
        print(partial_cat)
        es_cat.append(partial_cat)
        print()

    with open("tags_cats_es.csv", "w") as f:
        field_names = ["slug", "categorias", "tags"]
        writer = csv.DictWriter(f, fieldnames=field_names)
        writer.writeheader()
        for i, row in enumerate(lst):
            writer.writerow({"slug": row["slug"], "categorias": es_cat[i], "tags": es_tags[i]})
        
  
#csv_file = "../../csv_folder/new_cat_tags.csv"



# obteniendo la frecuencia de las categorias y tags
def freq_file(csv_file):
    lst = []
    with open(csv_file) as f:
        reader = csv.DictReader(f)
        for a in reader:
            lst.append(a)
    
    count = dict()
    count_tag = dict()
    for e in lst:
        cat = e["categorias"].replace("[","").replace("]","").split(",")
        for w in cat:
            word = w.strip()
            if word not in count:
                count[word] = 0
            count[word] += 1
        tags = e["tags"].replace("[","").replace("]","").split(",")
        for t in tags:
            tag = t.strip()
            if tag not in count_tag:
                count_tag[tag] = 0
            count_tag[tag] += 1
    # Verificando que no existan categorias que esten como tags
    for el in count:
        if el in count_tag:
            print(el)
    return count, count_tag
#reemplazando tags de acuerdo al csv_file
def replace_tags_cats(csv_file):
    lst = []
    with open(csv_file) as f:
        reader = csv.DictReader(f)
        for a in reader:
            lst.append(a)
   
    for lst1 in lst:
        path = "../../content/blog/"+lst1["slug"]+"/index.md"
        try:
            with open(path, "r") as fw:
                reader = fw.read()
        
            
            pattern_tags = re.compile(r"(tags:\s).+")
            tags = pattern_tags.search(reader).group()

            reader = reader.replace(tags, "tags: " + lst1["tags"])

            pattern_cat = re.compile(r"(categories:\s).+")
            cats = pattern_cat.search(reader).group()

            reader = reader.replace(cats, "categories: " + lst1["categorias"])
            
            with open(path, "w") as f:
                f.write(reader)
        except Exception as e:
            print(f"error en {path}", e)


def make_image(dct):
    #colormap = colors.ListedColormap(['#FF0000','#FF7F50','#FFE4C4'])
    colormap = mpl.colormaps["Paired"]
    wc = WordCloud(background_color = "white",width=1400, height=900, repeat=True, colormap=colormap)
    wc.generate_from_frequencies(dct)
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()

# slug categorias y tags
csv_file = "./tags_cats_es.csv"
#freq_file(csv_file)
cats, tags = freq_file(csv_file)
make_image(tags)
#make_image(cats)
