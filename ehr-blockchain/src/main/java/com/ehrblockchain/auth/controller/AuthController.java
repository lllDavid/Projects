package com.ehrblockchain.auth.controller;

import jakarta.validation.Valid;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.oauth2.jwt.JwtEncoder;
import org.springframework.web.bind.annotation.*;

import com.ehrblockchain.auth.LoginRequest;
import com.ehrblockchain.user.dto.UserCreateDTO;
import com.ehrblockchain.user.dto.UserDTO;
import com.ehrblockchain.user.service.UserService;
import com.ehrblockchain.auth.service.AuthService;

@RestController
@RequestMapping("/auth")
public class AuthController {

    private final UserService userService;
    private final AuthService authService;

    public AuthController(UserService userService, AuthService authService, AuthenticationManager authenticationManager, JwtEncoder jwtEncoder) {
        this.userService = userService;
        this.authService = authService;
    }

    @PostMapping("/register")
    public ResponseEntity<UserDTO> register(@Valid @RequestBody UserCreateDTO userCreateDTO) {
        UserDTO savedUserDTO = userService.createUser(userCreateDTO);
        return ResponseEntity.status(HttpStatus.CREATED).body(savedUserDTO);
    }

    @PostMapping("/login")
    public ResponseEntity<?> authorize(@RequestBody LoginRequest request) {
        return ResponseEntity.ok(authService.authenticateAndGenerateToken(request.email(), request.password()));
    }

    @GetMapping("/profile")
    public ResponseEntity<UserDTO> profile() {
        UserDTO dto = authService.getCurrentUser();
        return ResponseEntity.ok(dto);
    }
}