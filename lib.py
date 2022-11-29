N = int(input("Введите количество списков\n"))
strings = []
repeats = []
dictionary = []
count = 0
for i in range(N):
    strings.append(input("Введите строку " + str(i + 1) + "\n"))
for i in range(len(strings)):
    stroka = strings[i]
    for j in range(len(stroka)):
        if dictionary.__contains__(stroka[j]):
            count += 1
            repeats.append(stroka[j])
        else:
            dictionary.append(stroka[j])
print(repeats)
print("Количество повторяющихся символов: ", len(repeats))
