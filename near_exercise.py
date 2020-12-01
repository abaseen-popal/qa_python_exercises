
is_true = False
def cal(first_string, second_string):
    word1 = list(first_string)
    word2 = list(second_string)
    is_true = False
    for i in range(len(word1)):
        temp_list = list(word1)
        temp_list.pop(i)
        if temp_list == word2:
            is_true = True
            
            break
        else:
            is_true = False
    print(is_true)
        
            

cal("reset","rest")
cal("dragoon","dragon")
cal("eave","leave")
cal("sleet","lets")