from Crypto.Cipher import AES
import random
import base64

class Encrypt:
    def __init__(self):
        self.iv = '0102030405060708'
        self.character = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        self.modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b' \
                       '5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417' \
                       '629ec4ee341f56135fccf695280104e0312ecbda92557c93' \
                       '870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b' \
                       '424d813cfe4875d3e82047b97ddef52741d546b8e289dc69' \
                       '35b3ece0462db0a22b8e7'
        self.nonce = '0CoJUm6Qyw8W8jud'
        self.public_key = '010001'

    def creatRandomBytes(self):
        newCharacter = random.sample(self.character, 16)
        generated_string = ''.join(newCharacter)
        return generated_string

    def getParamsAndSecKey(self, text):
        i = self.creatRandomBytes()
        i='Qc3luhRLNkX8bZ2H'
        input_text = self.pkcs7padding(text)

        encText = self.AESencrypt(input_text, self.nonce)
        encText = self.AESencrypt(encText, i)
        encSecKey = self.RSAencrypt(i, self.public_key, self.modulus)
        from_data = {
            'params': encText,
            'encSecKey': encSecKey
        }
        return from_data

    def AESencrypt(self, data, key):
        data = self.pkcs7padding(data).encode()
        key = key.encode()
        iv = self.iv
        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted = cipher.encrypt(data)
        return base64.b64encode(encrypted).decode()

    def pkcs7padding(self, data):
        # AES.block_size 16位
        bs = AES.block_size
        try:
            length = len(data.encode())
        except:
            length = len(data)
        padding = bs - length % bs
        padding_text = chr(padding) * padding
        return data+padding_text

    def RSAencrypt(self, i, e, n):
        num = pow(int(i[::-1].encode().hex(), 16), int(e, 16), int(n, 16))
        result = format(num, 'x')
        return result


def test():
    pass

if __name__ == '__main__':
    pass
