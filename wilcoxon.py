def tuple_sort(tpl):  
    tpl.sort(key = lambda x: x[0])  
    return tpl

def rank_calculator(lst):
    temp={}
    temp_rank = 1
    for no in sorted(lst):
        if no not in temp:
            temp[no] = temp_rank
            temp_rank = temp_rank + 1
    return[temp[m] for m in lst]

def wilcoxon_test(list1,list2):
    
    #List with difference
    diff_list = [x-y for x,y in zip(list1,list2) if x-y]
    
    #List of sign values
    sgn_list = [0 if v == 0 else 1 if v > 0 else -1 for v in diff_list]
    
    #Convert difference values in absolute values
    abs_list = [(abs(x),y) for x,y in zip(diff_list,sgn_list)]
    
    #Sort list based on absolute difference
    sorted_list = tuple_sort(abs_list)
    
    #Calculate rank for all elements
    ranked_list = rank_calculator(sorted_list)
    
    #Initialize and calculate test statistic
    W = 0
    
    for x,y in zip(sorted_list,ranked_list):
        W += x[1]*y
    
    #Initialize and calculate rank sum
    S = 0
    for i in range(1,len(diff_list)+1):
        S += i
        
    rank_corelation = W/S
    
    return round(rank_corelation,5)	