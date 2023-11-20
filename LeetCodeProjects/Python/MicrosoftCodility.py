def solution(S):
    # write your code in Python 3.6
    count_set = set()
    num_of_substring = 1

    i = 0
    while i < len(S):
        if S[i] not in count_set:
            count_set.add(S[i])
            i += 1
        else:  # if S[i] in the set add substring
            count_set = set()
            count_set.add(S[i])
            num_of_substring += 1
            i += 1

    return num_of_substring


def getDistance(blocks):
    n = len(blocks)
    max_jump_left, max_jump_right = [0] * n, [0] * n

    # jump left
    i = 1
    while i < n:
        # previous block is greater than the current block
        if blocks[i] <= blocks[i - 1]:
            max_jump_left[i] = max_jump_left[i - 1] + 1
        i += 1

    # jump right
    j = n - 2
    while j >= 0:
        # next block is greater than the current block
        if blocks[j] <= blocks[j + 1]:
            max_jump_right[j] = max_jump_right[j + 1] + 1
        j -= 1

    # find the index that maximize the distance
    res = 0
    for k in range(n):
        res = max(res, max_jump_left[k] + max_jump_right[k] + 1)

    return res


if __name__ == '__main__':
    print(getDistance([1, 5, 5, 2, 6, 2, 7]) == 4)
    print(getDistance([1, 1]) == 2)
    print(getDistance([1]) == 1)
    print(getDistance([]) == 0)
    print(getDistance([2, 6, 8, 5]) == 3)
    print(getDistance([6, 5, 5, 6]) == 4)
    print(solution("dddd") == 4)
    print(solution("dD") == 1)
    print(solution("") == 1)
    print(solution("ccaa") == 3)
    print(solution("cycle") == 2)
    print(solution("abba") == 2)
    print(solution("acbdacbdd") == 3)
    print(solution("abcdevrtyu") == 1)
    print(solution("abbccc") == 4)
    print(solution("aaaabbbbcccc") == 10)
