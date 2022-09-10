'''print("------------program 1------------")

number=input("Enter any number :")
i=0
for i in range(len(number)):              #using a for loop range a length of number
    if number[i]!=number[-1-i]:           #using a reversed a number for if conditional statement
        print('It is not a palindrome')
        break                            # using a break control statement for the loop
    else:
        print('It is a palindrome')
        break '''

'''string=input(("Enter a string: "))
if(string==string[::-1]):
      print("This a palindrome")
else:
      print("Not a palindrome")'''

'''print("----------------program 2-----------")
n1 = 1234
n2 = 9999
output = 0

if len(str(n1)) == len(str(n2)):         #using a if condition to length of the string
    for i in range(len(str(n1))):        #using a for loop in i range of length of string
        x = str(n1)
        y = str(n2)

        output += (int(x[i]) + int(y[i]))
print(output)'''




'''print("-----------program 3------------")


def reverseString(text):
    index = -1

    # Loop from last index until half of the index
    for i in range(len(text) - 1, int(len(text) / 2), -1):         # using a for loop condition in i range

        # match character is alphabet or not
        if text[i].isalpha():
            temp = text[i]
            while True:
                index += 1
                if text[index].isalpha():
                    text[i] = text[index]
                    text[index] = temp
                    break
    return text


# Driver code
string = "ab@#cd!ef"
print("Input string: ", string)
string = reverseString(list(string))
print("Output string: ", "".join(string))'''


'''print("--------------program4--------------")

some_list = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
dict1 = {}
for key in some_list:                                                      # using a for loop  some list
    for value in some_list:                                                # using a nested for loop multiple conditions we want
        if some_list.count(value)>1 and some_list.count(key)>1 :
            dict1[key] = value
            dict1[value] = some_list.count(value)
print("The Output dictionary is : " + str(dict1))'''


print("------------program5----------------")
# print("""
#  t1 = (1, 2, 3, "a", "c")
#  t2 = ("b", "d", 9, 8, 7)
#    Output: (10,10,10,"ab","cd")
""")

t1 = (1, 2, 3, "a", "c")
t2 = ("b", "d", 9, 8, 7)


def sort_ele_of_diff_types_t1(inp):
    strs = list(filter(lambda x: type(x) == str, inp))
    ints = list(filter(lambda x: type(x) == int, inp))

    output = sorted(ints) + sorted(strs)
    return output


def sort_ele_of_diff_types(inp):
    strs = list(filter(lambda x: type(x) == str, inp))
    ints = list(filter(lambda x: type(x) == int, inp))

    output = sorted(ints, reverse=True) + sorted(strs)
    return output


list_of_t1 = sort_ele_of_diff_types_t1(t1)
list_of_t2 = sort_ele_of_diff_types(t2)

for t_1, t_2 in zip(list_of_t1, list_of_t2):
    print(t_1 + t_2)

'''print("------------program6----------------")

import re
ip = "216.08.094.196"
string = re.sub('\.[0]*', '.', ip)
print(string)'''


'''print("--------------program7------------------")

def flatten_list(n_list):
    result_list = []
    if not n_list: return result_list
    stack = [list(n_list)]
    while stack:
        c_num = stack.pop()
        next = c_num.pop()
        if c_num: stack.append(c_num)
        if isinstance(next, list):
            if next: stack.append(list(next))
        else: result_list.append(next)
    result_list.reverse()
    return result_list
n_list = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
print("Original list:")
print(n_list)
print("\nFlatten list:")
print(flatten_list(n_list))'''

print("--------------program8---------------")



with open(r'C:\\Users\\mogul\\Documents\\santhosh.txt', 'r') as fp:
    lines = fp.readlines()
    print(lines)
    for i in lines:
        print("T xxhe number of words are:",len(i.split()))
    words = i.split()
    for word in words:
        vow = sum(letter in 'aeiou' for letter in word.lower())
        if vow>=3:
            word=word[::-1]
        print("The number of vowels in", word, " :", vow)






