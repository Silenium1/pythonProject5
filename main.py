bugs = []
features = []
design = []
while True:
    x = input().split(': ')
    if len(x) == 2:
        if x[0] == 'Добавить в bugs':
            bugs.append(x[1])
        elif x[0] == 'Добавить в features':
            features.append(x[1])
        elif x[0] == 'Добавить в design':
            design.append(x[1])
    if len(x) == 1 and x[0] != 'Релиз!':
        if x[0] == "Убрать задание из bugs":
            bugs.pop()
        elif x[0] == "Убрать задание из features":
            features.pop()
        elif x[0] == "Убрать задание из design":
            design.pop()
    if x[0] == "Релиз!":
        if len(bugs) == 0:
            print("Все исправлено!")
        else:
            print(bugs[-1])
        if len(features) == 0:
            print("Все исправлено!")
        else:
            print(features[-1])
        if len(design) == 0:
            print("Все исправлено!")
        else:
            print(design[-1])
        break


