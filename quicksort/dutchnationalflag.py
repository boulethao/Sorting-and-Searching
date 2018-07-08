def dutch_national_flag(arr):

    if arr is None or len(arr) <= 1:
        return


    red = 0
    blue = len(arr)-1
    i = 0

    while i <= blue:

        if arr[i] == 'R':
            arr[i], arr[red] = arr[red], arr[i]
            red += 1
            i += 1

        elif arr[i] == 'W':
            i += 1

        elif arr[i] == 'B':
            arr[i], arr[blue] = arr[blue], arr[i]
            blue -= 1

arr = ["W", "R", "R", "W", "B", "W", "R", "B", "R" ]
dutch_national_flag(arr)
print (arr)

