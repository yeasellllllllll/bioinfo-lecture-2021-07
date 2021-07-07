'''
file_name = "read_sample.txt"

#파일읽는 방법 1
with open(file_name, "r") as handle:
    for line in handle:
        print(line)

#한줄씩 띄어져서 출력되는 이유는 ?????
#-> 원래 line에 엔터가 있었고 print에도 엔터가 있어서
#print(line.strip())->으로 엔터를 날려버린다.
#with open 파일 오픈 변수를 handle로 연다.
#for문의로 한줄한줄 가져올수 있다.

#파일 읽는 방법 2
file_name = "read_sample.txt"

handle = open(file_name, "r")

for line in handle:
    print(line.strip())
handle.close() 
#with open에서는 close를 쓰지 않아도 된다. 그게 가장큰 장점!!!
'''

#파일 읽는 방법 3
file_name = "read_sample.txt"
handle = open(file_name, "r")

lines = handle.readlines()
for line in lines:
    print(line.strip())
handle.close() 

#3번을 with open 수정시
file_name = "read_sample.txt"

with open(file_name, "r") as handle:
    lines = handle.readlines()
    for line in lines:
        print(line.strip())



