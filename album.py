from getflickr import FlickrGettr
import generique
import random
from PIL import Image, ImageDraw, ImageFont


res = generique.generate(['band/keywords', 'band/album', 'band/base', '1'])[0]
album_title = res.split('~~')[1].strip()
band_name = res.split('~~')[2].strip()

keywords = []
for a in res.split('~~')[0].split('~'):
    keywords.append(a.strip())

random.shuffle(keywords)

fg = FlickrGettr()

for keyword in keywords:
    # Prioritise the ones in the actual title
    if album_title.lower().find(keyword.lower()) >= 0:
        if fg.GetKeyword(keyword) != None:
            break;

# Create canvas for album pic
bg_colour = [0, random.randrange(32), random.randrange(64)]
random.shuffle(bg_colour)
cover = Image.new("RGB", (800,800), tuple(bg_colour))
art = Image.open('001.jpg')

width, height = art.size

# Get a random part of the image up to 800 x 600 pixels and paste it into the album art

clip_width = min(800, width)
clip_height = min(600, height)
cropped = art.crop((0,0,clip_width,clip_height))
cover.paste(cropped, ((800 - clip_width) // 2,100 + (600 - clip_height) // 2))


d = ImageDraw.Draw(cover)

# Draw the band name, trying smaller font sizes if needed
if random.randrange(100) < 40:
    band_name = band_name.upper()

band_font_size = 90
band_typeface = random.choice(['cour.ttf', 'ariali.ttf', 'tahoma.ttf', 'lucon.ttf', 'impact.ttf', 'verdana.ttf', 'verdanai.ttf'])

done = False
while not done:
    band_font = ImageFont.truetype(band_typeface, band_font_size)
    text_width, text_height = d.textsize(band_name, band_font)
    if text_width > 760:
        band_font_size -= 4
    else:
        done = True

band_colour = [255, random.randrange(255), random.randrange(128,256)]
random.shuffle(band_colour)

d.text((400 - (text_width / 2), 80 - text_height), band_name, font=band_font, fill=tuple(band_colour))

# Draw the album name
if random.randrange(100) < 20:
    album_title = album_title.lower()

done = False
album_font_size = 56
album_typeface = random.choice(['cour.ttf', 'ariali.ttf', 'tahoma.ttf', 'lucon.ttf', 'impact.ttf', 'verdana.ttf', 'verdanai.ttf'])

while not done:
    album_font = ImageFont.truetype(album_typeface, album_font_size)
    text_width, text_height = d.textsize(album_title, album_font)
    if text_width > 760:
        album_font_size -= 4
    else:
        done = True

album_color = [255, random.randrange(255), random.randrange(128,256)]
random.shuffle(album_color)

text_width, _ = d.textsize(album_title, font=album_font)
d.text((780 - text_width, 720), album_title, font=album_font, fill=tuple(album_color))

cover.save('res.jpg')