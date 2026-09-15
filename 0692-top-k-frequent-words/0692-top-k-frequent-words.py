from collections import Counter
"""手写堆"""
class Node:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word
    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        return self.word > other.word

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        heap = []
        for word, freq in cnt.items():
            heapq.heappush(heap, Node(freq, word))
            if len(heap) > k:
                heapq.heappop(heap)
        
        ans = [heapq.heappop(heap).word for _ in range(len(heap))]
        return ans[::-1]