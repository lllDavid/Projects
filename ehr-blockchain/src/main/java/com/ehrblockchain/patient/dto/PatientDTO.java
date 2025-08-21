package com.ehrblockchain.patient.dto;

import java.time.LocalDate;

public record PatientDTO(
        String firstName,
        String lastName,
        LocalDate dateOfBirth,
        String gender,
        Double height,
        Double weight,
        String bloodType,
        String phoneNumber,
        String email,
        String emergencyContact,
        AddressDTO address,
        InsuranceDTO insurance
) {}
