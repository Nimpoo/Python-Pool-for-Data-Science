def callLimit(limit: int):

    """
    limit the nbr of time function was called
    """

    count = 0

    def callLimiter(function):

        """
        return limited function
        """

        nonlocal count

        def limit_function(*args, **kwargs):

            """
            if it can be called, it was called, sinon error
            """

            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwargs)
            else:
                print("Error:", function, "called too many times")
                return
        return limit_function

    return callLimiter
