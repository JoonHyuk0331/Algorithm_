nums = [3, 5, 2, None, 1, 4]
#sorted(num)x
sorted([num for num in nums if num])

#sort 와 sorted의 차이
numbers = [3, 1, 4, 1, 5]
numbers.sort()  # 원본 리스트를 직접 수정 (반환값은 None임)
print(numbers)  # [1, 1, 3, 4, 5]

numbers = [3, 1, 4, 1, 5]
new_numbers = sorted(numbers)  # 새로운 리스트 반환
print(numbers)      # [3, 1, 4, 1, 5] (원본 그대로)
print(new_numbers)  # [1, 1, 3, 4, 5] (정렬된 새 리스트)