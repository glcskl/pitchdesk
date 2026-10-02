# pitchdesk — self-contained offline pitch deck

A startup pitch deck that works on a phone with unreliable internet. Instead of a folder of files that a viewer must download, the build script produces one HTML file with every image, font and style embedded, plus a QR code that points at it. Once the file is on the phone, the deck opens with no network access at all.

Built as a personal project between 6 and 9 September 2026.

## Features

- Single self-contained HTML output, no external requests at runtime
- Images embedded as base64, so nothing depends on an image host
- Fonts embedded, so text renders identically offline
- QR code generated so the deck can be opened on a second device
- Layout fixed for a phone viewport, tested at presentation size
- Repeatable build from the source assets

## Tech stack

| Layer | Technology |
| --- | --- |
| Build script | Python 3 |
| Image processing | Pillow |
| QR generation | qrcode |
| Encoding | base64, standard library |
| Output | Static HTML |

## Getting started

### Requirements

- Python 3.9 or newer

### Environment variables

None. The build is fully local.

### Installation

```bash
git clone https://github.com/glcskl/pitchdesk.git
cd pitchdesk
python -m venv .venv
source .venv/bin/activate
pip install pillow qrcode
```

### Running

Place the source images into `assets/`, then build:

```bash
python build_web.py
```

The script writes a self-contained HTML file and a QR code, and refreshes the redirect in `index.html`.

## Project structure

```
build_web.py                     build script
index.html                       entry point, redirects to the deck
StartUpSpace_web_prezentatsiya.html   generated deck
assets/                          source images
fonts/                           fonts embedded into the output
qr/                              generated QR code
```

## Build process

`build_web.py` reads the images from `assets/`, normalises them with Pillow, encodes each one as a base64 data URI, inlines the fonts as base64, assembles the deck and writes the result as a single HTML file. The QR code is generated from the deck location and written to `qr/`.

## Notes

The file is large, because everything is embedded by design. That is the trade-off that makes it work without a connection. The deck is a presentation artefact; the build script is the source of truth.