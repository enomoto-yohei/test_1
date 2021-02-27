# -*- coding: utf-8 -*-

f = open('test.txt', 'w')
for i in range(300):
    f.write("HARdata"+str(i).zfill(5))
    f.write("\n")
f.close()
