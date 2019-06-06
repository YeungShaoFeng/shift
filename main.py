import hashlib


class shiftIt:
    def __init__(self, password, plainText):
        self.password = password
        self.plainText = plainText
        self.cipherText = ''
        self.hash_value = ''
        self.judger = 0


    def shift(self):
        password = list(self.password)
        plainText = list(self.plainText)
        for i in range(len(plainText)):
            plainText[i] = chr(ord(plainText[i])*2 % 255)
        print(plainText)
        plainText = ''.join(plainText)
        return plainText
    

    def shifUp(self):
        password = list(self.password)
        plainText = list(self.plainText)
        for j in range(len(password)):
            for i in range(len(plainText)):
                plainText[i] = chr(ord(plainText[i])*2 % 255)
            print(plainText)
        plainText = ''.join(plainText)
        return plainText

    def unshift(self):
        cipherText = list(self.plainText)
        for i in range(len(cipherText)):
            if(ord(cipherText[i])%2==0):
                cipherText[i] = chr(ord(cipherText[i])//2)
            else:
                cipherText[i] = chr((ord(cipherText[i])+255)//2)
        print(cipherText)
        cipherText = ''.join(cipherText)
        return cipherText

    def hasher(text):
        hash_object = hashlib.sha256(text.encode('utf-8'))
        hex_digt = hash_object.hexdigest()
        print(f"hash_text: {hex_digt}")
        return hex_digt

    def passwordChecker(self):
        password_hash = hasher(self.password)
        return password


    def lengthJudge(a, b):
        len_a = len(a)
        len_b = len(b)
        if (len_a > len_b):
            judger = len_a - len_b
        elif(len_a == len_b):
            judger = 0
        else:
            judger = len_a - len_b
        return  judger


    def shiftIn(self):
        self.hash_value = hasher(self.password)
        self.cipherText = shift(self)
        self.judger = lengthJudge(password, plainText)
        if (self.judger > 0):
            shifUp(self)
        elif(self.judger < 0):
            shiftDown(self)
        else:
            shift(self)






plainText = input("plainText: ")
password = input("password: ")
shiftIt_obj = shiftIt(plainText, password)

print(shiftIt_obj.shift())
print(shiftIt_obj.unshift())



# yuanli

#print(f"i\ti*2\ti*2%255")
#for i in range(256):
#    print(f"{i}\t{i*2}\t{i*2%255}")
