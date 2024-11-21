import hashlib
import json
from datetime import datetime

# Block class to represent a single block in the blockchain
class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

    def to_dict(self):
        return {
            "index": self.index,
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "data": self.data,
            "hash": self.hash
        }

# Blockchain class to manage the chain
class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        # Create the first block (genesis block)
        genesis_block = Block(0, "0", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Genesis Block", self.hash_block("0", "Genesis Block"))
        self.chain.append(genesis_block)

    def hash_block(self, previous_hash, data):
        # Simple hash function to hash block data
        block_string = json.dumps({"previous_hash": previous_hash, "data": data}, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def add_block(self, data):
        last_block = self.chain[-1]
        new_index = last_block.index + 1
        new_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_hash = self.hash_block(last_block.hash, data)
        new_block = Block(new_index, last_block.hash, new_timestamp, data, new_hash)
        self.chain.append(new_block)

    def get_chain(self):
        return [block.to_dict() for block in self.chain]

