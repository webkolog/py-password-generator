# py-password-generator

[](https://opensource.org/licenses/MIT)

**Version:** 1.0

**Last Updated:** 2026-07-18

**Compatibility:** Python 3.14

**Created By:** Ali Candan ([@webkolog](https://github.com/webkolog))

**Website:** [http://webkolog.net](http://webkolog.net)

**Copyright:** (c) 2026 Ali Candan

**License:** MIT License ([http://mit-license.org](http://mit-license.org))

**py-password-generator** is a simple, lightweight Python tool designed to generate secure, random alphanumeric passwords. It is perfect for developers who need a quick utility to create temporary passwords or unique keys.

## Installation

Ensure you have Python installed. You can clone this repository to your local machine:

```bash
git clone https://github.com/webkolog/py-password-generator.git
cd py-password-generator

```

## Usage

### Running the Script

Simply run the script using the Python interpreter:

```bash
python generator.py

```

This will output a randomly generated 8-character alphanumeric string to your terminal.

### Using with Docker

If you prefer to run it in a containerized environment, you can use the provided Dockerfile:

```bash
docker build -t py-password-generator .
docker run --rm py-password-generator

```

## Features

* **Lightweight:** No external dependencies required.
* **Secure:** Uses Python's standard `random` and `string` libraries.
* **Customizable:** You can easily modify the length variable in `generator.py` to generate longer or shorter passwords.

## Example Output

```text
Your secure password:
aB3dE9fG

```

## Customization

To change the password length, edit the `generator.py` file:

```python
# Change the range value for a different length
password = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(12)) 

```

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please feel free to open an issue or submit a pull request on the GitHub repository.

## License

This project is open-source software licensed under the [MIT license](https://mit-license.org/).

Copyright (c) 2026 Ali Candan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Support

For any questions or support, you can refer to the project's GitHub repository or contact the author via [webkolog.net](http://webkolog.net).
