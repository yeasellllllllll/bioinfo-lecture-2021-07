#gzip 압축하기 : gzip 파일명 -> 파일명.gz
#     압축풀기 : gunzip 파일명.gz -> 파일명 (압축파일 삭제됨)
#     압축풀기(stdout) : gunzip-c 파일명.gz > 파일명 (압출파일 그냥 파일 다 가지고 싶을때 사용방법)

#파일받고
#gzip으로 압축하고 -> gzip covid19.fasta
#python script로 gzip 파일 읽어서 A,C,G,T 숫자세기
'''
f_name = 'covid19.fasta'

data = dict() #data = {}  / 리스트 초기화 data=list()=[]
              #set 초기화 s = set()
with open(f_name, 'r') as handle:
    for line in handle:
        if line.startswith(">"): 
            continue 
        for base in line.strip(): #fasta 파일은 line마다 엔터로 나눠짐
            if base not in data:
                data[base] = 0
            data[base] += 1
print(data)

'''
import gzip
ff_name = 'covid19.fasta.gz'
#파일 경로가 다른경우 해당경로 다음에 파일 이름을 넣어서 name 지정한다.
data = dict() 

with gzip.open(ff_name, 'rt') as handle: #rt -> text, rb->바이너리
# 'rt' -> 'rb'로 파일을 여는 경우
    for line in handle:
        #line = line.decode("utf-8")
        if line.startswith(">"): 
            continue 
        for base in line.strip():
            if base not in data:
                data[base] = 0
            data[base] += 1
print(data)


    
