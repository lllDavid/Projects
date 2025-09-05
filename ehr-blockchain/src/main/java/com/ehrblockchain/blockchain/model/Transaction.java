package com.ehrblockchain.blockchain.model;

import java.util.UUID;

/**
 * Represents a blockchain transaction for a patients health record
 *
 * @param transactionId Unique identifier for this transaction (UUID)
 * @param patientId     The ID of the patient this transaction relates to
 * @param action        The action performed (e.g., "readRecord", "writeRecord", "deleteRecord")
 * @param actorId       The ID of the user performing the action
 * @param hash          The merkle root hash of the associated HealthRecords lists
 * @param timestamp     Epoch time in milliseconds when the transaction was created
 * @param signature     Digital signature of the actor, or "unsigned" if not signed
 */
public record Transaction(UUID transactionId, long patientId, String action, long actorId, String hash,
                          long timestamp, String signature) {
}