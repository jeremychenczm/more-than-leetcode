"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # 员工1：[[1,2],[5,6]]，员工2：[[1,3]]，员工3：[[4,10]]
        # 找出员工共同的空闲区间

        # 区间调度问题首先想到扫描线
        # 把所有员工自己的intervals全部拍平到x轴
        events = []
        for employee in schedule:
            for interval in employee:
                events.append((interval.start, 1))
                events.append((interval.end, -1))
        # 区间起点升序排，起点相同，终点升序        
        events.sort(key=lambda e: (e[0], e[1]))

        ans = []
        event_cnt = 0
        free_start = None

        for time, delta in events:
            # 处于空闲 event_cnt == 0 且 当前区间是要开始工作 delta == 1
            # 且 非初始化时event_cnt == 0 and free_start is not None
            if event_cnt == 0 and delta == 1 and free_start is not None and free_start < time:
                ans.append(Interval(free_start, time))
            event_cnt += delta
            if event_cnt == 0:
                free_start = time
        
        return ans