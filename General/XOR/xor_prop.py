a = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
ba = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
bc = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
kacb = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"
a = list(bin(int(a, 16))[2:])
ba = list(bin(int(ba, 16))[2:])
bc = list(bin(int(bc, 16))[2:])
kacb = list(bin(int(kacb, 16))[2:])


# adding zeros infront of string


def addZeros(str1, str2):
    diff1 = len(str1)-len(str2)
    if diff1 > 0:
        for i in range(diff1):
            str2.insert(i, '0')
    elif diff1 < 0:
        for i in range(-diff1):
            str1.insert(i, '0')
    else:
        pass

# calcualting xor values


def xor_calc(str1, str2):
    str3 = ""
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            str3 += "0"
        else:
            str3 += "1"
    return str3


addZeros(a, ba)
b = xor_calc(a, ba)
addZeros(b, bc)
c = xor_calc(b, bc)
addZeros(b, kacb)
k1 = xor_calc(b, kacb)
addZeros(k1, c)
k2 = xor_calc(k1, c)
addZeros(a, k2)
k3 = xor_calc(k2, a)
print(k3)
