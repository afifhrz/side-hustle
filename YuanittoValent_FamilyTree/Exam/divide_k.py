def divides_k (nums, k):
    temp = 0
    for number in nums:
        if number%k == 0:
            if number > temp:
                temp = number
        
    if temp == 0:
        return None
    else:
        return temp