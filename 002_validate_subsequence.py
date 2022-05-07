# O(n) time | O(1) space
def validate_subsequence_while(array, sequence):
    arr_idx = 0
    seq_idx = 0
    while arr_idx < len(array) and seq_idx < len(sequence):
        if sequence[seq_idx] == array[arr_idx]:
            seq_idx += 1
        arr_idx += 1
    return seq_idx == len(sequence)


# O(n) time | O(1) space
def validate_subsequence_for(array, sequence):
    seq_idx = 0
    for value in array:
        if sequence[seq_idx] == len(sequence):
            break
        if sequence[seq_idx] == value:
            seq_idx += 1
    return seq_idx == len(sequence)


print(validate_subsequence_for([1, 2, 3], [1, 2]))
