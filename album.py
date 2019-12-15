from albumart import AlbumArt
import generique

# Random generation of a band, album and keywords
res = generique.generate(['band/keywords', 'band/album', 'band/base', '1'])[0]
album_title = res.split('~~')[1].strip()
band_name = res.split('~~')[2].strip()

keywords = []
for a in res.split('~~')[0].split('~'):
    keywords.append(a.strip())

album = AlbumArt(band_name, album_title, keywords)
album.generate()
album.emit()