package com.ehrblockchain.blockchain.model;

public class MerkleTreeNode<T> {
    private MerkleTreeNode<T> left;
    private MerkleTreeNode<T> right;
    private T value;
    private String hash;
    private boolean isDuplicate;

    public MerkleTreeNode(MerkleTreeNode<T> left, MerkleTreeNode<T> right, String hash, T value, boolean isDuplicate) {
        this.left = left;
        this.right = right;
        this.hash = hash;
        this.value = value;
        this.isDuplicate = isDuplicate;
    }

    public MerkleTreeNode<T> copy() {
        return new MerkleTreeNode<>(this.left, this.right, this.hash, this.value, true);
    }

    public MerkleTreeNode<T> getLeft() {
        return left;
    }

    public void setLeft(MerkleTreeNode<T> left) {
        this.left = left;
    }

    public MerkleTreeNode<T> getRight() {
        return right;
    }

    public void setRight(MerkleTreeNode<T> right) {
        this.right = right;
    }

    public T getValue() {
        return value;
    }

    public void setValue(T value) {
        this.value = value;
    }

    public String getHash() {
        return hash;
    }

    public void setHash(String hash) {
        this.hash = hash;
    }

    public boolean isDuplicate() {
        return isDuplicate;
    }

    public void setDuplicate(boolean isDuplicate) {
        this.isDuplicate = isDuplicate;
    }
}