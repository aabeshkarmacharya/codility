def solution(A):
    sum = 0
    cum = []
    sum_i = 0
    cum_i = []
    for i in A:
        sum += i
        cum.append(sum)
    A.reverse()
    for i in A:
        sum_i += i
        cum_i.append(sum_i)
    cum.pop()
    cum_i.pop()
    cum_i.reverse()
    min_value = 100000
    for i, (j, k) in enumerate(zip(cum, cum_i)):
        dif = abs(j - k)
        if dif < min_value:
            min_value = dif
    return min_value


if __name__ == '__main__':
    print(solution([3, 1, 2, 4, 3]))
    # 3,4,6,10
    # 10, 9, 7, 3
