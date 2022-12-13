# mypy
A library that makes using the Python Interpreter more convenient for Neural Network testing and training.
## Usage

Import the functionalities.
```python
>>> from mypy import *
```

### Functionalities

- The ability to asynchronously run functions, and query the changing variables in the function/class.
```python
>>> async_run(func_name, *args, **kwargs)
```
To query the changing variables, the function should use function attributes:
```python
>>> def func_name():
...     func_name.x = 0
...     while True:
...         func_name.x += 1
>>> async_run(func_name)
>>> print(func_name.x)
```

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
echo "# mypy python package" >> ~/.bashrc
echo "alias extout='python3 $PWD/extout.py'" >> ~/.bashrc
```
