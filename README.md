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

**From a web browser:** Place the code into your web server directory, then point your browser at the top level `index.php` file. Your web server will need to allow shell execution of Python from within PHP. You may ned to edit the python path in the subdirectory `index.php` files.

**From the command line:** The `generique.py` script assumes that it is being called from a subdirectory. Change to a generator subdirectory (e.g. `<subdir>` = `test` or `tavern`) and run either:

* `python ../generique.py <subdir>/base <numlines>`
* `php index.php`

## Vocabulary file specification

The Python generator code `generique.py` takes two arguments:

1. A base vocabulary file name path, without the `.txt` extension.
1. A number of lines of text to generate.

All vocabulary files (including the base vocabulary file) are text files assumed to have `.txt` extensions. Vocabulary files may contain the following:

* **Comments.** Lines starting with a `#` character are comments, ignored by the parser.
* **Format specifier.** A line starting with `@format` is a format specifier. See "Format specifiers" below.
* **Case specifier.** (TBD)
* **Text, possibly with substitution strings.** Either vocabulary words, or substitution strings starting with a dollar-sign.

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
* `walk` - A regular verb.
* `love|loves|loved|loving`, `eat|eats|ate|eating`, `have|has|had|having` - Irregular verbs.

Text lines may contain words starting with dollar signs. These indicate substitution strings. Example:

* `the $noun` - The parser returns the word `the` followed by a random selection from the vocabulary file `noun.txt`.
* `the $noun_S` - The parser returns the word `the` followed by *the plural form* of a random selection from the vocabulary file `noun.txt`.
* `a $adjective $noun` - The parser returns the word `a` followed by a random selection from the vocabulary file `adjective.txt` followed by a random selection from the vocabulary file `noun.txt`.
* `a $adjective_ER $noun` - The parser returns the word `a` followed by *the comparative form* of a random selection from the vocabulary file `adjective.txt` followed by a random selection from the vocabulary file `noun.txt`.
* `a $adjective_EST $noun` - The parser returns the word `a` followed by *the superlative form* of a random selection from the vocabulary file `adjective.txt` followed by a random selection from the vocabulary file `noun.txt`.
* etc.
