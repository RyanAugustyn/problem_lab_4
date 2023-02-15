#Problem Solving IV 

#Task 1: return indices of numbers that add to target 

#input array of numbers
#starting with first loop through the others and add to see if reaches target 
#if no, start looping again at next number

def find_indices_of_target(list_input, target):
    result =[]
    for x in range(len(list_input)):
        for y in range(1, len(list_input)):
            if list_input[x] + list_input[y] == target:
                result.append(x)
                result.append(y)
    if result == []:
        print("no number combination works to reach target")
        return "none"

    print(result)
    return result

# find_indices_of_target([5, 17, 77, 50])


#Task 2: Palindrome

#done in lab 3, recopying

def palindrome_minus_punc(string_input):
    user_input = string_input.lower()
    alphanum_string =''
    for char in range(len(string_input)):
        if user_input[char].isalnum(): 
            alphanum_string += user_input[char]
    print(alphanum_string)
    halfway = int(len(alphanum_string)/2) + 1
    for i in range(halfway):
        if alphanum_string[i] != alphanum_string[-1 - i]:
            print("Is not a palindrome")
            return False
        
    print("Yes, it is a palindrome")
    return True


# palindrome_minus_punc("  A man, a plan, a canal: PANAMA")



#Task 3: Given a list of integers, return a bool that represents whether or not all integers in the list can form a sequence of incrementing integers 

list1 = [5, 7, 3, 8, 6]  #returns False (no 4 to complete the sequence) 
list2 = [17, 15, 20, 19, 21, 16, 18]  # returns True

#find lowest value number in list, or or sort list from lowest to highest
#once found lowest, the increment is 1, so search through to see if num + 1 is found
#if loop completes, return true, else return false

#sort list function 
def sort_num_list(input_list): 
    new_list = []
    temp = 0
    while (len(input_list)) > 0: 
        temp = input_list[0]
        for x in range(len(input_list)):
            if temp > input_list[x]: 
                temp = input_list[x]
        new_list.append(temp)
        input_list.remove(temp)
    return new_list

#task function
def is_incrementing_sequence(input_list):
    list = sort_num_list(input_list)

    for x in range(len(list) - 1):
        if list[x] + 1 != list[x + 1]:
            return False
    return True

# print(is_incrementing_sequence(list1))
# print(is_incrementing_sequence(list2))




#Task 4:  Take an array of positive and negative numbers. Return an array where the first element is the count of the positive numbers and the second element is the sum of negative numbers.  
# Use case: [7, 9, -3, -32, 107, -1, 36, 95, -14, -99, 21] 

#take array as input
#loop through list, if num is positive add to one list, if neg to the other
#combine the lists and return them 

def sum_pos_and_neg(input_list): 
    pos_sum = 0
    neg_sum = 0
    result = []
    for x in range(len(input_list)):
        if input_list[x] > 0:
            pos_sum += input_list[x]
        else:
            neg_sum += input_list[x]
    result.append(pos_sum)
    result.append(neg_sum)
    return result

#print(sum_pos_and_neg([7, 9, -3, -32, 107, -1, 36, 95, -14, -99, 21]))




#Task 5: Create a method that accepts a string of space separated numbers and returns the highest and lowest number as a string 
#Use case: “3 9 0 1 4 8 10 2”  returns: “0 10” 

#take in number string
#use isalphanum function to remove spaces: looked up, better isnumeric() 
#loop through string and change into integers and append to list
#use above sorting list method
#append a result list the returns the values at indices 0 and -1 
#did not acccount for multi digit numbers 
#create temp value to hold all numeric chars until hit a space 

def high_and_low_string(input_string):
    list = []
    result = []
    temp_string = ''
    for x in range(len(input_string)):
        if input_string[x].isnumeric():   
            temp_string += input_string[x]
            continue
        else:
            list.append(int(temp_string))
            temp_string = ''
    list = sort_num_list(list)
    result.append(list[0])
    result.append(list[-1])

    return result


#print(high_and_low_string("3 9 0 1 4 8 10 2"))




#Task 6 : Email validation Create a method that accepts a string, checks if it’s a valid email address and returns either true or false depending on the valuation. 
# Think about what is necessary to have a valid email address. 
#Use case: “mike1@gmail.com” returns True “gmail.com” returns False 

#email contains alphanumeric characters, an '@' symbol, some more alphanumeric characters, and ends in '.com' or '.org'
#function to loop through and checks first is alphanumceric, 
#if not then checks for @ and if found continues
#checks for more alphanumeric until period is found
#then checks if .com or .org
#if fails any of the tests, not valid 
#break into multiple loops in case of two '@'s 
#switch '.' check and isalnum check in 2nd loop 

def is_valid_email(user_input):
    #check if starts with valid char
    if user_input[0].isalnum() != True:
        return False
    temp = 0
    for x in range(1, len(user_input)):
        if user_input[x].isalnum():
            continue
        elif user_input[x] == '@':
            temp = x
            break
        else:
            return False
    for x in range(temp, len(user_input)):
        if user_input[x] == '.': 
            temp = x
            break 
        elif user_input[x].isalnum:
            continue
        else:
            return False
    string =''
    for x in range(temp, len(user_input)):
        string += user_input[x]
    if string == '.com' or string == '.org':
        return True
    else:
        return False 


# print(is_valid_email("mike1@gmail.com"))
# print(is_valid_email("gmail.com"))



#Task 7 Create a method that takes in a string and replaces each letter with its appropriate position in the alphabet and returns the string 
#Use case: “abc” returns “1 2 3” “coding is fun” returns “3 15 4 9 14 7 9 19 6 21 14” 

#try printing an int of a letter, doesn't work 
#looked up 'ord' function, which translates letter to ASCII character 
#change all letters to lowercase and subtract 96 to get alphabet position 
#take in string, 
#if space add in extra space

def letters_to_alpha_position(user_input): 
    results = ''
    for x in range(len(user_input)):
        lower_case = user_input.lower()
        if lower_case[x].isalpha():   
            num = ord(lower_case[x])
            results += str(num - 96)
            results += " "
            continue
        else:
            results += "  "
    return results
            



# print(letters_to_alpha_position("coding is fun"))






#Task 8: Briefcase Lock  A briefcase has a four-digit rolling-lock. Each digit is a number from 0-9 that can be rolled either forwards or backwards. W
# rite a method that returns the smallest number of turns it takes to transform the lock from current combination to the target combination. 
# One turn is equivalent to rolling a number forwards or backwards by one.  

#Use case:  Current lock: 3893 Target lock: 5296 

#subtract numbers  find absolute value: which is abs() 
#loop through lock and find number of turns for each
#add to result and return 
#translate numbers, to str, back to int
#so 8-2 case not accounted for, nor something like 7-1
#in both cases, difference is 4, which can be reached by adding 10 to smaller number and subtracting other (1 + 10 - 7 = 4)
#can get abs number subtraction, compare with other method, and user smaller number

def add_ten_to_smaller(num1, num2): 
    if num1 < num2:
        num1 += 10
    else:
        num2 += 10
    return abs(num1 - num2)

def num_of_turns(current_lock, target_lock):
    current = str(current_lock)
    target = str(target_lock)
    result = 0
    for x in range(len(current)):
        num1 = int(current[x])
        num2 = int(target[x])
        modified = add_ten_to_smaller(num1, num2)
        if modified < abs(num1 - num2):
            result += modified
        else:
            result += abs(num1 - num2)

    return result

#print(num_of_turns(3893, 5296))





#Task 9: Given a number, return the reciprocal of the reverse of the original number, as a double.  
#Use case: If given 17, return 0.01408 (1/71) 


#take in number, convert to string, reverse, 
#convert to double with float(), divide one by that number 
#return the result 

def reciprocal_reverse(num1): 
    num1 = str(num1)
    reversed_num = ''
    result = 0
    for x in range(len(num1)):
        reversed_num = num1[x] + reversed_num
        print(reversed_num)
    result = 1 / float(reversed_num)
    return result


# print(reciprocal_reverse(17))