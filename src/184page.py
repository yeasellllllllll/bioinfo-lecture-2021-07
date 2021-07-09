import sys
n_pivo = sys.argv[1]
l_pivo = [0, 1]

def pivo(n):
    for i in range(n- len(l_pivo))
        l_pivo.append(l_pivo[-1] + l_pivo[-2])
    print(l_pivo[-1])
    print(l_pivo)
pivo(n_pivo)


# import sys

# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# n = int(sys.argv[1])
# print(fib(n))
