#! /usr/bin/env python

# 251
# 클래스:똑같은 무엇인가를 계속해서 만들어낼 수 있는 설계, 틀과 같은 것
# 속성
# method
# 객체:객체(object)는 클래스에 의해서 만들어진 물건, 실체를 뜻합니다.
# 인스턴스: 클래스에 의해서 만들어진 객체를 인스턴스(instance)

# # 252
# from os import name


# class Human:
#     pass


# # 253
# class Human:
#     pass


# areum = Human()

# # 254
# class Human:
#     def __init__(self):
#         print("응애응애")


# areum = Human()

# # 255
# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex


# areum = Human("아름", 25, "여자")
# print(areum.name)
# print(areum.age)
# print(areum.sex)

# # 257
# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex

#     def who(self):
#         print(f"이름: {self.name}, 나이 {self.age}, 성별: {self.sex}")


# areum = Human("아름", 25, "여자")
# print(areum.name)
# print(areum.age)
# print(areum.sex)
# areum.who()

# # 258
# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex

#     def who(self):
#         print(f"이름: {self.name}, 나이: {self.age}, 성별: {self.sex}")

#     def setInfo(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex


# areum = Human("불명", "미상", "모름")
# areum.who()

# areum.setInfo("아름", 25, "여자")
# areum.who()

# # 259
# class Human:
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex

#     def who(self):
#         print(f"이름: {self.name}, 나이: {self.age}, 성별: {self.sex}")

#     def __del__(self):
#         print("나의죽음을 알리지 마라")

#     def setInfo(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex


# areum = Human("아름", 25, "여자")
del areum

# 260
class OMG:
    def print():
        print("Oh my god")


mystock = OMG()
mystock.print()
