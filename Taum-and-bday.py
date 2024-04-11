import os


# primeira resolução
def taumBday_v1(b, w, bc, wc, z):
    # Write your code here
    if bc != wc:
        low = bc if bc < wc else wc
        high = bc if wc < bc else wc
        if high > low + z:
            qttd_convert = w if bc < wc else b
            gift_buys = (b + w) * low
            converted = qttd_convert * z
            return gift_buys + converted
    return (b * bc) + (w * wc)


# segunda resolução
def taumBday_v2(b, w, bc, wc, z):
    return min((b * bc) + (w * wc), (b + w) * bc + (w * z), (b + w) * wc + b * z)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        b = int(first_multiple_input[0])

        w = int(first_multiple_input[1])

        second_multiple_input = input().rstrip().split()

        bc = int(second_multiple_input[0])

        wc = int(second_multiple_input[1])

        z = int(second_multiple_input[2])

        result = taumBday(b, w, bc, wc, z)

        fptr.write(str(result) + "\n")

    fptr.close()
