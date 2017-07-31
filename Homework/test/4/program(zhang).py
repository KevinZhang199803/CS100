def quick_sort(a_list):
    quick_sort_helper(a_list, 0, len(a_list) - 1)
    
def quick_sort_helper(a_list, first, last):
    if first < last:
        split_point = partition(a_list, first, last)
        quick_sort_helper(a_list, first, split_point - 1)
        quick_sort_helper(a_list, split_point + 1, last)
        
def partition(a_list, first, last):
    pivot_value = a_list[first]
    left_mark = first + 1
    right_mark = last
    done = False
    while not done:
        while left_mark <= right_mark and a_list[left_mark] <= pivot_value:
            left_mark = left_mark + 1
        while a_list[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1
        if right_mark < left_mark:
            done = True
        else:
            temp = a_list[left_mark]
            a_list[left_mark] = a_list[right_mark]
            a_list[right_mark] = temp
    temp = a_list[first]
    a_list[first] = a_list[right_mark]
    a_list[right_mark] = temp
    return right_mark

def change2str(std):# turn a list matrix into a string matrix
    matrix_str = ''
    for i in range(len(std)):
        element = str(std[i]).replace('(','').replace(')','').replace(' ','').strip('[').strip(']')
        matrix_str = matrix_str + element + ';'
    matrix_str = '[' + matrix_str.rstrip(';') + ']'
    return matrix_str

class program:
    
    def __init__(self,s):
        self.origin = s.replace('\t','')
        self.code = self.origin.split('\n')
        for i in range(len(self.code)):
            self.code[i] = self.code[i].replace(' ','').rstrip(';')
        del_pos = []
        count = 0
        for i in range(len(self.code)):
            if self.code[i] == '':
                del_pos.append(i - count)
                count = count + 1
        for i in range(len(del_pos)):
            del self.code[del_pos[i]]
            
        # First, type in all the variables
        position = 0
        for i in range(len(self.code)):
            if self.code[i] == 'main()':
                position = i
        start = ''
        for i in range(position):
            self.code[i] = self.code[i].lstrip('bool')
            start = start + self.code[i] + '\n'

        # Second, divide every part
        div_part = []
        position = 0
        for i in range(len(self.code)):
            if self.code[i] == 'main()':
                position = i + 2
        while position <= len(self.code) - 1:
            if 'while' in self.code[position]:
                i = position
                while '{' not in self.code[i] and 'fi' not in self.code[i] and 'done' not in self.code[i]:
                    i = i - 1
                position_start = i + 1
                element = []
                if position_start != position:
                    element.append(self.code[position_start:position])
                    div_part.append(element)
                
                i = position
                element = []
                element.append([self.code[i]])
                element.append('while')
                div_part.append(element)

                i = position + 1
                while 'done' not in self.code[i]:
                    i = i + 1
                position_end = i
                element = []
                element.append(self.code[position + 1:position_end])
                div_part.append(element)
                position = position_end + 1
                
            elif 'if' in self.code[position]:
                i = position
                while '{' not in self.code[i] and 'fi' not in self.code[i] and 'done' not in self.code[i]:
                    i = i - 1
                position_start = i + 1
                element = []
                element.append(self.code[position_start:position + 1])
                element.append('if')
                div_part.append(element)

                i = position
                while 'fi' not in self.code[i]:
                    i = i + 1
                position_end = i
                element = []
                element.append(self.code[position + 1:position_end])
                div_part.append(element)
                position = position_end + 1

            else:
                position = position + 1
                if position == len(self.code) - 1:
                    while '{' not in self.code[i] and 'fi' not in self.code[i] and 'done' not in self.code[i]:
                        i = i - 1
                    position_start = i + 1
                    element = []
                    element.append(self.code[position_start:position])
                    div_part.append(element)
        
        # Third, draw CFG
        for i in range(len(div_part)):
            pos = div_part[i][0][0].find(':')
            num = div_part[i][0][0][0:pos]
            div_part[i].append(num)
        
        # draw each route in the graph, stored in the list 'connection'
        connection =[]
        for i in range(len(div_part) - 1):
            connection.append([div_part[i][-1],div_part[i+1][-1]])
        for i in range(len(div_part)):
            if 'if' in div_part[i]:
                if i <= len(div_part) - 3:
                    connection.append([div_part[i][-1],div_part[i+2][-1]])
            elif 'while' in div_part[i]:
                if i <= len(div_part) - 3:
                    connection.append([div_part[i][-1],div_part[i+2][-1]])
                    connection.append([div_part[i+1][-1],div_part[i][-1]])
                    pos = 0
                    for k in range(len(connection)):
                        if connection[k] == [div_part[i+1][-1],div_part[i+2][-1]]:
                            pos = k
                    del connection[pos]
                else:
                    connection.append([div_part[i+1][-1],div_part[i][-1]])
        
        # change the list into the graph matrix
        graph = [[0 for x in range(len(div_part))] for y in range(len(div_part))]
        num = []
        for i in range(len(div_part)):
            num.append(div_part[i][-1])
        quick_sort(num)
        rank = {}
        for i in range(len(num)):
            rank[num[i]] = i
        for i in range(len(connection)):
            graph[rank[connection[i][0]]][rank[connection[i][1]]] = 1
        self.graph = change2str(graph)
        print (self.code)
                
    def getCFG(self):
        return self.graph

    def evaluate(self):
        pos = 0
        for i in range(len(self.code)):
            self.code[i] = self.code[i].split(':')[-1]
        for i in range(len(self.code)):
            if self.code[i] == 'main()':
                pos = i
                break
        start = self.code[0:pos]
        var = {}
        var_name = []
        for i in range(len(start)):
            div = start[i].split('=')
            var_name.append(div[0])
            var[div[0]] = 'self.' + div[0]
            div[0] = 'self.' + div[0]
            start[i] = div[0] + '=' + div[1]
            exec(start[i])

        for i in range(len(self.code)):
            if self.code[i] == '{':
                pos = i
                break
        run = self.code[i+1:-1]

        for i in range(len(run)):
            if '=' in run[i]:
                mid = run[i].split('=')
                mid[0] = var[mid[0]]
                mid[1] = '(' + mid[1] + ')'
                j = 0
                start = 0
                first = True
                while j <= len(mid[1]) - 1:
                    if first:
                        if mid[1][j] == '(' or mid[1][j] == ')' or mid[1][j] == '|' or mid[1][j] == '&':
                            j = j + 1
                        else:
                            first = False
                            start = j
                            j = j + 1
                    else:
                        if mid[1][j] != '(' and mid[1][j] != ')' and mid[1][j] != '|' and mid[1][j] != '&':
                            j = j + 1
                        else:
                            first = True
                            var_a = mid[1][start:j]
                            if var_a == 'True' or var_a == 'False':
                                j = j + 1
                            elif '!' in var_a:
                                var_b = var_a.split('!')[-1]
                                var_a = '!' + var[var_b]
                                pre = mid[1][:start]
                                post = mid[1][j:]
                                mid[1] = pre + var_a + post
                                j = len(pre) + len(var_a)
                            else:
                                pre = mid[1][:start]
                                post = mid[1][j:]
                                mid[1] = pre + var[var_a] + post
                                j = len(pre) + len(var[var_a])
                
                run[i] = mid[0] + '=' + mid[1]
            elif 'if' in run[i]:
                j = 2
                start = 2
                first = True
                while j <= len(run[i]) - 1:
                    if first:
                        if run[i][j] == '(' or run[i][j] == ')' or run[i][j] == '|' or run[i][j] == '&':
                            j = j + 1
                        else:
                            first = False
                            start = j
                            j = j + 1
                    else:
                        if run[i][j] != '(' and run[i][j] != ')' and run[i][j] != '|' and run[i][j] != '&':
                            j = j + 1
                        else:
                            first = True
                            var_a = run[i][start:j]
                            if var_a == 'True' or var_a == 'False':
                                j = j + 1
                            elif '!' in var_a:
                                var_b = var_a.split('!')[-1]
                                var_a = '!' + var[var_b]
                                pre = run[i][:start]
                                post = run[i][j:]
                                run[i] = pre + var_a + post
                                j = len(pre) + len(var_a)
                            else:
                                pre = run[i][:start]
                                post = run[i][j:]
                                run[i] = pre + var[var_a] + post
                                j = len(pre) + len(var[var_a])
                run[i] = 'if ' + run[i][2:] + ':'
            elif 'while' in run[i]:
                j = 5
                start = 5
                first = True
                while j <= len(run[i]) - 1:
                    if first:
                        if run[i][j] == '(' or run[i][j] == ')' or run[i][j] == '|' or run[i][j] == '&':
                            j = j + 1
                        else:
                            first = False
                            start = j
                            j = j + 1
                    else:
                        if run[i][j] != '(' and run[i][j] != ')' and run[i][j] != '|' and run[i][j] != '&':
                            j = j + 1
                        else:
                            first = True
                            var_a = run[i][start:j]
                            if var_a == 'True' or var_a == 'False':
                                j = j + 1
                            elif '!' in var_a:
                                var_b = var_a.split('!')[-1]
                                var_a = '!' + var[var_b]
                                pre = run[i][:start]
                                post = run[i][j:]
                                run[i] = pre + var_a + post
                                j = len(pre) + len(var_a)
                            else:
                                pre = run[i][:start]
                                post = run[i][j:]
                                run[i] = pre + var[var_a] + post
                                j = len(pre) + len(var[var_a])
                run[i] = 'while ' + run[i][5:] + ':'
            elif 'return' in run[i]:
                var_a = run[i][6:]
                var_a = '(' + var_a + ')'
                j = 0
                start = 0
                first = True
                while j <= len(var_a) - 1:
                    if first:
                        if var_a[j] == '(' or var_a[j] == ')' or var_a[j] == '|' or var_a[j] == '&':
                            j = j + 1
                        else:
                            first = False
                            start = j
                            j = j + 1
                    else:
                        if var_a[j] != '(' and var_a[j] != ')' and var_a[j] != '|' and var_a[j] != '&':
                            j = j + 1
                        else:
                            first = True
                            var_aa = var_a[start:j]
                            if var_aa == 'True' or var_aa == 'False':
                                j = j + 1
                            elif '!' in var_aa:
                                var_b = var_aa.split('!')[-1]
                                var_aa = '!' + var[var_b]
                                pre = var_a[:start]
                                post = var_a[j:]
                                var_a = pre + var_aa + post
                                j = len(pre) + len(var_aa)
                            else:
                                pre = var_a[:start]
                                post = var_a[j:]
                                var_a = pre + var[var_aa] + post
                                j = len(pre) + len(var[var_aa])
                run[i] = 'return ' + var_a

        for i in range(len(run)):
            run[i] = run[i].replace('!',' not ').replace('|',' or ').replace('&',' and ')
            
        point = 0
        self.result = 0
        while point <= len(run) - 1:
            if 'if' in run[point]:
                i = point + 1
                while run[i] != 'fi':
                    i = i + 1
                code_r = run[point] + '\n'
                code_rl = run[point+1:i]
                pos = 0
                a = True
                for k in range(len(code_rl)):
                    if 'return' in code_rl[k]:
                        pos = k
                        a = False
                        break
                if a:
                    for j in range(len(code_rl)):
                        code_r = code_r + '    ' + code_rl[j] + '\n'
                    exec(code_r)
                    point = i + 1
                else:
                    jud = code_r.strip('\n')[2:]
                    jud2 = eval(jud.strip(':'))
                    if jud2:
                        final = code_rl[pos]
                        code_rl = code_rl[:pos]
                        for j in range(len(code_rl)):
                            code_r = code_r + '    ' + code_rl[j] + '\n'
                        exec(code_r)
                        self.result = eval(final.lstrip('return '))
                        break
                    else:
                        point = i + 1
            elif 'while' in run[point]:
                i = point + 1
                while run[i] != 'done':
                    i = i + 1
                code_r = run[point] + '\n'
                code_rl = run[point+1:i]
                pos = 0
                a = True
                for k in range(len(code_rl)):
                    if 'return' in code_rl[k]:
                        pos = k
                        a = False
                        break
                if a:
                    for j in range(len(code_rl)):
                        code_r = code_r + '    ' + code_rl[j] + '\n'
                    self.counting = 0
                    code_r = code_r + '    self.counting = self.counting + 1\n    if (self.counting >= 100):\n        break\n'
                    exec(code_r)
                    if self.counting >= 100:
                        self.result = 'infinite'
                        break
                    point = i + 1
                else:
                    jud = code_r.strip('\n')[5:]
                    jud2 = eval(jud.strip(':'))
                    if jud2:
                        final = code_rl[pos]
                        code_rl = code_rl[:pos]
                        code_r = code_r.replace('while ','if ')
                        for j in range(len(code_rl)):
                            code_r = code_r + '    ' + code_rl[j] + '\n'
                        exec(code_r)
                        self.result = eval(final.lstrip('return '))
                        break
                    else:
                        point = i + 1
            elif 'return' in run[point]:
                self.result = eval(run[point].lstrip('return '))
                break
            else:
                exec(run[point])
                point = point + 1    

        return self.result

s="""
    bool x = True;
    bool y = False;
    bool z = True;
    bool a = True;
    main()
    {
    1:  x= True;
    2:  z= !x;
    3:  if ( (x & y) | (! z) )
    4:      y= !y;
    5:      pass;
        fi
    8:  while (True)
    6:  x=!y;
    7:  z=!z;
    11: return x;
    12: x=True;
        done
    } 
"""
p = program(s)
p.evaluate()
