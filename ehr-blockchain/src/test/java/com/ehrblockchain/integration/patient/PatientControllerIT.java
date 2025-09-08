package com.ehrblockchain.integration.patient;

import com.fasterxml.jackson.databind.ObjectMapper;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import com.ehrblockchain.patient.model.Patient;
import com.ehrblockchain.patient.repository.PatientRepository;
import com.ehrblockchain.patient.dto.PatientCreateDTO;
import com.ehrblockchain.patient.dto.PatientUpdateDTO;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.MediaType;
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
class PatientControllerIT {

    @Autowired
    private MockMvc mockMvc;

    @Autowired
    private PatientRepository patientRepository;

    @Autowired
    private ObjectMapper objectMapper;

    private Patient savedPatient;

    @BeforeEach
    void setup() {
        patientRepository.deleteAll();
        savedPatient = patientRepository.save(createDefaultPatient());
    }

    // -------------------
    // GET /patients/{id}
    // -------------------

    @Test
    @WithMockUser(roles = {"ADMIN"})
    void getPatientById_notFound_returns404() throws Exception {
        mockMvc.perform(get("/patients/9999999999")
                        .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isNotFound());
    }

    @Test
    @WithMockUser(username = "user", roles = {"PATIENT"})
    void getPatientById_unauthorized_returns403() throws Exception {
        mockMvc.perform(get("/patients/" + savedPatient.getId())
                        .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isForbidden());
    }

    @Test
    @WithMockUser(roles = {"PATIENT"})
    void getPatientById_roleWithoutAccess_returns403() throws Exception {
        mockMvc.perform(get("/patients/" + savedPatient.getId())
                        .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isForbidden());
    }

    // -------------------
    // GET /patients
    // -------------------

    @Test
    @WithMockUser(roles = {"ADMIN"})
    void getAllPatients_returnsPatients() throws Exception {
        mockMvc.perform(get("/patients")
                        .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$[0].id").value(savedPatient.getId()));
    }

    @Test
    @WithMockUser(roles = {"ADMIN"})
    void getAllPatients_empty_returnsEmptyList() throws Exception {
        patientRepository.deleteAll();
        mockMvc.perform(get("/patients")
                        .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.length()").value(0));
    }

    @Test
    @WithMockUser(username = "user", roles = {"PATIENT"})
    void getAllPatients_unauthorized_returns403() throws Exception {
        mockMvc.perform(get("/patients")
                        .contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isForbidden());
    }

    // -------------------
    // POST /patients
    // -------------------

    @Test
    @WithMockUser(roles = {"ADMIN"})
    void createPatient_success_returns201() throws Exception {
        PatientCreateDTO dto = createDefaultPatientCreateDTO();
        dto.setEmail("new@example.com");

        mockMvc.perform(post("/patients")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(dto)))
                .andExpect(status().isCreated())
                .andExpect(jsonPath("$.email").value("new@example.com"));
    }

    @Test
    @WithMockUser(roles = {"ADMIN"})
    void createPatient_withOptionalFieldsNull_returns201() throws Exception {
        PatientCreateDTO dto = createDefaultPatientCreateDTO();
        dto.setFirstName(null);
        dto.setLastName(null);
        dto.setDateOfBirth(null);
        dto.setGender(null);
        dto.setHeight(null);
        dto.setWeight(null);
        dto.setBloodType(null);
        dto.setPhoneNumber(null);
        dto.setEmergencyContact(null);
        dto.setAddress(null);
        dto.setInsurance(null);
        dto.setEmail("optional@example.com");

        mockMvc.perform(post("/patients")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(dto)))
                .andExpect(status().isCreated())
                .andExpect(jsonPath("$.id").exists())
                .andExpect(jsonPath("$.email").value("optional@example.com"))
                .andExpect(jsonPath("$.firstName").value((Object) null))
                .andExpect(jsonPath("$.lastName").value((Object) null))
                .andExpect(jsonPath("$.dateOfBirth").value((Object) null))
                .andExpect(jsonPath("$.gender").value((Object) null))
                .andExpect(jsonPath("$.height").value((Object) null))
                .andExpect(jsonPath("$.weight").value((Object) null))
                .andExpect(jsonPath("$.bloodType").value((Object) null))
                .andExpect(jsonPath("$.phoneNumber").value((Object) null))
                .andExpect(jsonPath("$.emergencyContact").value((Object) null))
                .andExpect(jsonPath("$.address").value((Object) null))
                .andExpect(jsonPath("$.insurance").value((Object) null));
    }

    @Test
    @WithMockUser(roles = {"DOCTOR"})
    void createPatient_roleWithoutAccess_returns403() throws Exception {
        PatientCreateDTO dto = createDefaultPatientCreateDTO();
        dto.setEmail("doctor@example.com");

        mockMvc.perform(post("/patients")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(dto)))
                .andExpect(status().isForbidden());
    }

    // -------------------
    // PATCH /patients/{id}
    // -------------------

    @Test
    @WithMockUser(roles = {"ADMIN"})
    void updatePatient_success_returns200() throws Exception {
        PatientUpdateDTO dto = createDefaultPatientUpdateDTO();
        dto.setFirstName("UpdatedName");

        mockMvc.perform(patch("/patients/" + savedPatient.getId())
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(dto)))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.firstName").value("UpdatedName"));
    }

    @Test
    @WithMockUser(roles = {"ADMIN"})
    void updatePatient_notFound_returns404() throws Exception {
        PatientUpdateDTO dto = createDefaultPatientUpdateDTO();

        mockMvc.perform(patch("/patients/9999999999")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(dto)))
                .andExpect(status().isNotFound());
    }

    @Test
    @WithMockUser(roles = {"ADMIN"})
    void updatePatient_duplicateEmail_returns409() throws Exception {
        Patient otherPatient = createDefaultPatient();
        otherPatient.setEmail("other@example.com");
        otherPatient = patientRepository.save(otherPatient);

        PatientUpdateDTO dto = createDefaultPatientUpdateDTO();
        dto.setEmail(otherPatient.getEmail());

        mockMvc.perform(patch("/patients/" + savedPatient.getId())
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(objectMapper.writeValueAsString(dto)))
                .andExpect(status().isConflict());
    }

    // -------------------
    // DELETE /patients/{id}
    // -------------------

    @Test
    @WithMockUser(roles = {"ADMIN"})
    void deletePatient_success_returns204() throws Exception {
        mockMvc.perform(delete("/patients/" + savedPatient.getId()))
                .andExpect(status().isNoContent());
    }

    @Test
    @WithMockUser(roles = {"ADMIN"})
    void deletePatient_nonExistent_returnsNoContent() throws Exception {
        mockMvc.perform(delete("/patients/9999999999"))
                .andExpect(status().isNoContent());
    }

    @Test
    @WithMockUser(roles = {"DOCTOR"})
    void deletePatient_roleWithoutAccess_returns403() throws Exception {
        mockMvc.perform(delete("/patients/" + savedPatient.getId()))
                .andExpect(status().isForbidden());
    }
}