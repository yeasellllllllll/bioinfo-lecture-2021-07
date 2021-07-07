#! /usr/bin/env python
'''
#171
price_list = [32100, 32150, 32000, 32500]

for i in range(4):
    print(price_list[i])

for i in range(len(price_list)):
    print(price_list[i])

#172
price_list = [32100, 32150, 32000, 32500]
pp = list(enumerate(price_list))
print(pp)

for i, j in enumerate(price_list):
    print(i, j)

#173
price_list = [32100, 32150, 32000, 32500]
print(len(price_list))
for i in range(len(price_list)):
    print(3-i, price_list[i])

#174
price_list = [32100, 32150, 32000, 32500]

for i in range(1,4):
    print(90+10*i, price_list[i])

#175
my_list = ["가", "나", "다", "라"]

for i in range(3):
    print(my_list[i], my_list[i+1])

#176
my_list = ["가", "나", "다", "라", "마"]

for i in range(len(my_list)-2):
    print(my_list[i], my_list[i+1], my_list[i+2])

#177
my_list = ["가", "나", "다", "라"]

for i in range(1, len(my_list)):
    print(my_list[-i], my_list[3-i])

#178
my_list = [100, 200, 400, 800]

for i in range(len(my_list)-1): #[0, 1, 2]
    print(my_list[i+1] - my_list[i])

#179
my_list = [100, 200, 400, 800, 1000, 1300]

for i in range(len(my_list)-2): #[0,1,2,3]
    print(int(my_list[i] + my_list[i+1] + my_list[i+2]) / 3)
'''    
#180
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatility = []
for i in range(len(low_prices)):
    volatility.append(high_prices[i] - low_prices[i])

print(volatility)

