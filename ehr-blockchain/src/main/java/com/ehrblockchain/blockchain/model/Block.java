package com.ehrblockchain.blockchain.model;

import java.util.List;

/**
 * Represents a block in the blockchain
 *
 * @param index        The position of this block in the chain
 * @param previousHash The hash of the previous block in the chain
 * @param hash         The hash of this block (computed from index + previousHash + timestamp + merkle root of all transaction hashes + validatorId)
 * @param timestamp    Epoch time in milliseconds when the block was created
 * @param transactions List of transactions included in this block
 * @param validatorId  Identifier of the validator who signed this block
 */
public record Block(long index, String previousHash, String hash, long timestamp, List<Transaction> transactions,
                    String validatorId) {
}