#! /usr/bin/env python

# # 261
# class Stock:
#     pass


# # 262
# class Stock:
#     def __init__(self, name, code):
#         self.name = name
#         self.code = code


# 삼성 = Stock("삼성전자", "005930")
# print(삼성.name)
# print(삼성.code)

# # 263
# class Stock:
#     def __init__(self, name, code):
#         self.name = name
#         self.code = code

#     def set_name(self, name):
#         self.name = name


# a = Stock(None, None)
# a.set_name("삼성전자")
# print(a.name)

# # 264
# class Stock:
#     def __init__(self, name, code):
#         self.name = name
#         self.code = code

#     def set_name(self, name):
#         self.name = name

#     def set_code(self, code):
#         self.code = code


# a = Stock(None, None)
# a.set_code("005930")
# print(a.code)

# print()
# # 265
# class Stock:
#     def __init__(self, name, code):
#         self.name = name
#         self.code = code

#     def set_name(self, name):
#         self.name = name

#     def set_code(self, code):
#         self.code = code

#     def get_stock(self):
#         return self.code

#     def get_name(self):
#         return self.name


# a = Stock(None, None)
# a.set_code("005930")
# print(a.code)
# 삼성 = Stock("삼성전자", "005930")
# print(삼성.get_stock())
# print(삼성.get_name())

# # 266
# class Stock:
#     def __init__(self, name, code, float(PER), float(PBR), float(add)):
#         self.name = name
#         self.code = code
#         self.PER = float(PER)
#         self.PBR = float(PBR)
#         self.add = float(add)

# 267
# class Stock:
#     def __init__(self, name, code, PER, PBR, add):
#         self.name = name
#         self.code = code
#         self.PER = float(PER)
#         self.PBR = float(PBR)
#         self.add = float(add)


# a = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
# print(a.name)
# print(a.code)
# print(a.PER)
# print(a.PBR)
# print(a.add)

# # 268, 269
# class Stock:
#     def __init__(self, name, code, PER, PBR, add):
#         self.name = name
#         self.code = code
#         self.PER = float(PER)
#         self.PBR = float(PBR)
#         self.add = float(add)

#     def set_per(self, PER):
#         self.PER = float(PER)

#     def set_pbr(self, PBR):
#         self.PBR = float(PBR)

#     def set_dividend(self, add):
#         self.add = float(add)


# a = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
# a.set_per(12.75)
# print(a.PER)

# 270
class Stock:
    def __init__(self, name, code, per, pbr, add):
        self.name = name
        self.code = code
        self.per = float(per)
        self.pbr = float(pbr)
        self.add = float(add)

    def set_per(self, PER):
        self.per = float(per)

    def set_pbr(self, PBR):
        self.pbr = float(pbr)

    def set_dividend(self, add):
        self.add = float(add)


삼성전자 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "0665700", 317.34, 0.69, 1.37)

l_stock = []
l_stock.append(삼성전자)
l_stock.append(현대차)
l_stock.append(LG전자)
print(l_stock)

for i in l_stock:
    print(i.code, i.per)
