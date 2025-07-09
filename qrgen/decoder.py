#!/usr/bin/env python3
"""
QR decoder
"""

from pyzbar import pyzbar
from PIL import Image


class QRdecoder():
    "Decode a QR code from an image file"

    def __init__(self, image_path):
        self.image_path = image_path

    def decode(self):
        "Decode the QR code and return the data"
        try:
            # Open image
            image = Image.open(self.image_path)

            # Decode QR codes
            decoded_objects = pyzbar.decode(image)

            # Extract data from decoded objects
            data = [obj.data.decode('utf-8') for obj in decoded_objects]
            return data

        except OSError as e:
            return f"Error opening image file: {e}"
        except pyzbar.PyzbarError as e:
            return f"Error decoding QR code: {e}"
