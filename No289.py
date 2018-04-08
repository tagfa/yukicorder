'''
問題文
文字列S
が与えられるので, その中のそれぞれの数字を1桁の数値とみなして, 全ての合計値を求めてください.
例えば1test23という文字列の数字の合計値は1+2+3=6
となる.
2016/05/31 追記
注意: 数字がない場合は0
を出力してください。
入力
S
1≤|S|≤10000
|S| は文字列Sの長さである.
文字列S
は半角英数字のみで構成される.
出力
各数字の合計値を出力してください
'''

l=list(input())
sum=0

for item in l:
    if item.isdigit()==True:
        sum+=int(item)

print(sum)