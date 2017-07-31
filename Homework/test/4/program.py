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
        self.s = s
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
                
    def getCFG(self):
        return self.graph

    def evaluate(self):
        self.result = None
        self.origin = self.origin.replace(' ','').replace('bool','').replace('\r','').replace('\t','').replace('&',' and ').replace('!',' not ').replace('|',' or ')
        self.code = self.origin.split('\n')

        pos = 0
        del_pos = []
        for i in range(len(self.code)):
            if self.code[i] == ''or self.code[i] == '{'or self.code[i] == '}'or self.code[i] == 'main()':
                del_pos.append(i - pos)
                pos = pos + 1
        for i in range(len(del_pos)):
            del self.code[del_pos[i]]
        
        for i in range(len(self.code)):
            if 'while' in self.code[i] or 'if' in self.code[i]:
                if 'if' in self.code[i]:
                    self.code[i] = self.code[i].replace('if','if ')
                elif 'while' in self.code[i]:
                    self.code[i] = self.code[i].replace('while','while ')
                self.code[i] = self.code[i].split(':')[-1]
                self.code[i] = self.code[i] + ':'
            elif ':' in self.code[i]:
                self.code[i] = self.code[i].split(':')[-1]
            if 'return' in self.code[i]:
                self.code[i] = self.code[i].replace('return','self.result = ')
        for i in range(len(self.code)):
            self.code[i] = self.code[i] + '\n'
        # print(self.code)
        
        start = None
        end = None
        for i in range(len(self.code)):
            if 'if' in self.code[i]:
                start = i
            if 'fi' in self.code[i]:
                end = i
                run = self.code[start+1:end]
                for j in range(len(run)):
                    run[j] = '\t' + run[j]
                self.code[start+1:end] = run
        
        start = None
        end = None        
        for i in range(len(self.code)):
            if 'while' in self.code[i]:
                start = i
            if 'done' in self.code[i]:
                end = i
                run = self.code[start+1:end]
                for j in range(len(run)):
                    run[j] = '\t' + run[j]
                self.code[start+1:end] = run
        # print(self.code)

        self.c = ''.join(self.code)

        for i in range(len(self.code)):
            if 'if' in self.code[i]:
                start = i
            if 'fi' in self.code[i]:
                end = i
                run = self.code[start+1:end]
                # print(run)
                for j in range(len(run)):
                    run[j] = '\t' + run[j]
                    # print(run[j])
                self.code[start+1:end] = run
                i = end + 1
        for i in range(len(self.code)):
            if 'while' in self.code[i]:
                start = i
            if 'done' in self.code[i]:
                end = i
                self.code.insert(end+1,'\tk = k + 1\n\tif k>200:\n\t\tbreak;\n\telse:\n\t\tpass;\n')
        if 'while' in ''.join(self.code):
            self.code.insert(1,'global k\nk = 0\n')
        self.code.insert(0,'self.result = 0\n')
        # print(self.code)

        pos = 0
        del_pos = []
        for i in range(len(self.code)):
            if 'fi' in self.code[i] or 'done' in self.code[i]:
                del_pos.append(i-pos)
                pos = pos + 1
        for i in range(len(del_pos)):
            del self.code[del_pos[i]]

        run_f = ''.join(self.code)
        # print(run_f)
        exec(run_f)
        if 'while' in run_f:
            if k <= 200:
                return self.result
            else:
                return 'infinite'
        else:
            return self.result

        
