import rsa

class Human():
    _pub_key: rsa.PublicKey
    _private_key: rsa.PrivateKey

    def __init__(self):
        self._pub_key, self._private_key = rsa.newkeys(512)
    
    def get_public_key(self) -> rsa.PublicKey:
        return self._pub_key
    
    def write_message(self, msg: str, pub_key: rsa.PublicKey) -> bytes:
        message = rsa.encrypt(msg.encode(), pub_key)
        sign = rsa.sign(message, self._private_key, "SHA-256")

        return message, sign
    
    def read_message(self, msg: bytes, sign: bytes, pub_key: bytes):
        res = rsa.decrypt(msg, self._private_key).decode()

        try:
            rsa.verify(msg, sign, pub_key)
        except:
            return res, False
        
        return res, True

def main():
    alice = Human()
    bob = Human()

    msg, sign = alice.write_message("Привет друг!", bob.get_public_key())

    print(bob.read_message(msg, sign, alice.get_public_key()))

    print(bob.read_message(msg, sign, alice._private_key)) # Используется приватный ключ алисы

    print(bob.read_message(msg, sign, bob.get_public_key())) # Использован не правильный ключ
    print(bob.read_message(b"t3qewyrtjdk", sign, alice.get_public_key())) # Не то сообщение
    print(bob.read_message(msg, b"sign", alice.get_public_key())) # не та подпись

if __name__ == "__main__":
    main()