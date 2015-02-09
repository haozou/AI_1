'''
Created on 2013-2-21

@author: Administrator
'''

def magnitudePole(A):
    max = -21474836481
    min = 2147483647
    
    dic1 = {}
    dic2 = {}
    
    for i in range (0,len(A)):
        if A[i] >= max:
            dic1[i] = A[i]
            max = A[i]
    
    for i in range (len(A)-1,-1,-1):
        if A[i] <= min:
            dic2[i] = A[i]
            min = A[i]
    print dic1, dic2    
    for i in range (0,len(A)):
        if dic1.has_key(i) and dic2.has_key(i):
            return i
    
    return -1
def stack_machine_emulator ( S ):
    machine = []
    for s in S:
        if s.isdigit():
            machine.append(s)
        elif s == '+':
            if len(machine) > 1:
                a = machine.pop()
                b = machine.pop()
            else:
                return -1   
            machine.append(int(a)+int(b))
        elif s == '*':
            if len(machine) > 1:
                a = machine.pop()
                b = machine.pop()
            else:
                return -1   
            machine.append(int(a)*int(b))
        else:
            return -1
    
    return machine
if __name__ == '__main__':
    print stack_machine_emulator("11+11+")
    A = [4,2,2,3,1,4,7,8,6,9]
    print magnitudePole(A)
            