package com.ehrblockchain;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;

@SpringBootApplication
public class EhrBlockchainApplication {

    public static void main(String[] args) {
        ApplicationContext context = SpringApplication.run(EhrBlockchainApplication.class, args);
    }
}