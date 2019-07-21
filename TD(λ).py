
## coding: UTF-8
import  numpy   as  np

state_cost  =   [0]*11  #各頂点におけるコストを保存する場所


network     =   np.array(
                            [   
                                [-1,10,15,12,-1,-1,-1,-1,-1,-1,-1],
                                [-1,-1,-1,-1, 8,12,19,-1,-1,-1,-1],
                                [-1,-1,-1,-1, 9,11,13,-1,-1,-1,-1],
                                [-1,-1,-1,-1, 7,15,14,-1,-1,-1,-1],
                                [-1,-1,-1,-1,-1,-1,-1, 8,12,19,-1],
                                [-1,-1,-1,-1,-1,-1,-1, 9,11,13,-1],
                                [-1,-1,-1,-1,-1,-1,-1, 7,15,14,-1],
                                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 9],
                                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 6],
                                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,12],
                            ],
                        )




et_list     =   [0]*11  #etを保存しておくリスト

Alpha       =   0.5     #係数
Gamma       =   1       #係数
Lambda      =   0.9       #係数


def Temporary_Difference(new_cost , old_cost):
    delta   =   Alpha * (new_cost - old_cost)
    return delta


count = 1
while 1:
    print("{}回目".format(count))
    state   =   0
    
    et_list     =   [0]*11  #etを保存しておくリスト
    #中間分だけ繰り返す

    for state_num in range(3):  #state_numは今処理をしている段数を教えてくれる

        et_list         =   [data * Gamma * Lambda for data in et_list]         #リストの中身に重みをかけていく
        et_list[state]  =   1


        cost_list       =   []      #コストを一時的に保存しておくところ


        for i in range(3):
            cost_list.append(state_cost[state_num * 3 + i + 1] + Gamma * network[state,state_num * 3 + i + 1])
        
        next_state          =   np.argmin(cost_list) + state_num * 3 + 1
        
        delta  =  Temporary_Difference(cost_list[np.argmin(cost_list)] , state_cost[state])

        state_cost          =  [delta * et_list[arg] + state_cost[arg] for arg in range(len(state_cost))]
        
        state               =   next_state
    
    et_list             =   [data * Gamma * Lambda for data in et_list] 
    et_list[state]  =   1

    #最終層について

    cost                =   state_cost[10] + Gamma * network[state , 10]
    delta               =  Temporary_Difference(cost , state_cost[state])
    state_cost          =  [delta * et_list[arg] + state_cost[arg] for arg in range(len(state_cost))]
    count               +=1
    
    if(Temporary_Difference(cost , state_cost[state]) == 0):
        break

print(state_cost)
        






