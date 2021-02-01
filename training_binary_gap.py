def solution(N):
    binary_string = bin(N)[2:]
    counter = 0
    max_value = 0
    for i in binary_string:
        if i == "1":
            if counter > max_value:
                max_value = counter
            counter = 0
        elif i == "0":
            # increase counter
            counter += 1
    return max_value


if __name__ == '__main__':
    print(solution(1041))
