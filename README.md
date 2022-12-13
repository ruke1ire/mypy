# mypy

A library that makes using the Python Interpreter more convenient for Neural Network testing and training.

## Usage

Import the functionalities.
```python
>>> from mypy import *
```

### Functionalities

- The ability to asynchronously run functions, and query the changing variables in the function/class.

- The ability to write a function/class in a separate file, and import it without having to restart the python kernel.
```python
>>> reload()
```

- The abilty to restart the kernel and clear out all declared variables.
```python
>>> refresh()
```

- The ability to print on a different terminal.
```console
echo 'On another terminal'
python3 -m mypy.extout
```
```python
print('Hello different terminal...')
```

## Install 

```console
git clone https://github.com/ruke1ire/mypy.git
cd mypy
pip3 install .
```
