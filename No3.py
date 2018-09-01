'''
yukicorder
No.3 ビットすごろく

Carol は特殊なすごろくをしようとしている。
1からNの番号がふられている一直線に並べられているN個のマスがある。
1から開始のマスとして、ゴールはNが書かれているマスとする。
その場に書かれている数字の2進数で表現した時の1のビット数 だけ「前」または「後」に進めることができる。
(1未満とN+1以上のマスには移動することは出来ない、正確にNにならないとゴールできない）
自然数Nを与えられた時、ゴールに到達できる最短の移動数（開始のマスへも移動にカウントする）を求めてください。
到達できない場合は-1を出力してください。
開始のマスがすでにゴールになっている場合もあリます。
入力
N

マスの数を表す整数N(1≤N≤10000)

が与えられます。
出力

最短の移動数、または　-1
'''
import queue
#移動するマス数を求める関数
def calcpop(num):
    return bin(num).count("1")

N=int(input())
q=queue.Queue()
q.put(1)

masu =[]
masu=[0]*10010
masu[1]=1

while q.empty()==False:

    curpos=q.get()
    popcnt=calcpop(curpos)
    if (curpos-popcnt>0 and masu[curpos-popcnt]==0):
        masu[curpos-popcnt]=masu[curpos]+1
        q.put(curpos-popcnt)
    if (curpos+popcnt<=N and masu[curpos+popcnt]==0):
        masu[curpos+popcnt]=masu[curpos]+1
        q.put(curpos+popcnt)

if masu[N]==0:
    print(-1)
else:
    print(masu[N])
