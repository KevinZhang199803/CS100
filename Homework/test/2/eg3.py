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
                                    if int(eval(a)) == eval(a):
                                        a = str(int(eval(a))).replace(' ','')
                                if '.' in b:
                                    if int(eval(b)) == eval(b):
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
                                if '+j' in matrix_element[i]:
                                    matrix_element[i] = matrix_element[i].replace('+j','+1j')
                                if '-j' in matrix_element[i]:
                                    matrix_element[i] = matrix_element[i].replace('-j','-1j')
                                if matrix_element[i] == 'j':
                                    matrix_element[i] = '1j'
                                if matrix_element[i] == '-j':
                                    matrix_element[i] = '-1j'
                            else:
                                if (num[0] == ''):
                                    b = num[1]
                                    b = b.replace('j')
                                    if '.' in b:
                                        if int(eval(b)) == eval(b):
                                            b = str(int(eval(b))).replace(' ','')
                                    if (b != '0'):
                                        matrix_element[i] = b + 'j'
                                    else:
                                        matrix_element[i] = '0'
                                else:
                                    b = num[0]
                                    b = b.replace('j')
                                    if '.' in b:
                                        if int(eval(b)) == eval(b):
                                            b = str(int(eval(b))).replace(' ','')
                                    if (b != '0'):
                                        matrix_element[i] = b + 'j'
                                    else:
                                        matrix_element[i] = '0'
                                if '+j' in matrix_element[i]:
                                    matrix_element[i] = matrix_element[i].replace('+j','+1j')
                                if '-j' in matrix_element[i]:
                                    matrix_element[i] = matrix_element[i].replace('-j','-1j')
                                if matrix_element[i] == 'j':
                                    matrix_element[i] = '1j'
                                if matrix_element[i] == '-j':
                                    matrix_element[i] = '-1j'
                            
                        elif '-' in matrix_element[i]:
                            position1 = matrix_element[i].find('-')
                            num = []
                            if (position1 == 0):#第一个数含有负号
                                matrix_element[i] = matrix_element[i].lstrip('-')
                                if '-' not in matrix_element[i]:
                                    b = '-' + matrix_element[i].replace('j','')
                                    if '.' in b:
                                        if int(eval(b)) == eval(b):
                                            b = str(int(eval(b))).replace(' ','')
                                    matrix_element[i] = b + 'j'
                                    position1 = 's'
                                    break    
                            num = matrix_element[i].split('-')
                                
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
                                        matrix_element[i] = a + b + 'j'
                                    else:
                                        matrix_element[i] = a + '+' + b + 'j'
                                if ((a != '0') and (b == '0')):
                                    matrix_element[i] = a
                                if ((a == '0') and (b != '0')):
                                    matrix_element[i] = b + 'j'
                                if ((a == '0') and (b == '0')):
                                    matrix_element[i] = '0'
                                if '+j' in matrix_element[i]:
                                    matrix_element[i] = matrix_element[i].replace('+j','+1j')
                                if '-j' in matrix_element[i]:
                                    matrix_element[i] = matrix_element[i].replace('-j','-1j')
                                if matrix_element[i] == 'j':
                                    matrix_element[i] = '1j'
                                if matrix_element[i] == '-j':
                                    matrix_element[i] = '-1j'
                                    
                            else:
                                if ((num[0] == '') and (position1 != 666666)):
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
                                    if (position1 != 666666):
                                        b = num[0]
                                        b = b.replace('j','')
                                        if type(eval(b)) == float:
                                            if int(b) == eval(b):
                                                b = str(int(eval(b))).replace(' ','')
                                        if (b != '0'):
                                            matrix_element[i] = b + 'j'
                                        else:
                                            matrix_element[i] = '0'
                                if '+j' in matrix_element[i]:
                                    matrix_element[i] = matrix_element[i].replace('+j','+1j')
                                if '-j' in matrix_element[i]:
                                    matrix_element[i] = matrix_element[i].replace('-j','-1j')
                                if matrix_element[i] == 'j':
                                    matrix_element[i] = '1j'
                                if matrix_element[i] == '-j':
                                    matrix_element[i] = '-1j'
                                            
                        else:
                            if '.' in matrix_element[i]:
                                x = matrix_element[i].replace('j','')
                                if int(eval(x)) == eval(x):
                                    x = str(int(eval(x))).replace(' ','') + 'j'
                                    matrix_element[i] = x

                            if matrix_element[i] == 'j':
                                matrix_element[i] = '1j'

                            if matrix_element[i] == '-j':
                                matrix_element[i] = '-1j'


                    else:
                        if '.'in matrix_element[i]:
                            if int(eval(matrix_element[i])) == eval(matrix_element[i]):
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
    		    return self.std[n]
    		else:
    		    raise MatrixSyntaxError
    	elif (type(n) == tuple):
    		hang_r = n[0]
    		lie_r = n[1]
    		if ((type(hang_r) != int) or (type(lie_r) != int)):
    			raise MatrixSyntaxError
    		elif ((hang_r >= 0) and (hang_r <= self.hang-1) and (lie_r >= 0) and (lie_r <= self.lie-1)):
    			return self.std[hang_r][lie_r]
    		else:
    			raise MatrixSyntaxError
    	else:
    		raise MatrixSyntaxError

    def  __setitem__(self,n,value):
    	if (type(n) == int):
    	    if ((n >= 0) and (n <= self.hang-1)):
    	    	if (type(value) == Matrix):
    	    		if ((value.lie == self.lie) and (value.hang == 1)):
    	    			self.std[n] = value.std[0]
    	    			
    	    		else:
    	    			raise MatrixSyntaxError
    	    	else:
    	    		raise MatrixSyntaxError
    	    else:
    	    	raise MatrixSyntaxError
    	elif (type(n) == tuple):
    		hang_c = n[0]
    		lie_c = n[1]
    		if ((type(hang_c) != int) or (type(lie_c) != int)):
    			raise MatrixSyntaxError
    		elif ((hang_c >= 0) and (hang_c <= self.hang-1) and (lie_c >= 0) and (lie_c <= self.lie-1) and ((type(value) == int) or (type(value) == float) or (type(value) == complex))):
    			self.std[hang_c][lie_c] = value
    		else:
    			raise MatrixSyntaxError
    	else:
    		raise MatrixSyntaxError

    def __add__(self,matrix_2):
    	if (type(matrix_2) != Matrix):
    		raise MatrixSyntaxError








