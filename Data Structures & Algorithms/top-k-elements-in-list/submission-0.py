class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}
        ans = []
        for num in nums:
            freq[num] = freq.get(num,0) + 1

        res = sorted(freq.items(),key = lambda x: x[1], reverse = True)

        for i in range(k):
            ans.append(res[i][0])

        return ans

        