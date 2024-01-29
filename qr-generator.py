# animated_qrcode.py
'''
Simple QR code generator
Run and follow the prompts for a file and name. QR code will be saved in the same folder as the script.
'''
import segno
from urllib.request import urlopen

qr_link_prompt = str(input("Enter the link for your QR code:\nLink: "))
qrcode = segno.make_qr(qr_link_prompt)
qr_name_prompt = str(input("Enter the name of you QR code:\nName: "))

qrcode.save(
    f'{qr_name_prompt}.png',
    scale=5,
)