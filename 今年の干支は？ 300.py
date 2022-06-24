# 与えられたリスト（li）を使って、ある年（year）の干支（えと）を表示するプログラムを作ってみよう！
# ヒント1：2022年の干支は「とら」だよ
# ヒント2：割り算のあまりを使ってみよう

year = 2022
li = ["ねずみ", "うし", "とら", "うさぎ", "たつ", "へび", "うま", "ひつじ", "さる", "とり", "いぬ", "いのしし"]

keisan = (year+9) %12
# print(keisan)

if keisan == 0:
  keisan=11
else:
  keisan-=1

# print(keisan)
print(li[keisan])

#参考：https://wakei2022.seesaa.net/article/201912article_3.html