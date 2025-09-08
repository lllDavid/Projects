package com.ehrblockchain.integration.user;

import com.fasterxml.jackson.databind.ObjectMapper;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import com.ehrblockchain.user.dto.UserCreateDTO;
import com.ehrblockchain.user.dto.UserUpdateDTO;
import com.ehrblockchain.user.model.User;
import com.ehrblockchain.user.repository.UserRepository;
import com.ehrblockchain.security.role.repository.RoleRepository;
import com.ehrblockchain.fixtures.IntegrationFixtures;
import com.ehrblockchain.patient.model.Patient;
import com.ehrblockchain.patient.repository.PatientRepository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.MediaType;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.test.context.support.WithMockUser;
import org.springframework.test.context.ActiveProfiles;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.test.web.servlet.MockMvc;

import static com.ehrblockchain.fixtures.IntegrationFixtures.*;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
@AutoConfigureMockMvc
@ActiveProfiles("test")
class UserControllerIT {

    @Autowired
    private MockMvc mockMvc;

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private PatientRepository patientRepository;

    @Autowired
    private RoleRepository roleRepository;

    @Autowired
    private PasswordEncoder passwordEncoder;

    @Autowired
    private ObjectMapper objectMapper;

    private User savedUser;

    private Patient savedPatient;

    @BeforeEach
    void setup() {
        userRepository.deleteAll();
        patientRepository.deleteAll();

        savedPatient = patientRepository.save(IntegrationFixtures.createDefaultPatient());

        User user = IntegrationFixtures.createDefaultUser();
        user.setRole(roleRepository.save(user.getRole()));
        user.setPatient(savedPatient);
        user.setPassword(passwordEncoder.encode(IntegrationFixtures.DEFAULT_USER_PASSWORD));

        savedUser = userRepository.save(user);
    }

    // -------------------
    // GET /users
    // -------------------
    @Test
    @WithMockUser(roles = {"ADMIN"})
    void getAllUsers_admin_success_returns200() throws Exception {
        mockMvc.perform(get("/users")
                        .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$[0].email").value(savedUser.getEmail()));
    }

    @Test
    @WithMockUser(roles = {"USER"})
    void getAllUsers_user_forbidden_returns403() throws Exception {
        mockMvc.perform(get("/users")
                        .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isForbidden());
    }

    // -------------------
    // GET /users/{id}
    // -------------------
    @Test
    @WithMockUser(roles = {"ADMIN"})
    void getUserById_admin_success_returns200() throws Exception {
        mockMvc.perform(get("/users/" + savedUser.getId())
                        .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.email").value(savedUser.getEmail()));
    }

    @Test
    @WithMockUser(roles = {"ADMIN"})
    void getUserById_notFound_returns404() throws Exception {
        mockMvc.perform(get("/users/9999999999")
                        .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isNotFound());
    }

    // -------------------
    // POST /users
    // -------------------
    @Test
    @WithMockUser
    void createUser_success_returns201() throws Exception {
        UserCreateDTO dto = createDefaultUserCreateDTO();
        dto.setEmail("new.email+" + System.currentTimeMillis() + "@example.com");

        mockMvc.perform(post("/users")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(dto)))
                .andExpect(status().isCreated())
                .andExpect(jsonPath("$.email").value(dto.getEmail()));
    }

    // -------------------
    // POST /users/create-elevated
    // -------------------
    @Test
    @WithMockUser(roles = {"ADMIN"})
    void createElevatedUser_success_returns201() throws Exception {
        UserCreateDTO dto = createDefaultUserCreateDTO();
        dto.setEmail("unique.email+" + System.currentTimeMillis() + "@example.com");
        mockMvc.perform(post("/users/create-elevated")
                        .param("role", "DOCTOR")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(dto)))
                .andExpect(status().isCreated())
                .andExpect(jsonPath("$.roleName").value("DOCTOR"));

    }

    @Test
    @WithMockUser(roles = {"USER"})
    void createElevatedUser_unauthorized_returns403() throws Exception {
        UserCreateDTO dto = createDefaultUserCreateDTO();
        mockMvc.perform(post("/users/create-elevated")
                        .param("role", "DOCTOR")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(dto)))
                .andExpect(status().isForbidden());
    }

    // -------------------
    // PATCH /users/{id}
    // -------------------
    @Test
    @WithMockUser(roles = {"ADMIN"})
    void updateUser_success_returns200() throws Exception {
        UserUpdateDTO dto = createDefaultUserUpdateDTO();
        mockMvc.perform(patch("/users/" + savedUser.getId())
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(dto)))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.email").value(dto.getEmail()));
    }

    @Test
    @WithMockUser(roles = {"ADMIN"})
    void updateUser_notFound_returns404() throws Exception {
        UserUpdateDTO dto = createDefaultUserUpdateDTO();
        mockMvc.perform(patch("/users/9999999999")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(dto)))
                .andExpect(status().isNotFound());
    }

    // -------------------
    // PATCH /users/{id}/link-patient
    // -------------------
    @Test
    @WithMockUser(roles = {"ADMIN"})
    void linkUserToPatient_success_returns200() throws Exception {
        Long patientId = savedPatient.getId();
        mockMvc.perform(patch("/users/" + savedUser.getId() + "/link-patient")
                        .param("patientId", patientId.toString())
                        .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.patientId").value(savedPatient.getId()));

    }

    @Test
    @WithMockUser(roles = {"USER"})
    void linkUserToPatient_unauthorized_returns403() throws Exception {
        mockMvc.perform(patch("/users/" + savedUser.getId() + "/link-patient")
                        .param("patientId", savedPatient.getId().toString())
                        .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isForbidden());
    }

    @Test
    @WithMockUser(roles = {"ADMIN"})
    void linkUserToPatient_userNotFound_returns404() throws Exception {
        mockMvc.perform(patch("/users/9999999999/link-patient")
                        .param("patientId", savedPatient.getId().toString())
                        .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isNotFound());
    }

    @Test
    @WithMockUser(roles = {"ADMIN"})
    void linkUserToPatient_patientNotFound_returns404() throws Exception {
        mockMvc.perform(patch("/users/" + savedUser.getId() + "/link-patient")
                        .param("patientId", "9999999999")
                        .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isNotFound());
    }

    // -------------------
    // DELETE /users/{id}
    // -------------------
    @Test
    @WithMockUser(roles = {"ADMIN"})
    void deleteUser_success_returns204() throws Exception {
        mockMvc.perform(delete("/users/" + savedUser.getId()))
                .andExpect(status().isNoContent());
    }

    @Test
    @WithMockUser(roles = {"ADMIN"})
    void deleteUser_nonExistent_returnsNoContent() throws Exception {
        mockMvc.perform(delete("/users/9999999999"))
                .andExpect(status().isNoContent());
    }
}