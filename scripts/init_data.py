# coding: UTF-8
with open('./data/initnames.txt','r',encoding="utf-8") as f1,open("./data/data.txt",'w') as f2:
    line = f1.readline()
    index = 0
    while line:
        f2.write(line.strip() + "\t0\t0.5\n")
        line = f1.readline()
