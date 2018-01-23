import threading
from collections import Counter
space_count = 0     # To keep track of count of spaces in all the files
str = ""
dict = {}       # Empty dictionary to store all key value pairs


def read_file(filename):
    f2= open (filename, "r") #opening the file with read access
    final_str = f2.read()    # storing the content of file in final_str variable
    global str
    global dict
    for i in range(0, len(final_str)):   #Iterating through each character of a file
        if final_str[i] == " ":
            global space_count
            space_count+=1              # Keep track of the contents of spaces in all the files
            if str == "":
                continue
            elif dict.has_key(str):     # To check if that key already exist in our dictionary
                dict[str] += 1          # If yes, we are incrementing the value by 1
                str = ""
            else:
                dic1 = {str: 1}         # else we are adding the new key with count 1
                dict.update(dic1)
                str = ""

        else:
            str += final_str[i]
    if str != "":                       # Used this condition to access the last string of a file
        if dict.has_key(str):
            dict[str] += 1
            str = ""
        else:
            dic1 = {str: 1}
            dict.update(dic1)
            str = ""


t1 = threading.Thread(target= read_file("part1.txt"))       # created the thread and calling read_file function declared above
t2 = threading.Thread(target= read_file("part2.txt"))
t1.start()                                                  # Starting thread
t2.start()

temp_dic = {" ":space_count}                                # Adding the count of total spaces of all the files in a dictionary
dict.update(temp_dic)
print Counter(dict)                                         # Printing the key value pair from a dictionary.
