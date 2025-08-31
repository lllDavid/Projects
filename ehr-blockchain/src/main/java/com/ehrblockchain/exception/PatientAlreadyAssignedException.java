package com.ehrblockchain.exception;


public class PatientAlreadyAssignedException extends RuntimeException {

    public PatientAlreadyAssignedException(Long patientId) {
        super("Patient with id " + patientId + " is already assigned to a user.");
    }

    public PatientAlreadyAssignedException(String message) {
        super(message);
    }
}