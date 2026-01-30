n=int(input())
array=[]
for i in range(n):
    input_data=input().split()
    array.append((input_data[0],input_data[1]))

array=sorted(array,key=lambda student: student[1]) 
#key 옵션에 함수를 지정하면 각 원소에 이 함수를 호출한 결과를 기준으로 대소비교

# 람다 함수 대신 일반 함수 사용 시
# def get_second_element(student):
#     return student[1]
# array = sorted(array, key=get_second_element)
    
for student in array:
    print(student[0],end='')