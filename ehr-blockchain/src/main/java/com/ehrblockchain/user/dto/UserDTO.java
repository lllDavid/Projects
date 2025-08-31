package com.ehrblockchain.user.dto;

public record UserDTO(
        String firstName,
        String lastName,
        String email,
        String roleName,
        Long patientId
) {}