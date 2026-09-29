class IntervalTree:
    def __init__(self):
        self._intervals = []  # list of [start, end] sorted

    def add(self, start: int, end: int) -> None:
        if end < start:
            return
        new_start, new_end = start, end
        new_list = []
        inserted = False
        for s, e in self._intervals:
            if e < new_start - 1:
                new_list.append([s, e])
            elif s > new_end + 1:
                if not inserted:
                    new_list.append([new_start, new_end])
                    inserted = True
                new_list.append([s, e])
            else:
                new_start = min(new_start, s)
                new_end = max(new_end, e)
        if not inserted:
            new_list.append([new_start, new_end])
        self._intervals = new_list

    def remove(self, start: int, end: int) -> None:
        if end < start:
            return
        new_list = []
        for s, e in self._intervals:
            if e < start or s > end:
                new_list.append([s, e])
            else:
                if s < start:
                    new_list.append([s, start - 1])
                if e > end:
                    new_list.append([end + 1, e])
        self._intervals = new_list

    def get_intervals(self) -> list[tuple[int, int]]:
        return [(s, e) for s, e in self._intervals]
