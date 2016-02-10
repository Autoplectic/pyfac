import numbers

import operator

try:
    reduce
except:
    from functools import reduce

def is_nonneg_int(n):
    """
    Tests if `n` is a non-negative integer.
    """
    # Does python recognize it as a number?
    if not isinstance(n, numbers.Number):
        return False
    # If it is complex, is the imaginary part zero?
    try:
        if n.imag == 0:
            n = n.real
        else:
            return False
    except:
        pass
    # If it is real, is the decimal part zero?
    try:
        if not n.is_integer():
            return False
    except:
        pass
    # Is it non-negative?
    if n < 0:
        return False
    return True

def prod(factors):
    """
    Return the product of all nubmers in `factors`.
    """
    return reduce(operator.mul, factors, 1)

def factorial(n):
    """
    Return the factorial of `n`, n! = $\prod_{i=0}^{n} i$.
    
    Parameters
    ----------
    n : int >= 0
        The number to take the factorial of.
    
    Returns
    -------
    n! : int
        The factorial of `n`.
    
    Raises
    ------
    NotImplementedError:
        Raised if the input is not a non-negative integer.
    """
    if not is_nonneg_int(n):
        raise NotImplementedError("The factorial is only defined for positive integers")
    return prod(range(1, n+1))
