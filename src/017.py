
file_name = "write_sample.txt"

handle = open(file_name, "w")
handle.write("Hello\n")
handle.write("Bioinformatics\n") 
#문장하나씩이라도 엔터를 쳐야 한다고 생각한다.
handle.close()

with open(file_name, "a") as handle:
    handle.write("ken\n")

#:set list 라고 하면 tap이 문자로 $로 보임
#:set nolist tap과 엔터가 사라진다.
#:set nonu #라인 넘버 안보이게 하는것

s = "s1,s2,s3" #csv (콤마로 분리된 문자열)
data = s.split(",") # , 구분자
print(data) # ['s1', 's2', 's3']

with open(file_name, "a") as handle:
    handle.write("\t".join(data) + "\n") 
#data가 tap으로 join되서 [s1 tap s2 tap s3 tap]이 append 되서 파일에 저장된다.
#csv -> tsv (탭으로 구분된 문자열)

