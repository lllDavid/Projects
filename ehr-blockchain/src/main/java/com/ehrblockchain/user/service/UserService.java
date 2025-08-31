package com.ehrblockchain.user.service;

import java.util.List;
import java.util.stream.Collectors;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.ehrblockchain.user.mapper.UserMapper;
import com.ehrblockchain.user.model.User;
import com.ehrblockchain.user.repository.UserRepository;
import com.ehrblockchain.user.dto.UserCreateDTO;
import com.ehrblockchain.user.dto.UserDTO;
import com.ehrblockchain.user.dto.UserUpdateDTO;
import com.ehrblockchain.security.role.model.Role;
import com.ehrblockchain.security.role.repository.RoleRepository;
import com.ehrblockchain.exception.*;
import com.ehrblockchain.security.role.RoleEnum;
import com.ehrblockchain.patient.model.Patient;
import com.ehrblockchain.patient.repository.PatientRepository;

@Service
public class UserService {

    @Value("${app.default.user.role}")
    private String defaultUserRole;

    private final PasswordEncoder passwordEncoder;
    private final UserRepository userRepository;
    private final UserMapper userMapper;
    private final RoleRepository roleRepository;
    private final PatientRepository patientRepository;

    public UserService(PasswordEncoder passwordEncoder, UserRepository userRepository, UserMapper userMapper, RoleRepository roleRepository, PatientRepository patientRepository) {
        this.passwordEncoder = passwordEncoder;
        this.userRepository = userRepository;
        this.userMapper = userMapper;
        this.roleRepository = roleRepository;
        this.patientRepository = patientRepository;
    }

    @Transactional
    public UserDTO saveUser(User user) {
        userRepository.findByEmail(user.getEmail()).ifPresent(u -> {
            throw new EmailAlreadyExistsException(user.getEmail());
        });
        User savedUser = userRepository.save(user);

        return userMapper.toDto(savedUser);
    }

    @Transactional
    public UserDTO createUser(UserCreateDTO createDTO) {
        User user = userMapper.toEntity(createDTO);

        user.setPassword(passwordEncoder.encode(createDTO.getPassword()));

        Role role = roleRepository.findByName(RoleEnum.valueOf(defaultUserRole))
                .orElseThrow(() -> new RoleNotFoundException(defaultUserRole));
        user.setRole(role);

        return saveUser(user);
    }

    @Transactional
    // The selected role is passed as a query parameter (?role=DOCTOR)
    public UserDTO createElevatedUser(UserCreateDTO createDTO, RoleEnum roleEnum) {
        User user = userMapper.toEntity(createDTO);
        user.setPassword(passwordEncoder.encode(createDTO.getPassword()));

        Role role = roleRepository.findByName(roleEnum)
                .orElseThrow(() -> new RoleNotFoundException(roleEnum.name()));
        user.setRole(role);

        return saveUser(user);
    }

    @Transactional
    // The patient to link is passed as a query parameter (?patientId=1)
    public UserDTO linkPatient(Long userId, Long patientId) {
        User existingUser = userRepository.findById(userId)
                .orElseThrow(() -> new UserNotFoundException(userId));

        Patient patient = patientRepository.findById(patientId)
                .orElseThrow(() -> new PatientNotFoundException(patientId));

        existingUser.setPatient(patient);

        return userMapper.toDto(existingUser);
    }

    @Transactional
    public UserDTO updateUser(Long id, UserUpdateDTO updateDTO) {
        User existingUser = userRepository.findById(id)
                .orElseThrow(() -> new UserNotFoundException(id));

        userRepository.findByEmail(updateDTO.getEmail())
                .filter(u -> !u.getId().equals(existingUser.getId()))
                .ifPresent(u -> {
                    throw new EmailAlreadyExistsException(updateDTO.getEmail());
                });

        userMapper.updateFromDto(updateDTO, existingUser);

        return userMapper.toDto(existingUser);
    }

    @Transactional
    public void deleteUser(Long userId) {
        userRepository.deleteById(userId);
    }

    @Transactional(readOnly = true)
    public List<UserDTO> getAllUsers() {
        return userRepository.findAll().stream()
                .map(userMapper::toDto)
                .collect(Collectors.toList());
    }

    @Transactional(readOnly = true)
    public UserDTO getUserById(Long userId) {
        return userRepository.findById(userId)
                .map(userMapper::toDto)
                .orElseThrow(() -> new UserNotFoundException(userId));
    }

    @Transactional(readOnly = true)
    public UserDTO getUserByEmail(String email) {
        return userRepository.findByEmail(email)
                .map(userMapper::toDto)
                .orElseThrow(() -> new UserNotFoundException(email));
    }
}