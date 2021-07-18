"""1. 입력받은 DNA서열의 길이와 유효한 문자들을 센 값이 서로 같은지 확인하여 전체 서열이
유효한 문자를 가지고 있는지 확인한다.
>> 결과값 : 유효하면 True, 유효하지 않으면 False"""

a = input("DNA seq.: ")

if len(a) == a.count("A") + a.count("T") + a.count("G") + a.count("C"):
    print("True")
else:
    print("False")
