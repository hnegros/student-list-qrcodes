import csv
import os
from PIL import Image ,ImageDraw,ImageFont

import qrcode

version=3

border=2
box_size=14
font_size=40

os.makedirs("qrcodes",exist_ok=True)

def get_nb_module_version(n):
    return 21+(n-1)*4


with open('fake_student_list.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        qr = qrcode.QRCode(
            border=border,
            version=version,
            box_size=box_size
        )
        qr.add_data(";".join(row))
        qr.make(fit=True)

        size = (get_nb_module_version(qr.version)+(border*2))*box_size
        H,W = size,size

        img = qr.make_image()

        background = Image.new('RGBA', (H, W+3*(font_size+4) + 2*box_size), (255,255,255,255))
        draw = ImageDraw.Draw(background)

        font = ImageFont.truetype("Roboto-Regular.ttf",font_size)
        draw.text((H/2,W+(font_size/2)),row[0],(0,0,0),anchor="mm", font=font)
        draw.text((H/2,W+(font_size/2) + font_size+4),row[1],(0,0,0),anchor="mm", font=font)
        draw.text((H/2,W+(font_size/2)+ (font_size+4) *2),row[2],(0,0,0),anchor="mm", font=font)
        background.paste(img, (0,0))
        background.save(f'qrcodes/{"_".join(row)}.png')

 