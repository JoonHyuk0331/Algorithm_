#타임을 관리하지 않는 구조
def solution(prices):
    n = len(prices)
    ans = [0] * n
    st = []  # 인덱스만 담는 스택

    for i, price in enumerate(prices):
        # 가격이 떨어지는 순간, 스택에서 빼면서 시간 확정
        while st and prices[st[-1]] > price:
            top_idx = st.pop()
            ans[top_idx] = i - top_idx  # (현재 시간 - 들어온 시간)
        st.append(i)

    # 끝까지 안 떨어진 데이터 처리
    while st:
        top_idx = st.pop()
        ans[top_idx] = n - 1 - top_idx

    return ans