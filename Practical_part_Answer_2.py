import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        print("Mining block with difficulty =", difficulty)
        start_time = time.time()

        prefix_str = "0" * difficulty
        while not self.hash.startswith(prefix_str):
            self.nonce += 1
            self.hash = self.compute_hash()

        end_time = time.time()
        print("\nBlock mined successfully!")
        print("Nonce:", self.nonce)
        print("Hash:", self.hash)
        print("Time taken:", round(end_time - start_time, 4), "seconds")

# Run the block mining
if __name__ == "__main__":
    difficulty = 4
    block = Block(1, time.time(), "Transaction A -> B", "0")
    block.mine_block(difficulty)
