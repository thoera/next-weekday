# Installation and usage

Clone the repository:

```sh
git clone git@github.com:thoera/next-weekday.git
cd next-weekday
```

Create a new virtual environment and activate it:

```sh
python3 -m venv venv
. venv/bin/activate
```

Install the package (in development mode) :

```sh
pip install --editable .
```

Try to use it:

```sh
python -m next_weekday
```

Or with some arguments:

```sh
python -m next_weekday --date 2023-04-20 --weekday saturday
```

You could also build the wheel and install it.

With hatch:

```sh
pip install hatch
hatch build --target wheel
pip install dist/next_weekday-1.0.0-py3-none-any.whl
```
