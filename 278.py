# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        while l < r:
            m = (r-l)//2+l
            result = isBadVersion(m)
            if result == False:
                l = m+1
            else:
                r = m
        return l

print(Solution().firstBadVersion(2))