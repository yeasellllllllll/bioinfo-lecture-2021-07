#031
s = 'AA,AC,AG,AT'
data = s.split(",")
print(data)

#032
data.append("CA")
print(data)

#033
print(data[::-1])

#034
data = [3, 1, 1, 2, 0, 0, 2, 3, 3]
print(min(data))
print(max(data))

#035
data = [3, 1, 1, 2, 0, 0, 2, 3, 3]
d_data = {}

for num in data:
    if num not in d_data:
        d_data[num] = 0
    d_data[num] += 1
print(d_data)
