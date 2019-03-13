def counter(low,high):
    current =low
    while current <=high:
        yield current
        current=current+1
c=counter(7,12)
next(c)

        
