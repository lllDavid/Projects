package com.ehrblockchain.exception;

public class HealthRecordNotFoundException extends RuntimeException {

    public HealthRecordNotFoundException(Long id) {
        super("HealthRecord not found with id: " + id);
    }

    public HealthRecordNotFoundException(String message) {
        super(message);
    }
}