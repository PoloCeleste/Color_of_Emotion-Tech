'''
Gitlab Auto Clone Ver 1.0

깃랩 자동 클론 프로그램
사용자 정보와 과목 정보를 받아서 파일로 저장(프로그램과 같은 위치에 저장)
깃랩 레포 과목과 차수 정보를 받아서 자동으로 클론하도록 구현
깃허브에 올리고 싶은 경우 .git 폴더를 지울 수 있도록 구현
사용자가 본인의 OS를 입력하면 그에 맞게 실행 코드를 선택하도록 구현



Gitlab Auto Clone Ver 1.1

.exe파일은 Windows에서만 사용가능하므로
exe파일은 Windows용으로, py파일은 맥용으로 고정



Gitlab Auto Clone Ver 1.2

OS 정보 가져와서 자동으로 설정하도록 수정
클론기능 Linux에서 사용 가능하도록 수정
OS에 맞게 쉘 명령어 동작 수정



Gitlab Auto Clone Ver 2.0

requests 모듈 설치 필요
클론 후 .gitignore 파일 생성 기능 추가
추가할 이그노어 속성 변경 가능(기본값 제외)



Gitlab Auto Clone Ver 2.1

상대경로 -> 절대경로 변경 (feat. 지연쓰 ~Error, Mistake(닉네임 오타))
예외처리 추가 -> 오류 내역 상세 출력



Gitlab Auto Clone Ver 2.2

ROOT 폴더명 추가 및 차수 폴더 과목명 ALL 대문자로 변경
차수 다중입력 기능 추가
종료 시 원한다면 계속 Clone에 머무를 수 있도록 변경

    Gitlab Auto Clone Ver 2.2.1
    vue 실습실 레포규칙 달라서 그에 맞게 대응 코드 추가
'''

from os import path, getcwd
from time import sleep
from platform import system
from getpass import getpass
from subprocess import run
from requests import get
from sys import exc_info

SEPERATOR=['hw','ws']
STAGE=[['2','4'], ['1','2','3','4','5','a','b','c'], ['1','2','3']]

os_nlst={'Windows':1, 'Darwin':2, 'Linux':3, 'Ubuntu':4, '':5}  # 운영체제 정보 가져오기
sc={'!':'%21','#':'%23','$':'%24','&':'%26',"'":'%27','(':'%28',')':'%29','*':'%2A','+':'%2B',  # 리눅스 사용자 클론 시 비밀번호에 특수문자가 존재할 경우
    ',':'%2C','/':'%2F',':':'%3A',';':'%3B','=':'%3D','?':'%3F','@':'%40','[':'%5B',']':'%5D'}  # 에러 방지 위해 URL인코딩 사용
glst=['windows','macos','visualstudiocode','pycharm','python','django','flask','vuejs','database']  # gitignore 생성 기본값
lst=['linux','eclipse','intellij','java','c','c++','go','dart','flutter']  # gitignore 추가 생성값
gitignore=''  # 생성될 gitignore 문자열
clear=''

def set_ignore(p=0):  # gitignore 문자열 받아오기
    global gitignore
    alst=[]
    
    if p==0:
        print()
        for i in range(len(lst)):
            print(i+1, lst[i], end='\t')
            if (i+1)%4==0:print()
        print()
        d=input("\n추가할 속성의 번호를 선택해 주세요.(구분자 공백 사용) : ").split()
        for di in d:alst.append(lst[int(di)-1])
    gurl='https://www.toptal.com/developers/gitignore/api'
    print('\ngitignore 생성중입니다......\n')
    gitignore=get(f'{gurl}/{",".join(glst+alst)}').text


def ignore(folder):
    try:
        with open(f'{folder}/.gitignore', 'w', encoding="UTF-8") as f:
            f.write(gitignore)
            print(f"{folder}에 gitignore 파일 생성")
        f.close()
    except Exception as e:
        exc_type, exc_obj, exc_tb = exc_info()
        fname = path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)


def file(i=0):  # 설정 파일 읽기/쓰기/변경; 기본값 설정 생성or읽기
    try:
        if i==1:
            with open('clone.ini', 'w', encoding="UTF-8") as f:
                user=input("\n깃랩 사용자 이름을 입력해주세요. : ")
                sub=input("과목명을 입력해주세요. (ex> django, js...) : ")
                f.write(user+'\n')
                f.write(sub+'\n')
            f.close()
            print("\n변경 완료.\n")
        else:
            try:
                with open('clone.ini', 'r', encoding="UTF-8") as f:
                    user=f.readline()
                    sub=f.readline()
            except:
                with open('clone.ini', 'w', encoding="UTF-8") as f:
                    user=input("\n깃랩 사용자 이름을 입력해주세요. : ")
                    sub=input("과목명을 입력해주세요. (ex> django, js...) : ")
                    f.write(user+'\n')
                    f.write(sub+'\n')
            f.close()
        return user.strip(), sub.strip()
    except Exception as e:
        exc_type, exc_obj, exc_tb = exc_info()
        fname = path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)


def clone(USER_NAME, SUBJECT, OS_N):  # 깃랩 레포 클론하기
    run(clear, shell=True)
    print(f"\n{USER_NAME}의 {SUBJECT} 레포 관리\n")
    base_URL='https://lab.ssafy.com' if OS_N<=2 else f'https://{USER_NAME}:{"".join(sc[a] if a in sc else a for a in getpass("깃랩 비밀번호를 입력해주세요. (화면에 노출 X): "))}@lab.ssafy.com'
    DAYs=input("프로젝트 차수 입력 ( ex> 2 (단일), 1-3 (다중) ): ")
    
    if '-' in DAYs: DAY1, DAY2 = DAYs.split('-')
    else : DAY1 = DAY2 = DAYs
    
    if DAY2=='':DAY2=DAY1
    
    print("\n.gitignore 기본 세팅\n")
    print(*glst)
    x=input("\n.gitignore에 추가할거 있나요? (일회성, 넘기려면 enter) (Y/y)")
    if x=='Y' or x=='y' or x=='ㅇ' or x=='o' or x=='ㅇㅇ':set_ignore()
    else:set_ignore(1)
    run(clear, shell=True)
    
    for DAY in range(int(DAY1), int(DAY2)+1):
        DAY=str(DAY)
        for sep in range(len(SEPERATOR)):
            for st in STAGE[sep]:
                PROJECT=f'{SUBJECT}_{SEPERATOR[sep]}_{DAY}_{st}'
                r_folder=SUBJECT.upper()
                p_folder=f'{SUBJECT.upper()}_{DAY.zfill(2)}'
                print(f'\n{PROJECT} 클론 시도중...')
                URL=f'{base_URL}/{USER_NAME}/{PROJECT}'
                folder_path=path.join(getcwd(), r_folder, p_folder, PROJECT) # 절대 경로로 변경
                #folder_path=f'./{SUBJECT.upper() if SUBJECT == "js" else SUBJECT.capitalize()}_{DAY.zfill(2)}/{PROJECT}'
                cmd=f'git clone {URL}.git {folder_path}'
                output=run(cmd, shell=True, capture_output=True, text=True)
                
                if output.returncode==0:
                    print(f'{folder_path}에 {PROJECT} 클론 성공.')
                    if not path.exists(f'{folder_path}/.gitignore'):ignore(folder_path)
                elif output.returncode==128:
                    if 'denied' in output.stderr: print("권한 거부 당함.... 비번 틀렸을수도...?")
                    else: 
                        print(f'에러 : {output}\n{folder_path}에 {PROJECT} 폴더가 이미 존재합니다...\n아니면 깃 자격증명이 적용 안되었을지도...?')
                        if not path.exists(f'{folder_path}/.gitignore'):ignore(folder_path)
                else:print('무슨 문제일까요...? 알려주세요...\n', output, '\n')
        print(f'\n{DAY} 차수 클론 완료.')
        sleep(2)
        run(clear, shell=True)


def del_dot_git(USER, SUBJECT, OS_N):
    x=input("\n실습 진짜로 다함? (Y/y)")
    if x=='Y' or x=='y' or x=='ㅇ' or x=='o' or x=='ㅇㅇ':
        run(clear, shell=True)
        del_co= 'rmdir /s /q' if OS_N==1 else 'rm -rf'
        
        try:
            print(f"\n{USER}의 {SUBJECT} 레포 관리\n")
            DAYs=input(f"\n{SUBJECT} 프로젝트 차수 입력 ( ex> 2 (단일), 1-3 (다중) ): ")

            if '-' in DAYs: DAY1, DAY2 = DAYs.split('-')
            else : DAY1 = DAY2 = DAYs
            
            if DAY2=='':DAY2=DAY1
            
            for DAY in range(int(DAY1), int(DAY2)+1):
                DAY=str(DAY)
                for sep in range(len(SEPERATOR)):
                    for st in STAGE[sep]:
                        PROJECT=f'{SUBJECT}_{SEPERATOR[sep]}_{DAY}_{st}'
                        r_folder=SUBJECT.upper()
                        p_folder=f'{SUBJECT.upper()}_{DAY.zfill(2)}'
                        g='.git'
                        folder_path = f'"{path.join(getcwd(), r_folder, p_folder, PROJECT, g)}"'
                        print(f'\n{folder_path} 삭제 시도중...')
                        cmd=f'{del_co} {folder_path}'
                        output=run(cmd, shell=True, capture_output=True, text=True)
                        
                        if OS_N==1:
                            if output.returncode==0:print(f'{folder_path} 폴더가 삭제되었습니다.')
                            elif output.returncode==2:print(f'Error: {folder_path} 폴더를 찾지 못했습니다. 이미 삭제되었을 수도?')
                        else:print(f'{folder_path} 폴더가 삭제되었습니다.')
                        
                print(f'\n{DAY} 차수 클론 완료.')
                sleep(2)
                run(clear, shell=True)
        except:
            print("에러 발생...경로 없어용.....")
    else: print('\n다하고 오세요~')


def exit():
    print("\n클론 프로그램을 종료합니다.\n")
    sleep(2)


def main():
    print("\n주의 >> 실행파일과 동일 경로상에서 동작됩니다.")
    print("주의 >> 리눅스 사용자는 클론 시 살짝 위험할수도...?")
    print("주의 >> 실습실 생성은 다 하셨죠...?\n")
    global clear
    os_n=os_nlst[system()]  # 운영체제 정보 가져오기
    if os_n==5:print('운영체제 뭐쓰세요...? 정보가 없는데요....')
    clear = 'cls' if os_n==1 else 'clear'  # Windows에선 cls Mac/Linux에서는 clear
    sleep(2)
    u,su=file()  # 사용자 정보 등록/가져오기
    
    if su in ['vue', 'VUE', 'Vue']:
        SEPERATOR.append('ex')
        for _ in range(3):STAGE[1].pop()
    
    while 1:
        try:
            run(clear, shell=True)
            print(f"\n{u}의 {su} 레포 관리\n")
            s=int(input("1. GITLAB clone  2. Del .git  3. Modify Settings (exit : 0): "))
        except:
            print("\n정수만 입력해주세요.")
            sleep(2)
            continue
        if s==0:
            exit()  # 종료
            run(clear, shell=True)
            break
        if s==1:
            print()
            try: clone(u, su, os_n)  # 깃랩 클론 따오기
            except Exception as e:
                exc_type, exc_obj, exc_tb = exc_info()
                fname = path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
            if input("\n종료하려면 엔터를 눌러주세요. (clone 관리로 돌아가기 : 1) "):
                continue
            exit()
            run(clear, shell=True)
            break
        elif s==2:
            print()
            try: del_dot_git(u, su, os_n)  # git 설정 폴더 삭제
            except Exception as e:
                exc_type, exc_obj, exc_tb = exc_info()
                fname = path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
            if input("\n종료하려면 엔터를 눌러주세요. (clone 관리로 돌아가기 : 1) "):
                continue
            exit()
            run(clear, shell=True)
            break
        elif s==3:
            try: u,su=file(1)  # 사용자 정보 수정
            except Exception as e:
                exc_type, exc_obj, exc_tb = exc_info()
                fname = path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
            sleep(2)
            run(clear, shell=True)
        else:
            print("\n1, 2, 3 중 하나만 입력해주세요.\n")
            sleep(2)
            continue
