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
