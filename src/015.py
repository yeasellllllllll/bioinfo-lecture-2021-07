'''
import sys

if len(sys.argv) != 2:
    print(f"python {sys.argv[0]} [num]")
    sys.exit(1)

num = int(sys.argv[1])
try:
    res = 10 / num
except ZeroDivisionError as err:
    print(err)
    sys.exit(2)
print(res)
'''
'''
exit code
실행을 하면 그자체의 값으로서 프로그램이 실행시 나오는 문자가 있다.
echo $? -> '0' ->  정상종료
echo $? -> sys.exit(2) except에 넣어 둔 것이 나오면 저쪽에서 error가 발생했구나 
python 015.py 0 -> division by zero로 나오는 것을 확인할 수 있다.
'''

import sys

if len(sys.argv) != 2:
    print(f"python {sys.argv[0]} [num]")
    sys.exit(1)

try:
    num = int(sys.argv[1])
except ValueError as err:
    print(f"{err}, your input: {sys.argv[1]}")
    sys.exit(3)
try:
    res = 10 / num
except ZeroDivisionError as err:
    print(err)
    sys.exit(2)
print(res)

'''
python 015.py a -> a가 int로 변경되지 않기 때문에 에러가 발생하는 것을 미리 알려주려고 32line을 주어서 전체 조건을 잡는다.

세심하게 에러 위치를 잡기위한 것
방어적으로 코드를 짜기위한 방법이다.
사용자가 모든 사람의 생각을 알수 있기 위해서

echo $? -> '3'으로 알림이 나오는 것을 알수 있다.
'''

