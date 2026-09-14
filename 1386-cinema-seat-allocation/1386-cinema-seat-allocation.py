from collections import defaultdict
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        row_seats = defaultdict(set)
        for row, col in reservedSeats:
            if 2 <= col <= 9:
                row_seats[row].add(col)

        ans = (n - len(row_seats)) * 2

        l = {2, 3, 4, 5}
        m = {4, 5, 6, 7}
        r = {6, 7, 8, 9}

        for seats in row_seats.values():
            left_free = not (seats & l)
            right_free = not (seats & r)

            if left_free:
                ans += 1
            if right_free:
                ans += 1
            if not left_free and not right_free and not (seats & m):
                ans += 1
        
        return ans