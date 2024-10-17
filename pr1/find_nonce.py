import hashlib

def find_nonce(origin: str, difficulty: int, find_sym: str = '0'):
    nonce = 0
    find_nonce = find_sym * difficulty

    while True:
        new_orig = (origin + str(nonce)).encode()
        hash = hashlib.sha256(new_orig).hexdigest()

        if hash[:difficulty] == find_nonce:
            return nonce
        
        nonce += 1

def main():
    name = "Иван"

    for i in range(1, 8):
        nonce = find_nonce(name, i)
        hash = hashlib.sha256((name + str(nonce)).encode())

        print(nonce, hash.hexdigest())

if __name__ == "__main__":
    main()