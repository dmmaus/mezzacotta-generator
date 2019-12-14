from getflickr import FlickrGettr
import generique
import random
from PIL import Image, ImageDraw, ImageFont
import glob

# Random generation of a band, album and keywords
res = generique.generate(['band/keywords', 'band/album', 'band/base', '1'])[0]
album_title = res.split('~~')[1].strip()
band_name = res.split('~~')[2].strip()

keywords = []
for a in res.split('~~')[0].split('~'):
    keywords.append(a.strip())

fg = FlickrGettr()
matching_keyword = 'NONE'

# Random adjustments of the album/band
if random.randrange(100) < 20:
    album_title = album_title.lower()
if random.randrange(100) < 15:
    band_name = band_name.upper()

# Randomly split multi-word band names
spaces = len(band_name.split()) - 1
split_name = ''
if random.random() < (spaces * 0.1):
    newline_idx = random.randrange(spaces)
    words = band_name.split()
    idx = 0
    for w in words:
        split_name += w
        if idx == newline_idx:
            split_name += '\n'
        else:
            split_name += ' '
        idx += 1
    band_name = split_name

# Shuffle the keywords, with the ones that appear in the album title appearing first.
present_keywords = []
missing_keywords = []

for keyword in keywords:
    # Prioritise the ones in the actual title
    if album_title.lower().find(keyword.lower()) >= 0:
        present_keywords.append(keyword)
    else:
        missing_keywords.append(keyword)

random.shuffle(present_keywords)
random.shuffle(missing_keywords)
keyword_list = present_keywords + missing_keywords

for keyword in keyword_list:
    if fg.GetKeyword(keyword) != None:
        matching_keyword = keyword
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

# Select fonts for the album and band names, from a local directory.
band_typeface = random.choice(glob.glob('./Fonts/*'))
album_typeface = random.choice(glob.glob('./Fonts/*'))

band_colour = [255, random.randrange(255), random.randrange(128,256)]
random.shuffle(band_colour)

album_color = [255, random.randrange(255), random.randrange(128,256)]
random.shuffle(album_color)

if random.randrange(100) < 40:
    album_color = band_colour
if random.randrange(100) < 20:
    album_typeface = band_typeface

# Draw the band name, trying smaller font sizes if needed
band_font_size = random.randrange(80,160)

done = False
while not done:
    band_font = ImageFont.truetype(band_typeface, band_font_size)
    text_width, text_height = d.textsize(band_name, band_font)
    if text_width > 760:
        band_font_size -= 4
    else:
        done = True

if '\n' in band_name:
    d.multiline_text((20, 20), band_name, font=band_font, fill=tuple(band_colour), spacing=int(band_font_size * 0.2))
else:
    d.multiline_text((400 - (text_width / 2), 20), band_name, font=band_font, fill=tuple(band_colour), spacing=int(band_font_size * 0.2))

# Draw the album name
done = False
album_font_size = 56

while not done:
    album_font = ImageFont.truetype(album_typeface, album_font_size)
    text_width, text_height = d.textsize(album_title, album_font)
    if text_width > 760:
        album_font_size -= 4
    else:
        done = True

text_width, _ = d.textsize(album_title, font=album_font)
d.text((780 - text_width, 720), album_title, font=album_font, fill=tuple(album_color))

cover.save('res.jpg')

# Print useful information
print('Band: ' + band_name.replace('\n', ' ') + ' (' + band_typeface.split('\\')[-1] + ')')
print('Album: ' + album_title + ' (' + album_typeface.split('\\')[-1] + ')')
print('Artwork keyword: ' + matching_keyword)
