import random

tab1 = [random.randrange(1, 99) for _ in range(4)]
tab2 = [random.randrange(1, 99) for _ in range(2)]
tab3 = []
i1 =0
i2 =0
print(tab1)
print(tab2)
for i in range(0, len(tab1) + len(tab2)):
    if tab1[i1] < tab2[i2]:
        tab3.append(tab1[i1])
        tab1[i1]=tab1[i+1]
    else:
        tab3.append(tab2[i2])
        tab2[i2]=tab2[i+1]
    print(tab3, i)
