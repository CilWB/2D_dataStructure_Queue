class Queue:
    """
╲╲╲╲╲╲╲┏╮┏╮╲╲╲╲╲╲╲╲╲╲╲╲╲╲
╲╲╲╲╲╲╭┛┻┛┻╮╲╲╲╲╲╭━╮╲╲╲╲╲
╲╲╲╲▅━╯0┈0┈┃╲╲╲╲╲╰╮┃╲╲╲╲╲
╲╲╲╲┣━━━━━╯╰━━━━━╮┃┃╲╲╲╲╲
╲╲╲╲╰━━━━┓┈┈┈┈┈┈┈┗╯┃╲╲╲╲╲
╲╲╲╲╲╲╲╲╲┃┏┓┏━┳┳┓┏━╯╲╲╲╲╲
╲╲╲╲╲╲╲╲╲┗┛┗┛ ┗┛┗┛╲╲╲╲╲╲╲
    """

    def __init__(self,l=None):
        if l == None :
            self.items = []
        else:
            self.items = l
    def __str__(self):
        if self.size is None:
            return 0
        else:
            return 'Q size = ' + str(self.size())+' --> '+str(self.items)
    def size(self):
        if self.items == None:
            return 0
        else:
            return len(self.items)
    def enQ(self,data):
        self.items.append(data)
        return data # for easier in function "enCode(message,q)"
    def deQ(self):
        return self.items.pop(0)
    def head(self):
        return self.items[0]
    def tail(self):
        return self.items[-1]

def enCode(message,q): 
    # message: string you want to encode
    # q      : queue of 'Caesar Cipher'   
    q2 = Queue()
    for i in q.items :
        q2.enQ(i)            
    s = ''
    for i in message:
        if i.isalpha():
            base = ord('a' if i.islower() else 'A')-1
            enChar = (ord(i) - base +q2.enQ(q2.deQ()))
            if enChar > 26 :
                enChar -= 26
            s += chr( base + enChar  )
        else:
            s+=i
    return s

def deCode(message,q):
    # message: string you want to decode
    # q      : queue of 'Caesar Cipher'   
    q2 = Queue()
    for i in q.items :
        q2.enQ(i)
    s = ''
    for i in message :
        if i.isalpha():
            base = ord('a' if i.islower() else 'A')-1
            deChar = (ord(i) - base - q2.enQ(q2.deQ()))

            if deChar <= 0 :
                deChar += 26
            s+= chr(base + deChar)
        else:
            s+= i
    return s
if __name__ == '__main__':
    q = Queue([2,5,6,1,8,3])
    s = input('Input your String : ')
    s2 = enCode(s,q)
    print('EnCode  string  =  ',s2)
    print('DeCode  string  =  ',deCode(s2,q))

    ##### uncomment this line for your better coding :D !!!! 
    #print(q.__doc__) 

