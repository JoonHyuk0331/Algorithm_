"""
https://school.programmers.co.kr/learn/courses/30/lessons/60057?language=python3
"""

def solution():
    arr=input()
    length=len(arr)
    min_compressed_size=length
    for size in range(1,length):
        print(f'loop: size={size}')
        compressed_size=length
        dup_cnt=0
        i=0
        while i<length+1:
            print(f'{arr[i:i+size]} vs {arr[i+size:i+2*size]}')
            if not arr[i:i+size]:
                break
            if arr[i:i+size]==arr[i+size:i+2*size]:
                print("동일")
                dup_cnt+=1
                i=i+size
            else:
                print("다름")
                if dup_cnt:
                    print("누적된 dup_cnt 있음")
                    digits = len(str(dup_cnt+1))
                    print(f'digits:{digits}')
                    compressed_size=compressed_size+digits - size*dup_cnt
                    print(f'압축된 크기는 --> {compressed_size}')
                dup_cnt=0#중복 초기화
                i=i+size
        min_compressed_size=min(compressed_size,min_compressed_size)

    return min_compressed_size

print(solution())