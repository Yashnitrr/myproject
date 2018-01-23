import threading
from collections import Counter
dic = {}
def read_file(filename):
    f2 = open (filename,"r")
    global dic
    final_str = f2.read()
    lst= final_str.split(" ")
    for i in lst:
        if dic.has_key(i):
            dic[i]+=1
        else:
            temp_dic = {i:1}
            dic.update(temp_dic)
    return

if __name__ == '__main__':
    t1 = threading.Thread(target=read_file("part1.txt"))
    t2 = threading.Thread(target=read_file("part2.txt"))
    t1.start()
    t2.start()
    print (Counter(dic))