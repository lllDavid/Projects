package com.ehrblockchain.exception;

public class PatientNotFoundException extends RuntimeException {

    public PatientNotFoundException(Long id) {
        super("Patient not found with id: " + id);
    }

    public PatientNotFoundException(String email) {
        super("Patient not found with email: " + email);
    }
}