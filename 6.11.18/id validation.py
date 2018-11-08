def get_sum(num):
    sum =0
    for i in num:
        sum+= i
    return sum

def is_valid(id):
    multipler = [1,2,1,2,1,2,1,2,1]
    multipler_result = [0,0,0,0,0,0,0,0,0]
    # add zero if the id is too short
    if len(id) < 9:
        id = '0'*(abs(len(id)-9)) +id
    for index,value in enumerate(id) :
        multipler_result[index] = int(value) * multipler[index]
    print(multipler_result)   
    for index,value in enumerate(multipler_result):
        if value > 9:
            multipler_result[index] = int((value / 10)) + int(value%10)
    print(multipler_result)
    print(get_sum(multipler_result))
    if get_sum(multipler_result) % 10 ==0:
        return True


def check_is_digit(id):
    # length check
    if len(id) > 9:
        return False
    
    for i in id:
        if ord(i) < 48 or ord(i)  > 57:
            return False
    return True


user_id = input("Please enter id to validate: ")
# check that the user enter just numbers
while not check_is_digit(user_id):
    print("the id you entered contain unvalid chars or is too long")
    user_id = input("Please enter id to validate: ")

if is_valid(user_id):
    print("the id: {0} is valid".format(user_id))
else:
    print("the id: {0} isn't valid".format(user_id))






    