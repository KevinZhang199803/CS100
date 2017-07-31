def Str2Mat(s):
    if '{' in s:
        # 稀疏矩阵转换
        hanglie = s.split('-')
        hang = int(hanglie[0])
        # 行数
        hanglie2 = hanglie[1].split('{')
        lie = int(hanglie2[0])
        # 列数
        hanglie2[1] = hanglie2[1].rstrip('}')
        position = hanglie2[1].split('),(')
        position[0] = position[0].strip('(')
        position[-1] = position[-1].strip(')')
        for i in range(len(position)):
            position[i] = '[' + position[i] +']'
            position[i] = eval(position[i])
        # hang为行数，lie为列数，position为各个非零位置的坐标和值
        sparse = [hang,lie]
        for i in range(len(position)):
            sparse.append(position[i])
        return sparse
    # A.C.
    
    else:
        # 标准矩阵转换
        matrix = s
        matrix = matrix.replace('[','')
        matrix = matrix.replace(']','')
        matrixStd = matrix.split(';')
        for j in range(len(matrixStd)):
            matrixStd[j] = '[' + matrixStd[j] + ']'
            matrixStd[j] = eval(matrixStd[j])
        # matrixStd中每一个元素代表一行
        return matrixStd
    # A.C.

def IsStandard(A):
    FatherChen = str(A[0])
    if '[' in FatherChen:
        return 'True'
    else:
        return 'False'

def Mat2StrStandard(A):
    FatherChen = str(A[0])
    if '[' in FatherChen:
        std = '['
        for i in range(len(A)):
            j = str(A[i])
            j = j.strip('[')
            j = j.strip(']')
            std = std + j + ';'
        std = std.rstrip(';')
        std = std + ']'
        return std
    # StdMatrix
    # A.C.
    
    else:
    # 稀疏矩阵，A[0]为行，A[1]为列
        t = [0]
        for m in range(A[1]-1):
            t.append(0)
        spa = [t]
        for m in range(A[0]-1):
            spa.append(t)
        # 所有元素赋值为0
        for m in range(len(spa)):
            spa[m] = eval(str(spa[m]))
        for m in range(2,len(A)):
            a = A[m]
            b = spa[a[0]-1]
            b[a[1]-1] = a[2]
            t = a[0]-1
            spa[t] = b
        # 填充有非零值的数
        std2 = '['
        for m in range(len(spa)):
            n = str(spa[m])
            n = n.strip('[')
            n = n.strip(']')
            std2 = std2 + n + ';'
        std2 = std2.rstrip(';')
        std2 = std2 + ']'
        return std2
    # 记住，在Python中，‘=’相当于指针，不是值！！！！！！！！！！
    # A.C.

def Mat2StrSparse(A):
    FatherChen = str(A[0])
    spa = []
    if '[' in FatherChen:
        for m in range(len(A)):# m为行
            q = A[m]
            for n in range(len(A[0])):# n为列
                if q[n] != 0:
                    spa.append([m,n,q[n]])
        
        std2 = str(len(A)) + '-' + str(len(A[0])) + '{'
        for m in range(len(spa)):
            w = str(spa[m])
            w = w.replace('[','(').replace(']',')')
            std2 = std2 + w + ','
        std2 = std2.strip(',')
        std2 = std2 + '}'
        return std2
    # 标准矩阵

    else:
        std3 = str(A[0]) + '-' + str(A[1]) + '{'
        for r in range(2,len(A)):
            t = str(A[r])
            t = t.replace('[','(').replace(']',')')
            std3 = std3 + t + ','
        std3 = std3.strip(',')
        std3 = std3 + '}'
        return std3
        
        
        
            
    
