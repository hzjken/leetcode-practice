class Solution:
    '''basic method, exceed time limit'''
    def canCompleteCircuit(self, gas, cost):
        output = -1
        
        for i in range(len(gas)):
            current = i
            if gas[current] >= cost[current]:
                cum_gas = [gas[current]]
                cum_cost = [cost[current]]
                
                finish = True
                for j in range(1, len(gas)):
                    new_gas = cum_gas[-1]
                    new_cost = cum_cost[-1]
                    new_gas += gas[(current + j) % len(gas)]
                    new_cost += cost[(current + j) % len(cost)]
                    if new_gas >= new_cost:
                        cum_gas.append(new_gas)
                        cum_cost.append(new_cost)
                    else:
                        finish = False
                        break
                
                if finish:
                    output = current
                    break
                    
        return output


class Solution2:
    def canCompleteCircuit(self, gas, cost):
        if sum(cost) > sum(gas):
            return -1
        
        new_list = [gas[i]-cost[i] for i in range(len(gas))]
        cum_to_end_list = [sum(new_list[i:]) for i in range(len(gas))]    
                    
        return cum_to_end_list.index(max(cum_to_end_list))