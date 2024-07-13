def solution(number):
    if number < 0:
        return 0
    i = 0
    sum = 0
    while i < number-1:
        i += 1
        if i % 3 == 0 and i % 5 == 0:
            sum += i
            continue
        elif i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum
