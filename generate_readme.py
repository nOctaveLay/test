from datetime import datetime, timedelta
def generate_paper(change_contents:str, text_file_path = "./README.md"):
    """
    "README.md"의 paper를 월에 맞춰서 생성
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

def generate_retrospects(text_file_path = "./README.md"):
    """
    "README.md"의 retrospect의 날짜 
    '### 24.09.02 MON - 24.09.06 FRI'를 만듬
    
    """
    new_contents = ''
    now = datetime.now()
    end = now + timedelta(days = 5)

    with open(text_file_path,'r',encoding = 'utf-8') as f:
        lines = f.readlines()
        i = 0
        while i < len(lines):
            new_string = lines[i].strip()
            # 주간 정리 위에 올릴 예정
            if new_string == f"## 📝주간 정리 (optional)":
                string = f"### {now.strftime('%y.%m.%d')} {now.strftime('%a').upper()} - {end.strftime('%y.%m.%d')} {end.strftime('%a').upper()}\n\n"
                new_contents += string
                new_contents += '- **📍Hello**\n- **📍IsSomeone**\n- **📍HowAreYou**\n- **📍AndSomeone**\n- **📍Isasking**\n- **📍Someone**\n\n'
                new_contents += "".join(lines[i:])
                print(new_contents)
                break
            else:
                new_contents += new_string + "\n"
            i += 1
            
    print(new_contents)

generate_retrospects()
