import random
import os

playername = input("あなたの名前を入力: ")
print(f'\nようこそ {playername} さん！')

print('ゲームモードを選択\n')
print('1 乱数当てゲームLv.100')
print('2 乱数当てゲームLv.10')
print('3 乱数当てゲームLv.5')
print('4 じゃんけん(未実装)')

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
    print('2 が選択されたよ!!')
    num = random.randint(0,9)
    player_num = input('0~10までの整数でどの値が出ると思う？？: ')

    if(int(num) == int(player_num)):
        print('正解！！！')

    elif(int(player_num) != num):
        print('残念！')
        print(f'コンピュータが出した値: {num}')
        print(f'あなたが予想した値: {player_num}')

    else:
        print('何らかのエラー！')

    flag = input("\nEnterで終了")

elif(int(mode) == 3):
    print('3 が選択されたよ!!')
    num = random.randint(0,4)
    player_num = input('0~5までの整数でどの値が出ると思う？？: ')

    if(int(num) == int(player_num)):
        print('正解！！！')

    elif(int(player_num) != num):
        print('残念！')
        print(f'コンピュータが出した値: {num}')
        print(f'あなたが予想した値: {player_num}')

    else:
        print('何らかのエラー！')

    flag = input("\nEnterで終了")