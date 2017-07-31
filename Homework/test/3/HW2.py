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
                    if type(mat1) == list or type(mat2) == list:#矩阵与矩阵或者常数相乘
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
                    if type(mat1) == list or type(mat2) == list:#矩阵与矩阵或者常数相乘
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
#-------------------------separate element apart part-------------------------------------------------------------------------------------------------------------------------------------------------------
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
# delete every empty string                    
            position_del = []        
            j = 0
            for i in range(len(element)):
                if element[i] == '':
                    position_del.append(i-j)
                    j = j + 1
            
            for i in range(len(position_del)):
                del element[position_del[i]]
#-------------------------part ends-------------------------------------------------------------------------------------------------------------------------------------------------------------------------                
#-------------------------change every element to standard form part----------------------------------------------------------------------------------------------------------------------------------------
                
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
#---------------------------------part ends------------------------------------------------------------------------------------------------------------
#---------------------------------change infix to postfix part-----------------------------------------------------------------------------------------
            
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
#------------------------------------part ends-----------------------------------------------------------------------------------------------
#------------------------------------calculate part------------------------------------------------------------------------------------------

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
                    if type(mat1) == list or type(mat2) == list:#矩阵与矩阵或者常数相乘
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
            
        self.std = self.result
        if self.std != []:
            for i in range(len(self.std)):
                for j in range(len(self.std[0])):
                    if self.std[i][j] == 0j or self.std[i][j] == -0j:
                        self.std[i][j] = 0
                    elif type(self.std[i][j]) == complex:
                        self.std[i][j] = eval(change2std(str(self.std[i][j]).replace(' ','').replace('(','').replace(')','')))
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
#-----------------------------------------------------------------------------part ends------------------------------------------------------------------------------------------------        
            
    def __str__(self):
        return change2str(self.std).replace(' ','').replace('(','').replace(')','')
