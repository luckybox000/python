import os
from openpyxl import Workbook

# 1. 파일들을 저장할 폴더 생성
folder_name = "쿠팡_물류_보고서"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"'{folder_name}' 폴더를 생성했습니다.")

# 2. 100개의 엑셀 파일 생성 루프
for i in range(1, 101):
    # 새 워크북(엑셀 파일) 객체 생성
    wb = Workbook()
    ws = wb.active
    
    # (선택) 파일 내부에 간단한 내용 입력
    ws['A1'] = f"{i}번 보고서입니다."
    
    # 3. 파일 이름 설정 및 저장
    file_name = f"배송현황_리포트_{i:03d}.xlsx"  # 001, 002 형식으로 이름 지정
    file_path = os.path.join(folder_name, file_name)
    
    wb.save(file_path)

print(f"총 {i}개의 엑셀 파일 생성이 완료되었습니다!")
