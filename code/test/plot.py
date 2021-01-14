import numpy as np
import math
import matplotlib.pyplot as plt
import deal


def cal(day, Xdata, Ydata, step=4, zoom=100):
    # 设置范围
    mon_input = int(day / 30)
    index_min = max(0, mon_input-step if mon_input<12 else int((mon_input-12)/3)+12-step)
    index_max = min(35, index_min+step*2)
    # 数值缩放
    Xday = day/zoom
    Ydata = Ydata/zoom

    # 提取数据列表
    Xdata = list(Xdata*30/zoom)
    res = deal.newton_inter(
            Xdata[index_min:index_max], 
            Ydata[index_min:index_max], 
            Xday)
    return res * zoom

if __name__ == "__main__":
    datasource = 'girl_height'
    step = 3

    X = {}
    Y = {}
    for SD in range(7):
        data = eval('deal.Meta.std_'+datasource)

        Xdata = np.array(list(data.keys()))
        Ydata = np.array(list(data.values()))
        Ydata = Ydata[:, SD]

        X[SD] = np.arange(0, 2400, 90)
        Y[SD] = []
        for i in X[SD]:
            Y[SD].append( cal(i, Xdata, Ydata, step=step, zoom=10) )
        # print(X[SD], cal(14, Xdata, Ydata, step=step, zoom=10) )
        plt.plot(X[SD], Y[SD], label="{}SD".format(SD-3))
        print( SD, cal(14, Xdata, Ydata) )

    plt.title(datasource+'_step={}'.format(step))
    plt.legend()
    plt.xlabel("x")
    plt.ylabel("y")
    plt.ylim(40, 140)
    plt.grid(True)
    plt.show()