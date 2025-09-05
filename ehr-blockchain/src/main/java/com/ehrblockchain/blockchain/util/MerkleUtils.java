package com.ehrblockchain.blockchain.util;

import java.util.ArrayList;
import java.util.List;

import com.ehrblockchain.blockchain.model.MerkleTree;
import com.ehrblockchain.blockchain.model.MerkleTreeNode;
import com.ehrblockchain.blockchain.model.Transaction;
import com.ehrblockchain.healthrecord.dto.HealthRecordDTO;

public class MerkleUtils {
    private MerkleUtils() {
    }

    public static List<Object> flattenHealthRecord(HealthRecordDTO recordDTO) {
        List<Object> leaves = new ArrayList<>();
        leaves.addAll(recordDTO.diagnoses());
        leaves.addAll(recordDTO.notes());
        leaves.addAll(recordDTO.treatmentPlans());
        leaves.addAll(recordDTO.prescriptions());
        leaves.addAll(recordDTO.vitals());
        leaves.addAll(recordDTO.cbcTests());
        leaves.addAll(recordDTO.allergies());
        leaves.addAll(recordDTO.labResults());
        leaves.addAll(recordDTO.immunizations());
        leaves.addAll(recordDTO.medicalHistory());
        leaves.addAll(recordDTO.familyHistory());
        leaves.addAll(recordDTO.encounters());
        leaves.addAll(recordDTO.procedures());

        return leaves;
    }

    public static String computeTransactionHash(HealthRecordDTO recordDTO) {
        List<Object> leaves = flattenHealthRecord(recordDTO);
        if (leaves.isEmpty()) {
            return HashUtils.hashData("empty");
        }

        MerkleTree<Object> tree = new MerkleTree<>();
        MerkleTreeNode<Object> root = tree.buildTree(leaves);
        return root.getHash();
    }

    public static String computeBlockHash(List<Transaction> transactions) {
        if (transactions.isEmpty()) {
            return HashUtils.hashData("empty");
        }

        List<String> leaves = transactions.stream()
                .map(Transaction::hash)
                .toList();

        MerkleTree<String> tree = new MerkleTree<>();
        MerkleTreeNode<String> root = tree.buildTree(leaves);
        return root.getHash();
    }
}