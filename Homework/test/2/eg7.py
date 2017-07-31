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
                print (eval(matrixStd[j]))
                try:
                    print (eval(matrixStd[j]))
                    matrixStd[j] = eval(matrixStd[j])
                except:
                    raise MatrixSyntaxError
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
        print(self.origin)

        self.origin = change2str(matrixStd)
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
        if self.std == []:
            raise MatrixSyntaxError
        elif (type(n) == int):
            if ((n >= 0) and (n <= self.hang-1)):
                xq = self.std[n]
                return Matrix(change2str(xq))
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
                        return change2str(result)
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
                        len(n) == 2
                        hang_cut = []
                        for i in range(self.hang):
                            hang_cut.append(i)
                        hang_cut = hang_cut[n[0]]
                        lie_cut = []
                        for i in range(self.lie):
                            lie_cut.append(i)
                        lie_cut = lie_cut[n[1]]
                        for i in range(len(hang_cut)):
                            for j in range(len(lie_cut)):
                                self.std[hang_cut[i]][lie_cut[j]] = value.std[i][j]
                        self = Matrix(change2str(self.std))
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
        if type(other) == Matrix and self.lie == other.hang:
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
                for m in range (other):
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




x = Matrix("  [12j,-0.35+j,4j,3;0.000007,3,4,5;100j,4,5,6;1,2,3,4]")
print (x)
y = Matrix('[-10-j,-j-2,j-1,j+1;123,25.000000000000000000000000005,-9,2;8,13,3j,98;1,2,3,4]')
print (y)



print (x.determinant())
print (x.inverse())
x[1] = Matrix('[1,4,3,5]');print (x)

x[1,0] = 0j;print (x)

print (Matrix('[1,2,3]'))
print (Matrix('[]')**3)
print (x[2,0])
print (x[1:2:1,0:3:2])
print (x[1])




print (x[1,0])
print (MatAdd([],[]))
print (Matrix('[1,2,3]'))


b = Matrix('[2,1,2;-1,5,21;13,-1,-17]')
print (b.determinant())

c = Matrix('[1,2,3;2,2,3;4,1,4]')
print (c.determinant())


a = Matrix('[1,1,2;-1,2,0;1,1,3]')
print (a.inverse())












