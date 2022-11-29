import random
import os

playername = input("あなたの名前を入力: ")
print(f'\nようこそ {playername} さん！')

print('ゲームモードを選択\n')
print('1 乱数当てゲーム')
print('2 じゃんけん(未実装)')

mode = input('> ')

if(int(mode) == 1):
    print('1 が選択されたよ!!')
    num = random.randint(0,99)
    player_num = input('0~100までの整数でどの値が出ると思う？？: ')

    if(int(num) == int(player_num)):
        print('正解！！！')

    elif(int(player_num) != num):
        print('残念！')
        print(f'コンピュータが出した値: {num}')
        print(f'あなたが予想した値: {player_num}')

    else:
        print('何らかのエラー！')

    flag = input("\nEnterで終了")

elif(int(mode) == 2):
    exit(0)