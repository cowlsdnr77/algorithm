finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def is_existing_target_number_binary(target, array):
    # 구현해보세요!

    start = 0
    end = len(array)-1
    guess = (start+end)//2

    while start <= end:
        if array[guess] < target:
            start = guess+1
        elif array[guess] > target:
            end = guess-1
        else:
            return True
        guess = (start+end)//2
    return False
        


result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)