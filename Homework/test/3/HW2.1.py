class MatrixSyntaxError(Exception):
    pass

def change2std(s):
    if 'j' in s:
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
    if B == []:
        return A
    hang_A = len(A)
    lie_A = len(A[0])
    hang_B = len(B)
    lie_B = len(B[0])
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
    hang = len(A)
    lie = len(A[1])
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
    if type(A) == list and type(B) == list:
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
        if type(B) == int or (type(B) == float or complex or int):
            result = []
            for i in range(hang_A):
                element = []
                for j in range(lie_B):
                    element.append(A[i][j] * B)
                result.append(element)

            return result
        else:
            raise MatrixSyntaxError

    else:
        raise MatrixSyntaxError

def MatDiv(A,other):
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
                element.append(A[i][j] / other)
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
        origin = origin.replace(' ','').replace('[','&[').replace(']',']&').replace('T','&T&').replace('+','&+&').replace('-','&-&').replace('*','&*&').replace('/','&/&').replace('(','&(').replace(')',')&').strip('&')

        if len(position_T) > len(position_pre) or len(position_pre) != len(position_post):
            raise MatrixSyntaxError

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
        print(element)

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
                print(element[i])
                if element[i] != '[]':   
                    mat_element = element[i].strip('[').strip(']').split(';')
                    matstd = []
                    print(mat_element)
                    for j in range(len(mat_element)):
                        mat_element_element = mat_element[j].split(',')
                        matstd.append([])
                        print(mat_element_element)
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
            print(element)
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
                        stack.push(eval(num))
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
                    elif (type(mat1) == int or float or complex) and (type(mat1) == int or float or complex):
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
                    elif (type(mat1) == int or float or complex) and (type(mat1) == int or float or complex):
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
                    if type(mat1) == list and type(mat2) == list:
                        try:
                            stack.push(MatDiv(mat1,mat2))
                            pt_ele = pt_ele - 1
                        except:
                            raise MatrixSyntaxError
                    elif (type(mat1) == int or float or complex) and (type(mat1) == int or float or complex):
                        stack.push(mat1 / mat2)
                        pt_ele = pt_ele - 1
                    else:
                        raise MatrixSyntaxError
                elif element[pt_ele] == '*':
                    mat1 = stack.pop()
                    mat2 = stack.pop()
                    if (type(mat1) == list and (type(mat2) == list or int or float or complex)) or (type(mat2) == list and (type(mat1) == list or int or float or complex)):
                        try:
                            stack.push(MatMul(mat1,mat2))
                            pt_ele = pt_ele - 1
                        except:
                            raise MatrixSyntaxError
                    elif (type(mat1) == int or float or complex) and (type(mat1) == int or float or complex):
                        stack.push(mat1 * mat2)
                        pt_ele = pt_ele - 1
                    else:
                        raise MatrixSyntaxError
                else:
                    raise MatrixSyntaxError
            result = stack.pop()
            print(result)
					
                    

                    
                    

        


        
            
            
                
            
        
