#! /usr/bin/env python
'''
#221
def print_reverse(string):
    print(string[::-1])

print_reverse("python")

#222
def print_score(scores):
    average = sum(scores)/len(scores)   
    print(average)

print_score([1, 2, 3])
#223
def print_even(nums):
    result = []    
    for i in nums:
        if i % 2 ==0:
            result.append(i)
    print(i)
print_even ([1, 3, 2, 10, 12, 11, 15])

#224
def print_keys(dic):
    for keys in dic.keys():
        print(keys)

print_keys ({"이름":"김말똥", "나이":30, "성별":0})

#225
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}

def print_value_by_key (my_dict, key):
    print(my_dict[key])

print_value_by_key (my_dict, "10/26")

#226
def print_5xn(string):
    check_num = int(len(string) /5)
    print(check_num)
    for i in range(check_num + 1): #[0,1,2]
        print(string[i * 5 : i * 5 + 5])

print_5xn("아이엠어보이유알어걸")

#227
def print_mxn(string, num):
    check_num = int(len(string)/num)
    print(check_num)
    for i in range(check_num + 1):
        print(string[i*num : i*num + num])

print_mxn("아이엠어보이유알어걸", 3)

#228
def calc_monthly_salary(annual_salary):
    print(int(annual_salary/12))

calc_monthly_salary(12000000)
'''
#229

#230

'''
def func():
    return "abc"

v = func()
print(v) 

def func():
    print("abc")

v = func() 
print(v) 
'''
