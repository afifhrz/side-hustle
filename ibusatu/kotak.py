def kotakHartaYangPalingBerharga(N, S, rak):
    # Write your code here
    
    # max_res = 0 
    # for i in range(0,N-S+1): 
    #     for j in range(0,N-S+1): 
    #         max_tot = 0 
    #         for k in range(S): 
    #             max_row = 0 
    #             for l in range(S): 
    #                 max_row += rak[i+k][j+l] 
    #             max_tot += max_row 
    #         if max_tot > max_res: 
    #             max_res = max_tot 
    # return max_res

    max_res = float("-inf")
    for i in range(N - S + 1):
        for j in range(N - S + 1):
            subset_sum = 0

            for k in range(i, i + S):
                for l in range(j, j + S):
                    subset_sum += rak[k][l]

            max_res = max(max_res, subset_sum)

    return max_res

