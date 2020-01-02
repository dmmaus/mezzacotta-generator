import mispell
import generique


res = generique.generate(['band/base', '5'])

for word in res:
    word = word.lower()
    m = mispell.mispell(word).strip()
    print('' if m == word else '###', word, '->', m)

