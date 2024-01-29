# animated_qrcode.py
'''
Simpl QR code generator
Change the variable qrcode to reflect the
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