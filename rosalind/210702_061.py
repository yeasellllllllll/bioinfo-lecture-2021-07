#! /usr/bin/env python

#061
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

#062
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

#063
print(nums[1::2])

#064
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

#065
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], end=' ')
print(interest[2])
print(interest[0], interest[2])

#066
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(interest[:])
print(" ".join(interest))

#067
print("/".join(interest))

#068
print("\n".join(interest))

#69
string = "삼성전자/LG전자/Naver"
print(string.split('/'))

#70
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)
 
