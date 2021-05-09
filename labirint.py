import matplotlib.pyplot as plt
import random
x = 50
y = 50
res = []


def genmass(x, y):
    res = []
    val = 0
    l_val = [0]
    val2 = 1
    for i in range(y):
        l = []
        for j in range(x):
            if i % 2 == 0:
                if j % 2 == 0:
                    l.append(val)
                else:
                    l.append(val2)
            else:
                if j % 2 != 0:
                    l.append(val)
                else:
                    l.append(val2)
        res.append(l)
    res[0] = x * l_val
    res[-1] = res[0]
    for i in range(len(res)):
        if res[i][0] == 1:
            res[i][0] = 0
        if res[i][-1] == 1:
            res[i][-1] = 0
    return res


fig, ax = plt.subplots()

ax.imshow(genmass(x,y))

fig.set_figwidth(10)
fig.set_figheight(10)

plt.show()