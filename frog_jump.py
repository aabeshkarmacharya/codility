def solution(X, A):
    leaves = set()
    shortest_time = -1
    for K, leaf in enumerate(A):
        leaves.add(leaf)
        if len(leaves) == X:
            shortest_time = K
            break
    return shortest_time


if __name__ == '__main__':
    print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))
