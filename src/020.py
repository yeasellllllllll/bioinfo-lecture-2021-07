'''
a = input("string :")
b = input("string :")

print(a + b)
'''
'''
# class 를 배웠다고 하니
class A: 
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        return self.val + other.val
    def __mul__(self, other):
        return "__mul__"
a1 = A("a") 
a2 = A("b")
a1.val + a2.val #-> ab
print(a1.val + a2.val)
print(a1 + a2)
print(a1 * a2)
'''
