def sqsum1(nums):
    return sum(x^2 if x > 0 for x in nums)
sqsum1(24)