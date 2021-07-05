import sys

if len(sys.argv) != 3:   #인자가 3개가 아니면 알려준다.
    print(f"#usage: python {sys.argv[0]} [n1] [n2]")
    sys.exit()

n1 = int(sys.argv[1])
n2 = int(sys.argv[2])

print(f"{n1} + {n2} = {n1+n2}")
print(f"{n1} - {n2} = {n1-n2}")
print(f"{n1} * {n2} = {n1*n2}")
print(f"{n1} / {n2} = {n1/n2}")
print(f"{n1} % {n2} = {n1%n2}")
print(f"{n1} ** {n2} = {n1**n2}")

