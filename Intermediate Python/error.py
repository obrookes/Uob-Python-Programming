def addArrays(a, b):
    """Function to add together the two passed arrays, returning
       the result."""

    if len(a) != len(b):
        raise ValueError("Both arrays must have the same length.")

    c = []

    for a_, b_ in zip(a, b):
        c.append(a_ + b_)

    return c

if __name__ == "__main__":

    # this is runtime testing!

    a = [1, 2]
    b = [3, 4, 5]

    try:
        c = addArrays(a, b)
    except ValueError:
        # or print("Something went wrong here...")
        while(len(a) > len(b)):
            b.append(0)
        while(len(a) < len(b)):
            a.append(0)
        c = addArrays(a, b)
    print(c)

    test_add()
