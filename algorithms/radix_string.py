def sortByLengthAndRadix(arr):
    max_length = len(max(arr, key=len))
    buckets = [[] for _ in range(max_length + 1)]
    for s in arr:
        buckets[len(s)].append(s)
    for i in range(max_length + 1):
        if len(buckets[i]) > 0:
            radixSort(buckets[i])
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr


def radixSort(arr):
    max_len = len(max(arr, key=len))

    for i in range(max_len):
        buckets = [[] for _ in range(26)]
        for string in arr:
            char_index = -1 - i
            char = string[char_index] if -i <= len(string) else "\0"
            buckets[ord(char)].append(string)

        arr[:] = []
        for bucket in buckets:
            arr.extend(bucket)


# Example usage
arr = ["apple", "bat", "banana", "at", "an", "ace", "car"]
sorted_arr = sortByLengthAndRadix(arr)
print("Sorted array is: ", sorted_arr)
