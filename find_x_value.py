class Solution(object):
    def resultArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            next_dp = [0] * k
            val = num % k

            next_dp[val] += 1

            for r in range(k):
                if dp[r] > 0:
                    next_dp[(r * val) % k] += dp[r]

            for r in range(k):
                ans[r] += next_dp[r]

            dp = next_dp

        return ans