---
marp: true
---

# Vizlink to Python

---

## Project Description

This project uses [Vizlink][1] to read data from the ProDJLink network, transmitting the data as a JSON file to a Python script, which works with standard DMX lighting software. The project is still in development and is not yet ready for production use.

> **Disclaimer:** This project is not affiliated with AlphaTheta/Pioneer DJ Corp. or its related companies in any way and has been developed independently. Vizlink to Python is licensed under the [MIT license][license-link]. The maintainers of this project are not liable for any damages to your data, as this is an experimental project.  
> **Editor's Warning:** Any tool that is still under development should be tested thoroughly before relying on it for your next big DJ set. There is also a possibility that Pioneer DJ could close the loopholes that allow this to work in a future firmware update to CDJs – so update with caution.

---

## Table of Contents

1. Introduction
2. Requirements
3. Installation
4. Usage
5. Equipment

---

## Introduction

Inspired by a section in the great manual of Beat Link Trigger about [writing played songs in a text file][2], I want to work with analyzed data from Rekordbox with my played songs from the [Pioneer XDJ-XZ][3] in combination with standard DMX lighting software.

Another option is to show the playlist live on a website.

---

## Requirements

- Fully ProDJLink compatible hardware
- Vizlink
- Python 3.x

---

## Installation

1. Clone this repository: `git clone https://github.com/hfanieng/vizlink-to-python`
2. Install the Python dependencies:

```bash
pip install flask
pip install json  
pip install threading
```

---

## Usage

Run the Python script: `python main.py`

---

## Equipment Used for the Project

All tests were run with the reliable [Pioneer XDJ-XZ][3] with ❤️ and 🤩 in my hometown [Hagen-Wehringhausen][4].  
![XDJ-XZ][5]

---

## Structure

This is a Python library for converting data from a ProDJ-Link device via [Vizlink][1] into Python objects.

```plaintext
vizlink-to-python/
├── data/
│   ├── beat.json
│   ├── device.json
│   ├── error.json
│   ├── structure.json
│   ├── sys.json
│   ├── track.json
├── payloads/
│   ├── __init__.py
│   ├── art.py
│   ├── beat.py
│   ├── device.py
│   ├── error.py
│   ├── structure.py
│   ├── sys.py
│   ├── track.py
├── static/
│   ├── styles.css
├── templates/
│   ├── index.html
├── factory.py
└── app.py
```
---

## Excamples

### Device

```json
{
    "active": true,
    "name": "XDJ-XZ",
    "player": 33,
    "ms": 1723300683029,
    "type": "device",
    "version": 1
}
```

---

### Track

```json
{
    "album": "Smells Like Teen Spirit",
    "artist": "Nirvana",
    "cues": [
        {
            "comment": "",
            "ms": 1266
        }
    ],
    "duration": 280000,
    "player": 1,
    "source": {
        "id": 7560,
        "player": 1,
        "slot": "SD_SLOT"
    },
    "tempo": 116.52,
    "title": "Smells Like Teen Spirit",
    "year": 1991,
    "ms": 1723301236014,
    "type": "track",
    "version": 1
}
```

---

### Track-Structure

```json
{
    "bank": "default",
    "mood": "mid",
    "phrases": [
        {
            "beat": 3,
            "beats": 14,
            "kind": "intro"
        },
        {
            "beat": 17,
            "beats": 20,
            "kind": "verse_1"
        },
        {
            "beat": 37,
            "beats": 16,
            "kind": "bridge"
        },
        {
            "beat": 53,
            "beats": 16,
            "kind": "verse_2"
        },
        {
            "beat": 69,
            "beats": 32,
            "kind": "verse_2"
        },
        {
            "beat": 101,
            "beats": 36,
            "kind": "chorus"
        },
        {
            "beat": 137,
            "beats": 32,
            "kind": "chorus"
        },
        {
            "beat": 169,
            "beats": 12,
            "kind": "verse_1"
        },
        {
            "beat": 181,
            "beats": 16,
            "kind": "verse_1"
        },
        {
            "beat": 197,
            "beats": 8,
            "kind": "verse_2"
        },
        {
            "beat": 205,
            "beats": 8,
            "kind": "bridge"
        },
        {
            "beat": 213,
            "beats": 32,
            "kind": "verse_2"
        },
        {
            "beat": 245,
            "beats": 20,
            "kind": "chorus"
        },
        {
            "beat": 265,
            "beats": 56,
            "kind": "chorus"
        },
        {
            "beat": 321,
            "beats": 32,
            "kind": "chorus"
        },
        {
            "beat": 353,
            "beats": 20,
            "kind": "bridge"
        },
        {
            "beat": 373,
            "beats": 24,
            "kind": "verse_3"
        },
        {
            "beat": 397,
            "beats": 12,
            "kind": "chorus"
        },
        {
            "beat": 409,
            "beats": 20,
            "kind": "chorus"
        },
        {
            "beat": 429,
            "beats": 44,
            "kind": "chorus"
        },
        {
            "beat": 473,
            "beats": 40,
            "kind": "chorus"
        },
        {
            "beat": 513,
            "beats": 18,
            "kind": "outro"
        }
    ],
    "player": 1,
    "ms": 1723301236018,
    "type": "structure",
    "version": 1
}
```

---

### Beat

```json
{
    "beat": 208,
    "master": true,
    "onair": null,
    "ms": 1723301344416,
    "type": "beat",
    "version": 1
}
```

---

[1]:https://github.com/nzoschke/vizlink
[2]:<https://blt-guide.deepsymmetry.org/beat-link-trigger/7.4.1/Matching.html#writing-a-playlist>
[3]:<https://www.pioneerdj.com/en/product/all-in-one-system/xdj-xz/black/overview/>
[4]:<https://de.wikipedia.org/wiki/Wehringhausen>
[5]:<https://www.pioneerdj.com/-/media/pioneerdj/images/products/all-in-one-system/xdj-xz/xdj-xz_prm_top.png?h=1316&w=1792&hash=CDDC51D731D7571112C6D6AB25B04626>
[license-link]: https://github.com/hfanieng/vizlink-to-python/blob/main/LICENSE

