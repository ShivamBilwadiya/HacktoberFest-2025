def swap_first_two_digits(N):
    #return N after swapping first two digits
    num=N
    ans = 0
    count=0
    while num>0:
        count+=1
        num//=10
    first = N//(10**(count-1))
    second = N//(10**(count-2))
    second%=10
    rest=N%(10**(count-2))
    ans = second*(10**(count-1))+first*(10**(count-2))+rest
    return int(ans)



# The following code has already been implemented by the checker, so there is no need to rewrite it.
# N = int(input())
# print(swap_first_two_digits(N))
