'''
#1답
import sys

if len(sys.argv) != 2:   
    print(f"#usage: python {sys.argv[0]} [num]")
    sys.exit()

num = int(sys.argv[1])

if num % 3 == 0:
    result = "3의 배수"
elif num % 7 == 0:
    result = "7의 배수"
'''
#2답
import sys

if len(sys.argv) != 2:   
    print(f"#usage: python {sys.argv[0]} [num]")
    sys.exit()

num = int(sys.argv[1])
result = "neither 3,7"

if num % 3 == 0 and num % 7 == 0:
    result = '3,7'
elif num % 3 == 0:
    result = '3'
elif num % 7 == 0:
    result = '7'

print(result)
