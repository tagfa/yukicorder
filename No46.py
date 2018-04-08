'''
yukicorder
No.46 はじめのn歩
問題文
1歩でぴったりaセンチメートル歩ける。
bセンチメートルの区間を歩くのに最小で何歩歩く？
なお、区間はオーバーしても良い。
入力
a b
a b ともに正の整数。(1≤a,b≤109)
出力
歩数を答えよ。最後に改行を忘れずに。
'''
import math

a,b=map(int,input().split())
print(math.ceil(b/a))
