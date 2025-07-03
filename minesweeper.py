import random
import copy
i = 0
j = 0
minezone = []
mineshow = []
minenum = []
dummy = []
n = 0
size = 0
minecount = 0
note = 0
trycount = 0
maxtry = 0
conreturn = 0
while n != 1:
    size = (input("大きさ(3～10):"))
    try:
        size = int(size)
        if size < 3 or 10 < size:
            print("RangeError:「",size,"」は範囲外の数字です\n3～10の数字である必要があります")
            continue
        else:
            print(size,"×",size,"の地雷原を作成します")
    except ValueError:
        print("ValueError:「",size,"」は数字ではありません\n値は数字である必要があります")
        continue
    n = 1
for i in range(size):
    for j in range(size):
        n = 0
        n = random.randint(0,2)
        if n == 1:
            dummy.append(1)
            minecount += 1
        else:
            dummy.append(0)
    minezone.append(dummy)
    dummy = []


dummy = minezone
dummy =[]

def empty_array(array,dummy,size):
    dummy = []
    for i in range(size):
        for j in range(size):
            dummy.append("?")
        array.append(dummy)
        dummy = []
    return array
empty_array(mineshow,dummy=dummy,size=size)

minenum = copy.deepcopy(mineshow)


for i in range(size):
    for j in range(size):
        if minezone[i][j] == 1:
            minenum[i][j] = "B"
        elif i-1 < 0 and j-1 < 0:
            minenum[i][j] = minezone[i][j+1] + minezone[i+1][j] + minezone[i+1][j+1]
        elif i-1 < 0 and not j+1 >= size:
            minenum[i][j] = minezone[i][j-1] + minezone[i][j+1] + minezone[i+1][j-1] + minezone[i+1][j] + minezone[i+1][j+1]
        elif j-1 < 0 and not i+1 >= size:
            minenum[i][j] = minezone[i-1][j] + minezone[i-1][j+1] + minezone[i][j+1] + minezone[i+1][j] + minezone[i+1][j+1]
        elif j+1 >= size and i+1 >= size:
            minenum[i][j] = minezone[i-1][j] + minezone[i][j-1] + minezone[i-1][j-1]
        elif i+1 >= size and j-1 < 0:
            minenum[i][j] = minezone[i-1][j] + minezone[i-1][j+1] + minezone[i][j+1]
        elif j+1 >= size and i-1 < 0:
            minenum[i][j] = minezone[i][j-1] +minezone[i+1][j-1] + minezone[i+1][j]
        elif i+1 >= size:
            minenum[i][j] = minezone[i-1][j] + minezone[i-1][j+1] + minezone[i][j-1] + minezone[i][j+1] + minezone[i-1][j-1]
        elif j+1 >= size:
            minenum[i][j] = minezone[i-1][j] + minezone[i][j-1] +minezone[i+1][j-1] + minezone[i+1][j] + minezone[i-1][j-1]
        else:
            minenum[i][j] = minezone[i-1][j-1] + minezone[i-1][j] + minezone[i-1][j+1] + minezone[i][j-1] + minezone[i][j+1] + minezone[i+1][j-1] + minezone[i+1][j] + minezone[i+1][j+1]

#for i in range(size):
#    print(minezone[i])
#for i in range(size):
#    print(minenum[i])




def _check(datai,dataj):
    global mineshow , minenum , trycount , conreturn
    if mineshow[datai][dataj] != minenum[datai][dataj]:
        mineshow[datai][dataj] = minenum[datai][dataj]
        trycount += 1
        if mineshow[datai][dataj] == 0:
            conreturn += 1
   


print("ここには",minecount,"個の地雷が埋まっている。")
maxtry = size*size-minecount

while trycount < maxtry:

    print("地雷の数:",minecount)
    for n in range(size):
        print(mineshow[n])

    n = 0
    while n != 1:
        i = (input("上から何番目?:"))
        try:
            i = int(i)
            if 0 > i or i > size:
                print("RangeError:「",i,"」は範囲外の数字です\n","1～",size,"の数字である必要があります")
                continue
            else:
                i -= 1
                n = 1
        except ValueError:
            print("ValueError:「",i,"」は数字ではありません\n値は数字である必要があります")
            continue
    n = 0
    while n != 1:
        j = (input("左から何番目?:"))
        try:
            j = int(j)
            if 0 > j or j > size:
                print("RangeError:「",j,"」は範囲外の数字です\n","1～",size,"の数字である必要があります")
                continue
            else:
                j -= 1
                n = 1
        except ValueError:
            print("ValueError:「",j,"」は数字ではありません\n値は数字である必要があります")
            continue
    if mineshow[i][j] == minenum[i][j]:
        print("そこはすでに選んでいるぞ")
        continue
    else:
        mineshow[i][j] = minenum[i][j]
    
    if mineshow[i][j] == "B":
        print("上から",i+1,"番目、左から",j+1,"番目に爆弾あった...\nゲームオーバーだ")
        break
    elif mineshow[i][j] == 0:
        print("上から",i+1,"番目、左から",j+1,"番目は安全だ\n周りの安全地帯も開いておくぞ")
        conreturn += 1
        while conreturn >= 1:
            for i in range(size):
                for j in range(size):
                    if mineshow[i][j] == 0:
                        if size-1 > i > 0 and size-1 > j > 0:#真ん中(壁に接していない)
                            _check(i-1,j-1)
                            _check(i-1,j)
                            _check(i-1,j+1)
                            _check(i,j-1)
                            _check(i,j+1)
                            _check(i+1,j-1)
                            _check(i+1,j)
                            _check(i+1,j+1)
                        elif i == 0 and j == 0:#左上角
                            _check(i+1,j+1)
                            _check(i+1,j)
                            _check(i,j+1)
                        elif i == 0 and j+1 == size:#右上角
                            _check(i,j-1)
                            _check(i,j-1)
                            _check(i+1,j)
                        elif i+1 == size and j == 0:#左下角
                            _check(i-1,j)
                            _check(i-1,j+1)
                            _check(i,j+1)
                        elif i+1 == size and j+1 == size:#右下角
                            _check(i-1,j-1)
                            _check(i-1,j)
                            _check(i,j-1)
                        elif i == 0: #上の壁に接している
                            for z in range(size):
                                if mineshow[i][z] == 0:
                                    _check(i,z-1)
                                    _check(i+1,z-1)
                                    _check(i+1,z)
                                    if z+1 != size:
                                        _check(i,z+1)
                                        _check(i+1,z+1)
                        elif i+1 == size: #下の壁に接している
                            for z in range(size):
                                if mineshow[i][z] == 0:
                                    _check(i,z-1)
                                    _check(i-1,z-1)
                                    _check(i-1,z)
                                    if z+1 != size:
                                        _check(i,z+1)
                                        _check(i-1,z+1)
                        elif j == 0: #左の壁に接している
                            for z in range(size):
                                if mineshow[z][j] == 0:
                                    _check(z-1,j)
                                    _check(z-1,j+1)
                                    _check(z,j+1)
                                    if z+1 != size:
                                        _check(z+1,j)
                                        _check(z+1,j+1)
                        elif j+1 == size: #右の壁に接している
                            for z in range(size):
                                if mineshow[z][j] == 0:
                                    _check(z-1,j)
                                    _check(z-1,j-1)
                                    _check(z,j-1)
                                    if z+1 != size:
                                        _check(z+1,j)
                                        _check(z+1,j-1)
            conreturn -= 1
    else:
        print("上から",i+1,"番目、左から",j+1,"番目は安全だが...\n周りに",mineshow[i][j],"個の爆弾があるぞ")
    trycount += 1
        
for n in range(size):
    print(minenum[n])
if mineshow[i][j] == "B":
    None
else:
    print(minecount,"個すべての地雷を確認した\nゲームクリア")