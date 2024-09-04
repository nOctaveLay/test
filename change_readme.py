# import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument('-p', help ="change paper")

from datetime import datetime

now = datetime.now()

def change_table(lines:list,add_contents:str)->tuple:
    j = 0
    result_string = ''
    find_string = lines[j]
    while find_string != '\n':
        result_string += find_string
        j += 1                    
        find_string = lines[j]
    result_string += add_contents
    j += 1
    return j,result_string


def change_paper(change_contents:str, text_file_path = "./README.md"):
    """
    "README.md"의 paper 부분을 월에 맞춰서 바꿔줌.
    """
    new_contents = ''
    with open(text_file_path,'r',encoding = 'utf-8') as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            new_string = lines[i].strip()
            new_contents += new_string + "\n"
            if new_string == f"### {now.month}월 논문 발표":
                new_contents += '\n'
                j,result_string = change_table(lines[i+2:],change_contents)
                i = i+2+j
                new_contents += result_string + '\n'
            i += 1
    print(new_contents)
change_paper("./README.md")
# change_file("./README.md")
# if __name__ == "__main__":
#     args = parser.parse_args()
#     if args.p:
#         change_file("./README.md")

