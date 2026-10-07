class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        
        history = self.store[key]
        left = 0
        right = len(history)
        while left < right:
            mid = (left + right) // 2
            stored_timestamp = history[mid][0]
            if stored_timestamp <= timestamp:
                left = mid + 1
            else:
                right = mid
        
        if left == 0:
            return ""
        return history[left - 1][1]
        
