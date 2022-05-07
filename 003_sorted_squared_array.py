# O(nlog(n)) time | O(n) space
def sorted_squared_array_bf(array):
    sorted_squares = [0 for _ in array]

    for idx in range(len(array)):
        value = array[idx]
        sorted_squares[idx] = value * value

    sorted_squares.sort()
    return sorted_squares


# O(n) time | O(n) space
def sorted_squared_array_my(array):
    squared_array = [0 for _ in array]
    start = 0
    end = len(array) - 1
    sq_el = len(array) - 1

    for _ in range(len(array)):
        if abs(array[start]) > abs(array[end]):
            squared_array[sq_el] = array[start] * array[start]
            sq_el -= 1
            start += 1
        elif abs(array[start]) < abs(array[end]):
            squared_array[sq_el] = array[end] * array[end]
            sq_el -= 1
            end -= 1
        else:
            squared_array[0] = array[start] * array[start]

    return squared_array


# O(n) time | O(n) space
def sorted_squared_array(array):
    sorted_squares = [0 for _ in array]
    smaller_value_idx = 0
    larger_value_idx = len(array) - 1

    for idx in reversed(range(len(array))):
        smaller_value = array[smaller_value_idx]
        larger_value = array[larger_value_idx]

        if abs(smaller_value) > abs(larger_value):
            sorted_squares[idx] = smaller_value * smaller_value
            smaller_value_idx += 1
        else:
            sorted_squares[idx] = larger_value * larger_value
            larger_value_idx -= 1

    return sorted_squares


print(sorted_squared_array_my(sorted([-2, -12, 22, 321, -13, 3, 14])))
