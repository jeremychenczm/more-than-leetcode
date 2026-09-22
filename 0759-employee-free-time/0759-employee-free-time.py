"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = []
        for employee in schedule:
            for iv in employee:
                intervals.append(iv)

        intervals.sort(key=lambda iv: iv.start)

        ans = []
        current_end = intervals[0].end

        for iv in intervals[1:]:
            if iv.start > current_end:
                ans.append(Interval(current_end, iv.start))
                current_end = iv.end
            else:
                current_end = max(current_end, iv.end)

        return ans