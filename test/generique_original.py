#!/usr/bin/python
import random
import uuid

class Vocab:
    # Constructor. Open the specified base file, parse the format specificiation, and load lines.
    def __init__(self, base_spec):
        self.base_spec = base_spec
        self.lines = []
        self.contexts = {}

        try:
            f = open(base_spec + '.txt', 'r')
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

        res = ''

        if context is not None and self.contexts.has_key(context):
            line = self.contexts[context]
        else:
            line = self.lines[random.randrange(0, len(self.lines))]
            if context is not None:
                self.contexts[context] = line
        words = line.split()

        for word in words:
            if '|' in word:
                parts = word.split('|')
                if missing_inflection:
                    res += parts[inflection_idx] + '[UNKNOWN INFLECTION: ' + missing_inflection + '] '
                else:
                    res += parts[inflection_idx] + ' '
            else:
                res += word + ' '

        return res

class MezzaGenerator:
    def __init__(self):
        self.vocabs = {}
        self.replacements = {" .":".", " ,":",", " !":"!", " ?":"?", " _":"", " :":":",
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

        res = ''

        context_uuid = uuid.uuid1()
        for word in randomline.split():
            context = ''
            if '=' in word:
                context = word[word.find('=')+1:]
                word = word[:word.find('=')]

            if '$' in word:
                if context:
                    res += self.Expand(word[1:], str(context_uuid) + context)
                else:
                    res += self.Expand(word[1:])
            else:
                res += word + ' '

        return res

    #Expand a random line from a file, and neaten it
    def Generate(self, spec):
        res = self.Expand(spec)
        res = res[0].upper() + res[1:]

        for key in self.replacements.keys():
            if key in res:
                res = res.replace(key, self.replacements[key])

        return res


if __name__ == '__main__':

    gen = MezzaGenerator()
    for i in range(10):
        print gen.Generate('sentence')