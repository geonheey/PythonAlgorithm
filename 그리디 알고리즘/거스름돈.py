n = 1260 #거슬러 줘야할 돈
count = 0 # 동전의 개수

coin_types = [500,100,50,10]

for coin in coin_types :
    count += n // coin
    n %= coin

print(count)