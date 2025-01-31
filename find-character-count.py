def soln(word):
    cnt=0
    if 'C' in word:
        cnt+=1 
    return cnt

a=input()
print(soln(a))