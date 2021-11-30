def merge(nums, start, mid, end):
    front = nums[start:mid+1]
    rear = nums[mid+1:end+1]

    front_idx = 0
    rear_idx = 0
    nums_idx = start

    while front_idx < len(front) and rear_idx < len(rear):
        if front[front_idx] < rear[rear_idx]:
            nums[nums_idx] = front[front_idx]
            front_idx += 1
            nums_idx += 1
        else:
            nums[nums_idx] = rear[rear_idx]
            rear_idx += 1
            nums_idx += 1

    while front_idx < len(front):
        nums[nums_idx] = front[front_idx]
        front_idx += 1
        nums_idx += 1

    while rear_idx < len(rear):
        nums[nums_idx] = rear[rear_idx]
        rear_idx += 1
        nums_idx += 1

    return nums


nums = [4,2,3,7]
def mergeSort(nums, start, end):
    if start < end:

        mid = int((start+end)/2)

        f = nums[start:mid]
        b = nums[mid:end]

        mergeSort(nums, start, mid)
        mergeSort(nums, mid+1, end)
        merge(nums, start, mid, end)

        
mergeSort(nums, 0, len(nums))
print("Sorted", nums)