import math


def binary_search(target: int, l: list=[], start: int=0, end: int=1):
    """List has to be sorted"""
    if start > end:
        return False
    else:
        rel = l[start:end]
        mid = math.ceil(((end-1)-start)/2)
        mid_val = l[mid]
        
        if mid_val == target:
            return{mid: target}

        elif mid_val < target:
            return binary_search(target=target, l=l, start=mid, end=end)
        
        elif mid_val > target:
            return binary_search(target=target, l=l, start=start, end=mid)
    


nums = [3, 5, 7, 9, 10]

print(binary_search(target=3, l=nums, end=len(nums)))