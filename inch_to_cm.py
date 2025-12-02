#숫자를 입력받습니다.

row_intput = input("inch 단위의 숫자를 입력하세요 :")

# 입력받은 데이터를 숫자 자료형으로 변경하고, cm 단위로 변경합니다.
inch = int(row_intput)
cm = inch * 2.54

#출력합니다.
print(inch, "inch는", cm, "cm입니다.")
