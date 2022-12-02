import re
from _config import gen_all_files_with_extension

def get_slug(data):
    pattern_meta = re.compile(r"---.+---", re.DOTALL)
    meta = pattern_meta.search(data)
    
    if meta:
        pattern_slug = re.compile(r"(?<=slug:\s).+")
        slug = pattern_slug.search(meta.group())
        if slug:
            return slug.group()
        return None

def remove_meta_code(data):
    
    pattern_meta = re.compile(r"---.+---", re.DOTALL)
    data = pattern_meta.sub("", data)
    
    pattern_code = re.compile(r"```.+```", re.DOTALL)
    data = pattern_code.sub("", data)

    return data

def remove_punctuations(data):
    punctuations = "!"+"#$%&'()*+,-./:;<=>?@[\]^_`{|}~¿"+'"'
    for p in punctuations:
        if p in data:
            data = data.replace(p, "")
    return data 

def get_conj_words():
    with open("conjunciones_es.txt", "r") as f:
        reader = f.readlines()
    lst = []
    for line in reader:
        lst.append(line.rstrip())
    
    return lst

def remove_conjuctions_words(data_dict):
    conjunc = get_conj_words()
    for k in data_dict.copy():
        if k in conjunc:
            data_dict.pop(k)
    
    return data_dict

def get_tags(file):
    with open(file, "r") as f :
        reader = f.read()
    slug = get_slug(reader)
    data = remove_meta_code(reader)
    data = remove_punctuations(data)
    data = data.lower()
    data = data.split()

    freq = dict()
    for word in data:
        if word not in freq:
            freq[word] = 0
        freq[word] += 1
    tags = remove_conjuctions_words(freq)

    tags = sorted(tags,reverse = True, key= lambda x:tags[x])[:10]

    return slug, tags

def generate_csv_tags(path):
    file = open("../csv_folder/new_tags.csv", "w")
    file.write("slug, new_tags")
    file.write("\n")
    for md_file in gen_all_files_with_extension(path):
        slug, tags = get_tags(md_file)
        print(tags)
        new_tags = ", ".join(tags)
        if slug:
            file.write(f'{slug},"[{new_tags}]"')
            file.write("\n")
    file.close()


def main():
    PATH = "../content/blog/"
    generate_csv_tags(PATH)
    
if __name__ == "__main__":
    main()