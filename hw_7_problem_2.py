"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
"""

def three_sum(s):
    s = sorted(s)
    output = set()
    for k in range(len(s)):
        target = -s[k]
        i,j = k+1, len(s)-1
        while i < j:
            sum_two = s[i] + s[j]
            if sum_two < target:
                i += 1
            elif sum_two > target:
                j -= 1
            else:
                output.add((s[k],s[i],s[j]))
                i += 1
                j -= 1
    return output

nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))

"""
Variable        |       Value
s               |       [-1, 0, 1, 2, -1, -4]
output          |       {[-1, -1, 2], [-1, 0, 1]}
k               |       5
target          |       -2
i               |       6
j               |       5
sum_two         |       3
return value    |       {[-1, -1, 2], [-1, 0, 1]}
"""