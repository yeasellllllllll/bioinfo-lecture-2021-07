#! /usr/bin/env python

#091, 092
inventory ={'메로나':[300, 20], '비비빅':[400,3], '죠스바':[250, 100]}
print(inventory['메로나'][0], '원')

#093
print(inventory['메로나'][1],'개')

#094
inventory.update(월드콘=[500, 7])
print(inventory)

#095
icecream = {'탱크보이':1200, '폴라포':1200, '빵빠레':1800, '월드콘':1500, '메로나':1000}
print(icecream.keys())

#096
print(icecream.values())

#097
print(sum(icecream.values()))

#098
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)

#099
keys = ('apple', 'pear', 'peach')
vals = (300, 250, 400)
result = {keys[0]:vals[0], keys[1]:vals[1], keys[2]:vals[2]}

print(result)

#100

