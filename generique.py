#!/usr/bin/python
import random
import sys
from datetime import datetime
import math
import re
import string
import collections

def CapIt(s):
    if not s.startswith('^'):
        return '^' + s
    return s

def UnCapIt(s):
    return s.replace('^', '')

# Make first letter of string a capital letter
# Ignore spaces and HTML smart quote identities at start of string
def Capitalise(s):
    if len(s) > 1:
        if s.startswith("&ldquo;"):
            if len(s) > 7:
                return "&ldquo;" + Capitalise(s[7:])
            else:
                return "&ldquo;"
        elif re.match('^&.acute;', s):
            return re.sub('^&(.)acute;', lambda match:'&'+match.group(1).upper()+'acute;', s)
        elif re.match('^&.circ;', s):
            return re.sub('^&(.)circ;', lambda match:'&'+match.group(1).upper()+'circ;', s)
        elif re.match('^&.grave;', s):
            return re.sub('^&(.)grave;', lambda match:'&'+match.group(1).upper()+'grave;', s)
        elif re.match('^&.ring;', s):
            return re.sub('^&(.)ring;', lambda match:'&'+match.group(1).upper()+'ring;', s)
        elif re.match('^&.uml;', s):
            return re.sub('^&(.)uml;', lambda match:'&'+match.group(1).upper()+'uml;', s)
        else:
            if s.startswith(" "):
                return " " + Capitalise(s[1:])
            else:
                return s[0].upper() + s[1:]
    else:
        return s.upper()


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
        self.vocab_replacements = {}

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
                    elif line.startswith('@replace'):
                        # add specified replacements to the local vocabulary replacements dictionary
                        split_line = line.split('|')
                        if len(split_line) == 3:
                            self.vocab_replacements[split_line[1]] = split_line[2]
                    else:
                        self.lines.append(line)

                    if line.startswith('^'):
                        self.lines = []
                        self.lines.append('##### ' + line[1:] + ' #####')
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

    def GetStoreChoices(self):
        result = {}
        for cmd in self.store_cmds:
            v = Vocab(cmd['spec'])
            result[cmd['var']] = v.RandomLine(v.GetInflections().split('|'))
        return result

    # Return a random line, based on a list of inflections.
    def RandomLine(self, inflections = ['~']):
        if not isinstance(inflections, list):
            inflections = [inflections]

        line = self.RandomRawLine()
        results = {} # dictionary for returning results of multiple inflections

        universal_inflection = False
        if line.startswith('|'):
            universal_inflection = True
            line = line[1:]

        for inflection in inflections:
            if inflection not in self.inflections:
                results[inflection] = '[MISSING INFLECTION: ' + inflection + ' IN FILE: ' + self.base_spec + ']'
                continue
            inflection_idx = self.inflections.index(inflection)
            result = ''
            if universal_inflection:
                result = line
            else:
                # There's a bug here: if there's no '|' in the file, but the line ends in a word with $, it appends the inflection and gets an unknown file.
                if '|' not in line and inflection != '~':
                    result = line + inflection.lower() + ' '
                else:
                    words = line.split()

                    while words:
                        word = words.pop(0)

                        if '|' in word:
                            parts = word.split('|')
                            try:
                                result += parts[inflection_idx] + ' '
                            except IndexError:
                                print "[ERROR: NOT ENOUGH INFLECTIONS. FILE: " + self.base_spec + ": " + word + "]"
                                sys.exit()

                        # @recentyear command
                        elif word.startswith('@recentyear'):
                            try:
                                scale = int(word[len('@recentyear'):])
                            except ValueError:
                                scale = 1
                            year = int(datetime.now().year) + int(scale * math.log(random.random()))
                            if (year > 0):
                                # AD
                                result += str(year) + ' '
                            else:
                                # BC
                                result += str(1 - year) + ' B.C. '

                        # @random command
                        elif word.startswith('@random'):
                            result += self.RandomNumber(word[len('@random'):]) + ' '

                        # @set command
                        elif word.startswith('@set'):
                            word = word[len('@set'):]

                            picks_string = ''
                            while word[0].isdigit():
                                picks_string += word[0]
                                word = word[1:]
                            num_picks = int(picks_string)

                            selections = word[1:len(word)-1].split(',')
                            if num_picks > len(selections):
                                num_picks = len(selections)

                            random.shuffle(selections)

                            # re-insert the selections to the front of the remaining words
                            new_words = []
                            for i in range(num_picks):
                                if i < num_picks - 2:
                                    new_words.append(selections[i] + ' , ')
                                elif i == num_picks - 2:
                                    new_words.append(selections[i] + ' and ')
                                else:
                                    new_words.append(selections[i])

                            words = new_words + words

                        # @uptoset command
                        elif word.startswith('@uptoset'):
                            word = word[len('@uptoset'):]

                            picks_string = ''
                            while word[0].isdigit():
                                picks_string += word[0]
                                word = word[1:]
                            num_picks = random.randint(2,int(picks_string)+1)

                            selections = word[1:len(word)-1].split(',')

                            if num_picks > len(selections):
                                num_picks = len(selections)

                            random.shuffle(selections)

                            new_words = selections[:num_picks]

                            # re-insert the selections to the front of the remaining words
                            words = new_words + words


                        else:
                            result += word + ' '

            if self.quotechance is not None and self.quotechance > random.random():
                # add smart quotes HTML entities around the result, with spaces to avoid messing up replacements
                result = "&ldquo; " + result.rstrip() + " &rdquo;" + ' '

            results[inflection] = result

        if len(inflections) == 1:
            return results[inflections[0]], self.vocab_replacements
        else:
            return results, self.vocab_replacements


class MezzaGenerator:
    def __init__(self):
        self.vocabs = {}
        self.replacements = collections.OrderedDict([
            (" ^+",""), ("^ ","^"), ("^'","'"), (" ^&rdquo;","&rdquo;"),
            (" .","."), (" ,",","), (" '","'"), (" !","!"), (" ?","?"), (" :",":"), (" ;",";"),
            (" a a"," an a"),(" a e"," an e"),(" a o"," an o"),(" a u"," an u"),(" a i"," an i"),
            (" a A"," an A"),(" a E"," an E"),(" a O"," an O"),(" a U"," an U"),(" a I"," an I"),
            (" A A"," An A"),(" A E"," An E"),(" A O"," An O"),(" A U"," An U"),(" A I"," An I"),
            (" A a"," An a"),(" A e"," An e"),(" A o"," An o"),(" A u"," An u"),(" A i"," An i"),
            (" A the "," The "),(" a the "," the "),
            ("?.","?"),("!.","!"),("?'","? '"),("!'","! '"),(".'",". '"),
            (" )",")"),("( ","("),("- ","-"),(" -","-"),(" +",""),(",,",","),
            ("+ ",""), (" + ",""),
            ("&ldquo; ","&ldquo;"), (" &rdquo;","&rdquo;"),
            (" _",""), ("_ ", ""), ("_"," "), ("--", " - "), ("..", ".")
            ])

    def appendResult(self, a, b, varname):
        if varname is None:
            return a + b
        else:
            b = b.replace('^', '')
            return a + '{' + varname + ':'+ b.rstrip() + '} '

    # Perform full expansion of a random line from a file
    def Expand(self, spec, cap = False):

        non_cap_words = {
            'a', 'an', 'the',                                                       # articles
            'and', 'but', 'for', 'if', 'nor', 'or', 'so', 'yet',                    # conjunctions
            'as', 'at', 'by', 'from' 'in', 'of', 'off', 'on', 'than', 'that', 'then', 'to', 'with', 'vs'  # prepositions
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
        (randomline, vocab_replacements) = self.vocabs[base].RandomLine(inflection)
        # Add the vocabulary file replacements to the end of the ordered replacement dictionary
        for key in vocab_replacements.keys():
            self.replacements[key] = vocab_replacements[key]

        result = ''
        # Keep track if the previous word was a plus sign, to handle capitalisation of conjoined words
        plus = False

        for word in randomline.split():
        
            # First see if the word is a conditional (starts with a digit) and resolve the conditional probability
            # Don't trigger conditional parsing if the word is a pure integer number
            if word[0].isdigit() and not word.isdigit():
                # Grab the number at the start of the string (if any)
                chance_substring = ''
                while word[0].isdigit():
                    chance_substring += word[0]
                    word = word[1:]

                alt_text = ''
                if '>' in word:
                    alt_text = word[word.find('>') + 1:]
                    word = word[:word.find('>')]

                if chance_substring != '':
                    chance = int(chance_substring) / float(10 ** len(chance_substring))
                    if random.random() > chance:
                        word = alt_text


            # Any part after '=' is the variable name to record for post-processig.
            varname = None
            if '=' in word:
                varname = word[word.find('=') + 1:]
                word = word[:word.find('=')]

            # Words starting with $ are expanded using the file of the corresponding name
            if '$' in word:
                expansion = self.Expand(word[1:], cap = cap and not plus)
                result = self.appendResult(result, expansion, varname)
                plus = False

            elif varname is not None:
                result = self.appendResult(result, word, varname)

            elif word != '' and (word == "+" or word[0] == "-"):
                plus = True
                # Go back and capitalise the previous word fragment if necessary
                # Needed to capitalise fragments that are in non_cap_words, when joined with +
                resultlist = result.split()
                # Capitalise if: the second previous word was not also a plus sign; or previous word is the only word
                if cap and ((len(resultlist) > 1 and "+" not in resultlist[-2]) or len(resultlist) == 1):
                    resultlist[-1] = CapIt(resultlist[-1])
                result = string.join(resultlist)
                result += word + ' '

            else:
                if len(word) > 1 and cap and not plus and word not in non_cap_words:
                    word = CapIt(word)
                plus = False
                result += word + ' '

        return result

    # Expand a random line from a file, and neaten it
    def Generate(self, spec, debug=False):
        result = ' ' + self.Expand(spec)
        
        # remove duplicate spaces
        result = re.sub(' +', ' ', result)
        
        # Do the general replacements and custom replacements
        if debug:
            print "PRE-REPLACEMENTS: " + result
        for (key, value) in self.replacements.items():
            if key in result:
                result = result.replace(key, value)

        # remove duplicate spaces again - more may have been inserted by custom replacements
        result = re.sub(' +', ' ', result)
        
        # Strip leading space and any trailing spaces
        # Needs to be after the replacements to ensure the a->an replacement works at start of result
        result = result.strip()

        return result.strip()

# Post process the combined result of all the specified bases, harvesting any declarations and substituting them
# when indicated by *
def PostProcess(input_str):
    text = input_str
    result = ''

    d = {}

    # Assemble dictionary of replacements
    while '{' in text:
        pos1 = text.find('{')
        pos2 = text.find('}')

        dec = text[pos1 + 1:pos2]
        if ':' in dec:
            key = dec[:dec.find(':')]
            d[key] = dec[dec.find(':')+1:]

        if pos1 == 0:
            pre = ''
        else:
            pre = text[:pos1 - 1]
        post = text[pos2 + 1:]

        text = pre + post

    # Do the replacements
    for key in d.keys():
        # Insert ^ before each word of a replacement string if to be capitalised
        text = re.sub('\^\*' + key, '^' + d[key].replace(' ', ' ^'), text)
        # otherwise just do the replacement
        text = re.sub('\*' + key, d[key], text)

    return text

def ProcessCaps(input_str):
    s = input_str
    while '^' in s:
        pos = s.find('^')
        pre = s[:pos]
        post = s[pos + 1:]
        s = pre + Capitalise(post)

    return s


def generate(args):
    gen = MezzaGenerator()
    # Generate each of the base file names listed on the command line
    bases = args[0:-1]

    debug = False
    if bases[0] == '-d':
        bases.pop(0)
        debug = True

    try:
        num = int(args[-1])
    except ValueError:
        num = 1
        bases = args[1:]

    for n in range(num):
        result = ''
        for idx in range(len(bases)):
            result += gen.Generate(bases[idx])
            if idx < len(bases) - 1:
                result += ' ~~ '

        if '{' in result:
            if debug:
                print "PRE-POSTPROCESS: " + result
            result = PostProcess(result)

        if '^' in result:
            if debug:
                print "PRE-PROCESSCAPS: " + result
            result = ProcessCaps(result)

        # Make sentence case by default
        result = Capitalise(result)
        # capitalise first non-space character after each sentence-ending punctuation mark
        if '. ' in result:
            bits = []
            for bit in result.split('. '):
                bits.append(Capitalise(bit))
            result = '. '.join(bits)
        if '! ' in result:
            bits = []
            for bit in result.split('! '):
                bits.append(Capitalise(bit))
            result = '! '.join(bits)
        if '? ' in result:
            bits = []
            for bit in result.split('? '):
                bits.append(Capitalise(bit))
            result = '? '.join(bits)
        if '~~ ' in result:
            bits = []
            for bit in result.split('~~ '):
                bits.append(Capitalise(bit))
            result = '~~ '.join(bits)

        print result


if __name__ == '__main__':
    generate(sys.argv[1:])

