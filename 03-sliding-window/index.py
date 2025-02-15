# https://leetcode.com/problem-list/2af6ecom/

# https://leetcode.com/problems/contains-duplicate-ii
def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    hashmap = {}
    for index, value in enumerate(nums):
        if value in hashmap:
            if index - hashmap[value] <= k:
                return True
            else:
                hashmap[value] = index
        else:
            hashmap[value] = index

    return False

# https://leetcode.com/problems/longest-substring-without-repeating-characters
def lengthOfLongestSubstring(self, s: str) -> int:
    longest = 0
    hashmap = {}
    arr = []

    for index, value in enumerate(s):
        if value not in arr:
            hashmap[value] = index
            arr.append(value)
        else:
            first_value = hashmap[value] + 1
            hashmap[value] = index
            arr = list(s[first_value:index + 1])

        length = len(arr)
        if longest < length:
            longest = length

    return longest

# https://leetcode.com/problems/maximum-average-subarray-i
def findMaxAverage(self, nums: List[int], k: int) -> float:
    init_sum = sum(nums[:k])
    highest_sum = init_sum

    for index, value in enumerate(nums[k:]):
        init_sum = init_sum - nums[index] + value
        if highest_sum < init_sum:
            highest_sum = init_sum

    return highest_sum/k
