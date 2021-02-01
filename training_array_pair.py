def solution(A):
    value_counts = {}
    for i in A:
        if i in value_counts:
            value_counts[i] += 1
        else:
            value_counts[i] = 1
    for k, v in value_counts.items():
        if v % 2 == 1:
            return k


if __name__ == '__main__':
    print(solution([1, 1, 2, 2, 3, 3, 4, 4, 5]))
    print(solution([5]))
