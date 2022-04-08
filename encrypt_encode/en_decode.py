import base64
import json
import random as r
char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
all = char+num
def replace_all(list1,list2,text):
    output = ""
    for i in text:
        if i in list1:
            char = list1[list2.index(i)]
        else:
            char = i
        output = str(output+char)
    return output

def key_gen(key_type=None):
    char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    all = char+num
    if key_type == None:
        r.shuffle(all)
        return "".join(all)
    if key_type == 0:
        r.shuffle(all)
        return all
    else:
      pass

def encode(text):
    text_bytes = text.encode('ascii')
    base64_bytes = base64.b64encode(text_bytes)
    base64_text = base64_bytes.decode('ascii')
    return base64_text

def decode(text):
    base64_text = text
    base64_bytes = base64_text.encode('ascii')
    text_bytes = base64.b64decode(base64_bytes)
    text = text_bytes.decode('ascii')
    return text

def encrypt(text,key=None):
    char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    all = char+num
    encode_text = encode(text)
    if key == None:
        key_ = key_gen(0)
        encode_text = replace_all(all,key_,encode_text)
        return encode_text,"".join(key_)
    else:
        if type(key) == list:
            key_ = key
        elif type(key) == str:
            key_ = [x for x in key]
        encode_text = replace_all(all,key_,encode_text)
        return encode_text

def decrypt(text,key):
    char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    all = char+num
    key_ = key
    decode_text = replace_all(key_,all,text)
    return decode(decode_text)
