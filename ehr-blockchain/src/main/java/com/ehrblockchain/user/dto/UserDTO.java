package com.ehrblockchain.user.dto;

public record UserDTO(
        Long id,
        String firstName,
        String lastName,
        String email,
        String roleName,
        Long patientId
) {}