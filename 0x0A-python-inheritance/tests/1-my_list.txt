# Doctest document for the 1-my_list module

## Import the MyList Class from the module

    >>> MyList = __import__('1-my_list').MyList

### Inputs

    >>> my_list = MyList()

### Check with empty list

    >>> my_list.print_sorted()
    []

### Append to list

    >>> my_list.append(1)
    >>> my_list.append(4)
    >>> my_list.append(2)
    >>> my_list.append(3)
    >>> my_list.append(5)

### Print list

    >>> print(my_list)
    [1, 4, 2, 3, 5]

### Print sorted list using extended method

    >>> my_list.print_sorted()
    [1, 2, 3, 4, 5]

### Apppend negative numbers and print sorted

    >>> my_list.append(-6)
    >>> my_list.append(-2)
    >>> my_list.append(-27)
    >>> my_list.print_sorted()
    [-27, -6, -2, 1, 2, 3, 4, 5]

### Check print_sorted returns new list

    >>> print(my_list)
    [1, 4, 2, 3, 5, -6, -2, -27]
