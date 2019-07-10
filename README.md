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

## Grammar and vocabulary file specification

(to be written)
