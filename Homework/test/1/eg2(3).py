def Str2Mat(s):
    if '{' in s:
        # 稀疏矩阵
        hanglie = s.split('{')
        hanglie2 = hanglie[0].split('-')
        hang = int(hanglie2[0])
        lie = int(hanglie2[1])
        # 行数以及列数
        t = [0]
        for m in range(lie-1):
            t.append(0)
        spa = [t]
        for m in range(hang-1):
            spa.append(t)
        for m in range(len(spa)):
            spa[m] = eval(str(spa[m]))
        # 创建一个空矩阵
        if '),(' in hanglie[1]:
            hanglie[1] = hanglie[1].strip('}')
            position = hanglie[1].split('),(')
            position[0] = position[0].strip('(')
            position[-1] = position[-1].strip(')')
            for m in range(len(position)): 
                position[m] = '[' + position[m] + ']'
                position[m] = eval(position[m])
        # 将非零的值储存于列表之中
            for m in range(len(position)):
                a = position[m]
                b = spa[a[0]-1]
                b[a[1]-1] = a[2]
                c = a[0]-1
                spa[c] = b
        # 填充非零的数
            spa.append('spa')
        # 标记为“稀疏数列”
            return spa
        else:
            spa.append('spa')
            return spa
        # 讨论零矩阵的情况
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
        matrixStd.append('std')
        # 标记为标准矩阵
        return matrixStd
    # Finished

def IsStandard(A):
    if 'std' in A[-1]:
        return 'True'
    else:
        return 'False'

def Mat2StrStandard(A):
    matrix = A
    std = str(matrix[0])
    std = std.strip(']')
    std = std.replace('(','').replace(')','') + ';'
    for m in range(1,len(matrix)-1):
        q = str(matrix[m])
        q = q.strip('[').strip(']').replace('(','').replace(')','')
        std = std + q + ';'
    std = std.strip(';') + ']'
    std = std.replace(' ','')
    return std

def Mat2StrSparse(A):
    matrix = A
    hang = len(A)-1
    lie = len(A[0])
    spa = []
    for m in range(hang):
        a = matrix[m]
        for n in range(lie):
            if (a[n] != 0):
                q = '(' + str(m+1) + ',' + str(n+1) + ',' + str(a[n]).replace('(','').replace(')','') +')'
                spa.append(q)
    spa2 = str(hang) + '-' + str(lie) + '{'
    for m in range(len(spa)):
        spa2 = spa2 + spa[m] + ','
    spa2 = spa2.strip(',') + '}'
    spa2 = spa2.replace(' ','')
    return spa2

def Standard2Sparse(A):
    matrix = A
    matrix[-1] = 'spa'
    return matrix

def Sparse2Standard(A):
    matrix = A
    matrix[-1] = 'std'
    return matrix

def MatAdd(A,B):
    hang = len(A)-1
    lie = len(A[1])
    t = [0]
    for m in range(lie-1):
        t.append(0)
    spa = [t]
    for m in range(hang-1):
        spa.append(t)
    for m in range(len(spa)):
        spa[m] = eval(str(spa[m]))
    for m in range(hang):
        q1 = A[m]
        q2 = B[m]
        r = spa[m]
        for n in range(lie):
            r[n] = q1[n] + q2[n]
            spa[m] = r
            spa[m] = eval(str(spa[m]))
    spa.append('std')
    return spa

    

    
