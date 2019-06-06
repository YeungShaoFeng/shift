import hashlib


def hasher(text):
    hash_object = hashlib.sha512(text.encode('utf-8'))
    hex_digt = hash_object.hexdigest()
    print(f"hash_text: {hex_digt}")
    return hex_digt



# qq = []
text = "hello, World!"
a = hasher(text)
print(len(a))
# a = list(a)
# summy = len(text)
# for i in range(len(a)):
#     summy += ord(a[i])
# for i in range(len(a)):
#     qq.append(summy%ord(a[i]))
# # qq.sort()
# print(qq)

# ff = 95
# lista = [0] * ff
# for i in range(ff):
#     lista[i] = chr(i+32)
# print(lista)

# a = '912ec803b2ce49e4a541068d495ab570'
# a = list(a)
# print(a[16:0])
# a = '912ec803b2ce49e4a541068d495ab570'
# if ('4a54' in a):
#     print('4a54')