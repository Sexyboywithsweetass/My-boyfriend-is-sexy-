a = int(input("Кол-во часов:"))
b = int(input("Заработок в час:"))
if a>40:
    print("i=", a*b*1.5, sep="")
else:
    print("i=", a*b, sep="")
