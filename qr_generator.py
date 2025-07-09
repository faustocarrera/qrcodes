#!/usr/bin/env python3
"""
QR Code Generator CLI Tool
A command line tool to generate QR codes with customizable options.
"""

import click
from qrgen import get_path
from qrgen.encoder import QRencoder
from qrgen.decoder import QRdecoder


@click.command()
@click.argument('text', type=str)
@click.option('--output', '-o', default='qrcode.png', help='Output filename (default: qrcode.png)')
@click.option('--size', '-s', default=10, help='Size of the QR code (default: 10)')
@click.option('--border', '-b', default=4, help='Border size (default: 4)')
@click.option('--error-correction', '-e',
              type=click.Choice(['L', 'M', 'Q', 'H'], case_sensitive=False),
              default='M', help='Error correction level (L=Low, M=Medium, Q=Quartile, H=High)'
              )
@click.option('--fill-color', '-f', default='black', help='Fill color (default: black)')
@click.option('--back-color', '-bg', default='white', help='Background color (default: white)')
@click.option('--base64', '-b64', is_flag=True, help='Output as base64 encoded string instead of saving to file')
@click.option('--verbose', '-v', is_flag=True, default=False, help='Output messages')
def generate(text, output, size, border, error_correction, fill_color, back_color, verbose, base64):
    """
    Generate a QR code from the given TEXT.

    Examples:
        python qr_generator.py "Hello World"
        python qr_generator.py "https://example.com" -o example.png -s 15
        python qr_generator.py "Contact info" --fill-color blue --back-color yellow
    """
    qrcode_path = get_path(__file__, 'qrcodes', output)
    qrgen = QRencoder(text, filename=qrcode_path, verbose=verbose, base64=base64)
    qrgen.set_size(size)
    qrgen.set_border(border)
    qrgen.set_error_correction(error_correction)
    qrgen.set_colors(fill_color, back_color)
    result = qrgen.generate()
    if verbose:
        print(result)


@click.command()
@click.argument('filename', type=click.Path(exists=True))
def decode(filename):
    """
    Decode a QR code from an image file.

    Example:
        python qr_generator.py decode qrcode.png
    """
    qrdecoder = QRdecoder(filename)
    result = qrdecoder.decode()
    if isinstance(result, list):
        for data in result:
            print(data)
    else:
        print(result)


@click.group()
def cli():
    """QR Code Generator and Decoder CLI Tool"""
    pass


# Add commands to group
cli.add_command(generate, name='generate')
cli.add_command(decode, name='decode')


if __name__ == '__main__':
    cli()
