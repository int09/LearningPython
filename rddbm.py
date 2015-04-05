import dbm
db = dbm.open('zoj_list', 'r')
print(db['1001'])
for index in range(1001, 2000):
    in_ch = str(index)
    print(db[in_ch])



