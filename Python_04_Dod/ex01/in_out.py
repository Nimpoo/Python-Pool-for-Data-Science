def square(x: int | float) -> int | float:

    """Square"""

    if (x == 0 or x == 1):
        return x
    return x * x


def pow(x: int | float) -> int | float:

    """Power"""

    if (x == 0 or x == 1):
        return x
    return x**x


def outer(x: int | float, function) -> object:

    """Outer"""

    try:
        count = 0

        def inner() -> float:

            """Inner"""

            nonlocal x, count
            if count == 0:
                count += 1
                return function(x)
            else:
                x = function(x)
                count += 1
                return function(x)
    except Exception as e:
        print(e)
        exit()

    return inner
