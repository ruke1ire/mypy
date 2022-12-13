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
>>> reload(package_name)
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

- The ability to restart the kernel and clear out all declared variables.
```python
>>> refresh()
```

- The ability to print on a different terminal.
```console
extout # or python3 extout.py
```
print() on the main python interpreter will be relayed to extout:
```python
print('Hello different terminal...')
```

## Install 

```console
git clone https://github.com/ruke1ire/mypy.git
cd mypy
pip3 install .
echo "# mypy python package" >> ~/.bashrc
echo "alias extout='python3 $PWD/extout.py'" >> ~/.bashrc
```
