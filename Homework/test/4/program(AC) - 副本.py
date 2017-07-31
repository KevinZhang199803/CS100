class program():
    def __init__(self,s):
        self.vec_dic = {}
        self.command_list = []
        self.node_list = []
        self.edges = []
        self.CFG = []
        instr = s.replace(' ','').replace('\t','').replace('\n','').rstrip('}')
        define_part = instr.split('{')[0]
        exec_part = instr.split('{')[1]
        # define part 
        define_list = define_part.split(';')
        for stmt in define_list:
            if stmt != 'main()':
                vec = stmt[4:].split('=')[0]
                self.vec_dic[vec] = eval(stmt[4:].split('=')[1])
        # execute part
        exec_list = exec_part.split(';')
        for i in exec_list:
            if i == '':exec_list.remove(i)
        ##print (exec_list)
        for stmt in exec_list:      
            if stmt[0:2] == 'fi':
                fi_str = stmt[2:]
                self.command_list.append('fi')
                if fi_str.split(':')[1][0:2] == 'if':
                    point = 0
                    while fi_str[point] != '(':
                        point += 1  
                    avl = 1
                    point += 1
                    while avl != 0:
                        if fi_str[point] == '(':
                            avl += 1
                            point += 1
                        elif fi_str[point] == ')':
                            avl = avl - 1
                            point += 1
                        else:
                            point += 1
                    self.command_list.append('if_stmt')
                    self.command_list.append(fi_str[:point])
                    self.command_list.append(fi_str[point:])
                elif fi_str.split(':')[1][0:5] == 'while':
                    point = 0
                    while fi_str[point] != '(':
                        point += 1
                    avl = 1
                    point += 1
                    while avl != 0:
                        if fi_str[point] == '(':
                            avl += 1
                            point += 1
                        elif fi_str[point] == ')':
                            avl = avl - 1
                            point += 1
                        else:
                            point += 1
                    self.command_list.append('while_stmt')
                    self.command_list.append(fi_str[:point])
                    self.command_list.append(fi_str[point:])
                else:
                    self.command_list.append(fi_str)
            elif stmt[0:4] == 'done':
                fi_str = stmt[4:]
                self.command_list.append('done')
                if fi_str.split(':')[1][0:2] == 'if':
                    point = 0
                    while fi_str[point] != '(':
                        point += 1  
                    avl = 1
                    point += 1
                    while avl != 0:
                        if fi_str[point] == '(':
                            avl += 1
                            point += 1
                        elif fi_str[point] == ')':
                            avl = avl - 1
                            point += 1
                        else:
                            point += 1
                    self.command_list.append('if_stmt')
                    self.command_list.append(fi_str[:point])
                    self.command_list.append(fi_str[point:])
                elif fi_str.split(':')[1][0:5] == 'while':
                    point = 0
                    while fi_str[point] != '(':
                        point += 1
                    avl = 1
                    point += 1
                    while avl != 0:
                        if fi_str[point] == '(':
                            avl += 1
                            point += 1
                        elif fi_str[point] == ')':
                            avl = avl - 1
                            point += 1
                        else:
                            point += 1
                    self.command_list.append('while_stmt')
                    self.command_list.append(fi_str[:point])
                    self.command_list.append(fi_str[point:])
                else:
                    self.command_list.append(fi_str)
            elif stmt.split(':')[1][0:2] == 'if':
                point = 0
                while stmt[point] != '(':
                    point += 1  
                avl = 1
                point += 1
                while avl != 0:
                    if stmt[point] == '(':
                        avl += 1
                        point += 1
                    elif stmt[point] == ')':
                        avl = avl - 1
                        point += 1
                    else:
                        point += 1
                self.command_list.append('if_stmt')
                self.command_list.append(stmt[:point])
                self.command_list.append(stmt[point:])
            elif stmt.split(':')[1][0:5] == 'while':
                point = 0
                while stmt[point] != '(':
                    point += 1
                avl = 1
                point += 1
                while avl != 0:
                    if stmt[point] == '(':
                        avl += 1
                        point += 1
                    elif stmt[point] == ')':

                        avl = avl - 1
                        point += 1
                    else:
                        point += 1
                self.command_list.append('while_stmt')
                self.command_list.append(stmt[:point])
                self.command_list.append(stmt[point:])  
            else:
                self.command_list.append(stmt)
        #print (self.command_list)              
        
    def evaluate(self):
        point = 0
        while point < len(self.command_list):
            if self.command_list[point] == 'if_stmt':
                point += 1
                if_condition = self.command_list[point].split(':')[1][2:]
                if eval(expr(if_condition)):
                    point += 1
                    while self.command_list[point] != 'fi':
                        if self.command_list[point].split(':')[1] == 'pass':
                            point +=1
                        elif self.command_list[point].split(':')[1][0:6] == 'return':
                            stmt = self.command_list[point].split(':')[1][6:]
                            #print ('aaa',stmt)
                            return (eval(expr(stmt)))
                        else:
                            stmt = self.command_list[point].split(':')[1]
                            expa = stmt.split('=')[0]
                            self.vec_dic[expa] = eval(expr(stmt.split('=')[1]))
                            point += 1
                    point += 1
                else:
                    while self.command_list[point] != 'fi': point += 1
                    point += 1
            elif self.command_list[point] == 'while_stmt':
                point += 1
                time = 0
                while_condition = self.command_list[point].split(':')[1][5:]
                while time < 50 and eval(expr(self.command_list[point].split(':')[1][5:])):
                    time += 1
                    i = point + 1
                    while self.command_list[i] != 'done':
                        if self.command_list[i].split(':')[1] == 'pass':
                            i +=1
                        elif self.command_list[i].split(':')[1].find('return') == 0:
                            stmt = self.command_list[i].split(':')[1][6:]
                            return (eval(expr(stmt)))
                        else:
                            #print(self.command_list[i])
                            stmt = self.command_list[i].split(':')[1]
                            expa = stmt.split('=')[0]
                            self.vec_dic[expa] = eval(expr(stmt.split('=')[1]))
                            i += 1
                if time == 50: return 'infinite'
                while self.command_list[point] != 'done': point += 1
                point += 1
            elif self.command_list[point].split(':')[1][0:6] == 'return':
                stmt = self.command_list[point].split(':')[1][6:]
                return (eval(expr(stmt)))
            elif self.command_list[point].split(':')[1] == 'pass':
                point += 1
            else:
                stmt = self.command_list[point].split(':')[1]
                expa = stmt.split('=')[0]
                self.vec_dic[expa] = eval(expr(stmt.split('=')[1]))
                point += 1
                
    def getCFG(self):
        point = 0
        stack = []
        while point < len(self.command_list):
            if self.command_list[point] == 'if_stmt':
                point += 1
                stack.append(self.command_list[point].split(':')[0]+':if')
                self.node_list.append(stack)
                stack = []
                point += 1
                while self.command_list[point] != 'fi':
                    stack.append(self.command_list[point].split(':')[0])
                    point += 1
                self.node_list.append(stack)
                stack =[]
                point += 1
            elif self.command_list[point] == 'while_stmt':
                point += 1
                self.node_list.append(stack)
                stack = []
                stack.append(self.command_list[point].split(':')[0]+':while')
                self.node_list.append(stack)
                point += 1
                stack =[]
                while self.command_list[point] != 'done':
                    stack.append(self.command_list[point].split(':')[0])
                    point += 1
                self.node_list.append(stack)
                stack = []
                point += 1
            else:
                stack.append(self.command_list[point].split(':')[0])
                point += 1
        if stack != None: self.node_list.append(stack)

        nodelen = len(self.node_list)
        point = 0
        while point < nodelen:
            if self.node_list[point][-1].find(':if') != -1:
                edge1 = self.node_list[point][0]
                edge2 = self.node_list[point + 1][0]
                if point + 2 < nodelen:
                    edge3 = self.node_list[point + 2][0]                
                    self.edges.append([edge1,edge2])
                    self.edges.append([edge1,edge3])
                    self.edges.append([edge2,edge3])
                else:
                    self.edges.append([edge1,edge2])
                point += 2
            elif self.node_list[point][0].find(':while') != -1:
                edge1 = self.node_list[point][0]
                edge2 = self.node_list[point + 1][0]
                if point + 2 < nodelen:
                    edge3 = self.node_list[point + 2][0]
                    self.edges.append([edge1,edge2])
                    self.edges.append([edge1,edge3])
                    self.edges.append([edge2,edge1])
                else:
                    self.edges.append([edge1,edge2])
                    self.edges.append( [edge2,edge1])
                point += 2
            else:
                edge1 = self.node_list[point][0]
                if point + 1 < nodelen:
                    edge2 = self.node_list[point + 1][0]
                    self.edges.append([edge1,edge2])
                point += 1
            #print (self.edges)
        first_node = []
        for i in range(nodelen):
            first_node.append(self.node_list[i][0])
        first_node.sort()
        #print (first_node)
        for i in range(nodelen):
            self.CFG.append([])
            for j in range(nodelen):
                if [first_node[i],first_node[j]] in (self.edges):
                    self.CFG[i].append(1)
                else:
                    self.CFG[i].append(0)
        StaString = '['
        for i in range(len(self.CFG)):
            for j in range(len(self.CFG[i])):
                StaString = StaString + str(self.CFG[i][j]) + ','
            StaString = StaString.rstrip(',') + ';'
        StaString = StaString.rstrip(';') + ']'
        return StaString

def expr(s):
    i = 0
    condi = ''
    s = '('+s+')'
    length = len(s)
    #print (s)
    while i < length:
        if s[i] == '(' or s[i] ==')' or s[i] =='&' or s[i] =='|' or s[i] =='!': 
            condi = condi + s[i]
            i += 1 
        else:
            j = i
            while s[j] !=')' and s[j] != '&' and s[j] !='|' and s[j] !='!' : j += 1
            if s[i:j] == 'True':
                condi = condi + 'True'
            elif s[i:j] == 'False':
                condi  = condi + 'False'
            else:
                condi = condi + 'self.vec_dic[' + "'" + s[i:j] + "'" + ']'
            i = j
    condi = condi.replace('&',' and ').replace('|',' or ').replace('!',' not ')
    #print (condi)
    return condi



s="""
    bool x = True;
    bool y = False;
    bool z = True;
    bool a = True;
    bool i = True;
    bool l = True;
    main()
    {
    1:  i= !y;
    2:  z= !x;
    3:  if ( (x & y) | (! z) )
    4:    y= !y;
    5:    pass;
        fi
    6:  x=!y;
    7:  z=!z;
    8:  while ( True)
    9:    a=!y;
    10:  y=!z;
    11:     return x;
        done

    14: return z;
    } 
""" 

p =  program(s)

#print(p.evaluate())
print (p.getCFG())

