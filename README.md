# mezzacotta Generator

Source code for the [mezzacotta Generator](http://www.mezzacotta.net/generate/) web page and family of random text generators.

Unlike the predecessors, [mezzacotta Cafe](https://github.com/dmmaus/mezzacotta-cafe) and [mezzacotta Cinematique](https://github.com/dmmaus/mezzacotta-cinematique), this code is designed to be fully generic, extensible, and customisable to any random text generation context, with a common core of categorised vocabulary files.

## Contributing

Contributors are welcome to submit extensions to the source text files and grammar.

* Fork this repository, add your additions, and submit a pull request.
* You can run each subdirectory's index.php to generate a page of random text, however given the random nature of the generator it may take several runs to see the effects of your changes.

Ideas for generators that we want to make are listed [on the project wiki page](https://github.com/dmmaus/mezzacotta-generator/wiki).

## Authors

* **[Andrew Coker](https://github.com/voidstaroz)** - *Initial work in Python*
* **[David Morgan-Mar](https://github.com/dmmaus)** - *PHP, HTML, and Python modifications*

See also the list of [contributors](https://github.com/dmmaus/mezzacotta-generator/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details

# Documentation

## Environment

* PHP 7.
* Python 3. We use Python 3.6 or 3.7.
* The environment variable `PYTHONIOENCODING=UTF-8` must be set. This enables reading and printing UTF-8 characters without special handling.
* `album.py` requires the following Python packages:
    * flickrapi
    * Pillow
    * opencv-python

## Files

* The main executable file is `generique.py`.
* Core shareable vocabulary files are in the directory `vocabulary`.
* Other directories contain specific generators with PHP index file, base grammar file, and context-dependent vocabulary files (of limited use to other generators).

## Running the generators

The Python generator code `generique.py` takes two or more arguments:

1. The first *N*-1 arguments are base vocabulary file name paths, without the `.txt` extension. These specify which text generators to run. If more than one base file is given, the outputs of the base files are concatenated with a `~~` separator.
1. The final argument is the number of lines of text to generate.

**From a web browser:** Place the code into your web server directory, then point your browser at the top level `index.php` file. Your web server will need to allow shell execution of Python from within PHP. You may ned to edit the python path in the subdirectory `index.php` files. The PHP code calls the Python `generique.py` to generate a number of lines, and then formats the returned lines with HTML for browser display.

**From the command line:** The `generique.py` script assumes that it is being called from the base `generate` directory. Choose a generator subdirectory (e.g. `<subdir>` = `test` or `tavern`) and run either:

* `python generique.py <subdir>/base <numlines>` (n.b. May need `python3` to specify Python 3.)
* `cd <subdir>` followed by `php index.php`

# Vocabulary file specification

All vocabulary files (including the base vocabulary file) are text files assumed to have `.txt` extensions. Vocabulary files may contain lines starting with the following directives:

* `#`: Comments, ignored by the parser.
* `@format`: A format specifier. See "Format specifiers" below.
* `@XXXcase`: Specifies how returned text from the current file is to be capitalised. See "Case specifiers" below.
* `@quoted`: Followed by a decimal probability (0 to 1) that strings returned by the current file will be enclosed in quote marks. Useful if you want "scare quotes" around stuff.
* `@include`: Loads the following named file, as if it were reproduced in full within the current file. The parser checks that the `@format` specifier is the same, otherwise throws an error.
* `@replace`: Specifies a replacement string using the following syntax: `@replace|SEARCH|REPLACE`. Any instances of `SEARCH` in the generated text will be replaced with `REPLACE`. Useful to tweak output that may generate things like "Christmas Day Eve" (`@replace|Day Eve|Eve`).
* `[text]`: Text containing normal vocabulary words and/or replacement strings starting with a dollar sign. See "Text replacement" below. `#` can also be used on the same line to delineate a comment: `[text] # this is a comment`.

### Format specifiers

These are lines starting with `@format`. They tell the parser the format of inflected forms of words in the file. Examples:

* `@format ~` - None of the following text has inflected word forms. Each line is printed as-is.
* `@format ~|S` - The following lines of text may occur in two different inflected forms, as-is, and a form which defaults to as-is concatenated with a letter 's' at the end. This is typical of nouns, and provides a plural form. (Some nouns pluralise in a different way, see below for details.)
* `@format ~|ER|EST` - Three inflected forms, suitable for adjectives with comparative and superlative forms. e.g. {smart, smarter, smartest}. The default comparative is formed by adding 'er' to the end of the word, and the default superlative by adding 'est' to the end of the word. (Some adjectives form comparatives and superlatives in a different way, see below for details.)
* `@format ~|S|ED|ING` Four inflected forms, suitable for verb tenses. e.g. {walk, walks, walked, walking}. (Some verbs are irregular, see below for details.)

Example text lines in various formats:

* `dog` - A noun with a regular plural formed simply by appending `s` (`dogs`). The plural does not need to be specified.
* `fox|foxes`, `mouse|mice`, `fish|fish` - Nouns with an irregular plural.
* `|butter` - Noun with no plural form (a mass noun). This syntax ignores all inflections and always returns the word as given.
* `smart` - An adjective with regular comparative and superlative forms (`smarter|smartest`).
* `big|bigger|biggest`, `bad|worse|worst`, `orange|more_orange|most_orange` - Adjectives with irregular comparative and superlative forms. (`bigger` and `biggest` require an extra `g` to be inserted.)
* `walk` - A regular verb with fully regular inflection endings (`walks|walked|walking`).
* `love|loves|loved|loving`, `eat|eats|ate|eating`, `have|has|had|having` - Irregular and irregularly spelt verbs.

### Case specifiers

These specify how text should be capitalised. By default, the generated text has the first letter capitalised, but no other letters are changed.

A specifier in a given file capitalises the strings it returns (including text generated  by called files lower down the recursion stack), but does not affect text generated by calling files (further up the stack). This enables having text generated with subsections having specific capitalisation. e.g. "The adventurers found the Sword of Truth."

The only case specifier supported so far is:

* `@titlecase`: This specifies that strings returned by the current file will be capitalised in [Title Case](https://en.wiktionary.org/wiki/title_case).

## Text replacement

Text lines may contain words starting with dollar signs. These indicate replacement strings. Example:

* `the $noun` - The parser returns the word `the` followed by a random selection from the vocabulary file `noun.txt` in the `vocabulary` subdirectory.
* `the <subdir>/$noun` - The parser returns the word `the` followed by a random selection from the vocabulary file `noun.txt` in the `<subdir>` subdirectory.
* `the $noun_S` - The parser returns the word `the` followed by *the plural form* of a random selection from the vocabulary file `noun.txt`. (n.b. the plural forms must be defined in `noun.txt` - they are not automatically generated)
* `a $adjective $noun` - The parser returns the word `a` followed by a random selection from the vocabulary file `adjective.txt` followed by a random selection from the vocabulary file `noun.txt`.
* `a $adjective_ER $noun` - The parser returns the word `a` followed by *the comparative form* of a random selection from the vocabulary file `adjective.txt` followed by a random selection from the vocabulary file `noun.txt`.
* `a $adjective_EST $noun` - The parser returns the word `a` followed by *the superlative form* of a random selection from the vocabulary file `adjective.txt` followed by a random selection from the vocabulary file `noun.txt`.
* etc.

The parser recursively generates random strings from referenced files until it bottoms out, and then returns the entire generated string.

There are also special @-commands that produce substituted text. The `N` in each command may be any positive integer:

* `@randomN(A,B)+C` - Generates a random integer using the formula: (*N* die rolls of (a random integer from *A* to *B* inclusive)) + *C*. As well as `+`, the following operators are supported: `-`, `*`, `/` (performs integer division).
* `@recentyearN` - Generates a year number in the past, biased towards more recent years, and substitutes it in place. `N` is a number, which is interpreted as a scale factor for the logarithmic probability distribution. Most years generated will be within *N* years of the present, but there is a long low probability tail.
* `@setN(A,B,C...)` - Generates a randomly permuted combination of *N* items from the set A,B,C... (formatted with commas and a penultimate 'and')

### Saving variable state

Randomly generated strings may be saved so that they can be reused later in the same text. This is useful to refer back to the same random element.

* `$noun=FOO` - Saves the generated noun into a variable named `FOO`.
* `*FOO` - Substitues the saved value of `FOO` into the generated string.

Example: `Players get a $fruit=FRUIT. If they eat the *FRUIT, they win.` might generate "Players get a banana. If they eat the banana, they win."

Currently it is not possible to save/reuse multiple inflections.

### Automatic replacements

As a final pass, there are some automatic string replacements made to tidy up the generated text.

* If the parser generates the word `a` followed by a word that starts with a vowel, it automatically converts `a` to `an`.
* Underscores are converted to spaces. (Underscores are sometimes needed in vocabulary files to separate compound words with inflected forms, otherwise the inflection parsing gets confused.)
* Spaces around hyphens are removed. This is so you can specify prefixes and suffixes with hyphens. For example, `super-` as an adjective, and have the string `super-badger` returned without a space after the hyphen.
* Plus signs and spaces around them are removed. This is so you can specify prefixes and suffixes that join onto words without hyphens. For example, `super+` as an adjective, and have the string `superbadger` returned without a space or hyphen.
* Spaces before certain punctuation (`. , ? ! ' : ; )`) and spaces after open parentheses (`(`) are removed.
* Doubled up punctuation is reduced to a single punctuation character. Conflicting punctuation is resolved to the "strongest" character - e.g. `.!` becomes `!`.

### The difference between includes and replacements

Example: We have two text files:

```
# dinosaur.txt
@format ~|S
diplodocus|diplodocuses
Tyrannosaurus rex|rexes
```

```
# mammal.txt
@format ~|S
cat
dog
horse
rabbit
```

We want to make a file `animal.txt` that could select either dinosaurs or mammals, we could do either:

```
# animal.txt
@format ~|S
$dinosaur
$mammal
```

which would select a dinosaur 50% of the time and a mammal 50% of the time (i.e. diplodocus and T. Rex have probability 1/4, while cat, dog, horse, and rabbit all have probability 1/8), or:

```
# animal.txt
@format ~|S
@include dinosaur
@include mammal
```

which would select each animal with equal probability 1/6.

## Conditional text

Text may be preceded by a string of one or more digits. This indicates that the following text will only be included with probability 0.<digit_string>. The script generates a random number between 0 and 1, if it is greater than the probability, then the attached text is skipped. This is useful for additional words such as adjectives that you only want to include sometimes, allowing you to tune the frequency of inclusion.

If the text is followed by a `>` character and alternate text, the text following the `>` is treated as an "else" string, and returned if the first text is not selected.

Either text can be a replacement string beginning with $ as specified above. The text in a conditional cannot contain spaces; use underscores in place of spaces - they will be replaced with spaces by the parser.

Examples:

* `4really good` - 40% chance of returning "really good"; 60% chance of returning "good".
* `4really>very good` - 40% chance of returning "really good"; 60% chance of returning "very good".
* `4$adj>really_very good` - 40% chance of returning "[random adjective] good"; 60% chance of returning "really very good".

## Testing markers

If a line begins with the caret character `^`, it is always selected, rather than a random selection being made form that file. Output produced by this selection is surrounded by `#####` markers, as a reminder that it has been selected over other random possibilities.

Using the `^` marker on a line that calls itself produces an infinite loop, which the generator will detect and exit after a number of iterations. Try not to do this.

## PHP

The sample PHP code demonstrates how to call the Python generator and format returned lines into HTML. `dish/index.php` shows an example of HTML formatting output from multiple base generators in a single Python call.

The sample PHP code does the following replacements:

* Apostrophes are replaced with curly apostrophes. (We may remove this and rely on curly apostrophes in the vocabulary files.)
* Characters `&`, `<`, `>` are replaced with their respective HTML entities: `&amp;`, `&lt;`, `&gt;`.

PHP is also responsible for the HTML page styling, which can be customised for each generator.
