from collections import Counter

#리스트의 요소 개수 세기

fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
count = Counter(fruits)
print(count)  # Counter({'apple': 3, 'banana': 2, 'orange': 1})

#문자열의 문자 개수 세기

text = "hello world"
count = Counter(text)
print(count)  # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# 상위 2개
print(count.most_common(2))  # [('a', 3), ('b', 2)]

# 전체 (빈도순 정렬)
print(count.most_common())  # [('a', 3), ('b', 2), ('c', 1)]
