import hashlib

def mine_block(difficulty):
    nonce = 0
    while True:
        hash_value = hashlib.sha256(str(nonce).encode()).hexdigest()
        if hash_value[:difficulty] == '0' * difficulty:
            return nonce, hash_value
        nonce += 1

# Эксперимент: Майнинг с difficulty=4
difficulty = 4
nonce, hash_value = mine_block(difficulty)
print(f"Найден nonce: {nonce}, Хэш: {hash_value}")
