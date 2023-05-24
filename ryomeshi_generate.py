import configparser
import random

recipi = configparser.ConfigParser()

recipi.read("recipi.ini",encoding='utf-8')

i=0

#スープの語群定義
soup0 = ['大根','大根葉','葱','かぶ','高野豆腐','庄内麩','水菜','もやし','ほうれん草','豆腐','わかめ','玉ねぎ']
soup1 = ['味噌汁','スープ','中華スープ']

#朝飯を生成
print("朝飯")
print("ご飯、パン")
print()