from generate_readme import return_index_next_matching


# paper에 PR이 발생하면
# PR한 사람의 이름 / paper를 찾아서 매핑해준다.

def return_new_contents(pr_name:str, contents:str, file_name:str, matching:str):


    # README.md를 읽는다.
    new_contents = ''
    with open(file_name, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line_number, line_content in enumerate(lines):
            new_contents += line_content
            line_content = line_content.strip() # 줄 개행 문자 제거

            # 만약, update를 원하는 곳을 찾았다면

            if line_content == matching:
                match_line_number = return_index_next_matching(pr_name, lines[line_number+1:])
                
                # 만약 contents가 겹친다면
                if match_line_number == -1:
                    # 뒤의 모든 내용을 새롭게 저장하고 break
                    new_contents = "".join(lines[line_number+1:])
                    return new_contents
                
                # contents가 겹치지 않는다면
                else:
                    new_contents += "".join(lines[line_number+1:line_number+1+match_line_number])
                    # 그 matching된 곳에 써주고, 개행 문자를 남겨
                    new_contents += contents
                    new_contents += "".join(lines[line_number+1+match_line_number:])
                    return new_contents
                
        return  new_contents