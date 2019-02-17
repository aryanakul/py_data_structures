"""
Here I define a new exception class 'Empty' which I will raise when somebody
tries to perform 'top' or 'pop' operation on an empty Stack.
"""


class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass
