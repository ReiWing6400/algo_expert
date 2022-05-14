# O(nlog(n)) time | O(1) space
def non_constructible_change(array):
    array.sort()
    change = 0

    for coin in array:
        if coin > change + 1:
            return change + 1

        change += coin

    return change + 1


print(non_constructible_change([5, 7, 1, 1, 2, 3, 22]))
print(non_constructible_change([1, 1, 2, 3]))
