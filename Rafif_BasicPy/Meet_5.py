def prime_factors(n):
    result = {}
    start_factor = 2
    
    while n != 1:
        counter = 0
        while n % start_factor == 0:
            counter = counter + 1
            n = n / start_factor
        
        # to store the result
        # ex: counter = 1
        # start_factor = 2
        # result[2] = 1
        # print (result) -> 
        # {
        #     2 : 1
        # }
        
        if counter == 0:
            pass
        else:
            result[start_factor] = counter
            
        start_factor += 1
    return result

# print(prime_factors(50))
# print(prime_factors(220))
# print(prime_factors(265))
# print(prime_factors(1341648))

def add_time(time_1, time_2):   
    result = [0,0,0,0]
    minutes_addition = 0
    hour_addition = 0
    day_addition = 0
    
    # seconds addition
    temp_result = time_1[3] + time_2[3]
    if temp_result >= 60:
        minutes_addition = 1    
    result[3] = temp_result % 60
    
    # minutes addition
    temp_result = time_1[2] + time_2[2] + minutes_addition
    if temp_result >= 60:
        hour_addition = 1    
    result[2] = temp_result % 60
    
    # minutes addition
    temp_result = time_1[1] + time_2[1] + hour_addition
    if temp_result >= 24:
        day_addition = 1    
    result[1] = temp_result % 24
    
    # day
    result[0] = time_1[0] + time_2[0] + day_addition   
    
    return result

# print(add_time([1,23,59,59],[0,0,0,1]))
# print(add_time([0,12,59,30],[1,12,10,30]))

def fibonacci_list(indices):
    max_fibo = max(indices)
    # fibo_list = [0, 1, 1, 2, ] 
    fibo_list = [0, 1]
    for i in range(2,max_fibo+1):
        fibo_list.append(fibo_list[i-1]+fibo_list[i-2])
    
    result = []
    for i in indices:
        result.append(fibo_list[i])
    
    return result

print(fibonacci_list(range(10)))
print(fibonacci_list([3,4,3,9,8,3,2]))
    