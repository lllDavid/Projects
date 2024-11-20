import hashlib
import time
from dataclasses import dataclass, field

@dataclass
class Block:
    index: int
    timestamp: str
    data: str
    previous_hash: str
    hash: str = field(init=False)

    def __post_init__(self):
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        block_string = str(self.index) + self.timestamp + self.data + self.previous_hash
        return hashlib.sha256(block_string.encode('utf-8')).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self) -> Block:
        return Block(0, str(time.time()), "Genesis Block", "0")

    def get_latest_block(self) -> Block:
        return self.chain[-1]

    def add_block(self, new_block: Block):
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True


my_blockchain = Blockchain()

new_block_data = "First Block's data"
new_block = Block(1, str(time.time()), new_block_data, my_blockchain.get_latest_block().hash)
my_blockchain.add_block(new_block)

new_block_data = "Second Block's data"
new_block = Block(2, str(time.time()), new_block_data, my_blockchain.get_latest_block().hash)
my_blockchain.add_block(new_block)

for block in my_blockchain.chain:
    print(f"Index: {block.index}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Data: {block.data}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Hash: {block.hash}\n")

if my_blockchain.is_chain_valid():
    print("Blockchain is valid!")
else:
    print("Blockchain is not valid!")
