


l = [2, 5, 6, 5, 11]

def isPal(x):
    str_num = str(x)
    if len(str_num) == 1:
        return True
    if len(str_num) % 2 != 0:
        mid = int(len(str_num)/2)
        front = str_num[:mid] 
        back = str_num[mid+1:]
    else:
        mid = int(len(str_num)/2)
        front = str_num[:mid]
        back = str_num[mid:]

    stack = [i for i in back]

    back = ''
    for i in range(0, len(stack)):
        back = back + stack.pop()

    if front == back:    
        return True
    else:
        return False





print(isPal(1011301))                                                                                                                                                