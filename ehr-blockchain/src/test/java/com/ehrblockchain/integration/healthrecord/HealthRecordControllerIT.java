package com.ehrblockchain.integration.healthrecord;

import com.fasterxml.jackson.databind.ObjectMapper;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import com.ehrblockchain.healthrecord.dto.HealthRecordUpdateDTO;
import com.ehrblockchain.patient.model.Patient;
import com.ehrblockchain.patient.repository.PatientRepository;
import com.ehrblockchain.fixtures.IntegrationFixtures;
import com.ehrblockchain.security.role.repository.RoleRepository;
import com.ehrblockchain.user.model.User;
import com.ehrblockchain.user.repository.UserRepository;

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
class HealthRecordControllerIT {

    @Autowired
    private MockMvc mockMvc;

    @Autowired
    private PatientRepository patientRepository;

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private RoleRepository roleRepository;

    @Autowired
    private PasswordEncoder passwordEncoder;

    @Autowired
    private ObjectMapper objectMapper;

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

        userRepository.save(user);
    }

    // -------------------
    // GET /patients/{id}/healthrecord
    // -------------------

    @Test
    @WithMockUser(username = "john.doe@example.com", roles = {"ADMIN"})
    void getHealthRecord_success_returns200() throws Exception {
        mockMvc.perform(get("/patients/" + savedPatient.getId() + "/healthrecord")
                        .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.notes").exists());
    }

    @Test
    @WithMockUser(username = "john.doe@example.com", roles = {"RECEPTION"})
    void getHealthRecord_reception_success_returns200() throws Exception {
        mockMvc.perform(get("/patients/" + savedPatient.getId() + "/healthrecord")
                        .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isOk());
    }

    @Test
    @WithMockUser(roles = {"PATIENT"})
    void getHealthRecord_unauthorized_returns403() throws Exception {
        mockMvc.perform(get("/patients/" + savedPatient.getId() + "/healthrecord")
                        .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isForbidden());
    }

    @Test
    @WithMockUser(roles = {"ADMIN"})
    void getHealthRecord_notFound_returns404() throws Exception {
        mockMvc.perform(get("/patients/99999999/healthrecord")
                        .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isNotFound());
    }

    @Test
    @WithMockUser(username = "john.doe@example.com", roles = {"NURSE"})
    void getHealthRecord_nurseRole_returns200() throws Exception {
        mockMvc.perform(get("/patients/" + savedPatient.getId() + "/healthrecord")
                        .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.notes").exists());
    }

    // -------------------
    // PATCH /patients/{id}/healthrecord
    // -------------------

    @Test
    @WithMockUser(username = "john.doe@example.com", roles = {"ADMIN"})
    void updateHealthRecord_success_returns200() throws Exception {
        HealthRecordUpdateDTO dto = createDefaultHealthRecordUpdateDTO();
        mockMvc.perform(patch("/patients/" + savedPatient.getId() + "/healthrecord")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(dto)))
                .andExpect(status().isOk());
    }

    @Test
    @WithMockUser(username = "john.doe@example.com", roles = {"DOCTOR"})
    void updateHealthRecord_doctor_success_returns200() throws Exception {
        HealthRecordUpdateDTO dto = createDefaultHealthRecordUpdateDTO();
        mockMvc.perform(patch("/patients/" + savedPatient.getId() + "/healthrecord")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(dto)))
                .andExpect(status().isOk());
    }

    @Test
    @WithMockUser(roles = {"RECEPTION"})
    void updateHealthRecord_unauthorized_returns403() throws Exception {
        HealthRecordUpdateDTO dto = createDefaultHealthRecordUpdateDTO();
        mockMvc.perform(patch("/patients/" + savedPatient.getId() + "/healthrecord")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(dto)))
                .andExpect(status().isForbidden());
    }

    @Test
    @WithMockUser(roles = {"ADMIN"})
    void updateHealthRecord_notFound_returns404() throws Exception {
        HealthRecordUpdateDTO dto = createDefaultHealthRecordUpdateDTO();
        mockMvc.perform(patch("/patients/99999999/healthrecord")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(dto)))
                .andExpect(status().isNotFound());
    }

    @Test
    @WithMockUser(username = "john.doe@example.com", roles = {"NURSE"})
    void updateHealthRecord_nurseRole_returns200() throws Exception {
        HealthRecordUpdateDTO dto = createDefaultHealthRecordUpdateDTO();
        mockMvc.perform(patch("/patients/" + savedPatient.getId() + "/healthrecord")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(dto)))
                .andExpect(status().isOk());
    }

    @Test
    @WithMockUser(username = "john.doe@example.com", roles = {"ADMIN"})
    void updateHealthRecord_withEmptyDTO_returns200NoChanges() throws Exception {
        HealthRecordUpdateDTO emptyDto = new HealthRecordUpdateDTO();
        mockMvc.perform(patch("/patients/" + savedPatient.getId() + "/healthrecord")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(emptyDto)))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.notes").exists());
    }

    // -------------------
    // DELETE /patients/{id}/healthrecord
    // -------------------

    @Test
    @WithMockUser(username = "john.doe@example.com", roles = {"ADMIN"})
    void deleteHealthRecord_success_returns204() throws Exception {
        mockMvc.perform(delete("/patients/" + savedPatient.getId() + "/healthrecord"))
                .andExpect(status().isNoContent());
    }

    @Test
    @WithMockUser(roles = {"ADMIN"})
    void deleteHealthRecord_notFound_returns404() throws Exception {
        mockMvc.perform(delete("/patients/99999999/healthrecord"))
                .andExpect(status().isNotFound());
    }

    @Test
    @WithMockUser(roles = {"DOCTOR"})
    void deleteHealthRecord_unauthorized_returns403() throws Exception {
        mockMvc.perform(delete("/patients/" + savedPatient.getId() + "/healthrecord"))
                .andExpect(status().isForbidden());
    }

    @Test
    @WithMockUser(username = "john.doe@example.com", roles = {"ADMIN"})
    void deleteHealthRecord_alreadyDeleted_returns404() throws Exception {
        mockMvc.perform(delete("/patients/" + savedPatient.getId() + "/healthrecord"))
                .andExpect(status().isNoContent());

        mockMvc.perform(delete("/patients/" + savedPatient.getId() + "/healthrecord"))
                .andExpect(status().isNotFound());
    }
}