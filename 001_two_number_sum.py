# O(n^2) time | O(1) space
def two_number_sum(array, target_sum):
    for i in range(len(array) - 1):
        first_num = array[i]
        for j in range(i + 1, len(array)):
            second_num = array[j]
            if first_num + second_num == target_sum:
                return [first_num, second_num]
    return []


# O(n) time | O(n) space
def two_number_sum_hash(array, target_sum):
    nums = {}
    for num in array:
        potential_match = target_sum - num
        if potential_match in nums:
            return [potential_match, num]
        else:
            nums[num] = True
    return []


# O(nlog(n)) time | O(1) space
def two_number_sum_pointer(array, target_sum):
    array.sort()
    left_pointer = 0
    right_pointer = len(array) - 1
    while left_pointer < right_pointer:
        current_sum = array[left_pointer] + array[right_pointer]
        if current_sum == target_sum:
            return [array[left_pointer], array[right_pointer]]
        elif current_sum < target_sum:
            left_pointer += 1
        elif current_sum > target_sum:
            right_pointer -= 1
    return []


print(two_number_sum_pointer([1, -4, 12, 22, -3, 4, 3, 2], 0))