# Count the number of indexes such that i < j and arr[i] < arr[j]

def count_arr(arr):
    count = 0
    for i in range(len(arr)):
        j = len(arr) - 1
        while j > i:
            if arr[j] > arr[i]:
                count += 1
            j -= 1
    return count

if __name__ == '__main__':
    print(count_arr([7, 9, 5, 6, 3, 2]))
    print(count_arr([7, 9, 11, 6, 3, 2]))
