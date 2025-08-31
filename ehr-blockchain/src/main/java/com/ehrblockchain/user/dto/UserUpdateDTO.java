package com.ehrblockchain.user.dto;

import com.fasterxml.jackson.annotation.JsonInclude;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Pattern;
import jakarta.validation.constraints.Size;

@JsonInclude(JsonInclude.Include.NON_NULL)
public class UserUpdateDTO {

    private String firstName;
    private String lastName;
    private String email;
    // Temporary, implement password update method
    @NotBlank()
    @Pattern(regexp = "^(?=(?:.*[A-Z].*){2,})(?=(?:.*[a-z].*){2,})(?=(?:.*\\d.*){2,})(?=(?:.*[^a-zA-Z0-9].*){2,}).{12,255}$",
            message = "Password must include at least 2 uppercase letters, 2 lowercase letters, 2 numbers, and 2 special characters.")

    @Size(min = 12, max = 255)
    private String password;

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
}