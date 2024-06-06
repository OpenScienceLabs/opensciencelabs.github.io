---
title: "ArtBox: What is it and how to collaborate?"
slug: artbox-what-is-it-how-to-collaborete
date: 2024-04-02
authors: ["Daniela Iglesias Rocabado"]
tags: [open-source, art, python, multimedia processing]
categories: [python]
description: |
  ArtBox is a tool set for handling multimedia files with a bunch of useful functions.
thumbnail: "/header.jpg"
template: "blog-post.html"
---
# How to use it?

## What is ArtBox?

ArtBox is a versatile tool set designed for efficient multimedia file handling, offering a range of valuable functions to enhance your multimedia processing experience.


Key features of ArtBox include capabilities for text-to-audio conversion, YouTube video downloading, musical composition from notes, audio removal from video clips, audio extraction, and merging audio with video files. These functionalities position ArtBox as a pivotal tool for multimedia enthusiasts, content creators, and anyone in need of efficient multimedia processing solutions.


### Installation

ArtBox relies on certain dependencies that may not function optimally on your machine. To ensure a smooth installation process, it is recommended to create a conda/mamba environment and install ArtBox within that environment.

```bash
$ mamba create --name artbox "python>=3.8.1,<3.12" pygobject pip
```

The command is creating a conda environment named "artbox" with Python version 3.8.1 or later, and includes the pygobject and pip packages in the environment. This is useful for setting up an isolated environment for a specific project or application, ensuring compatibility and reproducibility of the software stack.

```bash
$ conda activate artbox
```

To prevent dependency conflicts, please install the numpy library using the following command:

```bash
$ pip install "numpy>=1.20"
```

The `conda activate artbox` command is used to activate the "artbox" conda environment, ensuring that subsequent commands or scripts run within this isolated environment. Activation modifies the system's `PATH` to prioritize the "artbox" environment, allowing for the use of specific Python versions and packages associated with the project, thus maintaining a clean and reproducible development or execution environment.


```python
$ !mamba install -q -y -c conda-forge pygobject pip
```


```python
$ !pip install -q artbox
```

The `pip install artbox` command is used to install the Python package named "artbox" using the pip package manager. This command fetches the "artbox" package from the Python Package Index (PyPI) and installs it into the currently active Python environment. The `pip install` command is commonly used to add external packages or libraries to a Python environment, expanding its functionality for a particular project or application.

## Examples of Artbox usage.
For the following examples, create the a temporary folder for artbox:


```python
$ mkdir /tmp/artbox
```

### Convert text to audio

By default, the `artbox voice` uses
[`edge-tts`](https://pypi.org/project/edge-tts/) engine, but you can also
specify [`gtts`](https://github.com/pndurette/gTTS) with the flag
`--engine gtts`.


```python
$ echo "Are you ready to join Link and Zelda in fighting off this unprecedented threat to Hyrule?" > /tmp/artbox/text.md
$ artbox speech from-text \
    --title artbox \
    --input-path /tmp/artbox/text.md \
    --output-path /tmp/artbox/speech.mp3 \
    --engine edge-tts
```

If you need to generate the audio for different language, you can use the flag
`--lang`:


```python
$ echo "Bom dia, mundo!" > /tmp/artbox/text.md
$ artbox speech from-text \
    --title artbox \
    --input-path /tmp/artbox/text.md \
    --output-path /tmp/artbox/speech.mp3 \
    --lang pt
```

If you are using `edge-tts` engine (the default one), you can also specify the
locale for the language, for example:


```python
$ echo "Are you ready to join Link and Zelda in fighting off this unprecedented threat to Hyrule?" > /tmp/artbox/text.md
$ artbox speech from-text \
    --title artbox \
    --input-path /tmp/artbox/text.md \
    --output-path /tmp/artbox/speech.mp3 \
    --engine edge-tts \
    --lang en-IN
```

Additionally, if you are using edge-tts, you can specify `--rate`, `--volume`, and  `--pitch`, for example:


```python
$ echo "Do you want some coffee?" > /tmp/artbox/text.md
$ artbox speech from-text \
    --title artbox \
    --input-path /tmp/artbox/text.md \
    --output-path /tmp/artbox/speech.mp3 \
    --engine edge-tts \
    --lang en \
    --rate +10% \
    --volume -10% \
    --pitch -5Hz
```

### Convert audio to text
ArtBox uses `speechrecognition` to convert from audio to text. Currently, ArtBox just support the google engine.

For this example, let's first create our audio:


```python
$ echo "Are you ready to join Link and Zelda in fighting off this unprecedented threat to Hyrule?" > /tmp/artbox/text.md
$ artbox speech from-text \
    --title artbox \
    --input-path /tmp/artbox/text.md \
    --output-path /tmp/artbox/speech.mp3 \
    --engine edge-tts
```

Now we can convert it back to text:


```python
$ artbox speech to-text \
    --input-path /tmp/artbox/speech.mp3 \
    --output-path /tmp/artbox/text-from-speech.md \
    --lang en
```

### Download a youtube video

If you want to download videos from the youtube, you can use the following
command:


```python
$ artbox youtube download \
    --url https://www.youtube.com/watch?v=zw47_q9wbBE \
    --output-path /tmp/artbox/
```

The command above downloads the video using a random resolution. If you want a specific resolution, use the flat `--resolution`:


```python
$ artbox youtube download \
    --url https://www.youtube.com/watch?v=zw47_q9wbBE \
    --output-path /tmp/artbox/ \
    --resolution 360p
```

### Remove the audio from a video

First, download the youtube video `https://www.youtube.com/watch?v=zw47_q9wbBE`, as explained before.

Next, run the following command:


```python
$ artbox video remove-audio \
  --input-path "/tmp/artbox/The Legend of Zelda Breath of the Wild - Nintendo Switch Presentation 2017 Trailer.mp4" \
  --output-path /tmp/artbox/botw.mp4
```

### Extract the audio from a video

First, download the youtube video `https://www.youtube.com/watch?v=zw47_q9wbBE`, 
as explained before.

Next, run the following command:


```python
$ artbox video extract-audio \
  --input-path "/tmp/artbox/The Legend of Zelda Breath of the Wild - Nintendo Switch Presentation 2017 Trailer.mp4" \
  --output-path /tmp/artbox/botw-audio.mp3
```

### Combine audio and video files

First, execute the previous steps:

- Download a youtube video
- Remove the audio from a video
- Extract the audio from a video

Next, run the following command:


```python
$ artbox video combine-video-and-audio \
  --video-path /tmp/artbox/botw.mp4 \
  --audio-path /tmp/artbox/botw-audio.mp3 \
  --output-path /tmp/artbox/botw-combined.mp4
```

## Additional dependencies

If you want to use Python to play your audio files, you can install `playsound`:


```python
$ pip wheel --use-pep517 "playsound (==1.3.0)"
```

### Demo Video

For a better explanation of the facilities and usage, please watch to the following video.

<iframe width="560" height="315" src="https://www.youtube.com/embed/sITnMuZTNAw?si=goPrd2BhPxy7Fqku" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
