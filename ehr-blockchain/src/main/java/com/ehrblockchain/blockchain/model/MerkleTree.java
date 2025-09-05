package com.ehrblockchain.blockchain.model;

import java.util.ArrayList;
import java.util.List;

import com.ehrblockchain.blockchain.util.HashUtils;

public class MerkleTree<T> {

    public MerkleTreeNode<T> buildTree(List<T> leaves) {
        List<MerkleTreeNode<T>> nodes = new ArrayList<>();
        for (T leaf : leaves)
            nodes.add(new MerkleTreeNode<>(null, null, HashUtils.hashData(leaf), leaf, false));

        if (nodes.size() % 2 == 1)
            nodes.add(nodes.get(nodes.size() - 1).copy());

        return build(nodes);
    }

    private MerkleTreeNode<T> build(List<MerkleTreeNode<T>> nodes) {
        if (nodes.size() == 1) return nodes.get(0);

        List<MerkleTreeNode<T>> parents = new ArrayList<>();
        for (int i = 0; i < nodes.size(); i += 2) {
            MerkleTreeNode<T> left = nodes.get(i), right = nodes.get(i + 1);
            String hash = HashUtils.hashData(left.getHash(), right.getHash());
            parents.add(new MerkleTreeNode<>(left, right, hash, null, false));
        }

        if (parents.size() % 2 == 1 && parents.size() > 1)
            parents.add(parents.get(parents.size() - 1).copy());

        return build(parents);
    }
}