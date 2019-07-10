#!/usr/bin/python
import random
import sys
import uuid

class Vocab:
    # Constructor. Open the specified base file, parse the format specificiation, and load lines.
    def __init__(self, base_spec):
        self.base_spec = base_spec
        self.lines = []
        self.contexts = {}

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

                    if line.startswith('#'):
                        continue

                    if line.startswith('@format'):
                        self.inflections = line[len('@format '):].split('|')
                    else:
                        self.lines.append(line)

                    if line.startswith('^'):
                        self.lines = []
                        self.lines.append(line[1:])
                        break

                f.close()

    # Return a random line, based on an inflection
    def RandomLine(self, inflection = '~', context = None):
        # Determine index of inflection
        missing_inflection = ''
        if not inflection in self.inflections:
            missing_inflection = inflection
            inflection = '~'

        inflection_idx = self.inflections.index(inflection)

        if context is not None and self.contexts.has_key(context):
            line = self.contexts[context]
        else:
            line = self.lines[random.randrange(0, len(self.lines))]
            if context is not None:
                self.contexts[context] = line

        # If there's no inflections in the line, then we form the inflection just by appending.
        # Otherwise, find the specified inflection.
        result = ''
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
                else:
                    result += word + ' '

        return result

class MezzaGenerator:
    def __init__(self):
        self.vocabs = {}
        self.replacements = {
            " .":".", " ,":",", " '":"&rsquo;", " !":"!", " ?":"?", " _":"", " :":":",
            " a a":" an a", " a e":" an e"," a o":" an o"," a u":" an u"," a i":" an i",
            " a A":" an A", " a E":" an E"," a O":" an O"," a U":" an U"," a I":" an I",
            " A A":" An A", " A E":" An E"," A O":" An O"," A U":" An U"," A I":" An I",
            "?.":"?", " )":")", "( ":"(", "_":" "
            }

    # Perform full expansion of a random line from a file
    def Expand(self, spec, caller_context = None):

        if '_' in spec:
            base = spec[:spec.find('_')]
            inflection = spec[spec.find('_') + 1:]
        else:
            base = spec
            inflection = '~'

        if not self.vocabs.has_key(base):
            self.vocabs[base] = Vocab(base)

        randomline = self.vocabs[base].RandomLine(inflection, caller_context)

        result = ''

        context_uuid = uuid.uuid1()
        for word in randomline.split():
            context = ''
            if '=' in word:
                context = word[word.find('=')+1:]
                word = word[:word.find('=')]

            # Words starting with $ are expanded using the file of the corresponding name
            if word.startswith('$'):
                if context:
                    result += self.Expand(word[1:], str(context_uuid) + context)
                else:
                    result += self.Expand(word[1:])
            else:
                result += word + ' '

        return result

    # Expand a random line from a file, and neaten it
    def Generate(self, spec):
        result = self.Expand(spec)
        # Make first letter of result upper case
        result = result[0].upper() + result[1:]

        for key in self.replacements.keys():
            if key in result:
                result = result.replace(key, self.replacements[key])

        # Remove trailing space and return
        return result.rstrip()


if __name__ == '__main__':

    gen = MezzaGenerator()
    # Read base file name from command line.
    basefilename = sys.argv[1]
    # Read number of lines to generate; default to 1.
    if (len(sys.argv) > 2):
        num = int(sys.argv[2])
    else:
        num = 1
    # Generate lines!
    for i in range(num):
        print gen.Generate(basefilename)
