package com.ehrblockchain.blockchain.controller;

import java.util.List;

import com.ehrblockchain.blockchain.model.Block;
import com.ehrblockchain.blockchain.model.Blockchain;

import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class BlockchainController {

    private final Blockchain blockchain;

    public BlockchainController(Blockchain blockchain) {
        this.blockchain = blockchain;
    }

    @PreAuthorize("hasRole('ADMIN')")
    @GetMapping("/chain")
    public List<Block> getChain() {
        return blockchain.getChain();
    }
}