class calculator:

    """
    Calculator class
    """

    def dotproduct(V1: list[float], V2: list[float]) -> None:

        """Dot product"""

        res = 0
        for i in range(len(V1)):
            res += V1[i] * V2[i]
        print("Dot product is:", res)

    def add_vec(V1: list[float], V2: list[float]) -> None:

        """Addition vector"""

        res = []
        for i in range(len(V1)):
            res.append(float(V1[i] + V2[i]))
        print("Add vector is:", res)

    def sous_vec(V1: list[float], V2: list[float]) -> None:

        """Substraction vector"""

        res = []
        for i in range(len(V1)):
            res.append(float(V1[i] - V2[i]))
        print("Add vector is:", res)
