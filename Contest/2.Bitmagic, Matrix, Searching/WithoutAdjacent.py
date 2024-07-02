def withoutAdjacent(arr):
    incl = 0
    excl = 0

    for i in arr:

        # Current max excluding i (No ternary in
        # Python)
        new_excl = excl if excl > incl else incl

        # Current max including i
        incl = excl + int(i)
        excl = new_excl

    # return max of incl and excl
    return excl if excl > incl else incl
