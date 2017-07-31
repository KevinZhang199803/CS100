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
        if '-j]' in self.origin:
            self.origin = self.origin.replace('-j]','-1j]')
        if 'j]' in self.origin:
            self.origin = self.origin.replace('j]','1j]')
        if ',j;' in self.origin:
            self.origin = self.origin.replace(',j;',',1j;')
        if ',-j;' in self.origin:
            self.origin = self.origin.replace(',-j;',',-1j;')
        if ';-j,' in self.origin:
            self.origin = self.origin.replace(';-j,',';-1j,')
        if ';j,' in self.origin:
            self.origin = self.origin.replace(';j,',';1j,')

        if ((self.origin.count('[') != 1) or (self.origin.count(']') != 1)):
            raise MatrixSyntaxError
    
        matrix = self.origin.replace('[','').replace(']','')
        self.origin = ''
        if (matrix != ''):
            matrixStd = matrix.split(';')
            for j in range(len(matrixStd)):
                matrix_element = matrixStd[j].split(',')
                for i in range(len(matrix_element)):# 修正各个数
                    if 'j' in matrix_element[i]:
                        if '+' in matrix_element[i]:
                            num = matrix_element[i].split('+')
                            if ((num[0] != '') and (num[1] != '')):
                                a = num[0]
                                b = num[1]
                                if 'j' in a:
                                    mid = a
                                    a = b
                                    b = mid
                                b = b.replace('j','')
                                if '.' in a:
                                    if int(a) == eval(a):
                                        a = str(int(eval(a))).replace(' ','')
                                if '.' in b:
                                    if int(b) == eval(b):
                                        b = str(int(eval(b))).replace(' ','')
                                if ((a != '0') and (b != '0')):
                                    if '-' in b:
                                        matrix_element[i] = a + b + 'j'
                                    else:
                                        matrix_element[i] = a + '+' + b + 'j'
                                if ((a != '0') and (b == '0')):
                                    matrix_element[i] = a
                                if ((a == '0') and (b != '0')):
                                    matrix_element[i] = b + 'j'
                                if ((a == '0') and (b == '0')):
                                    matrix_element[i] = '0'
                            else:
                                if (num[0] == ''):
                                    b = num[1]
                                    b = b.replace('j')
                                    if '.' in b:
                                        if int(b) == eval(b):
                                            b = str(int(eval(b))).replace(' ','')
                                    if (b != '0'):
                                        matrix_element[i] = b + 'j'
                                    else:
                                        matrix_element[i] = '0'
                                else:
                                    b = num[0]
                                    b = b.replace('j')
                                    if '.' in b:
                                        if int(b) == eval(b):
                                            b = str(int(eval(b))).replace(' ','')
                                    if (b != '0'):
                                        matrix_element[i] = b + 'j'
                                    else:
                                        matrix_element[i] = '0'
                            
                        elif '-' in matrix_element[i]:
                            position1 = matrix_element[i].find('-')
                            if (position1 == 0):#第一个数含有负号
                                matrix_element[i] = matrix_element[i].lstrip('-')
                                if '-' not in matrix_element[i]:
                                    b = '-' + matrix_element[i].replace('j','')
                                    if '.' in b:
                                        if int(b) == eval(b):
                                            b = str(int(eval(b))).replace(' ','')
                                    matrix_element[i] = b + 'j'
                                    
                            num = matrix_element[i].split('-')
                            if ((num[0] != '') and (num[1] != '')):
                                a = num[0]
                                
                                if position1 == 0:
                                    a = '-' + a
                                    
                                b = num[1]
                                if 'j' in a:
                                    mid = a
                                    a = b
                                    b = mid
                                b = b.replace('j','')
                                if type(eval(a)) == float:
                                    if int(a) == eval(a):
                                        a = str(int(eval(a)))
                                    if type(eval(b)) == float:
                                        if int(b) == eval(b):
                                            b = str(int(eval(b))).replace(' ','')
                                    if ((a != '0') and (b != '0')):
                                        matrix_element[i] = a + '-' + b + 'j'
                                    if ((a != '0') and (b == '0')):
                                        matrix_element[i] = a
                                    if ((a == '0') and (b != '0')):
                                        matrix_element[i] = b + 'j'
                                    if ((a == '0') and (b == '0')):
                                        matrix_element[i] = '0'
                                else:
                                    if (num[0] == ''):
                                        b = num[1]
                                        b = b.replace('j','')
                                        if type(eval(b)) == float:
                                            if int(b) == eval(b):
                                                b = str(int(eval(b))).replace(' ','')
                                        if (b != '0'):
                                            matrix_element[i] = b + 'j'
                                        else:
                                            matrix_element[i] = '0'
                                    else:
                                        b = num[0]
                                        b = b.replace('j','')
                                        if type(eval(b)) == float:
                                            if int(b) == eval(b):
                                                b = str(int(eval(b))).replace(' ','')
                                        if (b != '0'):
                                            matrix_element[i] = b + 'j'
                                        else:
                                            matrix_element[i] = '0'
                                            
                    else:
                        if '.'in matrix_element[i]:
                            if int(matrix_element[i]) == eval(matrix_element[i]):
                                matrix_element[i] = str(int(eval(matrix_element[i]))).replace(' ','')


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
            matrixStd = [0]
            hang = 0
            lie = 0

        self.std = matrixStd
        self.hang = hang
        self.lie = lie
        
    def __str__(self):
        if (self.origin == '[]'):
            return 0
        else:
            return self.origin

    def isIdentity(self):
        if (matrixStd == [0]):
            return True
        elif (hang != lie):
            return False
        else:
            t = [0]
            for m in range(lie-1):
                t.append(0)
            iden = [t]
            for m in range(hang-1):
                iden.append(t)
            for m in range(len(iden)):
                iden[m] = eval(str(iden[m]))
            for m in range(len(iden)):
                iden[m][m] = 1
            if (iden == matrixStd):
                return True
            else:
                return False

    def isSquare(self):
        if (matrixStd == [0]):
            return True
        elif (hang == lie):
            return True
        else:
            return False
        
    
