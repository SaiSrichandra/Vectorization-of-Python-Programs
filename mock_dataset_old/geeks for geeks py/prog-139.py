def empty_list_remove(input_list):
    new_list = []
    for ele in input_list:
        if ele:
            new_list.append(ele)
    return new_list
 
 
# input list vlues
input_list = [5, 6, [], 3, [], [], 9]
 
# print initial list values
print(f"The original list is : {input_list}")
# function-call & print values
print(f"List after empty list removal : {empty_list_remove(input_list)}")