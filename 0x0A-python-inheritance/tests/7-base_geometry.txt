# Doctest document for the 1-my_list module

## Import the BaseGeometry class from the module

    >>> BaseGeometry = __import__("7-base_geometry").BaseGeometry

### Inputs

    >>> bg = BaseGeometry()
    >>> bg.integer_validator("my_int", 12)

### Validate area

    >>> bg.area()
    Traceback (most recent call last):
        ...
    Exception: area() is not implemented

### Validate area doesn't take arguments

    >>> bg.area(1) # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    TypeError:

### Integer_validator empty

    >>> bg.integer_validator() # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    TypeError: 

### If value is not passed to integer_validator

    >>> bg.integer_validator("my_int") # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    TypeError:

### If value is less than 0

    >>> bg.integer_validator("my_int", -11)
    Traceback (most recent call last):
        ...
    ValueError: my_int must be greater than 0

### If value is equal to 0

    >>> bg.integer_validator("my_int", 0)
    Traceback (most recent call last):
        ...
    ValueError: my_int must be greater than 0

### If value is type bool

    >>> bg.integer_validator("my_int", True)
    Traceback (most recent call last):
        ...
    TypeError: my_int must be an integer

### If value is type string

    >>> bg.integer_validator("my_int", "76")
    Traceback (most recent call last):
        ...
    TypeError: my_int must be an integer

### If value is type list

    >>> bg.integer_validator("my_int", [76])
    Traceback (most recent call last):
        ...
    TypeError: my_int must be an integer

### If value is type tuple

    >>> bg.integer_validator("my_int", (76,))
    Traceback (most recent call last):
        ...
    TypeError: my_int must be an integer

### If value is type None

    >>> bg.integer_validator("my_int", None)
    Traceback (most recent call last):
        ...
    TypeError: my_int must be an integer

### If value is type dict

    >>> bg.integer_validator("my_int", {3, 4})
    Traceback (most recent call last):
        ...
    TypeError: my_int must be an integer
