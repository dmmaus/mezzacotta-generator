# Function to mispell (sic) a word, based on a dictionary of substitutions.
import random
import json


def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start


def mispell(word):

    word = '_' + word + '_'
    res= word

    with open('subs.txt') as json_file:
        try:
            subs = json.load(json_file)
        except ValueError as e:
            print("Invalid JSON file")
            return res[1:-1]

    subs_key_list = list(subs.keys())
    random.shuffle(subs_key_list)

    for s in subs_key_list:
        n = word.count(s)
        if n > 0:
            idx = random.randrange(n)
            start = find_nth(word, s, idx + 1)
            res = word[:start] + subs[s] + word[start + len(s):]
            break

    return res[1:-1]


def umlautify(word):
    letters = list(word)
    res = ''

    d = {
        'a': (20, ['ä', 'ä', 'à', 'á', 'â', 'å'),
        'e': (20, ['ë', 'ë', 'è', 'é', 'ê']),
        'i': (10, ['ï', 'ï', 'ì', 'í', 'î']),
        'o': (40, ['ö', 'ö', 'ö', 'ö', 'ò', 'ó', 'ô', 'ø']),
        'u': (30, ['ü', 'ü', 'ü', 'ù', 'ú', 'û'])
    }

    for letter in letters:
        cap = letter.isupper()
        letter = letter.lower()

        if letter in d.keys() and random.randrange(100) < d[letter][0]:
            letter = random.choice(d[letter][1])

        if cap:
            letter = letter.upper()

        res += letter

    return res


if __name__ == '__main__':
    print(umlautify('now with added umlauts'))

