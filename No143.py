
'''
問題文

yukiさんは一袋 K
粒だけ豆が入った袋を N 袋拾いました．
ところで，節分には年齢の数だけの豆を食べる習慣があります．
yukiさんの家族は F 人家族で，それぞれの年齢は A1,A2,…,AF 歳です．
それぞれが年齢の数だけの豆を食べたら最終的に何粒残るかを求める下さい．
ただし，全員が年齢の数だけ豆を食べることができないなら -1 を出力して下さい．

入力
K
 N
 F
A1 A2⋯AF
1≤K≤1000
1≤N≤1000
1≤F≤100
1≤Ak≤100
出力
残る豆の粒の数を出力するか，-1を出力して下さい．
'''

k,n,f=map(int,input().split())
l=list(map(int,input().split()))

sum_y=sum(l)
sum_b=int(k)*int(n)
if sum_b<sum_y:
    print(-1)
else:
    print(sum_b-sum_y)
