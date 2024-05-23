List = [1,3,4,5,6,7,8]
search=1
search_continue=True
while search_continue:
    search_continue = False
    i=int((len(List))/2)
    print(f'length{i}')
    for item in List:
        if List[i]==search:
            Ans=i
        if List[i]>search:
            i=i-1
            Ans = i
        if List[i] < search:
            i = i + 1
            Ans = i
    print(i)
    print(List[i])


