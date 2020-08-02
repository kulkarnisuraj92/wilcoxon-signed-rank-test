import csv
from itertools import combinations
from wilcoxon import wilcoxon_test


print("\n\n##Wilcoxon Signed Rank Test##\n\n")
filename = input("Enter file name:")

try:
    with open(filename, 'r') as infile:    
        #Creating dict, where headers are keys and column data is value
        reader = csv.DictReader(infile)
        data = {}
        for row in reader:
            for header, value in row.items():
                try:
                    data[header].append(value)
                except KeyError:
                    data[header] = [value]

    file_header = list(data.keys())

    #Converting str values to int
    for k, v in data.items():
        if k.isnumeric():
            data[k] = [int(x) for x in v]

    key_column = file_header[1]
    non_key_columns = file_header[2:]

    print("\nFile Header: "+str(file_header).strip('[').strip(']')+"\n")
    print("Key Column: "+str(key_column)+"\n")
    print("Non-Key Columns: "+str(non_key_columns).strip('[').strip(']')+"\n")
    print("Checking which non-key product has the best fit to the key product.\n")

    key_non_key_rank = {}

    for i in range(len(non_key_columns)):

        rank_corelation = wilcoxon_test(data[key_column],data[non_key_columns[i]])

        key_non_key_rank[str(key_column)+"_"+str(non_key_columns[i])] = rank_corelation

    print("Below are correlation rank result for given key and non key products\n")

    for k,v in key_non_key_rank.items():    
        print(str(k)+": "+str(v))

    best_non_key = max(key_non_key_rank, key=key_non_key_rank.get)

    print("\n"+best_non_key.split('_')[1] + ": Is the non-key product which has the best fit to the key product. With maximum rank correlation " + str(key_non_key_rank[best_non_key])+"\n")

    print("Checking which non-key product combination has the best fit to the key product.\n")

    all_non_key_combination = []

    for i in range(2,len(non_key_columns)+1):
        all_non_key_combination.extend(list(combinations(non_key_columns,i)))

    print("Below are all combinations:\n")
    for i in all_non_key_combination:
        print(*i)

    combinations_with_weight_list = {}

    for element in all_non_key_combination:

        temp_list = []
        temp_zipped_list = []
        for i in range(len(element)):
            temp_list.append(data[element[i]])
        temp_zipped_list = list(zip(*temp_list))
        combinations_with_weight_list[element] = [round(sum(list(x))/len(x),3) for x in temp_zipped_list]

    key_non_key_combinations_rank = {}

    for i in range(len(combinations_with_weight_list)):

        rank_corelation = wilcoxon_test(data[key_column],combinations_with_weight_list[list(combinations_with_weight_list.keys())[i]])

        key_non_key_combinations_rank[str(key_column)+"_"+str(list(combinations_with_weight_list.keys())[i])] = rank_corelation

    print("\nBelow are correlation rank result for all non key combinations with key product\n")

    for k,v in key_non_key_combinations_rank.items():    
        print(str(k)+": "+str(v))

    best_non_key_combination = max(key_non_key_combinations_rank, key=key_non_key_combinations_rank.get)

    print("\n"+best_non_key_combination.split('_')[1] + ": Is the non-key combination which has the best fit to the key product. With maximum rank correlation " + str(key_non_key_combinations_rank[best_non_key_combination])+"\n")

except Exception as e:
    
    print("\nError Occurred: " + str(e))   