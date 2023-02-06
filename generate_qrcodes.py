import csv
import os
from PIL import Image ,ImageDraw,ImageFont

import qrcode

version=3

border=2
box_size=14
font_size=25

def get_nb_module_version(n):
    return 21+(n-1)*4

for filename in os.listdir("input"):
    with open("input/"+filename) as csvfile:
        classe = filename.replace(".csv","")
        os.makedirs(f"qrcodes/{classe}",exist_ok=True)
        reader = csv.reader(csvfile,delimiter=";",quotechar="\"")
        for row in reader:
            qr = qrcode.QRCode(
                border=border,
                version=version,
                box_size=box_size
            )
            qr.add_data(row[0]+";"+classe)
            qr.make(fit=True)

            size = (get_nb_module_version(qr.version)+(border*2))*box_size
            H,W = size,size

            img = qr.make_image()

            background = Image.new('RGBA', (H, W+2*(font_size+4) + 2*box_size), (255,255,255,255))
            draw = ImageDraw.Draw(background)

            font = ImageFont.truetype("Roboto-Regular.ttf",font_size)
            draw.text((H/2,W+(font_size/2)),row[0],(0,0,0),anchor="mm", font=font)
            draw.text((H/2,W+(font_size/2) + font_size+4),classe,(0,0,0),anchor="mm", font=font)
            background.paste(img, (0,0))
            background.save(f'qrcodes/{classe}/{row[0]+"_"+classe}.png')

    