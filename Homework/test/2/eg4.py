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

class MatrixSyntaxError(Exception):
    pass

class Matrix:

    def __init__(self,s):
        self.origin = s.replace(' ','')
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
            matrixStd = [0]
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
            value_str = chang2std(value_str)
            value = eval(value_str)
            
            if hang >= 0 and hang <= self.hang-1 and lie >= 0 and lie <= self.lie-1:
                if (type(value) == int or type(value) == float or type(value) == complex):
                    self.std[hang][lie] = value
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
        
                    
            

        








        

