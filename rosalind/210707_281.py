#! /usr/bin/env python

# 281
# class 차:
#     def __init__(self, 바퀴, 가격):
#         self.바퀴 = 바퀴
#         self.가격 = 가격


# car = 차(2, 1000)
# print(car.바퀴)  # 2
# print(car.가격)  # 1000

# 282
# class 차:
#     def __init__(self, 바퀴, 가격):
#         self.바퀴 = 바퀴
#         self.가격 = 가격


# class 자전차(차):
#     def __init__(self, 바퀴, 가격, 구동계):
#         self.바퀴 = 바퀴
#         self.가격 = 가격
#         # 부모클래스(super)의 생성자 호출 위의 두줄을 한줄로 변경
#         # 밑에 두개 동일한 이야기임!
#         # super().__init__(바퀴, 가격)
#         # 차.__init__(바퀴, 가격)
#         self.구동계 = 구동계


# 283 (282+283)
# bicycle = 자전차(2, 100)
# print(bicycle.가격)  # 100

# 284 (282+284)
# bicycle = 자전차(2, 100, "시마노")
# print(bicycle.구동계)  # 시마노

# 285
# class 차:
#     def __init__(self, 바퀴, 가격):
#         self.바퀴 = 바퀴
#         self.가격 = 가격


# class 자동차(차):
#     def __init__(self, 바퀴, 가격):
#         super().__init__(바퀴, 가격)

#     def 정보(self):
#         print(f"바퀴수: {self.바퀴}")
#         print(f"가격: {self.가격}")


# car = 자동차(4, 1000)
# car.정보()  # 바퀴수 4, 가격 1000

# 286
# class 차:
#     def __init__(self, 바퀴, 가격):
#         self.바퀴 = 바퀴
#         self.가격 = 가격


# class 자전차(차):
#     def __init__(self, 바퀴, 가격, 구동계):
#         super().__init__(바퀴, 가격)
#         # 차.__init__(바퀴, 가격)
#         self.구동계 = 구동계

#     def 정보(self):
#         print(f"바퀴수: {self.바퀴}")
#         print(f"가격: {self.가격}")
#         print(f"구동계: {self.구동계}")


# bicycle = 자전차(2, 100, "시마노")
# bicycle.정보()  # 바퀴수 2, 가격 100

# 288 (메서드 오버라이딩)
class 부모:
    def 호출(self):
        print("부모호출")


class 자식(부모):
    def 호출(self):
        print("자식호출")


나 = 자식()
나.호출()  # 자식호출

# 289
class 부모:
    def __init__(self):
        print("부모생성")


class 자식(부모):
    def __init__(self):
        print("자식생성")


나 = 자식()
# 290
class 부모:
    def __init__(self):
        print("부모생성")


class 자식(부모):
    def __init__(self):
        print("자식생성")
        super().__init__()


나 = 자식()
