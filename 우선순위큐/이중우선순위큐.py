import heapq

def solution(operations):

    def op_phaser(ops):
        #print("def op_phaser")
        for op in ops:
            li=op.split(" ")
            command=li[0]
            val=int(li[1])
            if command=="I":
                insert(val)
            elif command=="D":
                if val==-1:
                    min_pop()
                else:
                    max_pop()

    def insert(val):
        nonlocal insert_order
        #print(f"def insert {val}")
        #최대 힙
        max_dic[insert_order]=[-val,True,insert_order] # 값,활성상태,인덱스
        heapq.heappush(max_heap, max_dic[insert_order])
        #최소 힙
        min_dic[insert_order]=[val,True,insert_order]
        heapq.heappush(min_heap,min_dic[insert_order])
        insert_order+=1

    def max_pop():
        #print("def max_pop")
        while True:
            #뺄 거 있는지부터 확인
            if not max_heap:
                return
            popdata=heapq.heappop(max_heap)
            #print(f'popdata:{popdata}')
            val=-popdata[0] # 음수 붙음
            is_active=popdata[1]
            insert_od=popdata[2]

            if is_active:
                #활성상태 갱신
                #print(f'pop: {val}')
                min_dic[insert_od][1]=False
                max_dic[insert_od][1]=False
                return val
            else:
                # 활성상태가 아니라면
                #print("pop한것이 비활성상태여서 다시 pop 하겠습니다")
                continue

    def min_pop():
        #print("def min_pop")
        while True:
            #뺄 거 있는지부터 확인
            if not min_heap:
                return
            popdata=heapq.heappop(min_heap)
            #print(f'popdata:{popdata}')
            val=popdata[0]
            is_active=popdata[1]
            insert_od=popdata[2]

            if is_active:
                #활성상태 갱신
                #print(f'pop: {val}')
                min_dic[insert_od][1]=False
                max_dic[insert_od][1]=False
                return val
            else:
                # 활성상태가 아니라면
                #print("pop한것이 비활성상태여서 다시 pop 하겠습니다")
                continue

    max_heap=[]
    min_heap=[]
    max_dic=dict()
    min_dic=dict()
    insert_order=0 #삽입 순서, 사전 인덱스로 쓰임

    #연산처리
    op_phaser(operations)
    #힙에서 비활성 상태 전부 삭제

    #최대힙에서 뺄게 있는지?
    max_res = max_pop()
    #최소힙에서 뺄게 있는지?
    min_res = min_pop()
    #둘다있다면 최소,최대 반환
    if max_res is not None and min_res is not None:
        return [max_res,min_res]
    #하나만있다면 그 하나를 최소,최소/최대,최대 반환
    if max_res:
        return [max_res,max_res]
    if min_res:
        return [min_res,min_res]

    #아무것도 없다면
    return [0,0]

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))