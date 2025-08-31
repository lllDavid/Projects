package com.ehrblockchain.user.controller;

import java.util.List;

import jakarta.validation.Valid;

import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;

import com.ehrblockchain.user.service.UserService;
import com.ehrblockchain.user.dto.UserCreateDTO;
import com.ehrblockchain.user.dto.UserUpdateDTO;
import com.ehrblockchain.user.dto.UserDTO;
import com.ehrblockchain.security.role.RoleEnum;

@RestController
@RequestMapping("/users")
public class UserController {

    private final UserService userService;

    public UserController(UserService userService) {
        this.userService = userService;
    }

    @PreAuthorize("hasRole('ADMIN')")
    @GetMapping
    public ResponseEntity<List<UserDTO>> getAllUsers() {
        return ResponseEntity.ok(userService.getAllUsers());
    }

    @PreAuthorize("hasRole('ADMIN')")
    @GetMapping("/{id}")
    public ResponseEntity<UserDTO> getUserById(@PathVariable Long id) {
        UserDTO user = userService.getUserById(id);
        return ResponseEntity.ok(user);
    }

    @PostMapping
    public ResponseEntity<UserDTO> createUser(@Valid @RequestBody UserCreateDTO userCreateDTO) {
        System.out.println("Controller called with password: " + userCreateDTO.getPassword());
        UserDTO savedUserDTO = userService.createUser(userCreateDTO);
        return ResponseEntity.status(HttpStatus.CREATED).body(savedUserDTO);
    }

    @PostMapping("/elevated")
    @PreAuthorize("hasRole('ADMIN')")
    public ResponseEntity<UserDTO> createElevatedUser(
            @Valid @RequestBody UserCreateDTO createDTO,
            @RequestParam RoleEnum role) {

        UserDTO createdUser = userService.createElevatedUser(createDTO, role);
        return ResponseEntity.status(HttpStatus.CREATED).body(createdUser);
    }

    @PreAuthorize("hasRole('ADMIN')")
    @PatchMapping("/{id}/patient")
    public ResponseEntity<UserDTO> linkUserToPatient(
            @PathVariable Long id,
            @RequestParam Long patientId) {

        UserDTO updatedUser = userService.linkPatient(id, patientId);
        return ResponseEntity.ok(updatedUser);
    }

    @PreAuthorize("hasRole('ADMIN')")
    @PatchMapping("/{id}")
    public ResponseEntity<UserDTO> updateUser(@PathVariable Long id,
                                              @Valid @RequestBody UserUpdateDTO updateDTO) {
        UserDTO updatedUserDto = userService.updateUser(id, updateDTO);
        return ResponseEntity.ok(updatedUserDto);
    }

    @PreAuthorize("hasRole('ADMIN')")
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteUser(@PathVariable Long id) {
        userService.deleteUser(id);
        return ResponseEntity.noContent().build();
    }
}