class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
            
        sorted_counts = sorted(counts.items(), key=lambda x : x[1], reverse=True)
        out = []
        for i in range(k):
            out.append(sorted_counts[i][0])

        return out