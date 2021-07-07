'''
#에러 이름 체크
with open("noname.txt",'r') as handle:
    data = handle.readlines()
print(data)
#에러이름으로 에러명 예외 처리하기(Debugging)
import sys

try:
    with open("noname.txt", 'r') as handle:
        data = handle.readlines()
    print(data)

except FileNotFoundError as err:
    print(err)
    sys.exit()

#파일이 없는 것을 확인하고 에러 메시지 나온 FileNotFoundError를 넣어준다.
#에러 명을 구체화 시켜 넣어 줘야한다!
'''

#109page

# 값을 0을 넣는경우 + 값을 넣지 않는 경우 오류 발생하게 하기
'''
에러 코드 확인하기
num = int(input("Enter: "))
print(10 / num)

# o -> ZeroDivisionError
# 값이 없을때 -> ValueError
'''
'''
import sys

try:
    val = int(input("Enter: "))
except ValueError as err:
    print(err)
    sys.exit()
try:
    print(10/val)
except ZeroDivisionError as err:
    print(err)
    sys.exit()
'''
# 두개의 err 합치는 방법
import sys

try:
    val = int(input("Enter: "))
    print(10 / val)
except ValueError as err1:
    print(err1)
    sys.exit()      
#err1, err2 구분 없이 err로 지정해도 같은 결과 나옴
except ZeroDivisionError as err2:
    print(err2)
    sys.exit()

