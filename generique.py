#!/usr/bin/python
import random
import sys
from datetime import datetime
import math
import re
import string

class Vocab:
    # Constructor. Open the specified base file, parse the format specificiation, and load lines.
    def __init__(self, base_spec):
        self.base_spec = base_spec
        self.lines = []
        self.includes = []
        self.includesize = 0
        self.titlecase = False
        self.inflectionstring = None
        self.quotechance = None

        # Get path and filename of vocabulary file. Path is relative to calling subdirectory.
        if '/' in base_spec:
            filename = '../' + base_spec + '.txt'
        else:
            filename = '../vocabulary/' + base_spec + '.txt'

        try:
            f = open(filename, 'r')
        except IOError:
            self.inflections = ['~']
            self.lines = ['[UNKNOWN FILE: ' + base_spec + ']']
        else:
            with f:
                for line in f:
                    line = line.rstrip()

                    if '#' in line:
                        line = line[:line.find('#')]

                    if line == '':
                        continue

                    if line.startswith('@format'):
                        self.inflectionstring = line[len('@format '):]
                        self.inflections = line[len('@format '):].split('|')
                    elif line.startswith('@titlecase'):
                        self.titlecase = True
                    elif line.startswith('@quoted'):
                        split_line = line.split()
                        if len(split_line) > 1:
                            self.quotechance = float(split_line[1])
                    elif line.startswith('@include'):
                        # create a new vocab object
                        split_line = line.split()
                        if len(split_line) > 1:
                            vocab = Vocab(split_line[1])
                            if vocab.GetInflections() == self.inflectionstring:
                                self.includes.append({'vocab': vocab, 'size': vocab.GetSize()})
                                self.includesize += vocab.GetSize()
                    else:
                        self.lines.append(line)

                    if line.startswith('^'):
                        self.lines = []
                        self.lines.append(line[1:])
                        break

                f.close()

    def GetInflections(self):
        return self.inflectionstring

    def GetSize(self):
        return len(self.lines) + self.includesize

    def RandomRawLine(self):
        rand_idx = random.randrange(0, len(self.lines) + self.includesize)
        range = 0
        line = None
        for include in self.includes:
            range += include['size']
            if rand_idx < range:
                line = include['vocab'].RandomRawLine()
                break;
        if line is None:
            line = self.lines[random.randrange(0, len(self.lines))]
        return line

    # Return a random number based on the dice code
    def RandomNumber(self, code):
        total = 0
        try:
            # Parse code
            (multiplier, code) = code.split("(")
            (lower, code) = code.split(",")
            (upper, adder) = code.split(")")
            if multiplier == "":
                multiplier = 1
            for i in range(int(multiplier)):
                total += random.randint(int(lower), int(upper))
            if adder != "":
                if adder[0] == "+":
                    total += int(adder[1:])
                elif adder[0] == "-":
                    total -= int(adder[1:])
                elif adder[0] == "*":
                    total *= int(adder[1:])
                elif adder[0] == "/":
                    total //= int(adder[1:])
        except ValueError:
            pass
        return str(total)

    # Return a random line, based on an inflection
    def RandomLine(self, inflection = '~'):
        # Determine index of inflection
        missing_inflection = ''
        if not inflection in self.inflections:
            missing_inflection = inflection
            inflection = '~'

        inflection_idx = self.inflections.index(inflection)

        # Choose a random line from the file, or any of its includes.
        line = self.RandomRawLine()

        # If there's no inflections in the line, then we form the inflection just by appending.
        # Otherwise, find the specified inflection.
        result = ''
        if line.startswith('|'):
            result = line[1:]
        else:
            if '|' not in line and inflection != '~':
                result = line + inflection.lower()
            else:
                words = line.split()

                for word in words:
                    if '|' in word:
                        parts = word.split('|')
                        if missing_inflection:
                            result += parts[inflection_idx] + '[UNKNOWN INFLECTION: ' + missing_inflection + '] '
                        else:
                            result += parts[inflection_idx] + ' '

                    # @recentyear command
                    elif word.startswith('@recentyear'):
                        try:
                            scale = int(word[len('@recentyear'):])
                        except ValueError:
                            scale = 1
                        result += str(int(datetime.now().year) + int(scale * math.log(random.random()))) + ' '

                    # @random command
                    elif word.startswith('@random'):
                        result += self.RandomNumber(word[len('@random'):]) + ' '

                    else:
                        result += word + ' '

        if self.quotechance is not None and self.quotechance > random.random():
            result = '\"' + result + '\"' + ' '

        return result

class MezzaGenerator:
    def __init__(self):
        self.vocabs = {}
        self.replacements = {
            " .":".", " ,":",", " '":"'", " !":"!", " ?":"?", " _":"", " :":":", " ;":";",
            " a a":" an a", " a e":" an e"," a o":" an o"," a u":" an u"," a i":" an i",
            " a A":" an A", " a E":" an E"," a O":" an O"," a U":" an U"," a I":" an I",
            " A A":" An A", " A E":" An E"," A O":" An O"," A U":" An U"," A I":" An I",
            " A a":" An a", " A e":" An e"," A o":" An o"," A u":" An u"," A i":" An i",
            "?.":"?", " )":")", "( ":"(", "_":" ", "- ":"-", " -":"-", " +":"", ",,":",",
            "+ ":"", " + ":"", " A the ":" The ", " a the ":" the "
            }

    # Perform full expansion of a random line from a file
    def Expand(self, spec, cap = False):

        non_cap_words = {
            'a', 'an', 'the',                                                       # articles
            'and', 'but', 'for', 'if', 'nor', 'or', 'so', 'yet',                    # conjunctions
            'as', 'at', 'by', 'from' 'in', 'of', 'off', 'on', 'than', 'that', 'then', 'to', 'with'  # prepositions
            }

        if '_' in spec:
            base = spec[:spec.find('_')]
            inflection = spec[spec.find('_') + 1:]
        else:
            base = spec
            inflection = '~'

        if not self.vocabs.has_key(base):
            self.vocabs[base] = Vocab(base)

        # If we are not instructed to capitalize words, check if this vocab specifies to do so
        if not cap:
            cap = self.vocabs[base].titlecase

        # Generate the random line of text
        randomline = self.vocabs[base].RandomLine(inflection)

        result = ''
        # Keep track if the previous word was a plus sign, to handle capitalisation of conjoined words
        plus = False

        for word in randomline.split():
            # Words starting with $ are expanded using the file of the corresponding name
            if '$' in word:
                alt_text = ''
                if '>' in word:
                    alt_text = word[word.find('>') + 1:]
                    word = word[:word.find('>')]

                chance_roll = False
                chance_failed = False
                if word[0].isdigit():
                    chance = int(word[0]) / 10.0
                    wordspec = word[1:]
                    chance_roll = chance > random.random()
                    if not chance_roll:
                        chance_failed = True
                else:
                    wordspec = word

                if word.startswith('$') or chance_roll:
                    result += self.Expand(wordspec[1:], cap = cap and not plus)

                if alt_text != '' and chance_failed:
                    result += alt_text + ' '

                plus = False

            elif word == "+" or word[0] == "-":
                plus = True
                # Go back and capitalise the previous word fragment if necessary
                # Needed to capitalise fragments that are in non_cap_words, when joined with +
                resultlist = result.split()
                # Capitalise if: the second previous word was not also a plus sign; or previous word is the only word
                if cap and ((len(resultlist) > 1 and "+" not in resultlist[-2]) or len(resultlist) == 1):
                    resultlist[-1] = resultlist[-1].capitalize()
                result = string.join(resultlist)
                result += word + ' '

            else:
                if cap and not plus and word not in non_cap_words:
                    word = word.capitalize()
                plus = False
                result += word + ' '

        return result

    # Expand a random line from a file, and neaten it
    def Generate(self, spec):
        result = self.Expand(spec)
        # Make first letter of result upper case
        result = ' ' + result[0].upper() + result[1:]

        for key in self.replacements.keys():
            if key in result:
                result = result.replace(key, self.replacements[key])

        #remove duplicate spaces
        result = re.sub(' +', ' ', result)

        # Remove surrounding space and return
        return result.strip()


if __name__ == '__main__':

    gen = MezzaGenerator()
    # Generate each of the base file names listed on the command line
    bases = sys.argv[1:-1]

    try:
        num = int(sys.argv[-1])
    except ValueError:
        num = 1
        bases = sys.argv[1:]

    for n in range(num):
        for idx in range(len(bases)):
            print gen.Generate(bases[idx]),
            if idx < len(bases) - 1:
                print '~~',
            else:
                print

