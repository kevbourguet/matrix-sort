with open("testmatrix1.txt", 'r') as input_file:

    input_file = [[int(i) for i in j.split()] for j in input_file] #presents each number in a list of lists by row
    # print(input_file)

    for row in input_file:
        matrix = (' '.join(map(str,row))) #displays the matrix
        # print(matrix)

    horizontal_sum_list = (list(map(sum, input_file))) #sum of each row horizontally
    # print(horizontal_sum_list)

    sorted_input_file = sorted(input_file, key=sum)
    # print(sorted_input_file)

    for x in sorted_input_file:
        matrix2 = (' '.join(map(str, x)))
        # print(matrix2)



    full_list = []
    invert_list = []
    newest_list = []
    for i in range(0, len(input_file[0])):#         forms everything into a single list
        for j in range(0,len(input_file)):
            full_list.append(input_file[j][i])
    # print(full_list)
    
    
    n = len(input_file)
    invert_list = ([full_list[i:i+n] for i in range(0, len(full_list), n) ]) #inverts the list 
    # print(invert_list)

    vertical_sum_list = (list(map(sum, invert_list))) #sum of each row vertically
    # print(vertical_sum_list)

    vertical_sum_sorted = sorted(invert_list, key=sum)
    # print(vertical_sum_sorted)

    vertical_sum_order = []
    for i in range(0, len(vertical_sum_sorted[0])):#         forms everything into a single list
        for j in range(0,len(vertical_sum_sorted)):
            vertical_sum_order.append(vertical_sum_sorted[j][i])

    print(vertical_sum_order)

    size = 1 + len(input_file)
    final_vertical_ordered_list = ([vertical_sum_order[i:i+size] for i  in range(0, len(vertical_sum_order), size)])
    
    for p in final_vertical_ordered_list:
        matrix3 = (' '.join(map(str,p))) #displays the matrix
        print(matrix3)


    

            
            
            
    