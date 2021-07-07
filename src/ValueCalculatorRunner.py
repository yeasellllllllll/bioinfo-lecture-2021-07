from ValueCalculator import ValueCalculator
#from "파일이름" improt "class 또는 함수이름"
#from ValueCalculator import A (해당파일에 있는 특정 A Class만 가져올때)
value_calculator_1 = ValueCalculator("a")
value_calculator_2 = ValueCalculator("b")

res = value_calculator_1 + value_calculator_2

print(res)


from ValueCalculator import Add
print(Add(2,3))

