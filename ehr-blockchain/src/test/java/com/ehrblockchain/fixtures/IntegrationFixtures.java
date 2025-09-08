package com.ehrblockchain.fixtures;

import java.time.LocalDate;
import java.util.ArrayList;

import org.springframework.test.util.ReflectionTestUtils;

import com.ehrblockchain.healthrecord.dto.HealthRecordCreateDTO;
import com.ehrblockchain.healthrecord.dto.HealthRecordDTO;
import com.ehrblockchain.healthrecord.dto.HealthRecordUpdateDTO;
import com.ehrblockchain.healthrecord.model.HealthRecord;
import com.ehrblockchain.patient.dto.*;
import com.ehrblockchain.patient.model.*;
import com.ehrblockchain.security.role.RoleEnum;
import com.ehrblockchain.security.role.model.Role;
import com.ehrblockchain.user.dto.UserCreateDTO;
import com.ehrblockchain.user.dto.UserDTO;
import com.ehrblockchain.user.dto.UserUpdateDTO;
import com.ehrblockchain.user.model.User;

public class IntegrationFixtures {

    public static final String DEFAULT_FIRST_NAME = "John";
    public static final String DEFAULT_LAST_NAME = "Doe";
    public static final String DEFAULT_EMAIL = "john.doe@example.com";
    public static final String DEFAULT_PHONE = "+1234567890";
    public static final String DEFAULT_GENDER = "Male";
    public static final String DEFAULT_BLOOD_TYPE = "O+";
    public static final Double DEFAULT_HEIGHT = 180.0;
    public static final Double DEFAULT_WEIGHT = 75.0;
    public static final LocalDate DEFAULT_DOB = LocalDate.of(1990, 1, 1);
    public static final String DEFAULT_EMERGENCY_CONTACT = "Jane Doe";
    public static final String DEFAULT_USER_PASSWORD = "PpAasword123@!#";
    public static final RoleEnum DEFAULT_ROLE = RoleEnum.PATIENT;
    public static final Long DEFAULT_USER_ID = 1L;
    public static final Long DEFAULT_PATIENT_ID = 1L;

    public static HealthRecord createDefaultHealthRecord() {
        return new HealthRecord(
                null,
                LocalDate.now(),
                new ArrayList<>(),
                new ArrayList<>(),
                new ArrayList<>(),
                new ArrayList<>(),
                new ArrayList<>(),
                new ArrayList<>(),
                new ArrayList<>(),
                new ArrayList<>(),
                new ArrayList<>(),
                new ArrayList<>(),
                new ArrayList<>(),
                new ArrayList<>(),
                new ArrayList<>()
        );
    }

    public static Address createDefaultAddress() {
        return new Address(
                "123 Main St",
                "City",
                "State",
                "12345",
                "Country"
        );
    }

    public static Insurance createDefaultInsurance() {
        return new Insurance(
                "ACME Health",
                "INS123456",
                "GRP7890",
                LocalDate.of(2020, 1, 1),
                LocalDate.of(2030, 12, 31)
        );
    }

    public static Patient createDefaultPatient() {
        return new Patient(
                createDefaultHealthRecord(),
                DEFAULT_FIRST_NAME,
                DEFAULT_LAST_NAME,
                DEFAULT_DOB,
                DEFAULT_GENDER,
                DEFAULT_PHONE,
                DEFAULT_EMAIL,
                createDefaultAddress(),
                createDefaultInsurance(),
                DEFAULT_HEIGHT,
                DEFAULT_WEIGHT,
                DEFAULT_BLOOD_TYPE,
                DEFAULT_EMERGENCY_CONTACT
        );
    }

    public static HealthRecordDTO createDefaultHealthRecordDTO() {
        return new HealthRecordDTO(
                new ArrayList<>(),
                new ArrayList<>(),
                new ArrayList<>(),
                new ArrayList<>(),
                new ArrayList<>(),
                new ArrayList<>(),
                new ArrayList<>(),
                new ArrayList<>(),
                new ArrayList<>(),
                new ArrayList<>(),
                new ArrayList<>(),
                new ArrayList<>(),
                new ArrayList<>()
        );
    }

    public static HealthRecordCreateDTO createDefaultHealthRecordCreateDTO() {
        HealthRecordCreateDTO dto = new HealthRecordCreateDTO();
        dto.setRecordDate(LocalDate.now());
        dto.setNotes(new ArrayList<>());
        dto.setDiagnoses(new ArrayList<>());
        dto.setTreatmentPlans(new ArrayList<>());
        dto.setPrescriptions(new ArrayList<>());
        dto.setVitals(new ArrayList<>());
        dto.setCbcTests(new ArrayList<>());
        dto.setAllergies(new ArrayList<>());
        dto.setLabResults(new ArrayList<>());
        dto.setImmunizations(new ArrayList<>());
        dto.setMedicalHistory(new ArrayList<>());
        dto.setFamilyHistory(new ArrayList<>());
        dto.setEncounters(new ArrayList<>());
        dto.setProcedures(new ArrayList<>());
        return dto;
    }

    public static HealthRecordUpdateDTO createDefaultHealthRecordUpdateDTO() {
        HealthRecordUpdateDTO dto = new HealthRecordUpdateDTO();
        dto.setNotes(new ArrayList<>());
        dto.setDiagnoses(new ArrayList<>());
        dto.setTreatmentPlans(new ArrayList<>());
        dto.setPrescriptions(new ArrayList<>());
        dto.setVitals(new ArrayList<>());
        dto.setCbcTests(new ArrayList<>());
        dto.setAllergies(new ArrayList<>());
        dto.setLabResults(new ArrayList<>());
        dto.setImmunizations(new ArrayList<>());
        dto.setMedicalHistory(new ArrayList<>());
        dto.setFamilyHistory(new ArrayList<>());
        dto.setEncounters(new ArrayList<>());
        dto.setProcedures(new ArrayList<>());
        return dto;
    }

    public static AddressDTO createDefaultAddressDTO() {
        Address a = createDefaultAddress();
        AddressDTO dto = new AddressDTO();
        dto.setStreet(a.getStreet());
        dto.setCity(a.getCity());
        dto.setState(a.getState());
        dto.setPostalCode(a.getPostalCode());
        dto.setCountry(a.getCountry());
        return dto;
    }

    public static InsuranceDTO createDefaultInsuranceDTO() {
        Insurance i = createDefaultInsurance();
        InsuranceDTO dto = new InsuranceDTO();
        dto.setProviderName(i.getProviderName());
        dto.setPolicyNumber(i.getPolicyNumber());
        dto.setGroupNumber(i.getGroupNumber());
        dto.setCoverageStartDate(i.getCoverageStartDate());
        dto.setCoverageEndDate(i.getCoverageEndDate());
        return dto;
    }

    public static PatientDTO createDefaultPatientDTO() {
        Patient p = createDefaultPatient();
        return new PatientDTO(
                null,
                p.getFirstName(),
                p.getLastName(),
                p.getDateOfBirth(),
                p.getGender(),
                p.getHeight(),
                p.getWeight(),
                p.getBloodType(),
                p.getPhoneNumber(),
                p.getEmail(),
                p.getEmergencyContact(),
                createDefaultAddressDTO(),
                createDefaultInsuranceDTO()
        );
    }

    public static PatientCreateDTO createDefaultPatientCreateDTO() {
        Patient p = createDefaultPatient();
        PatientCreateDTO dto = new PatientCreateDTO();
        dto.setFirstName(p.getFirstName());
        dto.setLastName(p.getLastName());
        dto.setDateOfBirth(p.getDateOfBirth());
        dto.setGender(p.getGender());
        dto.setHeight(p.getHeight());
        dto.setWeight(p.getWeight());
        dto.setBloodType(p.getBloodType());
        dto.setPhoneNumber(p.getPhoneNumber());
        dto.setEmail(p.getEmail());
        dto.setEmergencyContact(p.getEmergencyContact());
        dto.setAddress(createDefaultAddressDTO());
        dto.setInsurance(createDefaultInsuranceDTO());
        dto.setHealthRecord(createDefaultHealthRecordCreateDTO());
        return dto;
    }

    public static PatientUpdateDTO createDefaultPatientUpdateDTO() {
        PatientUpdateDTO dto = new PatientUpdateDTO();
        dto.setFirstName("UpdatedFirstName");
        dto.setLastName("UpdatedLastName");
        dto.setDateOfBirth(DEFAULT_DOB);
        dto.setGender(DEFAULT_GENDER);
        dto.setHeight(DEFAULT_HEIGHT);
        dto.setWeight(DEFAULT_WEIGHT);
        dto.setBloodType(DEFAULT_BLOOD_TYPE);
        dto.setPhoneNumber(DEFAULT_PHONE);
        dto.setEmail("updated@example.com");
        dto.setEmergencyContact("987-654-3210");
        dto.setAddress(createDefaultAddressDTO());
        dto.setInsurance(createDefaultInsuranceDTO());
        return dto;
    }

    public static Role createDefaultRole() {
        Role role = new Role();
        role.setName(DEFAULT_ROLE);
        role.setDescription("Role");
        ReflectionTestUtils.setField(role, "id", 1);
        return role;
    }

    public static User createDefaultUser() {
        return new User(
                "John",
                "Doe",
                "john.doe@example.com",
                DEFAULT_USER_PASSWORD,
                createDefaultRole()
        );
    }

    public static UserDTO createDefaultUserDTO() {
        User user = createDefaultUser();
        return new UserDTO(
                DEFAULT_USER_ID,
                user.getFirstName(),
                user.getLastName(),
                user.getEmail(),
                user.getRole().getName().name(),
                DEFAULT_PATIENT_ID
        );
    }

    public static UserCreateDTO createDefaultUserCreateDTO() {
        UserCreateDTO dto = new UserCreateDTO();
        dto.setFirstName("John");
        dto.setLastName("Doe");
        dto.setEmail("john.doe@example.com");
        dto.setPassword(DEFAULT_USER_PASSWORD);
        return dto;
    }

    public static UserUpdateDTO createDefaultUserUpdateDTO() {
        UserUpdateDTO dto = new UserUpdateDTO();
        dto.setFirstName("UpdatedFirstName");
        dto.setLastName("UpdatedLastName");
        dto.setEmail("updated@example.com");
        dto.setPassword("NnEewpassword123@!#");
        return dto;
    }
}