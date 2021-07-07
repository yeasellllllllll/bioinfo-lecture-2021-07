#1 /usr/bin/env python

letters = 'python'
print(letters[0] + ' ' +  letters[2])

license_plate = "24가 2210"
print(license_plate[4:])

string = "홀짝홀짝홀짝"
print(string[0]*3)
print(string[::2])

string = "PYTHON"
print(string[::-1])

phone_number = "010-1111-2222"
print(phone_number.replace('-', ' '))
phone_number1 = phone_number.replace('-', ' ')
print(phone_number1.replace(' ', ''))

url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split[-1])

string = 'abcdfe2a354a32a'
print(string.replace('a', 'A'))

a='3'
b='4'
print(a+b)
print(int(a) + int(b))

print('Hi' * 3)

t1 = 'python'
t2 = 'jave'

print((t1 + ' ' +  t2 + ' ') * 4)

name1 = '김민수'
name2 = '이철희'
age1 = 10
age2 = 13

print("이름: ", name1, "나이: ", age1)

상장주식수 = "5,969,782,550"
print(int(상장주식수.replace(',', '')))

a = "hello world"
print(a.split())

date = "2020-05-01"
print(date.split("-"))

data = "039490      "
print(data.rsplit())

movie_rank = ['닥터  스트레인지', '스플릿', '럭키', '배트맨']
print(movie_rank)
movie_rank.insert(1, '슈퍼맨')
print(movie_rank)
movie_rank.remove[2]
print(movie_rank)
