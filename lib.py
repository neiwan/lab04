N = int(input("Введите количество списков\n"))
strings = []
symbols = []
repeats = []
for i in range(N):
    strings.append(input("Введите строку " + str(i + 1) + "\n"))
for i in range(len(strings)):
    stroka = strings[i]
    for j in range(len(stroka)):
        ECTb = False
        for k in range(len(symbols)):
            if stroka[j] == symbols[k]:
                repeats[k] = True
                ECTb = True
        if not ECTb:
            symbols.append(stroka[j])
            repeats.append(False)
            K = 0
for i in range(len(repeats)):
    if repeats[i]:
        K += 1
print(repeats)
print(symbols)
print(stroka)
print("Количество повторяющихся символов: " + str(K))
