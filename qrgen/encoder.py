#!/usr/bin/env python3
"""
QR Code Generator
"""

import qrcode
import base64
from io import BytesIO

class QRencoder():
    "Generate a QR code from the given TEXT"

    error_levels = {
        'L': qrcode.constants.ERROR_CORRECT_L,
        'M': qrcode.constants.ERROR_CORRECT_M,
        'Q': qrcode.constants.ERROR_CORRECT_Q,
        'H': qrcode.constants.ERROR_CORRECT_H
    }

    def __init__(self, text, filename='qrcode.png', verbose=False, base64=False):
        self.text = text
        self.filename = filename
        self.size = 10
        self.border = 4
        self.error_correction = 'M'
        self.fill_color = 'black'
        self.back_color = 'white'
        self.base64 = base64
        self.verbose = verbose

    def set_size(self, size):
        "Set size of the QR code"
        self.size = size

    def set_border(self, border):
        "Set border size of the QR code"
        if border > 0:
            self.border = border
        else:
            self.border = 4  # Default to 4 if invalid

    def set_error_correction(self, error_correction):
        "Error correction level for the QR code"
        error_correction = error_correction.upper()
        # Validate error correction level
        if error_correction in self.error_levels:
            self.error_correction = error_correction
        else:
            self.error_correction = 'M'  # Default to Medium if invalid

    def set_colors(self, fill_color='black', back_color='white'):
        "Set fill and background colors for the QR code"
        self.fill_color = fill_color
        self.back_color = back_color

    def generate(self):
        "Generate the QR code and save it to the filename file"
        try:
            qr = qrcode.QRCode(
                version=1,
                error_correction=self.error_levels[self.error_correction],
                box_size=self.size,
                border=self.border,
            )
            qr.add_data(self.text)
            qr.make(fit=True)
            img = qr.make_image(fill_color=self.fill_color, back_color=self.back_color)
            # if base64 image
            if self.base64:
                return self.__image_to_base64(img, 'PNG')
            # save image to file
            img.save(self.filename, format='PNG')
            if self.verbose:
                print(f"QR code generated successfully: {self.filename}")
            return self.filename
        except qrcode.exceptions.DataOverflowError as e:
            print(f"Error: Data too large for the selected QR code version and error correction level: {str(e)}")
        except IOError as e:
            print(f"Error saving QR code image: {str(e)}")

    def __image_to_base64(self, img, format='PNG'):
        "Convert PIL Image to base64 string."
        buffer = BytesIO()
        img.save(buffer, format=format.upper())
        img_bytes = buffer.getvalue()
        buffer.close()
        # Encode to base64
        base64_string = base64.b64encode(img_bytes).decode('utf-8')
        # Return with data URI prefix
        mime_type = f"image/{format.lower()}"
        return f"data:{mime_type};base64,{base64_string}"