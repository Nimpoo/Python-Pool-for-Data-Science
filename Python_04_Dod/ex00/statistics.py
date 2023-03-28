def ft_statistics(*args: any, **kwargs: any) -> None:

    """
    Statistic calculs
    """

    res = 0

    try:
        for elem in kwargs:
            if len(args) == 0:
                print("ERROR")
            elif (kwargs[elem] == "mean"):
                res = sum(args) / len(args)
                print("mean :", res)
            elif (kwargs[elem] == "median"):
                sort = sorted(args)
                if len(sort) % 2 == 0:
                    res = (sort[len(sort) // 2] + sort[len(sort) // 2 - 1]) / 2
                else:
                    res = sort[len(sort) // 2]
                print("median :", res)
            elif (kwargs[elem] == "quartile"):
                quartile = []
                Q1, Q3 = 0, 0
                sort = sorted(args)
                if len(sort) % 2 == 0 and len(sort) > 2:
                    Q1 = (sort[len(sort) // 2] + sort[len(sort) // 2 - 1]) / 2
                    Q3 = (sort[len(sort) // 2] + sort[len(sort) // 2 + 1]) / 2
                elif len(sort) % 2 == 0 and len(sort) <= 2:
                    Q1 = sort[len(sort) // 2 - 1]
                    Q3 = sort[len(sort) // 2]
                elif len(sort) % 1 == 0 and len(sort) <= 1:
                    Q1 = sort[len(sort) // 2 - 1]
                    Q3 = sort[len(sort) // 2]
                else:
                    Q1 = float(sort[len(sort) // 2 - 1])
                    Q3 = float(sort[len(sort) // 2 + 1])
                quartile = [Q1, Q3]
                print("quartile :", quartile)
            elif (kwargs[elem] == "std"):
                res = (sum((x-(sum(args) / len(args)))**2
                       for x in args) / len(args))**0.5
                print("std :", res)
            elif (kwargs[elem] == "var"):
                mean = sum(args) / len(args)
                res = sum((i - mean) ** 2 for i in args) / len(args)
                print("var :", res)
    except Exception as e:
        print(e)
        exit()
