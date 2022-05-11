
a = input('input string:')
num=len(a)+1

if 1 <=len(a) and len(a)<= 50: ##  判斷字串長度
    s=list(a)
    for i in range(len(a)):  ################### 
        if s[i] == s[i].upper():
            if s[i] == a[i]:
                s[i] = s[i].lower()
                
        elif s[i] == s[i].lower():   ##轉換字串大小
            if s[i] == a[i]:
                s[i] = s[i].upper()
        else:
            s[i] = s[i]    ####################
    print("".join(s[-1:-num:-1]))
    
else:
  print('false')


