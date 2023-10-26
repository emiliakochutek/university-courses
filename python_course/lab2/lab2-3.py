import doctest

# Chcemy napisać funkcję sprawdzającą, czy ciąg jest ciągiem geometrycznym. Zakładamy, że argumentem funkcji będą tylko 
# ciągi składające się z liczb całkowitych, nie będzie więc potrzeby wykonywania operacji zmiennoprzecinkowych. 
# Zaproponuj testy dla tej funkcji w dwóch wersjach:

#     za pomocą serii instrukcji assert,
#     w docstringu.

# Napisz funkcje spełniającą Twoje testy.

def jestGeometryczny(seq):
    """
    >>> jestGeometryczny([])
    True
    >>> jestGeometryczny([-10])
    True
    >>> jestGeometryczny(1000 * [0] + [1])
    False
    """

    if not seq or set(seq) == 0:
        return True
    if seq[0] == 0 and len(set(seq)) > 1:
        return False
    for _ in range(len(seq)-2):
        if not (seq[_] * seq[_ + 2]) == (seq[_ + 1])**2:
            return False
    return True

assert jestGeometryczny([])
assert jestGeometryczny([-10])
assert jestGeometryczny((3, -6, 12))
assert jestGeometryczny([1, 2, 4, 8, 16])
assert jestGeometryczny([2, -2, 2, -2, 2, -2, 2])
assert jestGeometryczny([3, 3, 3, 3, 3, 3])
assert jestGeometryczny([0, 0, 0, 0])
assert jestGeometryczny([1, 0, 0, 0])
assert jestGeometryczny([8, 12, 18, 27])
assert not jestGeometryczny([1, 2, 4, 8, 17])
assert not jestGeometryczny([0, 1])
assert not jestGeometryczny(1000 * [0] + [1])


doctest.testmod(verbose = True)
