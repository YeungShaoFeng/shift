import hashlib
import random as rdm


class shiftIt:
    def __init__(self, plainText, password):
        self.password = password
        self.plainText = plainText
        self.cipherText = ''
        self.password_hash_value = ''
        self.palinText_hash_value = ''
        self.judger = 0
        self.lengths = {'plainText' : 0, 'password' : 0, 'plainText_hash' : 0, 'password_hash' : 0}
        self.boundList, self.mode = [], []


    def hasher(text):
        hash_object = hashlib.sha512(text.encode('utf-8'))
        hex_digt = hash_object.hexdigest()
        print(f"hash_text: {hex_digt}")
        return hex_digt


    def tailbonder(plainText, lengths):
        plainText += chr(lengths['plainText'])
        a = len(plainText) % lengths['password_hash']
        if (a):
            a = lengths['password_hash'] * 120 - a
            plainText += shiftIt.tailboundmaker(a)
        
        return plainText


    def tailboundmaker(a):
        tailList = [0] * a
        for i in range(a):
            tailList[i] = chr(rdm.randint(32, 126))
        return ''.join(tailList)


    def separate(text, lengths):
        boundList = []
        for i in range(lengths['plainText']//lengths['password_hash']):
            boundList.append(''.join(text[0:lengths['password_hash']-1]))
            text = text[lengths['password_hash']-1:]
        return boundList


    def summup(string, length):
        string = list(string)
        def passowrd_hash_sum(string, summy):
            for i in range(len(string)):
                summy += ord(string[i])
            return summy
        mode = []
        summy = length
        summy += passowrd_hash_sum(string, summy)
        for i in range(len(string)):
            mode.append(summy%ord(string[i]))
        return mode
    
    
    def preShift(plainText, shiftNum):
        plainText = list(plainText)
        for i in range(len(plainText)):
            plainText[i] = chr((ord(plainText[i])+shiftNum)%128)
        return plainText

    def inserter(self):
        password_hash_value = list(self.password_hash_value)
        # plainText = list(self.plainText)
        for i in range(len(self.mode)):
            self.mode[i] = chr(self.mode[i])

        for i in range(len(self.boundList)):
            tmp = list(self.boundList[i])
            tmp.insert(ord(password_hash_value[i]), self.mode[i])
            self.boundList[i] = ''.join(tmp)
        return


    def updateData(self):
        self.password_hash_value = shiftIt.hasher(self.password)
        self.palinText_hash_value = shiftIt.hasher(self.plainText)
        self.lengths['plainText'] = len(self.plainText)
        self.lengths['password'] = len(self.password)
        self.lengths['plainTxt_hash'] = len(self.palinText_hash_value)
        self.lengths['password_hash'] = len(self.password_hash_value)
        return


    def go(self):
        shiftIt.updateData(self)
        preShift(self.plainText, shiftIt.summup.passowrd_hash_sum(self.password_hash_value))
        self.plainText = shiftIt.tailbonder(self.plainText, self.lengths)
        self.mode = shiftIt.summup(self.password_hash_value, self.lengths['plainText'])
        self.lengths['plainText'] = len(self.plainText)
        self.boundList = shiftIt.separate(list(self.plainText), self.lengths)
        shiftIt.inserter(self)


plainText = input("plainText: ")
password = input("password: ")
shiftIt_obj = shiftIt(plainText, password)

shiftIt_obj.go()

print(shiftIt_obj.plainText)
print(len(shiftIt_obj.plainText))
print(shiftIt_obj.boundList)
print(len(shiftIt_obj.boundList[0]))
print(shiftIt_obj.mode)
print(len(shiftIt_obj.mode))
print()
