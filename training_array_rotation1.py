def solution(A, K):
    if A:
        for i in range(K):
            e = A.pop()
            A.insert(0, e)
    return A


if __name__ == "__main__":
    print(solution([1, 2, 3, 4], 2))
