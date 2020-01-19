s = str(input())
p = ""
cnt = 1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        cnt+=1
        if(i==len(s)-2):
            p+="({}, {}) ".format(cnt, s[i])
    else:
        p+="({}, {}) ".format(cnt, s[i])
        cnt=1
print(p)

# import itertools

# S = raw_input()

# for k, g in itertools.groupby(S):
#     print (len(list(g)), int(k)),