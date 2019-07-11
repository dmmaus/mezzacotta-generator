# mezzacotta Generator

Source code for the [mezzacotta Generator](http://www.mezzacotta.net/generate/) web page and family of random text generators.

Unlike the predecessors, [mezzacotta Cafe](https://github.com/dmmaus/mezzacotta-cafe) and [mezzacotta Cinematique](https://github.com/dmmaus/mezzacotta-cinematique), this code is designed to be fully generic, extensible, and customisable to any random text generation context, with a common core of categorised vocabulary files.

## Contributing

Contributors are welcome to submit extensions to the menu generating source text files and grammar.

* Fork this repository, add your additions, and submit a pull request.
* You can run each subdirectory's index.php to generate a page of random text, however given the random nature of the generator it may take several runs to see the effects of your changes.

## Authors

* **[Andrew Coker](https://github.com/voidstaroz)** - *Initial work in Python*
* **[David Morgan-Mar](https://github.com/dmmaus)** - *PHP, HTML, and Python modifications*

See also the list of [contributors](https://github.com/dmmaus/mezzacotta-generator/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details

# Documentation

* Core shareable vocabulary files are in the directory `vocabulary`.
* Other directories contain specific generators with PHP index file, base grammar file, and context-dependent vocabulary files (of limited use to other generators).

## Running the generators

The Python generator code `generique.py` takes two arguments:

1. A base vocabulary file name path, without the `.txt` extension. This specifies which text generator to run.
1. A number of lines of text to generate.

**From a web browser:** Place the code into your web server directory, then point your browser at the top level `index.php` file. Your web server will need to allow shell execution of Python from within PHP. You may ned to edit the python path in the subdirectory `index.php` files. The PHP code calls the Python `generique.py` to generate a number of lines, formatted for browser display.

**From the command line:** The `generique.py` script assumes that it is being called from a subdirectory. Change to a generator subdirectory (e.g. `<subdir>` = `test` or `tavern`) and run either:

* `python ../generique.py <subdir>/base <numlines>`
* `php index.php`

## Vocabulary file specification

All vocabulary files (including the base vocabulary file) are text files assumed to have `.txt` extensions. Vocabulary files may contain the following:

* **Comments.** Lines starting with a `#` character are comments, ignored by the parser.
* **Format specifier.** A line starting with `@format` is a format specifier. See "Format specifiers" below.
* **Case specifier.** A line specifying how returned text from the current file is to be capitalised. See "Case specifiers" below.
* **Text, possibly with substitution strings.** Either vocabulary words, or substitution strings starting with a dollar sign. See "Text substitution" below.

### Format specifiers

These are lines starting with `@format`. They tell the parser the format of inflected forms of words in the file. Examples:

* `@format ~` - None of the following text has inflected word forms. Each line is printed as-is.
* `@format ~|S` - The following lines of text may occur in two different inflected forms, as-is, and a form which defaults to as-is concatenated with a letter 's' at the end. This is typical of nouns, and provides a plural form. (Some nouns pluralise in a different way, see below for details.)
* `@format ~|ER|EST` - Three inflected forms, suitable for adjectives with comparative and superlative forms. e.g. {smart, smarter, smartest}. The default comparative is formed by adding 'er' to the end of the word, and the default superlative by adding 'est' to the end of the word. (Some adjectives form comparatives and superlatives in a different way, see below for details.)
* `@format ~|S|ED|ING` Four inflected forms, suitable for verb tenses. e.g. {walk, walks, walked, walking}. (Some verbs are irregular, see below for details.)

Example text lines in various formats:

* `dog` - A noun with a regular plural (`dogs`). The plural does not need to be specified.
* `fox|foxes`, `mouse|mice`, `fish|fish` - Nouns with an irregular plural.
* `smart` - An adjective with regular comparative and superlative forms.
* `big|bigger|biggest`, `bad|worse|worst`, `orange|more_orange|most_orange` - Adjectives with irregular comparative and superlative forms.
* `walk` - A regular verb with fully regular endings.
* `love|loves|loved|loving`, `eat|eats|ate|eating`, `have|has|had|having` - Irregular verbs.

### Case specifiers

These specify how text should be capitalised. A specifier in a given file capitalises the strings it returns (including text generated  by called files lower down the recursion stack), but does not affect text generated by calling files (further up the stack). This enables having text generated with subsections having specific capitalisation. e.g. "The adventurers found the Sword of Truth."

The only case specifier supported so far is:

* `@titlecase`. This specifies that strings returned by the current file will be capitalised in [Title Case](https://en.wiktionary.org/wiki/title_case).

## Text substitution

Text lines may contain words starting with dollar signs. These indicate substitution strings. Example:

* `the $noun` - The parser returns the word `the` followed by a random selection from the vocabulary file `noun.txt`.
* `the $noun_S` - The parser returns the word `the` followed by *the plural form* of a random selection from the vocabulary file `noun.txt`.
* `a $adjective $noun` - The parser returns the word `a` followed by a random selection from the vocabulary file `adjective.txt` followed by a random selection from the vocabulary file `noun.txt`.
* `a $adjective_ER $noun` - The parser returns the word `a` followed by *the comparative form* of a random selection from the vocabulary file `adjective.txt` followed by a random selection from the vocabulary file `noun.txt`.
* `a $adjective_EST $noun` - The parser returns the word `a` followed by *the superlative form* of a random selection from the vocabulary file `adjective.txt` followed by a random selection from the vocabulary file `noun.txt`.
* etc.

If the parser generates the word `a` followed by a word that starts with a vowel, it automatically converts `a` to `an`. It also converts underscores to spaces. (Underscores are sometimes needed in vocabulary files to separate compound words with inflected forms, otherwise the inflection parsing gets confused.)

The parser recursively generates random strings from referenced files until it bottoms out, and then returns the entire generated string.

### Conditional substitution

A dollar sign may be preceded by a digit (1-9). This indicates that the attached substitution string will only be included with probability (digit/10). The script generates a random number between 0 and 1, if it is greater than the probability, then the attached substitution is skipped. This is useful for additional words such as adjectives that you only want to include sometimes, allowing you to tune the frequency of inclusion.

If the substitution string is followed by a `>` character and alternate text, the text following the `>` is treated as an "else" string, and returned if the first substitution is not selected. For example:

* `with 3$number>a thousand meeples` - 30% of the time will return "with three [or some other number from number.txt] thousand meeples" and 70% of the time will return "with a thousand meeples".
