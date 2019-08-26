# Description

This is an output of the exercise.

# OS

This code is tested on Windows 10 operating system.

# Build and Installation

Without build and installation, "src/main.py" is available.

If build and installation is needed, follow below instraction:

The package requires a Python version >= 3.0. 

Install the package manually, execute following comands:

```
$ python setup.py build
$ python setup.py install
```


# License

License is free to any person.


# Usage

Execute command is named as "myApp".

Input a file which follows defined format (unique ID and numeric value) by using stdin or by giving an argument. 

After inputting the file, input an integer value to define the parameter X.

Case1: Input a file from stdin: 
```
$ myApp
```
  To finish stdin, put Ctrl + Z, and Enter for Windows system. 

Case2: Input a file from an argument: 

```
$ myApp example_1.txt
```

After reading the file, to define the parameter X put an integer value from stdin.


If the given X is not an integer value, input for X will be required again.

# Test

A directory "tests" include sample input files.

And if extremely a big size of sample file is needed,

execute a python program, "Create_100_million_lines.py" to create it.


