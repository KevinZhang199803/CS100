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
                                
                if type(eval(a)) == float:
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
    hang = len(A)
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


class MatrixSyntaxError(Exception):
    pass

class Matrix:

    def __init__(self,s):
        self.origin = s.replace(' ','').replace('(','').replace(')','')
        if '+j' in self.origin:
            self.origin = self.origin.replace('+j','+1j')
        if '-j' in self.origin:
            self.origin = self.origin.replace('-j','-1j')   
        if ',j,' in self.origin:
            self.origin = self.origin.replace(',j,',',1j,')   
        if ',-j,' in self.origin:
            self.origin = self.origin.replace(',-j,',',-1j,')   
        if '[j' in self.origin:
            self.origin = self.origin.replace('[j','[1j') 
        if '[-j' in self.origin:
            self.origin = self.origin.replace('[-j','[-1j')
        if ',-j]' in self.origin:
            self.origin = self.origin.replace(',-j]',',-1j]')   
        if ',j]' in self.origin:
            self.origin = self.origin.replace(',j]',',1j]')    
        if ',j;' in self.origin:
            self.origin = self.origin.replace(',j;',',1j;')   
        if ',-j;' in self.origin:
            self.origin = self.origin.replace(',-j;',',-1j;')   
        if ';-j,' in self.origin:
            self.origin = self.origin.replace(';-j,',';-1j,')   
        if ';j,' in self.origin:
            self.origin = self.origin.replace(';j,',';1j,')   
        if ',j+' in self.origin:
            self.origin = self.origin.replace(',j+',',1j+')
        if ',j-' in self.origin:
            self.origin = self.origin.replace(',j-',',1j-')   
        if ';j+' in self.origin:
            self.origin = self.origin.replace(';j+',';1j+')   
        if ';j-' in self.origin:
            self.origin = self.origin.replace(';j-',';1j-')
        if ((self.origin.count('[') != 1) or (self.origin.count(']') != 1)):
            raise MatrixSyntaxError
        if self.origin.find('[') != 0 or self.origin.find(']') != (len(self.origin)-1):
            raise MatrixSyntaxError
        
    
        matrix = self.origin.replace('[','').replace(']','')
        self.origin = ''
        if (matrix != ''):
            matrixStd = matrix.split(';')
            for j in range(len(matrixStd)):
                matrix_element = matrixStd[j].split(',')
                for i in range(len(matrix_element)):# 修正各个数
                    matrix_element[i] = change2std(matrix_element[i])
                    if matrix_element[i] == '0j':
                        matrix_element[i] = '0'
                    if matrix_element[i] == '-0j':
                        matrix_element[i] = '0'

                mid2 = ''
                for m in range(len(matrix_element)):
                    mid2 = mid2 + matrix_element[m] + ','
                mid2 = mid2.strip(',')  
                matrixStd[j] = mid2

                self.origin = self.origin + matrixStd[j] + ';'
                matrixStd[j] = '[' + matrixStd[j] + ']'
                matrixStd[j] = eval(matrixStd[j])
            self.origin = '[' + self.origin.strip(';').replace(' ','') + ']'
            hang = len(matrixStd)
            lie = len(matrixStd[0])
            for i in range(len(matrixStd)):
                if (len(matrixStd[i]) != lie):
                    raise MatrixSyntaxError
        
        else:
            self.origin = '[]'
            matrixStd = []
            hang = 0
            lie = 0

        self.std = matrixStd
        self.hang = hang
        self.lie = lie
        
    def __str__(self):
            return self.origin

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
            raise MatrixSyntaxError

    def __setitem__(self,n,value):
        if type(n) == int:
            if ((n >= 0) and (n <= self.hang-1)):
                if type(value) == Matrix and value.hang == 1 and value.lie == self.lie:
                    self.std[n] = value
                    strong = ''
                    for i in range(len(self.std)):
                        element = str(self.std[i]).replace('(','').replace(')','').replace(' ','').strip('[').strip(']')
                        strong = strong + element + ';'
                    strong = '[' + strong.rstrip(';') + ']'
                    self.origin = strong
                else:
                    raise MatrixSyntaxError
            else:
                raise MatrixSyntaxError
        elif type(n) == tuple:
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
            if value_str == 'j':
                value_str = '1j'
            if value_str == '-j':
                value_str = '-1j'
            value_str = change2std(value_str)
            value = eval(value_str)
            
            if hang >= 0 and hang <= self.hang-1 and lie >= 0 and lie <= self.lie-1:
                if (type(value) == int or type(value) == float or type(value) == complex):
                    self.std[hang][lie] = value
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
        if type(other) == Matrix and self.lie == other.hang:
            matrix_result = []
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
            other = eval(change2std(str(other).replace(' ','').replace('(','').replace(')','')))
            if type(other) == int or type(other) == float or type(other) == complex:
                for i in range(self.hang):
                    for j in range(self.lie):
                        self.std[i][j] = self.std[i][j] * other
                self.origin = change2str(self.std)
                return self
            else:
                raise MatrixSyntaxError

    def __truediv__(self,other):
        other = eval(change2std(str(other).replace(' ','').replace('(','').replace(')','')))
        if type(other) == int or type(other) == float or type(other) == complex:
            for i in range(self.hang):
                for j in range(self.lie):
                    self.std[i][j] = self.std[i][j] / other
            self.origin = change2str(self.std)
            return self
        else:
            raise MatrixSyntaxError

    def __neg__(self):
        for i in range(self.hang):
            for j in range(self.lie):
                self.std[i][j] = self.std[i][j] * (-1)
        self.origin = change2str(self.std)
        return self

    def __pow__(self,other):
        other = eval(change2std(str(other).replace(' ','').replace('(','').replace(')','')))
        if type(other) == int or type(other) == float or type(other) == complex:
            for i in range(self.hang):
                for j in range(self.lie):
                    self.std[i][j] = pow(self.std[i][j],other)
            self.origin = change2str(self.std)
            return self
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
            if self.hang == 0:
                return 1
            if self.hang == 1:
                return self.std[0][0]
            if self.hang == 2:
                return self.std[0][0] * self.std[1][1] - self.std[0][1] * self.std[1][0]
            if self.hang >= 3:
                result = 0
                for i in range(self.hang):#列
                    Matrix_det = []
                    for j in range(self.lie-1):#行
                        for k in range
                        
                

            
                    
            

        








        

