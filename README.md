QR Code Generator CLI Tool
==========================

A command line tool to generate QR codes with customizable options.

## Features:

- Generate QR codes from text with customizable options
- Decode QR codes from image files (optional feature)
- Multiple output formats - PNG, JPEG, BMP, GIF
- Customizable styling - colors, size, border, error correction
- User-friendly CLI with Click framework

## Installation

```bash
$ pip install -r requirements.txt
```

## Usage Examples:

__Basic usage:__

```bash
python qr_generator.py "Hello World"
python qr_generator.py generate "https://example.com" -o qrexample.png
```

__Advanced options:__

```bash
python qr_generator.py "My text" -s 15 -b 2 --fill-color blue --back-color yellow
python qr_generator.py "Data" --error-correction H