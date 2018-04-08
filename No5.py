'''
yukicorder
No.5 数字のブロック

Ellenは数字のブロックで遊ぼうとしている。
数字が書かれているブロックはそれぞれ高さ1で幅はWiである。
（同じ幅のブロックが複数存在することがある。）
それらのブロックを高さ1,幅Lの箱の中に入れる。
Ellenは大きな箱にどれだけブロックがたくさん入るか気になったが。
組み合わせがたくさんあって大変なことに気づいて、すぐに夜になってしまいそうである。
あなたは、代わりに大きな箱に最大何個のブロックが入るかを求めてください。
入力
 L
 N
 W1W2W3…WN
1行目は、大きな箱の幅を表すL(1≤L≤10000)
が与えられます。
2行目は、ブロックの数を表すN(1≤N≤10000)
3行目は、各ブロックの幅を表すWi(1≤Wi≤L)
が半角スペース区切りで与えられます。
出力
求めた数値を返してください。末尾に改行を付けてください。
'''

capa=int(input())
n=int(input())
l = list(map(int,input().split()))

l.sort()

itr=0
sum=0

while(itr<n):
    sum=sum+l[itr]
    if(capa<sum):
        break
    itr+=1

print(itr)
