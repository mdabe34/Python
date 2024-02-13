for i in range(1, 300):
    if i % 7 == 1:
        continue
    print(i)
for i in range(1,300):
    if i == 7:
        break
else:
    print("Loop completed without break")
    