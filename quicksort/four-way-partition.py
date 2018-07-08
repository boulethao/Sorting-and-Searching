
def fourwayspartition(arr):
    """
    This is an attempt to a four ways partition (extendable to more)
    """

    p1 = 0  # left to this boundary are elements equal to "!"
    p2 = 0  # left to this boundary are elements equal to "@"
    p3 = 0  # left to this boundary are elements equal to "#"
    p4 = 0  # left to this boundary are elements equal to "$"

    i = 0   # index walking through the array and inserting the element inside the
            #correspondant boundary

    while i < len(arr):


        if arr[i] == "!":
            #swap with the "!" boundary and make sure to shift all the other elements and their boundaries to the right.
            if (i > p1):
                arr[i], arr[p1] = arr[p1], arr[i]

            if (i > p2 and p2 > p1):
                arr[i], arr[p2] = arr[p2], arr[i]

            if (i > p3 and p3 > p2):
                arr[i], arr[p3] = arr[p3], arr[i]

            if (i > p4 and p4 > p3):
                arr[i], arr[p4] = arr[p4], arr[i]

            p1 += 1
            p2 += 1
            p3 += 1
            p4 += 1



        elif arr[i] == "@":
            # swap with the "@" boundary and make sure to shift all the other elements and their boundaries to the right.
            if (i > p2):
                arr[i], arr[p2] = arr[p2], arr[i]

            if (i > p3 and p3 > p2):
                arr[i], arr[p3] = arr[p3], arr[i]

            if (i > p4 and p4 > p3):
                arr[i], arr[p4] = arr[p4], arr[i]

            p2 += 1
            p3 += 1
            p4 += 1

        elif arr[i] == "#":
            # swap with the "#" boundary and make sure to shift all the other elements and their boundaries to the right.
            if (i > p3):
                arr[i], arr[p3] = arr[p3], arr[i]

            if (i > p4 and p4 > p3):
                arr[i], arr[p4] = arr[p4], arr[i]

            p3 += 1
            p4 += 1


        elif arr[i] == "$":
            # swap with the "$" boundary and make sure to shift all the other elements and their boundaries to the right.
            if (i > p4):
                arr[i], arr[p4] = arr[p4], arr[i]
            p4 += 1


        i += 1

        print("array %s" % arr)






arr = ["$", "$", "$", "@", "!", "$", "!", "@", "$", "$", "#", "$", "@", "!", "#", "!" ]
fourwayspartition(arr)