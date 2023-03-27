# inp = input()
# a, b = inp.split()
# a = int(a)
# b = int(b)
# print(a + b)

# inp = input()
# res = []
# words = inp.split()
# for word in words:
#     res.append(int(word))
# print(res)

# inp = input()
# res = []
# words = inp.split()
# res = list(map(int, words))
# print(res)


inp = input()
res = []
words = inp.split()
res = [int(word) for word in words]  приведение типа к list с помощью []
# res = sorted((int(word) for word in words), reeverse = True)
print(res)