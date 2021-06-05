str = input()

tmp = len(str)
cnt = 0

for i in range(1, len(str)):
    if str[i] == "=":
        if str[i-1] == "c" or str[i-1] == "s":
            # c= s=
            tmp -= 1
        elif str[i-1] == "z":
            if i-1 > 0:
                if str[i-2] == "d":
                    # dz=
                    tmp -= 2
                else:
                    # z=
                    tmp -= 1
            else:
                # z=
                tmp -= 1
    elif str[i] == "-":
        if str[i-1] == "c" or str[i-1] == "d":
            # c- d-
            tmp -= 1
    elif str[i] == "j":
        if str[i-1] == "l" or str[i-1] == "n":
            # lj nj
            tmp -= 1


print(tmp)
