class Block {
    constructor(index, data, previousHash = '') {
        this.index = index;
        this.timestamp = new Date().toISOString();
        this.data = data;
        this.previousHash = previousHash;
        this.hash = '';
    }

    async calculateHash() {
        this.hash = await sha256(this.index + this.timestamp + this.previousHash + JSON.stringify(this.data));
        return this.hash;
    }
}

class Blockchain {
    constructor() {
        this.chain = [this.createGenesisBlock()];
    }

    createGenesisBlock() {
        return new Block(0, 'Genesis Block', '0');
    }

    getLatestBlock() {
        return this.chain[this.chain.length - 1];
    }

    async addBlock(newBlock) {
        newBlock.previousHash = this.getLatestBlock().hash;
        await newBlock.calculateHash();
        this.chain.push(newBlock);
    }

    async renderBlockchain() {
        const container = document.getElementById('blockchain-container');
        container.innerHTML = '';

        for (const block of this.chain) {
            const blockElement = document.createElement('div');
            blockElement.classList.add('block');

            const blockHeader = document.createElement('div');
            blockHeader.classList.add('block-header');
            blockHeader.textContent = `Block #${block.index}`;

            const blockData = document.createElement('div');
            blockData.classList.add('block-data');
            blockData.textContent = `Data: ${block.data}`;

            const blockHash = document.createElement('div');
            blockHash.classList.add('hash');
            blockHash.textContent = `Hash: ${block.hash}`;

            const blockLink = document.createElement('div');
            blockLink.classList.add('block-link');
            blockLink.textContent = `Previous Hash: ${block.previousHash}`;

            blockElement.appendChild(blockHeader);
            blockElement.appendChild(blockData);
            blockElement.appendChild(blockHash);
            blockElement.appendChild(blockLink);

            container.appendChild(blockElement);
        }
    }
}

async function sha256(message) {
    const crypto = window.crypto
    const msgBuffer = new TextEncoder().encode(message);
    const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    const hashHex = hashArray.map(byte => byte.toString(16).padStart(2, '0')).join('');
    return hashHex;
}

const blockchain = new Blockchain();
blockchain.renderBlockchain();

setInterval(async () => {
    const newBlockData = `Block ${blockchain.chain.length} added at ${new Date().toLocaleTimeString()}`;
    const newBlock = new Block(blockchain.chain.length, newBlockData);
    await blockchain.addBlock(newBlock);
    blockchain.renderBlockchain();
}, 5000); 
