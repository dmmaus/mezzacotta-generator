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
        subs = json.load(json_file)

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

if __name__ == '__main__':
    print(mispell('cat'))
