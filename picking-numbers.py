def pickingNumbers(a):
    # Write your code here
    low = 0
    cur = a[0]
    for number in a:
        if cur != number:
            cur = number
            numbers = [num for num in a if cur - 1 <= num <= cur + 1]
            print(numbers)
            low = len(numbers) if len(numbers) < low else low
    print(low)
    return low


a = [98, 3, 99, 1, 97, 2]
pickingNumbers(a)
