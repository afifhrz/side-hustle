currentPosFiltered=[[None,None,None],
                    [None,None,None],
                    [0,None,0]]

filtered_state= [[None,None,None],
                 [0,None,None],
                 [0,None,None]]

init_state_kf = [currentPosFiltered[2][0], filtered_state[1][0], currentPosFiltered[2][2], filtered_state[2][0]]
print(init_state_kf)