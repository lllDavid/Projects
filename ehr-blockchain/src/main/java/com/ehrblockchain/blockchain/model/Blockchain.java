package com.ehrblockchain.blockchain.model;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import org.springframework.stereotype.Component;

import com.ehrblockchain.blockchain.util.HashUtils;

import static com.ehrblockchain.blockchain.util.MerkleUtils.computeBlockHash;

@Component
public class Blockchain {
    // TODO: Persist Blockchain, add actual validator nodes, add validation methods
    // Temporary for easier debugging, Change to Byte Size Limit
    private static final int MAX_TRANSACTIONS_PER_BLOCK = 3;

    private final List<Block> chain = new ArrayList<>();
    private final List<Transaction> pendingTransactions = new ArrayList<>();

    public synchronized void addTransaction(Transaction tx, String validatorId) {
        pendingTransactions.add(tx);
        // System.out.println("Added transaction: " + tx);
        // System.out.println("Pending transactions: " + pendingTransactions.size());

        if (pendingTransactions.size() == MAX_TRANSACTIONS_PER_BLOCK) {
            Block newBlock = createBlockFromPending(validatorId);
            addBlock(newBlock);
        }
    }

    public synchronized Block createBlockFromPending(String validatorId) {
        if (pendingTransactions.isEmpty()) {
            throw new IllegalStateException("No pending transactions to include in a block");
        }

        long index = chain.size();
        String previousHash = chain.isEmpty() ? "GENESIS" : chain.getLast().hash();
        long ts = System.currentTimeMillis();

        List<Transaction> txs = new ArrayList<>(
                pendingTransactions.subList(0, Math.min(pendingTransactions.size(), MAX_TRANSACTIONS_PER_BLOCK))
        );

        String merkleRoot = computeBlockHash(txs);
        String hash = HashUtils.hashData(index, previousHash, ts, merkleRoot, validatorId);

        return new Block(index, previousHash, hash, ts, txs, validatorId);
    }

    public synchronized void addBlock(Block block) {
        chain.add(block);
        // System.out.println(this);
        pendingTransactions.removeAll(block.transactions());
    }

    public synchronized List<Block> getChain() {
        return Collections.unmodifiableList(chain);
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Blockchain {\n");
        for (Block block : chain) {
            sb.append("  Block #").append(block.index()).append(" {\n");
            sb.append("    PreviousHash: ").append(block.previousHash()).append("\n");
            sb.append("    Hash: ").append(block.hash()).append("\n");
            String formattedTimestamp = java.time.Instant.ofEpochMilli(block.timestamp())
                    .atZone(java.time.ZoneId.systemDefault())
                    .toLocalDateTime()
                    .toString();
            sb.append("    Timestamp: ").append(formattedTimestamp).append("\n");

            sb.append("    ValidatorId: ").append(block.validatorId()).append("\n");
            sb.append("    Transactions:\n");
            for (Transaction tx : block.transactions()) {
                sb.append("      - ").append(tx.toString()).append("\n");
            }
            sb.append("  }\n");
        }
        sb.append("}\n");
        return sb.toString();
    }
}