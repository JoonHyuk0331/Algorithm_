def solution(prices):
    st = []
    ans = [0] * len(prices)
    for i, price in enumerate(prices):
        # 액션
        for idx, s in enumerate(st):
            st[idx][2] += 1
        # 팝
        while st and st[-1][1] > price:
            idx, val, time = st.pop()
            ans[idx] = time
        # 인서트
        st.append([i, price, 0])

    for data in st:
        idx, val, time = data
        ans[idx] = time

    return ans