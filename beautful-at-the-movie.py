import os


def invert_number(number):
    number_str = str(number)
    return int(number_str[::-1])


def beautifulDays(i, j, k):
    beautful_days = 0
    days = range(i, j + 1)
    print(days)
    for day in days:
        inverted = invert_number(day)
        sub = abs(day - inverted)
        if sub % k == 0:
            beautful_days += 1
    return beautful_days


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + "\n")

    fptr.close()
