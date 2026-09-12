from collections import defaultdict
class Logger:
    """ each same msg in 10s"""
    def __init__(self):
        self.mp = defaultdict(int)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.mp:
            self.mp[message] = timestamp
            return True
        elif timestamp - 10 >= self.mp[message]:
            self.mp[message] = timestamp
            return True
        else:
            return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)