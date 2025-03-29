numbers = [4, 7, 1, 9, 3]

while(len(numbers) != 1):

    left_idx = 0
    right_idx = len(numbers) - 1

    if numbers[left_idx] > numbers[right_idx]:
        numbers.pop(right_idx)
    else:
        numbers.pop(left_idx)

print(numbers)
