# py-password-generator

**Version:** 2.0

**Created Date:** 2026-07-18

**Last Updated:** 2026-07-20

**Compatibility:** Python 3.14

**Created By:** Ali Candan ([@webkolog](https://github.com/webkolog))

**Website:** [http://webkolog.net](http://webkolog.net)

**Copyright:** (c) 2026 Ali Candan

**License:** MIT License ([http://mit-license.org](http://mit-license.org))

**py-password-generator** is a secure, interactive command-line utility for generating cryptographically strong passwords.

## Features

* **Cryptographically Secure:** Utilizes the `secrets` module for high-security standards.
* **Customizable:** Choose from four different character sets (Numbers, Letters, Alphanumeric, or Alphanumeric + Symbols).
* **User-Defined Length:** Define exactly how long your password should be.
* **Interactive:** Simple terminal-based user interface.

## Usage

Simply run the script:

```bash
python main.py

```

Follow the on-screen prompts to define your security preferences.

## Docker Support

You can build and run the tool in a container:

```bash
docker build -t py-password-generator .
docker run -it py-password-generator

```

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.