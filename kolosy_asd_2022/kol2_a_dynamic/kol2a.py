from kol2atesty import runtests

def drivers( P, B ):
    control_list = [ (P[i][0],i) for i in range(len(P)) if not P[i][1]  ]
    control_list.sort(key=lambda x:x[0])
    place_list = [ (P[i][0],i) for i in range(len(P)) if P[i][1]  ]
    place_list.sort(key=lambda x:x[0])
    dp = [ [0,0] for _ in range(len(place_list)) ]
    ans1, ans2 = [],[]
    control_iterator = 0
    control_sum = [ 0 ] * len(place_list)
    for i in range(len(place_list)):
        while place_list[i][0] > control_list[control_iterator][0]:
            control_iterator+=1
            if control_iterator == len(control_list):
                break
        control_sum[i] = control_iterator
    print(control_sum)
    for i in range(len(place_list)):
        k = 1
        if i == 0:
            dp[i][0] = control_sum[i]
            continue
        while i - k and k < 4:
            if dp[i][1] < dp[i-k][0] + control_sum[i]-control_sum[i-k]:
                dp[i][1] = dp[i-k][0] + control_sum[i]-control_sum[i-k]
                ans1.append(place_list[i][1])
            if dp[i][0] > dp[i-k][1] + control_sum[i]-control_sum[i-k]:
                dp[i][0] = dp[i-k][1] + control_sum[i]-control_sum[i-k]
                ans2.append(place_list[i][1])
            k+=1
    print(dp)
    print(f"{ans1} {ans2}")
    ans = ans1 if dp[len(dp)-1][1] < len(control_list) - dp[len(dp)-1][0] else ans2
    return ans

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( drivers, all_tests = False )