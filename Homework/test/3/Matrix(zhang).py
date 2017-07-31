class MatrixSyntaxError(Exception):
    pass

def change2std(s):
    if 'j' in s:
        if '+j' in s:
            s = s.replace('+j','+1j')
        if '-j' in s:
            s = s.replace('-j','-1j')
        if 'j+' in s:
            s = s.replace('j+','1j+')
        if '-j+' in s:
            s = s.replace('-j+','-1j+')
        if '+' in s:
            num = s.split('+')
            if ((num[0] != '') and (num[1] != '')):
                a = num[0]
                b = num[1]
                if 'j' in a:
                    mid = a
                    a = b
                    b = mid
                b = b.replace('j','')
                if '.' in a:
                    if int(eval(a)) == eval(a):
                        a = str(int(eval(a))).replace(' ','')
                if '.' in b:
                    if int(eval(b)) == eval(b):
                        b = str(int(eval(b))).replace(' ','')
                if ((a != '0') and (b != '0')):
                    if '-' in b:
                        s = a + b + 'j'
                    else:
                        s = a + '+' + b + 'j'
                if ((a != '0') and (b == '0')):
                    s = a
                if ((a == '0') and (b != '0')):
                    s = b + 'j'
                if ((a == '0') and (b == '0')):
                    s = '0'
                if '+j' in s:
                    s = s.replace('+j','+1j')
                if '-j' in s:
                    s = s.replace('-j','-1j')
                if s == 'j':
                    s = '1j'
                if s == '-j':
                    s = '-1j'
            else:
                if (num[0] == ''):
                    b = num[1]
                    b = b.replace('j','')
                    if '.' in b:
                        if int(eval(b)) == eval(b):
                            b = str(int(eval(b))).replace(' ','')
                    if (b != '0'):
                        s = b + 'j'
                    else:
                        s = '0'
                else:
                    b = num[0]
                    b = b.replace('j')
                    if '.' in b:
                        if int(eval(b)) == eval(b):
                            b = str(int(eval(b))).replace(' ','')
                    if (b != '0'):
                        s = b + 'j'
                    else:
                        s = '0'
                if '+j' in s:
                    s = s.replace('+j','+1j')
                if '-j' in s:
                    s = s.replace('-j','-1j')
                if s == 'j':
                    s = '1j'
                if s == '-j':
                    s = '-1j'
                            
        elif '-' in s:
            position1 = s.find('-')
            num = []
            if (position1 == 0):#第一个数含有负号
                s = s.lstrip('-')
                if '-' not in s:
                    b = '-' + s.replace('j','')
                    if '.' in b:
                        if int(eval(b)) == eval(b):
                            b = str(int(eval(b))).replace(' ','')
                    s = b + 'j'
                    position1 = 's'
                    return s
            num = s.split('-')
                                
            if ((num[0] != '') and (num[1] != '') and (position1 != 's')):
                a = num[0]
                                
                if position1 == 0:
                    a = '-' + a
                                    
                b = '-' + num[1]
                if 'j' in a:
                    mid = a
                    a = b
                    b = mid
                b = b.replace('j','')
                                
                if isinstance(eval(a),float):
                    if int(eval(a)) == eval(a):
                        a = str(int(eval(a))).replace(' ','')
                if type(eval(b)) == float:
                    if int(eval(b)) == eval(b):
                        b = str(int(eval(b))).replace(' ','')
                if ((a != '0') and (b != '0')):
                    if '-' in b:
                        s = a + b + 'j'
                    else:
                        s = a + '+' + b + 'j'
                if ((a != '0') and (b == '0')):
                    s = a
                if ((a == '0') and (b != '0')):
                    s = b + 'j'
                if ((a == '0') and (b == '0')):
                    s = '0'
                if '+j' in s:
                    s = s.replace('+j','+1j')
                if '-j' in s:
                    s = s.replace('-j','-1j')
                if s == 'j':
                    s = '1j'
                if s == '-j':
                    s = '-1j'
                                    
            else:
                if ((num[0] == '') and (position1 != 's')):
                    b = num[1]
                    b = b.replace('j','')
                    if type(eval(b)) == float:
                        if int(b) == eval(b):
                            b = str(int(eval(b))).replace(' ','')
                    if (b != '0'):
                        s = b + 'j'
                    else:
                        s = '0'
                else:
                    if (position1 != 's'):
                        b = num[0]
                        b = b.replace('j','')
                        if type(eval(b)) == float:
                            if int(b) == eval(b):
                                b = str(int(eval(b))).replace(' ','')
                        if (b != '0'):
                            s = b + 'j'
                        else:
                            s = '0'
                if '+j' in s:
                    s = s.replace('+j','+1j')
                if '-j' in s:
                    s = s.replace('-j','-1j')
                if s == 'j':
                    s = '1j'
                if s == '-j':
                    s = '-1j'
                                            
        else:
            if '.' in s:
                x = s.replace('j','')
                if int(eval(x)) == eval(x):
                    x = str(int(eval(x))).replace(' ','') + 'j'
                    s = x

            if s == 'j':
                s = '1j'

            if s == '-j':
                s = '-1j'


    else:
        if '.'in s:
            if int(eval(s)) == eval(s):
                s = str(int(eval(s))).replace(' ','')

    if s == '0j' or s == '-0j':
        return '0'
    else: 
        return s

def MatAdd(A,B):
    if type(A) != list or type(B) != list:
        raise MatrixSyntaxError
    if len(A) != len(B):
        raise MatrixSyntaxError
    if B == []:
        return A
    elif A == []:
        return B
    else:
        hang = len(A)
        lie = len(A[0])
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
        return spa

def MatSub(A,B):
    if type(A) != list or type(B) != list:
        raise MatrixSyntaxError
    if len(A) != len(B):
        raise MatrixSyntaxError
    try:
        len(A[0]) == len(B[0])
    except:
        raise MatrixSyntaxError
    if B == []:
        return A
    hang_A = len(A)
    lie_A = len(A[0])
    hang_B = len(B)
    lie_B = len(B[0])
    t = [0]
    for m in range(lie_A-1):
        t.append(0)
    spa = [t]
    for m in range(hang_A-1):
        spa.append(t)
    for m in range(len(spa)):
        spa[m] = eval(str(spa[m]))
    for m in range(hang_A):
        q1 = A[m]
        q2 = B[m]
        r = spa[m]
        for n in range(lie_A):
            r[n] = q1[n] - q2[n]
            spa[m] = r
            spa[m] = eval(str(spa[m]))
    return spa

def change2str(std):# turn a list matrix into a string matrix
    matrix_str = ''
    for i in range(len(std)):
        element = str(std[i]).replace('(','').replace(')','').replace(' ','').strip('[').strip(']')
        matrix_str = matrix_str + element + ';'
    matrix_str = '[' + matrix_str.rstrip(';') + ']'
    return matrix_str

def MatTransposition(A):
    if A == []:
        return []
    hang = len(A)
    lie = len(A[0])
    t = [0]
    for m in range(hang-1):
        t.append(0)
    spa = [t]
    for m in range(lie-1):
        spa.append(t)
    for m in range(len(spa)):
        spa[m] = eval(str(spa[m]))
    for m in range(hang):
        q1 = A[m]
        for n in range(lie):
            r = spa[n]
            r[m] = q1[n]
            spa[n] = eval(str(r))
    return spa


def MatMul(A,B):
    if A == B == []:
        return []
    elif type(A) == list and type(B) == list:
        try:
            hang_A = len(A)
            hang_B = len(B)
            lie_A = len(A[0])
            lie_B = len(B[0])
        except:
            raise MatrixSyntaxError
        if lie_A == hang_B:
            matrix_result = []
            if A == B == []:
                return []
            else:
                for i in range(hang_A):#左边矩阵要操作的行数
                    element = []
                    for j in range(lie_B):#右边矩阵要操作的列数
                        detail = 0
                        for k in range(lie_A):#具体第几个元素相乘
                            detail = detail + A[i][k] * B[k][j]
                        element.append(detail)
                    matrix_result.append(element)
                return matrix_result
        else:
            raise MatrixSyntaxError

    elif type(A) == list or type(B) == list:# A is a list;B is a constant
        if type(A) != list:
            mid = A
            A = B
            B = mid
        try:
            hang_A = len(A)
            lie_A = len(A[0])
        except:
            raise MatrixSyntaxError
        try:
            if type(B) == int or type(B) == float or type(B) == complex:
                result = []
                for i in range(hang_A):
                    element = []
                    for j in range(lie_A):
                        element.append(A[i][j] * B)
                    result.append(element)

                return result
            else:
                raise MatrixSyntaxError
        except:
            raise MatrixSyntaxError

    else:
        raise MatrixSyntaxError

def MatDiv(A,other):
    if type(A) != list:
        raise MatrixSyntaxError
    if type(other) != int and type(other) != float and type(other) != complex:
        raise MatrixSyntaxError
    try:
        hang = len(A)
        lie = len(A[0])
    except:
        raise MatrixSyntaxError
    
    if other != 0:
        result = []
        for i in range(hang):
            element = []
            for j in range(lie):
                mid = A[i][j] / other
                if type(mid) != complex:
                    if int(mid) == mid:
                        mid = int(mid)
                else:
                    mid = complex(mid)
                element.append(mid)
            result.append(element)
        return result
    else:
        raise MatrixSyntaxError

def neg(A):
    result = []
    hang = len(A)
    lie = len(A[0])
    for i in range(hang):
        element = []
        for j in range(lie):
            element.append(A[i][j] * (-1))
        result.append(element)
    return result

def det(A):
    if len(A) == 0:
        return 1
    elif len(A) == 1:
        return A[0][0]
    elif len(A) == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    elif len(A) >= 3:
        result = 0
        for i in range(len(A)):#第一行元素的列数，第一行self.hang个元素，所以加self.hang次
            Matrix_det = []
            # 下面算余子式
            for j in range(len(A)-1):#行
                Matrix_det.append([])
                for k in range(len(A)):#列
                    if i != k:
                        Matrix_det[j].append(A[j+1][k])
            result = result + pow((-1),1+i+1) * A[0][i] * det(Matrix_det)
        return result
    else:
        raise MatrixSyntaxError

class Node:
    def __init__(self,v):
        self._v = v
        self._next = None
        self._pre = None

class Stack:
    def __init__(self):
        self._bottom = None
        self._top = None

    def peak(self):
        return self._top._v

    def isEmpty(self):
        return self._top == None

    def push(self,v):
        node = Node(v)
        if self._top == None:
            self._top,self_bottom  = node,node
        else:
            self._top._next = node
            node._pre = self._top
            self._top = node
    
    def pop(self):
        if self._top == None:
            raise MatrixSyntaxError
        else:
            node = self._top
            if self._top._pre != None:
                self._top._pre._next = None
                self._top = self._top._pre
            else:
                self._top, self._bottom = None, None
            return node._v


class Matrix:
    def __init__(self,s,mode = 'prefix'):
        if s.count('[') != s.count(']') or s.count('(') != s.count(')'):
            raise MatrixSyntaxError
        matrix_str = []
        matrix_std = []
        position_pre = []
        position_post = []
        position_T = []
        start1 = 0
        start2 = 0

        origin = s
        origin = origin.replace(' ','').replace('[','&[').replace(']',']&').replace('T','&T&').replace('*','&*&').replace('/','&/&').replace('(','&(').replace(')',')&').strip('&')

        element = origin.split('&')
        for i in range(len(element)):
            if ('[' not in element[i]) and (']' not in element[i]) and ('(' not in element[i]) and (')' not in element[i]):
                element[i] = element[i].replace('+','&+&').replace('-','&-&')
        origin = ''
        for i in range(len(element)):
            origin = origin + '&' + element[i]
        origin = origin.strip('&')
        element = origin.split('&')
        
        position_del = []
        j = 0
        for i in range(len(element)):
            if element[i] == '':
                position_del.append(i-j)
                j = j + 1
            if element[i] == '(':
                position_del.append(i-j)
                j = j + 1
            if element[i] == ')':
                position_del.append(i-j)
                j = j + 1
        for i in range(len(position_del)):
            del element[position_del[i]]
        
        #for i in range(len(element)):
        #    if ('[' not in element[i]) and (']' not in element[i]) and ('(' not in element[i]) and (')' not in element[i]):
        #        element[i] = element.replace('+','&+&').replace('-','&-&')

        for i in range(len(element)):
            if '[' and ']' in element[i]:
                if '+j' in element[i]:
                    element[i] = element[i].replace('+j','+1j')
                if '-j' in element[i]:
                    element[i] = element[i].replace('-j','-1j')   
                if ',j,' in element[i]:
                    element[i] = element[i].replace(',j,',',1j,')   
                if ',-j,' in element[i]:
                    element[i] = element[i].replace(',-j,',',-1j,')   
                if '[j' in element[i]:
                    element[i] = element[i].replace('[j','[1j') 
                if '[-j' in element[i]:
                    element[i] = element[i].replace('[-j','[-1j')
                if ',-j]' in element[i]:
                    element[i] = element[i].replace(',-j]',',-1j]')   
                if ',j]' in element[i]:
                    element[i] = element[i].replace(',j]',',1j]')    
                if ',j;' in element[i]:
                    element[i] = element[i].replace(',j;',',1j;')   
                if ',-j;' in element[i]:
                    element[i] = element[i].replace(',-j;',',-1j;')   
                if ';-j,' in element[i]:
                    element[i] = element[i].replace(';-j,',';-1j,')   
                if ';j,' in element[i]:
                    element[i] = element[i].replace(';j,',';1j,')   
                if ',j+' in element[i]:
                    element[i] = element[i].replace(',j+',',1j+')
                if ',j-' in element[i]:
                    element[i] = element[i].replace(',j-',',1j-')   
                if ';j+' in element[i]:
                    element[i] = element[i].replace(';j+',';1j+')   
                if ';j-' in element[i]:
                    element[i] = element[i].replace(';j-',';1j-')
                if element[i] != '[]':   
                    mat_element = element[i].strip('[').strip(']').split(';')
                    matstd = []
                    for j in range(len(mat_element)):
                        mat_element_element = mat_element[j].split(',')
                        matstd.append([])
                        for k in range(len(mat_element_element)):
                            mat_element_element[k] = change2std(mat_element_element[k])
                            if mat_element_element[k] == '0j':
                                mat_element_element[k] = '0'
                            if mat_element_element[k] == '-0j':
                                mat_element_element[k] = '0'
                            try:
                                matstd[j].append(eval(mat_element_element[k]))
                            except:
                                raise MatrixSyntaxError

                        mid = ''
                        for k in range(len(mat_element_element)):
                            mid = mid + mat_element_element[k] + ','
                        mid = mid.strip(',')
                        mat_element[j] = mid

                    mid2 = ''
                    for j in range(len(mat_element)):
                        mid2 = mid2 + mat_element[j] + ';'
                    mid2 = mid2.strip(';')
                    element[i] = '[' + mid2 + ']'
                    matrix_std.append(matstd)
                else:
                    element[i] = '[]'
                    matrix_std.append([])

            
        if mode == 'prefix':

            #对前缀表达式求值，要从右至左扫描表达式，
            #首先从右边第一个字符开始判断，若当前字符是数字则一直到数字串的末尾再记录下来，若为运算符，则将右边离得最近的两个“数字串”作相应运算，
            #然后以此作为一个新的“数字串”并记录下来；扫描到表达式最左端时扫描结束，最后运算的值即为表达式的值。
            #例如：对前缀表达式“- 1 + 2 3”求值，扫描到3时，记录下这个数字串，扫描到2时，记录下这个数字串，当扫描到+时，将+右移做相邻两数字串的运算符，记为2+3，结果为5，记录下5这个新数字串，然后继续向左扫描，扫描到1时，记录下这个数字串，扫描到-时，将-右移做相邻两数字串的运算符，记为1-5，结果为-4，此时关于这个表达式的全部运算已完成，故表达式的值为-4。
            stack = Stack()
            pt_ele = len(element) - 1
            pt_mat = len(matrix_std) - 1
            while pt_ele >= 0:
                if '[' and ']' in element[pt_ele]:
                    try:
                        stack.push(matrix_std[pt_mat])
                        pt_mat = pt_mat - 1
                        pt_ele = pt_ele - 1
                    except:
                        raise MatrixSyntaxError
                elif '(' and ')' in element[pt_ele]:
                    try:
                        num = change2std(element[pt_ele].strip('(').strip(')'))
                        stack.push(eval(change2std(num)))
                        pt_ele = pt_ele - 1
                    except:
                        raise MatrixSyntaxError
                elif element[pt_ele] == '+':
                    mat1 = stack.pop()
                    mat2 = stack.pop()
                    if type(mat1) == list and type(mat2) == list:
                        try:
                            stack.push(MatAdd(mat1,mat2))
                            pt_ele = pt_ele - 1
                        except:
                            raise MatrixSyntaxError
                    elif (type(mat1) == int or type(mat1) == float or type(mat1) == complex) and (type(mat2) == int or type(mat2) == float or type(mat2) == complex):
                        stack.push(mat1 + mat2)
                        pt_ele = pt_ele - 1
                    else:
                        raise MatrixSyntaxError
                elif element[pt_ele] == '-':
                    mat1 = stack.pop()
                    mat2 = stack.pop()
                    if type(mat1) == list and type(mat2) == list:
                        try:
                            stack.push(MatSub(mat1,mat2))
                            pt_ele = pt_ele - 1
                        except:
                            raise MatrixSyntaxError
                    elif (type(mat1) == int or type(mat1) == float or type(mat1) == complex) and (type(mat2) == int or type(mat2) == float or type(mat2) == complex):
                        stack.push(mat1 - mat2)
                        pt_ele = pt_ele -1
                    else:
                        raise MatrixSyntaxError
                elif element[pt_ele] == 'T':
                    mat = stack.pop()
                    if type(mat) == list:
                        stack.push(MatTransposition(mat))
                        pt_ele = pt_ele - 1
                    else:
                        raise MatrixSyntaxError
                elif element[pt_ele] == '/':
                    mat1 = stack.pop()
                    mat2 = stack.pop()
                    if (type(mat1) == int or type(mat1) == float or type(mat1) == complex) and (type(mat2) == int or type(mat2) == float or type(mat2) == complex):
                        stack.push(mat1 / mat2)
                    elif type(mat1) == list and (type(mat2) == int or type(mat2) == float or type(mat2) == complex):
                        stack.push(MatDiv(mat1,mat2))
                        pt_ele = pt_ele - 1
                    else:
                        raise MatrixSyntaxError
                elif element[pt_ele] == '*':
                    mat1 = stack.pop()
                    mat2 = stack.pop()
                    if (type(mat1) == list and type(mat2) == list) or (type(mat1) == list and (type(mat2) == int or type(mat2) == float or type(mat2) == complex)):#矩阵与矩阵或者常数相乘
                        try:
                            stack.push(MatMul(mat1,mat2))
                            pt_ele = pt_ele - 1
                        except:
                            raise MatrixSyntaxError
                    elif (type(mat2) == list and (type(mat1) == int or type(mat1) == float or type(mat1) == complex)):
                        try:
                            stack.push(MatMul(mat2,mat1))
                            pt_ele = pt_ele - 1
                        except:
                            raise MatrixSyntaxError
                    elif (type(mat1) == int or type(mat1) == float or type(mat1) == complex) and (type(mat2) == int or type(mat2) == float or type(mat2) == complex):#常数与常数相乘
                        stack.push(mat1 * mat2)
                        pt_ele = pt_ele - 1
                    else:
                        raise MatrixSyntaxError
                else:
                    raise MatrixSyntaxError
            self.result = stack.pop()
            if stack.isEmpty() == False:
                raise MatrixSyntaxError
        
        elif mode == 'postfix':
            mid = [i for i in range(len(element))]
            for i in range(len(element)):
                mid[-1-i] = element[i]
            element = mid
            
            mid = [i for i in range(len(matrix_std))]
            for i in range(len(matrix_std)):
                mid[-1-i] = matrix_std[i]
            matrix_std = mid

            stack = Stack()
            pt_ele = len(element) - 1
            pt_mat = len(matrix_std) - 1
            while pt_ele >= 0:
                if '[' and ']' in element[pt_ele]:
                    try:
                        stack.push(matrix_std[pt_mat])
                        pt_mat = pt_mat - 1
                        pt_ele = pt_ele - 1
                    except:
                        raise MatrixSyntaxError
                elif '(' and ')' in element[pt_ele]:
                    try:
                        num = change2std(element[pt_ele].strip('(').strip(')'))
                        stack.push(eval(change2std(num)))
                        pt_ele = pt_ele - 1
                    except:
                        raise MatrixSyntaxError
                elif element[pt_ele] == '+':
                    mat1 = stack.pop()
                    mat2 = stack.pop()
                    if type(mat1) == list and type(mat2) == list:
                        try:
                            stack.push(MatAdd(mat2,mat1))
                            pt_ele = pt_ele - 1
                        except:
                            raise MatrixSyntaxError
                    elif (type(mat1) == int or type(mat1) == float or type(mat1) == complex) and (type(mat2) == int or type(mat2) == float or type(mat2) == complex):
                        stack.push(mat2 + mat1)
                        pt_ele = pt_ele - 1
                    else:
                        raise MatrixSyntaxError
                elif element[pt_ele] == '-':
                    mat1 = stack.pop()
                    mat2 = stack.pop()
                    if type(mat2) == list and type(mat1) == list:
                        try:
                            stack.push(MatSub(mat2,mat1))
                            pt_ele = pt_ele - 1
                        except:
                            raise MatrixSyntaxError
                    elif (type(mat1) == int or type(mat1) == float or type(mat1) == complex) and (type(mat2) == int or type(mat2) == float or type(mat2) == complex):
                        stack.push(mat2 - mat1)
                        pt_ele = pt_ele -1
                    else:
                        raise MatrixSyntaxError
                elif element[pt_ele] == 'T':
                    mat = stack.pop()
                    if type(mat) == list:
                        stack.push(MatTransposition(mat))
                        pt_ele = pt_ele - 1
                    else:
                        raise MatrixSyntaxError
                elif element[pt_ele] == '/':
                    mat1 = stack.pop()
                    mat2 = stack.pop()
                    if (type(mat1) == int or type(mat1) == float or type(mat1) == complex) and (type(mat2) == int or type(mat2) == float or type(mat2) == complex):
                        stack.push(mat2 / mat1)
                    elif type(mat2) == list and (type(mat1) == int or type(mat1) == float or type(mat1) == complex):
                        stack.push(MatDiv(mat2,mat1))
                        pt_ele = pt_ele - 1
                    else:
                        raise MatrixSyntaxError
                elif element[pt_ele] == '*':
                    mat1 = stack.pop()
                    mat2 = stack.pop()
                    if (type(mat1) == list and type(mat2) == list) or (type(mat2) == list and (type(mat1) == int or type(mat1) == float or type(mat1) == complex)):#矩阵与矩阵或者常数相乘
                        try:
                            stack.push(MatMul(mat2,mat1))
                            pt_ele = pt_ele - 1
                        except:
                            raise MatrixSyntaxError
                    elif (type(mat1) == list and (type(mat2) == int or type(mat2) == float or type(mat2) == complex)):
                        try:
                            stack.push(MatMul(mat1,mat2))
                            pt_ele = pt_ele - 1
                        except:
                            raise MatrixSyntaxError
                    elif (type(mat1) == int or type(mat1) == float or type(mat1) == complex) and (type(mat2) == int or type(mat2) == float or type(mat2) == complex):#常数与常数相乘
                        stack.push(mat1 * mat2)
                        pt_ele = pt_ele - 1
                    else:
                        raise MatrixSyntaxError
                else:
                    raise MatrixSyntaxError
            self.result = stack.pop()
            if stack.isEmpty() == False:
                raise MatrixSyntaxError

        elif mode == 'infix':
            change = Stack()
            origin = s
            origin = origin.replace(' ','').replace('[','&[').replace(']',']&').replace('T','&T&').replace('*','&*&').replace('/','&/&').replace('(','&(').replace(')',')&').strip('&')

            element = origin.split('&')
            for i in range(len(element)):
                if ('[' not in element[i]) and (']' not in element[i]) and ('(' not in element[i]) and (')' not in element[i]):
                    element[i] = element[i].replace('+','&+&').replace('-','&-&')
            origin = ''
            for i in range(len(element)):
                origin = origin + '&' + element[i]
            origin = origin.strip('&')
            element = origin.split('&')    
                    
            position_del = []        
            j = 0
            for i in range(len(element)):
                if element[i] == '':
                    position_del.append(i-j)
                    j = j + 1
            
            for i in range(len(position_del)):
                del element[position_del[i]]
            
            for i in range(len(element)):
                if '[' and ']' in element[i]:
                    if '+j' in element[i]:
                        element[i] = element[i].replace('+j','+1j')
                    if '-j' in element[i]:
                        element[i] = element[i].replace('-j','-1j')   
                    if ',j,' in element[i]:
                        element[i] = element[i].replace(',j,',',1j,')   
                    if ',-j,' in element[i]:
                        element[i] = element[i].replace(',-j,',',-1j,')   
                    if '[j' in element[i]:
                        element[i] = element[i].replace('[j','[1j') 
                    if '[-j' in element[i]:
                        element[i] = element[i].replace('[-j','[-1j')
                    if ',-j]' in element[i]:
                        element[i] = element[i].replace(',-j]',',-1j]')   
                    if ',j]' in element[i]:
                        element[i] = element[i].replace(',j]',',1j]')    
                    if ',j;' in element[i]:
                        element[i] = element[i].replace(',j;',',1j;')   
                    if ',-j;' in element[i]:
                        element[i] = element[i].replace(',-j;',',-1j;')   
                    if ';-j,' in element[i]:
                        element[i] = element[i].replace(';-j,',';-1j,')   
                    if ';j,' in element[i]:
                        element[i] = element[i].replace(';j,',';1j,')   
                    if ',j+' in element[i]:
                        element[i] = element[i].replace(',j+',',1j+')
                    if ',j-' in element[i]:
                        element[i] = element[i].replace(',j-',',1j-')   
                    if ';j+' in element[i]:
                        element[i] = element[i].replace(';j+',';1j+')   
                    if ';j-' in element[i]:
                        element[i] = element[i].replace(';j-',';1j-')
                    if element[i] != '[]':   
                        mat_element = element[i].strip('[').strip(']').split(';')
                        matstd = []
                        for j in range(len(mat_element)):
                            mat_element_element = mat_element[j].split(',')
                            matstd.append([])
                            for k in range(len(mat_element_element)):
                                mat_element_element[k] = change2std(mat_element_element[k])
                                if mat_element_element[k] == '0j':
                                    mat_element_element[k] = '0'
                                if mat_element_element[k] == '-0j':
                                    mat_element_element[k] = '0'
                                try:
                                    matstd[j].append(eval(mat_element_element[k]))
                                except:
                                    raise MatrixSyntaxError

                            mid = ''
                            for k in range(len(mat_element_element)):
                                mid = mid + mat_element_element[k] + ','
                            mid = mid.strip(',')
                            mat_element[j] = mid
 
                        mid2 = ''
                        for j in range(len(mat_element)):
                            mid2 = mid2 + mat_element[j] + ';'
                        mid2 = mid2.strip(';')
                        element[i] = '[' + mid2 + ']'
                        matrix_std.append(matstd)
                    else:
                        element[i] = '[]'
                        matrix_std.append([])
            
            position_del = []
            j = 0
            for i in range(len(element)):
                if element[i] == '':
                    position_del.append(i-j)
                    j = j + 1
            for i in range(len(position_del)):
                del element[position_del[i]]
            
            #从右至左扫描中缀表达式，从右边第一个字符开始判断：
            #如果当前字符是数字，则分析到数字串的结尾并将数字串直接输出。
            #如果是运算符，则比较优先级。如果当前运算符的优先级大于等于栈顶运算符的优先级(当栈顶是括号时，直接入栈)，则将运算符直接入栈；
            #否则将栈顶运算符出栈并输出，直到当前运算符的优先级大于等于栈顶运算符的优先级(当栈顶是括号时，直接入栈)，再将当前运算符入栈。
            #如果是括号，则根据括号的方向进行处理。如果是右括号，则直接入栈；否则，遇左括号前将所有的运算符全部出栈并输出，遇右括号后将左右的两括号一起删除。
    
            i = len(element) - 1
            mid = []
            prior = {'+':1,'-':1,'*':2,'/':2,'T':3,')':0}
            while i >= 0:
                if '[' in element[i] and ']' in element[i]:
                    mid.append(element[i])
                    i = i - 1
                    j = j - 1
                elif element[i] == ')':
                    change.push(')')
                    i = i - 1
                elif element[i] == '(':
                    if change.peak() == ')':
                        nouse = change.pop()
                        i = i - 1
                    else:
                        try:
                            while change.peak() != ')':
                                mid.append(change.pop())
                            nouse2 = change.pop()
                            i = i - 1
                        except:
                            raise MatrixSyntaxError
                elif '(' in element[i] and ')' in element[i]:
                    mid.append(element[i])
                    i = i - 1
                #如果是运算符，则比较优先级。如果当前运算符的优先级大于等于栈顶运算符的优先级(当栈顶是括号时，直接入栈)，则将运算符直接入栈；
                #否则将栈顶运算符出栈并输出，直到当前运算符的优先级大于等于栈顶运算符的优先级(当栈顶是括号时，直接入栈)，再将当前运算符入栈。
                elif element[i] == '+':
                    if change.isEmpty() == True:
                        change.push(element[i])
                        i = i - 1
                    else:
                        try:
                            if prior[element[i]] >= prior[change.peak()]:
                                change.push(element[i])
                                i = i - 1
                            else:
                                while prior[element[i]] < prior[change.peak()]:
                                    mid.append(change.pop())
                                change.push(element[i])
                                i = i - 1
                        except:
                            raise MatrixSyntaxError
                elif element[i] == '-':
                    if change.isEmpty() == True:
                        change.push(element[i])
                        i = i - 1
                    elif change.peak() != ('+' or '-' or '*' or '/' or 'T'):
                        change.push(element[i])
                        i = i - 1
                    else:
                        try:
                            if prior[element[i]] >= prior[change.peak()]:
                                change.push(element[i])
                                i = i - 1
                            else:
                                while change.peak() != ')' or prior[element[i]] < prior[change.peak()]:
                                    mid.append(change.pop())
                                change.push(element[i])
                                i = i - 1
                        except:
                            raise MatrixSyntaxError
                elif element[i] == '*':
                    if change.isEmpty() == True:
                        change.push(element[i])
                        i = i - 1
                    elif change.peak() != ('+' or '-' or '*' or '/' or 'T'):
                        change.push(element[i])
                        i = i - 1
                    else:
                        try:
                            if prior[element[i]] >= prior[change.peak()]:
                                change.push(element[i])
                                i = i - 1
                            else:
                                while change.peak() != ')' or prior[element[i]] < prior[change.peak()]:
                                    mid.append(change.pop())
                                change.push(element[i])
                                i = i - 1
                        except:
                            raise MatrixSyntaxError
                elif element[i] == '/':
                    if change.isEmpty() == True:
                        change.push(element[i])
                        i = i - 1
                    elif change.peak() != ('+' or '-' or '*' or '/' or 'T'):
                        change.push(element[i])
                        i = i - 1
                    else:
                        try:
                            if prior[element[i]] >= prior[change.peak()]:
                                change.push(element[i])
                                i = i - 1
                            else:
                                while change.peak() != ')' or prior[element[i]] < prior[change.peak()]:
                                    mid.append(change.pop())
                                change.push(element[i])
                                i = i - 1
                        except:
                            raise MatrixSyntaxError
                elif element[i] == 'T':
                    if change.isEmpty() == True:
                        change.push(element[i])
                        i = i - 1
                    elif change.peak() != ('+' or '-' or '*' or '/' or 'T'):
                        change.push(element[i])
                        i = i - 1
                    else:
                        try:
                            if prior[element[i]] >= prior[change.peak()]:
                                change.push(element[i])
                                i = i - 1
                            else:
                                while change.peak() != ')' or prior[element[i]] < prior[change.peak()]:
                                    mid.append(change.pop())
                                change.push(element[i])
                                i = i - 1
                        except:
                            raise MatrixSyntaxError
                else:
                    raise MatrixSyntaxError
                
            while change.isEmpty() == False:
                mid.append(change.pop())
            element = mid

            mid = len(element) // 2
            for i in range(mid):
                mid2 = element[i]
                element[i] = element[len(element) - 1 -i]
                element[len(element) - 1 - i] = mid2
  
            stack = Stack()
            pt_ele = len(element) - 1
            pt_mat = len(matrix_std) - 1
            while pt_ele >= 0:
                if '[' and ']' in element[pt_ele]:
                    try:
                        stack.push(matrix_std[pt_mat])
                        pt_mat = pt_mat - 1
                        pt_ele = pt_ele - 1
                    except:
                        raise MatrixSyntaxError
                elif '(' and ')' in element[pt_ele]:
                    try:
                        num = change2std(element[pt_ele].strip('(').strip(')'))
                        stack.push(eval(change2std(num)))
                        pt_ele = pt_ele - 1
                    except:
                        raise MatrixSyntaxError
                elif element[pt_ele] == '+':
                    mat1 = stack.pop()
                    mat2 = stack.pop()
                    if type(mat1) == list and type(mat2) == list:
                        try:
                            stack.push(MatAdd(mat1,mat2))
                            pt_ele = pt_ele - 1
                        except:
                            raise MatrixSyntaxError
                    elif (type(mat1) == int or type(mat1) == float or type(mat1) == complex) and (type(mat2) == int or type(mat2) == float or type(mat2) == complex):
                        stack.push(mat1 + mat2)
                        pt_ele = pt_ele - 1
                    else:
                        raise MatrixSyntaxError
                elif element[pt_ele] == '-':
                    mat1 = stack.pop()
                    mat2 = stack.pop()
                    if type(mat1) == list and type(mat2) == list:
                        try:
                            stack.push(MatSub(mat1,mat2))
                            pt_ele = pt_ele - 1
                        except:
                            raise MatrixSyntaxError
                    elif (type(mat1) == int or type(mat1) == float or type(mat1) == complex) and (type(mat2) == int or type(mat2) == float or type(mat2) == complex):
                        stack.push(mat1 - mat2)
                        pt_ele = pt_ele -1
                    else:
                        raise MatrixSyntaxError
                elif element[pt_ele] == 'T':
                    mat = stack.pop()
                    if type(mat) == list:
                        stack.push(MatTransposition(mat))
                        pt_ele = pt_ele - 1
                    else:
                        raise MatrixSyntaxError
                elif element[pt_ele] == '/':
                    mat1 = stack.pop()
                    mat2 = stack.pop()
                    if (type(mat1) == int or type(mat1) == float or type(mat1) == complex) and (type(mat2) == int or type(mat2) == float or type(mat2) == complex):
                        stack.push(mat1 / mat2)
                    elif type(mat1) == list and (type(mat2) == int or type(mat2) == float or type(mat2) == complex):
                        stack.push(MatDiv(mat1,mat2))
                        pt_ele = pt_ele - 1
                    else:
                        raise MatrixSyntaxError
                elif element[pt_ele] == '*':
                    mat1 = stack.pop()
                    mat2 = stack.pop()
                    if (type(mat1) == list and type(mat2) == list) or (type(mat1) == list and (type(mat2) == int or type(mat2) == float or type(mat2) == complex)):#矩阵与矩阵或者常数相乘
                        try:
                            stack.push(MatMul(mat1,mat2))
                            pt_ele = pt_ele - 1
                        except:
                            raise MatrixSyntaxError
                    elif (type(mat2) == list and (type(mat1) == int or type(mat1) == float or type(mat1) == complex)):
                        try:
                            stack.push(MatMul(mat2,mat1))
                            pt_ele = pt_ele - 1
                        except:
                            raise MatrixSyntaxError
                    elif (type(mat1) == int or type(mat1) == float or type(mat1) == complex) and (type(mat2) == int or type(mat2) == float or type(mat2) == complex):#常数与常数相乘
                        stack.push(mat1 * mat2)
                        pt_ele = pt_ele - 1
                    else:
                        raise MatrixSyntaxError
                else:
                    raise MatrixSyntaxError
            self.result = stack.pop()
            if stack.isEmpty() == False:
                raise MatrixSyntaxError
            
            
        self.std = self.result
        if self.std != []:
            for i in range(len(self.std)):
                for j in range(len(self.std[0])):
                    if self.std[i][j] == 0j or self.std[i][j] == -0j:
                        self.std[i][j] = 0
                    elif type(self.std[i][j]) == complex:
                        self.std[i][j] = complex(change2std(str(self.std[i][j]).replace(' ','').replace('(','').replace(')','')))
                    elif type(self.std[i][j]) == float:
                        if int(self.std[i][j]) == self.std[i][j]:
                            self.std[i][j] = int(self.std[i][j])
                            
            self.hang = len(self.std)
            self.lie = len(self.std[0])
            self.origin = change2str(self.std)
        else:
            self.hang = 0
            self.lie = 0
            self.origin = '[]'
        
            
    def __str__(self):
        return change2str(self.std).replace(' ','').replace('(','').replace(')','')

    def isIdentity(self):
        if (self.std == [0]):
            return True
        elif (self.hang != self.lie):
            return False
        else:
            t = [0]
            for m in range(self.lie-1):
                t.append(0)
            iden = [t]
            for m in range(self.hang-1):
                iden.append(t)
            for m in range(len(iden)):
                iden[m] = eval(str(iden[m]))
            for m in range(len(iden)):
                iden[m][m] = 1
            if (iden == self.std):
                return True
            else:
                return False

    def isSquare(self):
        if (self.std == [0]):
            return True
        elif (self.hang == self.lie):
            return True
        else:
            return False

    def __getitem__(self,n):
        if (type(n) == int):
            if ((n >= 0) and (n <= self.hang-1)):
                xq = self.std[n]
                xq = str(xq).replace('(','').replace(')','').replace(' ','')
                xq2 = Matrix(xq)
                return xq2
            else:
                raise MatrixSyntaxError
        elif (type(n) == tuple):
            if not isinstance(n[0],slice) and not isinstance(n[1],slice):
                hang_r = n[0]
                lie_r = n[1]
                if ((type(hang_r) != int) or (type(lie_r) != int)):
                    raise MatrixSyntaxError
                elif ((hang_r >= 0) and (hang_r <= self.hang-1) and (lie_r >= 0) and (lie_r <= self.lie-1)):
                    value = self.std[hang_r][lie_r]
                    return value
                else:
                    raise MatrixSyntaxError
            else:
                if not isinstance(n[0],slice) or not isinstance(n[1],slice):
                    raise MatrixSyntaxError
                else:
                    try:
                        hang_cut = [k for k in range(self.hang)][n[0]]
                        lie_cut = [k for k in range(self.lie)][n[1]]
                        result = []
                        for i in range(len(hang_cut)):
                            result.append([])
                            for j in range(len(lie_cut)):
                                result[i].append(self.std[hang_cut[i]][lie_cut[j]])
                        return Matrix(change2str(result))
                    except:
                        raise MatrixSyntaxError
                                
        elif isinstance(n,slice):
            return Matrix(change2str(self.std[n]))
        else:
            raise MatrixSyntaxError

    def __setitem__(self,n,value):
        if type(n) == int:
            if ((n >= 0) and (n <= self.hang-1)):
                if type(value) == Matrix and value.hang == 1 and value.lie == self.lie:
                    self.std[n] = value.std[0]
                    self.origin = change2str(self.std)
                else:
                    raise MatrixSyntaxError
            else:
                raise MatrixSyntaxError
        elif type(n) == tuple:
            if not isinstance(n[0],slice) and not isinstance(n[1],slice):
                hang = n[0]
                lie = n[1]
            
                value_str = str(value).replace(' ','').replace('(','').replace(')','')
                if 'j+' in value_str:
                    value_str = value_str.replace('j+','1j+')
                if 'j-' in value_str:
                    value_str = value_str.replace('j-','1j-')
                if '-j+' in value_str:
                    value_str = value_str.replace('-j+','-1j+')
                if '-j-' in value_str:
                    value_str = value_str.replace('-j-','-1j-')
                if value_str == '0j' or value_str == '-0j':
                    value_str = '0'
                if value_str == 'j':
                    value_str = '1j'
                if value_str == '-j':
                    value_str = '-1j'
                value_str = change2std(value_str)
                value = eval(value_str)
            
                if hang >= 0 and hang <= self.hang-1 and lie >= 0 and lie <= self.lie-1:
                    if (type(value) == int or type(value) == float or type(value) == complex):
                        self.std[n[0]][n[1]] = value
                        matrix_str = ''
                        for i in range(len(self.std)):
                            element = str(self.std[i]).replace('(','').replace(')','').replace(' ','').strip('[').strip(']')
                            matrix_str = matrix_str + element + ';'
                        matrix_str = '[' + matrix_str.rstrip(';') + ']'
                        self.origin = matrix_str
                    else:
                        raise MatrixSyntaxError
                else:
                    raise MatrixSyntaxError
            else:
                if not isinstance(n[0],slice) or not isinstance(n[1],slice):
                    raise MatrixSyntaxError
                else:
                    try:
                        hang_change = [k for k in range(self.hang)][n[0]]
                        lie_change = [k for k in range(self.lie)][n[1]]
                        for i in range(len(hang_change)):
                            for j in range(len(lie_change)):
                                self.std[hang_change[i]][lie_change[j]] = value.std[i][j]
                        self.origin = change2str(self.std)
                    except:
                        raise MatrixSyntaxError           
        else:
            raise MatrixSyntaxError

    def __add__(self,other):
        if type(other) == Matrix and other.hang == self.hang and other.lie == self.lie:
            result_list = MatAdd(self.std,other.std)
            result_str = change2str(result_list)
            result = Matrix(result_str)
            return result
        else:
            raise MatrixSyntaxError

    def __sub__(self,other):
        if type(other) == Matrix and other.hang == self.hang and other.lie == self.lie:
            result_list = MatSub(self.std,other.std)
            result_str = change2str(result_list)
            result = Matrix(result_str)
            return result
        else:
            raise MatrixSyntaxError

    def __mul__(self,other):
        if type(other) == Matrix:
            if self.lie == other.hang:
                matrix_result = []
                if self.std == other.std == []:
                    return Matrix('[]')
                else:
                
                    for i in range(self.hang):#左边矩阵要操作的行数
                        element = []
                        for j in range(other.lie):#右边矩阵要操作的列数
                            detail = 0
                            for k in range(self.lie):#具体第几个元素相乘
                                detail = detail + self.std[i][k] * other.std[k][j]
                            element.append(detail)
                        matrix_result.append(element)
                    return Matrix(change2str(matrix_result))
            else:
                raise MatrixSyntaxError

        else:
            other = eval(change2std(str(other).replace(' ','').replace('(','').replace(')','')))
            if type(other) == int or type(other) == float or type(other) == complex:
                result = []
                for i in range(self.hang):
                    element = []
                    for j in range(self.lie):
                        element.append(self.std[i][j] * other)
                    result.append(element)
                return Matrix(change2str(result))
            else:
                raise MatrixSyntaxError

    def __truediv__(self,other):
        if other != 0:
            result = []
            for i in range(self.hang):
                element = []
                for j in range(self.lie):
                    element.append(self.std[i][j] / other)
                result.append(element)
            return Matrix(change2str(result))
        else:
            raise MatrixSyntaxError

    def __neg__(self):
        result = []
        for i in range(self.hang):
            element = []
            for j in range(self.lie):
                element.append(self.std[i][j] * (-1))
            result.append(element)
        return Matrix(change2str(result))

    def __pow__(self,other):
        if isinstance(other,int) and other>=1:
            if other == 1:
                return self
            else:
                return self * (self ** (other-1))
        else:
            raise MatrixSyntaxError

    def __eq__(self,other):
        if type(other) == Matrix:
            return self.std == other.std
        else:
            raise MatrixSyntaxError

    def determinant(self):#余子式法，除去第一行元素，以及所在列，得到的矩阵求行列式
        if self.hang != self.lie:
            raise MatrixSyntaxError
        else:
            return det(self.std)

    def transposition(self):
        self.std = MatTransposition(self.std)
        self = Matrix(change2str(self.std))
        return self

    def inverse(self):
        if self.hang != self.lie:
            raise MatrixSyntaxError
        elif self.std == []:
            raise MatrixSyntaxError
        elif self.hang == 1:
            return Matrix(change2str(self.std / self.determinant))
        elif self.hang == 2:
            result = [[],[]]
            result[0].append(self.std[1][1] / self.determinant())
            result[0].append((-1) * self.std[0][1] / self.determinant())
            result[1].append((-1) * self.std[1][0] / self.determinant())
            result[1].append(self.std[0][0] / self.determinant())
            return Matrix(change2str(result))
        elif self.hang >= 3:
            #主对角元素是将原矩阵该元素所在行列去掉再求行列式.
            #非主对角元素 是"""原矩阵该元素的共轭位置的元素去掉所在行列求"""行列式"""乘以(-1)^(x+y) x,y为该元素的共轭位置的元素的行和列的序号，序号从1开始的.
            bansui = []
            for i in range (self.hang):#伴随矩阵的行
                bansui.append([])
                for j in range (self.lie):#伴随矩阵的列
                    trans = []
                    x = -1
                    #下面，求"""原矩阵该元素的共轭位置的元素去掉所在行列求"""的矩阵
                    for k in range (self.lie):#共轭元素的行 j 
                        if k != i:
                            trans.append([])
                            x = x + 1
                            for p in range (self.hang):#共轭元素的列 i
                                if p != j:
                                    trans[x].append(self.std[k][p])
                    bansui[i].append(det(trans) * (-1) ** (i+1+j+1))

            bansui_trans = MatTransposition(bansui)
            bansui_det = det(self.std)
            bansui_matrix = Matrix(change2str(bansui_trans))
            return bansui_matrix / bansui_det
        else:
            raise MatrixSyntaxError


print(Matrix('[1,2,3]*(2)','infix'),type(Matrix('[1,2,3]*(2)','infix')))
print(Matrix('[1,2,3]')*Matrix('T[1,2,3]'),type(Matrix('[1,2,3]')*Matrix('T[1,2,3]')))
print(Matrix('*-[j,3+0j;5.6,8][j,2;0.6,j](2)')+Matrix('[1,2;3,4]'))
print(Matrix('[1,2;3,4][3,j;-0-j,0j]T*(2)*','postfix'))
print(Matrix('T+**[2,3;9,4][1,2;3,4](-0-j)[1,2;3,4]','prefix'))
x = Matrix("[1,3; 2,4; 3, 5]T[1,2; 3,4; 5, 6]*", "postfix")
print(x,type(x))
x = Matrix("[1,2,3; 3,4,5] [1,2; 3,4; 5, 6] *", "postfix")
print(x)
print (x * 122j)
x = Matrix("[1,3; 2,4; 3, 5]T[1,2; 3,4; 5, 6]*", "postfix")
print(str(x))
x = Matrix("[1]T[22j]*[3]+", "postfix")
print(str(x))
x = Matrix("*(122 j)T[1]", "prefix")
print(str(x))
x = Matrix("([31]*[2]T+[5]*(9))*(10)", "infix")
print(str(x))
x = Matrix("((31)*[2]T+(5)*[9])*(10)","infix") 
print(x)
x = Matrix("((([1]+[-2j])*(3)+([4]+[5])*(1+2j))T*[9+j]T/(2+2j))T","infix")
print(x)
y = Matrix("([3]*[2 ]+[5] * (9))T* (10)/(10)", "infix")
print(str(y))
print(x+y)
z = Matrix('[2]')
print(x+z)
print(Matrix('(([ 7,8;9,1 0]+[1,2;3,4j]/(2))T+[1,2;3,4])','infix'))
print(Matrix('[233,1;  233,2]'))
x = Matrix("([2]T*(31)+[9]*(5))*(10)", "infix")
print(x)
x = Matrix("([3]*[2]+[ 9]*(5))T*(10)/(10)", "infix")
print(x)
x = Matrix("[1.1,2.2]*(1j)", "infix")
print(x)
Y = Matrix("((([1]+ [2j])*(3)+([4]+[5])*(6.1j))T*[9+j]T/(2))T", "infix")
print(Y)
x = Matrix("[1+j]*(22j) *[3]", "infix")
print(x)
print(Matrix('[1,2;3,4]T[1,3; 2,4]+(12)/T','postfix'))

#x = Matrix("[1+j]T[0.9j](3.1)(4 )**","postfix")
#print(x)
#x = Matrix("[1]*2","infix")
#print(x)
#x = Matrix("[1]+[1]")
#print(x)

x = Matrix("([-1-3j]*[1]+[ 1]*(1))T*(10)/(10)", "infix")
print(x)


x = Matrix("[1,2,3; 4,5,6; 7,8,9]")
y = Matrix("[0,1,2; 3,4,5; 6,7,8]")
print(str(Matrix("+ [1,2,3; 4,5,6; 7,8,9] [0,1,2; 3,4,5; 6,7,8]")) == str(x+y))
print(str(Matrix("- [1,2,3; 4,5,6; 7,8,9] [0,1,2; 3,4,5; 6,7,8]")) == str(x-y))
print(str(Matrix("* [1,2,3; 4,5,6; 7,8,9] [0,1,2; 3,4,5; 6,7,8]")) == str(x*y))
print(str(Matrix("* [1,2,3; 4,5,6; 7,8,9] (2)")) == str(x*2))
print(str(Matrix("/ [1,2,3; 4,5,6; 7,8,9] (2)")) == str(x/2))
print(str(Matrix("T [1,2,3; 4,5,6; 7,8,9]")))
z = x * y
print(str(Matrix("/ [24,30,36;51,66,81;78,102,126] (2)")) == str(z / 2))
print()

print(str(Matrix(" [1,2,3; 4,5,6; 7,8,9] + [0,1,2; 3,4,5; 6,7,8]", "infix")) == str(x+y))
print(str(Matrix(" [1,2,3; 4,5,6; 7,8,9] - [0,1,2; 3,4,5; 6,7,8]", "infix")) == str(x-y))
print(str(Matrix(" [1,2,3; 4,5,6; 7,8,9] * [0,1,2; 3,4,5; 6,7,8]", "infix")) == str(x*y))
print(str(Matrix(" [1,2,3; 4,5,6; 7,8,9] * (2)", "infix")) == str(x*2))
print(str(Matrix(" [1,2,3; 4,5,6; 7,8,9] / (2)", "infix")) == str(x/2))
print(str(Matrix("[1,2,3; 4,5,6; 7,8,9] T", "infix")))
z = x * y
print(str(Matrix("[24,30,36;51,66,81;78,102,126] / (2)", "infix")) == str(z / 2))
print()

print(str(Matrix(" [1,2,3; 4,5,6; 7,8,9]  [0,1,2; 3,4,5; 6,7,8] +", "postfix")) == str(x+y))
print(str(Matrix(" [1,2,3; 4,5,6; 7,8,9]  [0,1,2; 3,4,5; 6,7,8] -", "postfix")) == str(x-y))
print(str(Matrix(" [1,2,3; 4,5,6; 7,8,9]  [0,1,2; 3,4,5; 6,7,8] *", "postfix")) == str(x*y))
print(str(Matrix(" [1,2,3; 4,5,6; 7,8,9]  (2) *", "postfix")) == str(x*2))
print(str(Matrix(" [1,2,3; 4,5,6; 7,8,9]  (2) /", "postfix")) == str(x/2))
print(str(Matrix("[1,2,3; 4,5,6; 7,8,9] T", "postfix")))
z = x * y
print(str(Matrix("[24,30,36;51,66,81;78,102,126] (2) / ", "postfix")) == str(z / 2))
print()
x = Matrix("[1,2,3; 4,5,6; 7,8,9]")
y = Matrix("[0,1,2; 3,4,5; 6,7,8]")
print(x+y)
print(Matrix("+ [1,2,3; 4,5,6; 7,8,9] [0,1,2; 3,4,5; 6,7,8]"). transposition())

x=Matrix("((([-9+1j]+[-2j])*(3)+([4]+[5])*[1+2j])T*[9+j]T/(2+2j))T","infix")
print(x)
x = Matrix("+[3]*T[1](122 j)", "prefix")
print(str(x))
x = Matrix("+[3]*T[1](122 j)", "prefix")
print(str(x))


x = Matrix("[1]T[22j]*[3]+", "postfix")
print(str(x))

x = Matrix("*(122 j)T[1]", "prefix")
print(str(x))


x=Matrix('[2.5]*(2)','infix')
print(x)
x=Matrix('-[2.5][1]')
print(x)
x=Matrix('[]')
print(x)
x=Matrix('*[123](3)','prefix')
print(x)
x=Matrix('[123]/(3)','infix')
print(x)

x = Matrix('T+**[2,3;9,4][1,2;3,4](-0-j)[1,2;3,4]')
print(x)
x = Matrix('[0-j][0+j]+','postfix')
print(x)    
x = Matrix('(([2,3;9,4]*([1,2;3,4]*(-0-j))+[1,2;3,4]))T','infix')
print(x)
x = Matrix("[1,3; 2,4; 3, 5]T[1,2; 3,4; 5, 6]*", "postfix")
print(x,type(x))
x = Matrix("[1,2,3; 3,4,5] [1,2; 3,4; 5, 6] *", "postfix")
print(x)
x = Matrix("[1,3; 2,4; 3, 5]T[1,2; 3,4; 5, 6]*", "postfix")
print(str(x))
x = Matrix("[1]T[22j]*[3]+", "postfix")
print(str(x))

#x = Matrix("+[3]*(122 j)T[1]", "prefix") baocuo

#print(str(x))

x = Matrix("([31]*[2]T+[5]*(9))*(10)", "infix")
print(str(x))   

x = Matrix("((31)*[2]T+(5)*[9])*(10)","infix")  #±šŽí
print('-------------', x)

#z=Matrix('((([1]+[-2j]*3+[4]+[5]*(1+2j))T*[9+1j]T/(2+2j))T)+(([3]*[2]+[5]*9)T*10/10)','infix')
#print (z)
x = Matrix("((([1]+[-2j])*(3)+([4]+[5])*(1+2j))T*[9+j]T/(2+2j))T","infix")
print(x)
y = Matrix("([3]*[2 ]+[5] * (9))T* (10)/(10)", "infix")
print(y)
print(x+y)

z = Matrix('[2]')
print(z)
print(x+z,)
print()
print(Matrix('(([ 7,8;9,1 0]+[1,2;3,4j]/(2))T+[1,2;3,4])','infix'))
print(Matrix('[233,1;  233,2]'))
x = Matrix("([2]T*(31)+[9]*(5))*(10)", "infix")
print(x)
x = Matrix("([3]*[2]+[ 9]*(5))T*(10)/(10)", "infix")
print(x) 
x = Matrix("[1.1,2.2]*(1j)", "infix")
print(x)  
Y = Matrix("((([1]+ [2j])*(3)+([4]+[5])*(6.1j))T*[9+j]T/(2))T", "infix")
print(Y)
x = Matrix("[1+j]*(22j) *[3]", "infix")
print(x)
print(Matrix('[1,2;3,4]T[1,3; 2,4]+(12)/T','postfix'))

#x = Matrix("[1+j]T[0.9j](3.1)(4 )**","postfix")
#print(x) #±šŽí

#x = Matrix("[1]*2","infix") 
#print(x)

x = Matrix("[1]+[1]",'infix')
print(x)
x = Matrix("+[3]*T[1](122 j)", "prefix")
print(str(x))
x = Matrix("([-1-3j]*[1]+[ 1]*(1))T*(10)/(10)", "infix")
print(x)


x = Matrix("[1,2,3; 4,5,6; 7,8,9]")
y = Matrix("[0,1,2; 3,4,5; 6,7,8]")
print(str(Matrix("+ [1,2,3; 4,5,6; 7,8,9] [0,1,2; 3,4,5; 6,7,8]")) == str(x+y))
print(str(Matrix("- [1,2,3; 4,5,6; 7,8,9] [0,1,2; 3,4,5; 6,7,8]")) == str(x-y))
print(str(Matrix("* [1,2,3; 4,5,6; 7,8,9] [0,1,2; 3,4,5; 6,7,8]")) == str(x*y))
print(str(Matrix("* [1,2,3; 4,5,6; 7,8,9] (2)")) == str(x*2))
print(str(Matrix("/ [1,2,3; 4,5,6; 7,8,9] (2)")) == str(x/2))
print(str(Matrix("T [1,2,3; 4,5,6; 7,8,9]")))
z = x * y
print(str(Matrix("/ [24,30,36;51,66,81;78,102,126] (2)")) == str(z / 2))
print()

print(str(Matrix(" [1,2,3; 4,5,6; 7,8,9] + [0,1,2; 3,4,5; 6,7,8]", "infix")) == str(x+y))
print(str(Matrix(" [1,2,3; 4,5,6; 7,8,9] - [0,1,2; 3,4,5; 6,7,8]", "infix")) == str(x-y))
print(str(Matrix(" [1,2,3; 4,5,6; 7,8,9] * [0,1,2; 3,4,5; 6,7,8]", "infix")) == str(x*y))
print(str(Matrix(" [1,2,3; 4,5,6; 7,8,9] * (2)", "infix")) == str(x*2))
print(str(Matrix(" [1,2,3; 4,5,6; 7,8,9] / (2)", "infix")) == str(x/2))
print(str(Matrix("[1,2,3; 4,5,6; 7,8,9] T", "infix")))
z = x * y
print(str(Matrix("[24,30,36;51,66,81;78,102,126] / (2)", "infix")) == str(z / 2))
print()

print(str(Matrix(" [1,2,3; 4,5,6; 7,8,9]  [0,1,2; 3,4,5; 6,7,8] +", "postfix")) == str(x+y))
print(str(Matrix(" [1,2,3; 4,5,6; 7,8,9]  [0,1,2; 3,4,5; 6,7,8] -", "postfix")) == str(x-y))
print(str(Matrix(" [1,2,3; 4,5,6; 7,8,9]  [0,1,2; 3,4,5; 6,7,8] *", "postfix")) == str(x*y))
print(str(Matrix(" [1,2,3; 4,5,6; 7,8,9]  (2) *", "postfix")) == str(x*2))
print(str(Matrix(" [1,2,3; 4,5,6; 7,8,9]  (2) /", "postfix")) == str(x/2))
print(str(Matrix("[1,2,3; 4,5,6; 7,8,9] T", "postfix")))
z = x * y
print(str(Matrix("[24,30,36;51,66,81;78,102,126] (2) / ", "postfix")) == str(z / 2))
print()
x = Matrix("[1,2,3; 4,5,6; 7,8,9]")
y = Matrix("[0,1,2; 3,4,5; 6,7,8]")
print(x+y)
#print(Matrix("+ [1,2,3; 4,5,6; 7,8,9] [0,1,2; 3,4,5; 6,7,8]"). transposition())

x=Matrix("((([-9+1j]+[-2j])*(3)+([4]+[5])*(1+2j))T*[9+j]T/(2+2j))T","infix")
print(x)

x =Matrix("*[1]((((1))))")
print(x)
x =Matrix("[1]*((((1))))","infix")
print(x)
x =Matrix("[1]((((1))))*","postfix")
print(x)

x = Matrix("/[1](1)","infix")#±šŽí
print(x)
#x = Matrix("*[1,2,3;4,5,6 (1)")#±šŽí
#print(x)
