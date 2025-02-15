# https://leetcode.com/problem-list/2mcxw10e/

# https://leetcode.com/problems/merge-sorted-array
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    while m > 0 and n > 0:
        if nums1[m - 1] < nums2[n - 1]:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
        else:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1

    if m == 0:
        nums1[:n] = nums2[:n]

# https://leetcode.com/problems/valid-palindrome


def isPalindrome(self, s: str) -> bool:
    l, r = 0, len(s)-1
    while l < r:
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        elif s[r].lower() == s[l].lower():
            l += 1
            r -= 1
        else:
            return False

    return True

# https://leetcode.com/problems/two-sum

# https://leetcode.com/problems/container-with-most-water


def maxArea(self, height: List[int]) -> int:
    area = 0
    l, r = 0, len(height) - 1

    while l < r:
        newarea = min(height[l], height[r]) * (r-l)
        if newarea > area:
            area = newarea

        if height[l] < height[r]:
            l += 1
        elif height[l] > height[r]:
            r -= 1
        else:
            l += 1
            r -= 1
    return area


# https://leetcode.com/problems/trapping-rain-water
def trap(self, height: List[int]) -> int:
    l_max, r_max, total = 0, 0, 0
    l, r = 0, len(height) - 1

    while l < r:
        if l_max < height[l]:
            l_max = height[l]
        if r_max < height[r]:
            r_max = height[r]
        if height[l] < height[r]:
            total += min(l_max, r_max) - height[l]
            l += 1
        elif height[l] > height[r]:
            total += min(l_max, r_max) - height[r]
            r -= 1
        else:
            l += 1

    return total
