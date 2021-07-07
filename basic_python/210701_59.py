#! /usr/bin/env python


#내꺼답!
test = 'We tried list and we tried dicts also we tried Zen'

l_test = test.split()
ll_test = set(l_test)
d_dictionary = dict()
for i in ll_test:
    print(i, l_test.count(i))
    d_dictionary[i] = l_test.count(i)
print(d_dictionary)

'''
강사님 팁준거?
d_dict = dict() #create empty dictionary
if 'and' in d_dict: print('theres and!') #check if keys in dictionary 않나오면 key없는것

d_dict.get('and') #get value from dictionary 

d_dict['and'] = 1 #assign key-value parir for dict

if 'and' in d_dict: # check if keys in dictionary
    print('theres and!')

d_dict.get('and')
'''

toCount = 'We tried list and we tried dicts also we tried Zen'

d_Count = dict()

l_toCount = toCount.split()
for key in l_toCount: #단어리스트
    print(key.strip()) #단어확인

    if key not in d_Count: #딕셔너리 키유무
        d_Count[key] = 1 #없으면1
    else:
        d_Count[key] += 1 #있으면 +1

#강사님 방법1
for i in d_Count:
    print(i, d_Count[i])

#강사님 방법2
for k, v in d_Count.items():
    print(k, v)


'''
목표
{단어:개수} 딕셔너리 (key:value)
key가 딕셔너리에 없으면 1
key가 딕셔너리에 있으면 +1
'''
