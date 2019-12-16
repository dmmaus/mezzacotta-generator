from getflickr import FlickrGettr
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps, ImageEnhance
import glob


class AlbumArt():
    def __init__(self, band_name, album_title, keywords):
        self.band_name = band_name
        self.album_title = album_title
        self.keywords = keywords

        self.fg = FlickrGettr()

        # Create canvas for album pic
        self.inverted_colours = random.random() < 0.4

        if self.inverted_colours:
            bg_colour = [255, random.randrange(192, 256), random.randrange(128, 256)]
        else:
            bg_colour = [0, random.randrange(64), random.randrange(128)]
        random.shuffle(bg_colour)
        self.cover = Image.new("RGB", (800,800), tuple(bg_colour))

    def drawBand(self, typeface, colour):
        # Draw the band name, trying smaller font sizes if needed
        d = ImageDraw.Draw(self.cover)
        band_font_size = random.randrange(80, 160)

        done = False
        while not done:
            band_font = ImageFont.truetype(typeface, band_font_size)
            text_width, text_height = d.textsize(self.band_name, band_font)
            if text_width > 760:
                band_font_size -= 4
            else:
                done = True

        if '\n' in self.band_name:
            d.multiline_text((20, 20), self.band_name, font=band_font, fill=colour,
                             spacing=int(band_font_size * 0.2))
        else:
            d.multiline_text((400 - (text_width / 2), 20), self.band_name, font=band_font, fill=colour,
                             spacing=int(band_font_size * 0.2))

    def drawTitle(self, typeface, colour):
        # Draw the album name
        d = ImageDraw.Draw(self.cover)
        done = False
        album_font_size = 56

        while not done:
            album_font = ImageFont.truetype(typeface, album_font_size)
            text_width, text_height = d.textsize(self.album_title, album_font)
            if text_width > 760:
                album_font_size -= 4
            else:
                done = True

        text_width, _ = d.textsize(self.album_title, font=album_font)
        d.text((780 - text_width, 720), self.album_title, font=album_font, fill=colour)

    def filter(self, command, full=False):

        if full:
            x_min, x_max, y_min, y_max = 0, 800, 0, 800
        else:
            # Cut out a random rectangle of the cover art, apply filter, then paste back.
            width = random.randrange(300, 700)
            height = random.randrange(300, 700)
            x_min = random.randrange(800 - width)
            x_max = x_min + width
            y_min = random.randrange(800 - height)
            y_max = y_min + height

        copy = self.cover.copy()
        cropped = copy.crop((x_min, y_min, x_max, y_max))

        if command == 'blur':
            cropped = cropped.filter(ImageFilter.GaussianBlur(random.random() * 2.0))

        if command == 'convolve':
            kernel_weights = [random.gauss(0, 3) for _ in range(9)]
            cropped = cropped.filter(ImageFilter.Kernel((3,3), kernel_weights))

        if command == 'quantize':
            cropped = cropped.quantize(random.randrange(2, 20), 2)

        if command == 'invert':
            cropped = ImageOps.invert(cropped)

        if command == 'grayscale':
            cropped = ImageOps.grayscale(cropped)

        if command == 'posterize':
            cropped = ImageOps.posterize(cropped, 1)

        if command == 'solarize':
            cropped = ImageOps.solarize(cropped, threshold=random.randrange(30, 230))

        if command == 'brightness':
            enhancer = ImageEnhance.Brightness(cropped)
            cropped = enhancer.enhance(0.25 + random.random() * 2.0)

        # Small chance of pasted with shift (but not when using the entire canvas)
        if random.randrange(100) < 15 and not full:
            self.cover.paste(cropped, (x_min + random.randrange(-20,20), y_min + random.randrange(-20,20)))
        else:
            self.cover.paste(cropped, (x_min, y_min))

    def generate(self):
        # Random adjustments of the album/band
        if random.randrange(100) < 20:
            self.album_title = self.album_title.lower()
        if random.randrange(100) < 8:
            self.band_name = self.band_name.upper()

        # Randomly split multi-word band names
        spaces = len(self.band_name.split()) - 1
        split_name = ''
        if random.random() < (spaces * 0.1):
            newline_idx = random.randrange(spaces)
            words = self.band_name.split()
            idx = 0
            for w in words:
                split_name += w
                if idx == newline_idx:
                    split_name += '\n'
                else:
                    split_name += ' '
                idx += 1
            self.band_name = split_name

        # Shuffle the keywords, with the ones that appear in the album title appearing first.
        present_keywords = []
        missing_keywords = []

        for keyword in self.keywords:
            # Prioritise the ones in the actual title
            if self.album_title.lower().find(keyword.lower()) >= 0:
                present_keywords.append(keyword)
            else:
                missing_keywords.append(keyword)

        random.shuffle(present_keywords)
        random.shuffle(missing_keywords)
        keyword_list = present_keywords + missing_keywords

        matching_keyword = 'NONE'
        for keyword in keyword_list:
            if self.fg.GetKeyword(keyword) is not None:
                matching_keyword = keyword
                break;

        art = Image.open('001.jpg')

        width, height = art.size

        # Get a random part of the image up to 800 x 600 pixels and paste it into the album art

        clip_width = min(800, width)
        clip_height = min(600, height)
        cropped = art.crop((0,0,clip_width,clip_height))
        self.cover.paste(cropped, ((800 - clip_width) // 2,100 + (600 - clip_height) // 2))

        # Select fonts for the album and band names, from a local directory.
        band_typeface = random.choice(glob.glob('./Fonts/*'))
        album_typeface = random.choice(glob.glob('./Fonts/*'))

        if self.inverted_colours:
            band_colour = [0, random.randrange(255), random.randrange(128)]
        else:
            band_colour = [255, random.randrange(255), random.randrange(128,256)]
        random.shuffle(band_colour)

        if self.inverted_colours:
            album_colour = [0, random.randrange(255), random.randrange(128)]
        else:
            album_colour = [255, random.randrange(255), random.randrange(128,256)]
        random.shuffle(album_colour)

        if random.randrange(100) < 40:
            album_colour = band_colour
        if random.randrange(100) < 20:
            album_typeface = band_typeface

        # Set up list of commands - it always contains drawing the band and album names, but can include filtering.
        # Shuffle the list and apply them.

        commands = ['band', 'title']
        filter_chances = {
            'convolve': 30,
            'blur': 25,
            'invert': 5,
            'quantize': 30,
            'grayscale': 15,
            'posterize': 10,
            'solarize': 20,
            'brightness': 20
        }

        for c in filter_chances.keys():
            if random.randrange(100) < filter_chances[c]:
                commands.append(c)

        random.shuffle(commands)
        print(commands)

        for command in commands:
            if command == 'band':
                self.drawBand(band_typeface, tuple(band_colour))
            elif command == 'title':
                self.drawTitle(album_typeface, tuple(album_colour))
            else:
                self.filter(command, random.randrange(100) < 25)


        # Print useful information
        print('Band: ' + self.band_name.replace('\n', ' ') + ' (' + band_typeface.split('\\')[-1] + ')')
        print('Album: ' + self.album_title + ' (' + album_typeface.split('\\')[-1] + ')')
        print('Artwork keyword: ' + matching_keyword)

    def emit(self, filename='res.jpg'):
        self.cover.save(filename)
