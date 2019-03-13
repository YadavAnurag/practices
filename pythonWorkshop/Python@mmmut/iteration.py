class counter:
    def __init__(self, low, high):
        self.current =low
        self.high =high
    def __iter__(self):
        return self
    def next(self):
        if self.current<self.high:
            self.current=self.current+1
            return self.current
        else:
            return StopIteration
    
