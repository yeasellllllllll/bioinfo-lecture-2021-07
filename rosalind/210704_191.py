#! /usr/bin/env python
'''
#191
#data에는 매수한 종목들의 OHLC (open/high/low/close) 가격 정보가 바인딩 되어있다.

data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

for line in data:
    for column in line:
        print(column * 1.00014)

#192
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

for line in data:
    for column in line:
        print(column * 1.00014)
    print("----")

#193
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
result = []

for line in data:
    for column in line:
        result.append(column * 1.00014)
print(result)

#194
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
result = []

for line in data:
    lines = []
    for column in line:
        lines.append(column * 1.00014)
    result.append(lines)
print(result)

#195
#ohlc 리스트에는 시가(open), 고가 (high), 저가 (low) , 종가(close)가 날짜별로 저장

ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for line in ohlc[1:]:
    print(line[3])

#196
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for line in ohlc[1:]:
    if(line[3]>150)
        print(line[3])

#197
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for line in ohlc[1:]:
    if(line[3] >= line[0]):
        print(line[3])

#198
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

valatility = []
for line in ohlc[1:]:
    valatility.append(line[1] - line[2])
print(valatility)

#199
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for line in ohlc[1:]:
    if line[3] > line[0]:
        print(line[1] - line[2])

#200
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
gap = []
for line in ohlc[1:]:
    gap.append(line[3] - line[0])
print(sum(gap))
'''
#다른답
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

profit = 0
for row in ohlc[1:]:
    profit += (row[3] - row[0])
print(profit)
