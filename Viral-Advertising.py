import os


def viralAdvertising(n):
    cumulative = 0
    shared = 5
    for i in range(n):
        liked = shared // 2
        cumulative += liked
        shared = liked * 3
    return cumulative


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + "\n")

    fptr.close()
