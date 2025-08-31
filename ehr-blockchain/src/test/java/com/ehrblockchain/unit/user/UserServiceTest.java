package com.ehrblockchain.unit.user;

import java.util.List;
import java.util.Optional;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;

import static org.junit.jupiter.api.Assertions.*;
import static org.assertj.core.api.Assertions.assertThat;

import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.*;

import static com.ehrblockchain.fixtures.fixtures.DEFAULT_ROLE;

import com.ehrblockchain.patient.repository.PatientRepository;
import com.ehrblockchain.user.mapper.UserMapper;
import com.ehrblockchain.user.dto.UserDTO;
import com.ehrblockchain.user.dto.UserCreateDTO;
import com.ehrblockchain.user.dto.UserUpdateDTO;
import com.ehrblockchain.user.model.User;
import com.ehrblockchain.user.repository.UserRepository;
import com.ehrblockchain.security.role.model.Role;
import com.ehrblockchain.security.role.repository.RoleRepository;
import com.ehrblockchain.exception.EmailAlreadyExistsException;
import com.ehrblockchain.exception.UserNotFoundException;
import com.ehrblockchain.security.role.RoleEnum;
import com.ehrblockchain.fixtures.fixtures;
import com.ehrblockchain.user.service.UserService;

import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.test.util.ReflectionTestUtils;

@ExtendWith(MockitoExtension.class)
class UserServiceTest {

    @Mock
    private PasswordEncoder passwordEncoder;

    @Mock
    private UserRepository userRepository;

    @Mock
    private UserMapper userMapper;

    @Mock
    private RoleRepository roleRepository;

    @Mock
    PatientRepository patientRepository;

    private UserService underTest;

    @BeforeEach
    void setUp() {
        underTest = new UserService(passwordEncoder, userRepository, userMapper, roleRepository, patientRepository);
        lenient().when(passwordEncoder.encode(anyString())).thenReturn("encodedPassword");
        ReflectionTestUtils.setField(underTest, "defaultUserRole", "PATIENT");
    }

    @Test
    void shouldSaveUser() {
        User user = fixtures.createDefaultUser();
        UserDTO userDTO = fixtures.createDefaultUserDTO();

        when(userRepository.findByEmail(user.getEmail())).thenReturn(Optional.empty());
        when(userRepository.save(user)).thenReturn(user);
        when(userMapper.toDto(user)).thenReturn(userDTO);

        UserDTO result = underTest.saveUser(user);

        assertNotNull(result);
        assertThat(result).usingRecursiveComparison().isEqualTo(userDTO);

        verify(userRepository).findByEmail(user.getEmail());
        verify(userRepository).save(user);
        verify(userMapper).toDto(user);
    }

    @Test
    void shouldCreateUser() {
        UserCreateDTO createDTO = fixtures.createDefaultUserCreateDTO();
        User user = fixtures.createDefaultUser();
        UserDTO userDTO = fixtures.createDefaultUserDTO();
        Role role = fixtures.createDefaultRole();

        when(userMapper.toEntity(createDTO)).thenReturn(user);
        when(roleRepository.findByName(DEFAULT_ROLE)).thenReturn(Optional.of(role));
        when(userRepository.findByEmail(user.getEmail())).thenReturn(Optional.empty());
        when(userRepository.save(user)).thenReturn(user);
        when(userMapper.toDto(user)).thenReturn(userDTO);

        UserDTO result = underTest.createUser(createDTO);

        assertNotNull(result);
        assertThat(result).usingRecursiveComparison().isEqualTo(userDTO);

        verify(userMapper).toEntity(createDTO);
        verify(roleRepository).findByName(DEFAULT_ROLE);
        verify(userRepository).findByEmail(user.getEmail());
        verify(userRepository).save(user);
        verify(userMapper).toDto(user);
    }


    @Test
    void shouldUpdateUser() {
        User existingUser = fixtures.createDefaultUser();
        UserUpdateDTO updateDTO = fixtures.createDefaultUserUpdateDTO();
        UserDTO updatedUserDTO = fixtures.createDefaultUserDTO();

        when(userRepository.findById(existingUser.getId())).thenReturn(Optional.of(existingUser));
        doAnswer(invocation -> {
            UserUpdateDTO dto = invocation.getArgument(0);
            User user = invocation.getArgument(1);
            user.setFirstName(dto.getFirstName());
            user.setLastName(dto.getLastName());
            return null;
        }).when(userMapper).updateFromDto(updateDTO, existingUser);

        when(userMapper.toDto(existingUser)).thenReturn(updatedUserDTO);

        UserDTO result = underTest.updateUser(existingUser.getId(), updateDTO);

        assertNotNull(result);
        assertThat(result).usingRecursiveComparison().isEqualTo(updatedUserDTO);

        verify(userRepository).findById(existingUser.getId());
        verify(userMapper).updateFromDto(updateDTO, existingUser);
        verify(userMapper).toDto(existingUser);
    }

    @Test
    void shouldDeleteUser() {
        Long userId = 1L;

        underTest.deleteUser(userId);

        verify(userRepository).deleteById(userId);
        verifyNoMoreInteractions(userRepository);
    }

    @Test
    void shouldGetAllUsers() {
        List<User> users = List.of(fixtures.createDefaultUser());
        List<UserDTO> userDTOs = List.of(fixtures.createDefaultUserDTO());

        when(userRepository.findAll()).thenReturn(users);
        when(userMapper.toDto(any(User.class))).thenAnswer(invocation -> fixtures.createDefaultUserDTO());

        List<UserDTO> result = underTest.getAllUsers();

        assertNotNull(result);
        assertEquals(userDTOs.size(), result.size());
        assertThat(result).usingRecursiveComparison().isEqualTo(userDTOs);

        verify(userRepository).findAll();
        verify(userMapper).toDto(any(User.class));
    }

    @Test
    void shouldGetUserById() {
        Long userId = 1L;

        when(userRepository.findById(userId)).thenReturn(Optional.of(fixtures.createDefaultUser()));
        when(userMapper.toDto(any(User.class))).thenReturn(fixtures.createDefaultUserDTO());

        UserDTO result = underTest.getUserById(userId);

        assertThat(result).isNotNull();
        assertThat(result).usingRecursiveComparison().isEqualTo(fixtures.createDefaultUserDTO());

        verify(userRepository).findById(userId);
        verify(userMapper).toDto(any(User.class));
    }

    @Test
    void shouldGetUserByEmail() {
        String email = "test@example.com";
        User user = fixtures.createDefaultUser();
        UserDTO userDTO = fixtures.createDefaultUserDTO();

        when(userRepository.findByEmail(email)).thenReturn(Optional.of(user));
        when(userMapper.toDto(user)).thenReturn(userDTO);

        UserDTO result = underTest.getUserByEmail(email);

        assertNotNull(result);
        assertThat(result).usingRecursiveComparison().isEqualTo(userDTO);

        verify(userRepository).findByEmail(email);
        verify(userMapper).toDto(user);
    }

    @Test
    void shouldThrowWhenSavingUserIfEmailExists() {
        User user = fixtures.createDefaultUser();

        when(userRepository.findByEmail(user.getEmail())).thenReturn(Optional.of(user));

        assertThrows(EmailAlreadyExistsException.class, () -> underTest.saveUser(user));

        verify(userRepository).findByEmail(user.getEmail());
        verify(userRepository, never()).save(any());
        verify(userMapper, never()).toDto(any(User.class));
    }

    @Test
    void shouldThrowWhenCreatingUserIfEmailExists() {
        UserCreateDTO createDTO = fixtures.createDefaultUserCreateDTO();
        User user = fixtures.createDefaultUser();
        Role role = fixtures.createDefaultRole();
        when(roleRepository.findByName(RoleEnum.PATIENT))
                .thenReturn(Optional.of(role));


        when(userMapper.toEntity(createDTO)).thenReturn(user);
        when(userRepository.findByEmail(user.getEmail())).thenReturn(Optional.of(user));

        assertThrows(EmailAlreadyExistsException.class, () -> underTest.createUser(createDTO));

        verify(userMapper).toEntity(createDTO);
        verify(userRepository).findByEmail(user.getEmail());
        verify(userRepository, never()).save(any());
        verify(userMapper, never()).toDto(any());
    }

    @Test
    void shouldThrowWhenUpdatingUserIfNotFound() {
        Long userId = 1L;
        UserUpdateDTO updateDTO = fixtures.createDefaultUserUpdateDTO();

        when(userRepository.findById(userId)).thenReturn(Optional.empty());

        assertThrows(UserNotFoundException.class, () -> underTest.updateUser(userId, updateDTO));

        verify(userRepository).findById(userId);
        verify(userMapper, never()).updateFromDto(any(), any());
        verify(userMapper, never()).toDto(any());
    }

    @Test
    void shouldPropagateWhenMapperThrowsOnUpdate() {
        User existingUser = fixtures.createDefaultUser();
        UserUpdateDTO updateDTO = fixtures.createDefaultUserUpdateDTO();

        when(userRepository.findById(existingUser.getId())).thenReturn(Optional.of(existingUser));
        doThrow(new RuntimeException("mapper failure")).when(userMapper).updateFromDto(updateDTO, existingUser);

        assertThrows(RuntimeException.class, () -> underTest.updateUser(existingUser.getId(), updateDTO));

        verify(userRepository).findById(existingUser.getId());
        verify(userMapper).updateFromDto(updateDTO, existingUser);
        verify(userRepository, never()).save(any());
    }

    @Test
    void shouldPropagateWhenRepositoryThrowsOnDelete() {
        Long userId = 1L;

        doThrow(new RuntimeException("delete failed")).when(userRepository).deleteById(userId);

        assertThrows(RuntimeException.class, () -> underTest.deleteUser(userId));

        verify(userRepository).deleteById(userId);
    }

    @Test
    void shouldPropagateWhenMapperThrowsOnGetAll() {
        List<User> users = List.of(fixtures.createDefaultUser());

        when(userRepository.findAll()).thenReturn(users);
        when(userMapper.toDto(any(User.class))).thenThrow(new RuntimeException("map fail"));

        assertThrows(RuntimeException.class, () -> underTest.getAllUsers());

        verify(userRepository).findAll();
        verify(userMapper).toDto(any(User.class));
    }

    @Test
    void shouldThrowWhenGetUserByIdNotFound() {
        Long userId = 1L;

        when(userRepository.findById(userId)).thenReturn(Optional.empty());

        assertThrows(UserNotFoundException.class, () -> underTest.getUserById(userId));

        verify(userRepository).findById(userId);
        verify(userMapper, never()).toDto(any());
    }

    @Test
    void shouldThrowWhenGetUserByEmailNotFound() {
        String email = "notfound@example.com";

        when(userRepository.findByEmail(email)).thenReturn(Optional.empty());

        assertThrows(UserNotFoundException.class, () -> underTest.getUserByEmail(email));

        verify(userRepository).findByEmail(email);
        verify(userMapper, never()).toDto(any());
    }
}