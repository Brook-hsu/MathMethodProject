import deal
import numpy as np

def write(msg):
    file = open('code\\debug.txt', 'a')
    file.write(msg+'\n')
    file.close()

def inter(day, gender, step=4):
    Meta = eval('deal.Meta.std_'+gender+'_height')
    zoom = 100
    mon_input = int(day / 30)
    index_min = max(0, mon_input-step if mon_input<12 else int((mon_input-12)/3)+12-step)
    index_max = min(35, index_min+step*2)
    Xday = day/zoom
    Xmon = np.array( list(Meta.keys()) )
    Yall = np.array( list(Meta.values()) )
    # 提取数据列表
    Y = Yall[:, 0]          
    X = list(Xmon*30/zoom)
    res = deal.newton_inter(
            X[index_min:index_max], 
            Y[index_min:index_max], 
            Xday)

    print('result{:.3f}'.format(res) )
    write('step='+str(step)+', day='+str(day)+', result='+str(res) )


if __name__ == "__main__":
    # for day_input in range(2330, 2350):
        # inter(day_input, 'boy', step=6)
    a = {}
    a['1'] = {}
    a['1']['2'] = 23
    a['1']['3'] = 2
    print(a)
        
# 格式数据字典
def modidata():
    file = open('data.txt', mode='w')
    a = deal.Meta.std_boy_height
    for each_key in a:
        file.write('{:2d}'.format(each_key) + ' : [ ' )
        flag = 0
        for each_num in a[each_key]:
            if flag :
                file.write(', ')
            else :  flag = 1
            file.write('{:.2f}'.format(each_num))
        file.write(' ],\n')
    file.close()

# 生成数据字典
def createdata():
    file = open('data.txt', mode='w')
    a = [0]
    while a[0]!=-1:
        a = list(map(float, input().split()))
        file.write('{:2d} : '.format(int(a[0]))+str(a[1:])+',\n')
    file.close()


# createdata()
# modidata()