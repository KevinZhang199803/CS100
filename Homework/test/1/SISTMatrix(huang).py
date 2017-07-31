# _*_ coding:utf-8 _*_

def isStandard(A):
    return A[-1]

def Str2Mat(s):
    if s[0].isalnum():
        #获取m-by-n的矩阵大小
        x = s.index('-')
        m = eval(s[0:x])
        s = s[x+1:]
        x = s.index('{')
        n = eval(s[0:x])
        s = s[x:]
        #构建稀疏结构
        Mat = []
        Mat.append([m,n])
        for x in range(m):
            Mat.append([0]*n)
        Mat.append(False)
        #完善信息
        dict = eval(s)
        count = 0
        for x in dict:
            i = x[0]
            j = x[1]-1
            num = x[2]
            Mat[i][j] = num
            count+=1
        Mat[0].append(count)
        return Mat
    else:
        Mat = []
        m = 1
        while True:
            x = s.find(';')
            if(x<0): break
            line = eval('['+s[1:x]+']')
            Mat.append(line)
            s = '['+s[x+1:]
            m+=1
        Mat.append(eval(s))
        Mat.append(True)
        n = len(Mat[0])
        Mat = [[m,n]] + Mat
        return Mat


            
        
