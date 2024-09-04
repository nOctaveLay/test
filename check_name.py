import os
print(os.listdir("./paper/"))
print(os.path.isfile("./datas/last_name"))
if not os.path.isfile("./datas/last_name"):
    new_file_list = list()
    for x in os.listdir("./paper/"):
        x1,extention = x.split(".")
        x2 = x1.split("_")
        if not x2[-1].isdigit():
            x2.append(0)
        new_file_list.append(x2 + [extention])
    file_list = new_file_list
    # file_list = [x.split('_') for x in os.listdir("./paper/")]
    print(file_list)
    file_list = sorted(file_list, key= lambda x: (int(x[0]),len(x),int(x[-2])), reverse=True)
    print(file_list)

