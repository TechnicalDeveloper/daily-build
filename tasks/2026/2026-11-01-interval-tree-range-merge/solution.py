class IntervalTree:
    def __init__(self):
        self.intervals = []  # list of [start, end)

    def add(self, interval):
        start, end = interval
        # Remove everything in the range to avoid overlap
        self.remove((start, end))
        self.intervals.append([start, end])

    def remove(self, interval):
        start, end = interval
        new_intervals = []
        for s, e in self.intervals:
            if e <= start or s >= end:
                new_intervals.append([s, e])
            else:
                if s < start:
                    new_intervals.append([s, start])
                if e > end:
                    new_intervals.append([end, e])
        self.intervals = new_intervals

    def query(self, point):
        count = 0
        for s, e in self.intervals:
            if s <= point < e:
                count += 1
        return count

    def merge(self):
        if not self.intervals:
            return []
        sorted_intervals = sorted(self.intervals, key=lambda x: x[0])
        merged = []
        current_start, current_end = sorted_intervals[0]
        for s, e in sorted_intervals[1:]:
            if s <= current_end:
                if e > current_end:
                    current_end = e
            else:
                merged.append([current_start, current_end])
                current_start, current_end = s, e
        merged.append([current_start, current_end])
        return merged
