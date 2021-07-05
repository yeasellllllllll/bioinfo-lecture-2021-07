'''
def greet():
    print("Hello, Bioinformatics.")

def greet1(name):
    print(f"Hello, {name}")

def greet2(num):
    return num * 2

greet()
ret1 = greet1("ken")  # Hello, ken
print(ret1)           # None 출력됨

ret2 = greet2(3)      # None
print(ret2)           # 6

'''

def greet():
    print("Hello, Bioinformatics")
def greet1(name: str) -> str:  #None:(return되지 않기때문에)
    print(f"Hello, {name}")
def greet2(num: int) -> int:  #int:
    return num*2

greet()
ret1 = greet1("ken")
print(ret1)

ret2 = greet2(3)
print(ret2)

print()
def greet():
    print('Hello, Bioinformatics')

def greet1(name: str) -> None:
    print(f'Hello, {name}')

def greet2(num: int) -> int:
    return num*2

greet()
ret1 = greet2('zion')
print(ret1)

ret2=greet2(3)
print(ret2)
