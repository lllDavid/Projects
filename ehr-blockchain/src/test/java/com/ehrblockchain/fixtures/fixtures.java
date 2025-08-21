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

public class fixtures {

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

    public static HealthRecord createDefaultHealthRecord() {
        HealthRecord record = new HealthRecord(
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
        ReflectionTestUtils.setField(record, "id", 1L);
        return record;
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
        Patient patient = new Patient(
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
        ReflectionTestUtils.setField(patient, "id", 1L);
        return patient;
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
        Address address = createDefaultAddress();
        AddressDTO dto = new AddressDTO();
        dto.setStreet(address.getStreet());
        dto.setCity(address.getCity());
        dto.setState(address.getState());
        dto.setPostalCode(address.getPostalCode());
        dto.setCountry(address.getCountry());
        return dto;
    }

    public static InsuranceDTO createDefaultInsuranceDTO() {
        Insurance insurance = createDefaultInsurance();
        InsuranceDTO dto = new InsuranceDTO();
        dto.setProviderName(insurance.getProviderName());
        dto.setPolicyNumber(insurance.getPolicyNumber());
        dto.setGroupNumber(insurance.getGroupNumber());
        dto.setCoverageStartDate(insurance.getCoverageStartDate());
        dto.setCoverageEndDate(insurance.getCoverageEndDate());
        return dto;
    }

    public static PatientDTO createDefaultPatientDTO() {
        Patient patient = createDefaultPatient();
        return new PatientDTO(
                patient.getFirstName(),
                patient.getLastName(),
                patient.getDateOfBirth(),
                patient.getGender(),
                patient.getHeight(),
                patient.getWeight(),
                patient.getBloodType(),
                patient.getPhoneNumber(),
                patient.getEmail(),
                patient.getEmergencyContact(),
                createDefaultAddressDTO(),
                createDefaultInsuranceDTO()
        );
    }

    public static PatientCreateDTO createDefaultPatientCreateDTO() {
        Patient patient = createDefaultPatient();
        PatientCreateDTO createDTO = new PatientCreateDTO();
        createDTO.setFirstName(patient.getFirstName());
        createDTO.setLastName(patient.getLastName());
        createDTO.setDateOfBirth(patient.getDateOfBirth());
        createDTO.setGender(patient.getGender());
        createDTO.setHeight(patient.getHeight());
        createDTO.setWeight(patient.getWeight());
        createDTO.setBloodType(patient.getBloodType());
        createDTO.setPhoneNumber(patient.getPhoneNumber());
        createDTO.setEmail(patient.getEmail());
        createDTO.setEmergencyContact(patient.getEmergencyContact());
        createDTO.setAddress(createDefaultAddressDTO());
        createDTO.setInsurance(createDefaultInsuranceDTO());
        createDTO.setHealthRecord(createDefaultHealthRecordCreateDTO());
        return createDTO;
    }

    public static PatientUpdateDTO createDefaultPatientUpdateDTO() {
        PatientUpdateDTO updateDTO = new PatientUpdateDTO();
        updateDTO.setFirstName("UpdatedFirstName");
        updateDTO.setLastName("UpdatedLastName");
        updateDTO.setDateOfBirth(LocalDate.of(1990, 1, 1));
        updateDTO.setGender("Male");
        updateDTO.setHeight(180.0);
        updateDTO.setWeight(75.0);
        updateDTO.setBloodType("O+");
        updateDTO.setPhoneNumber("123-456-7890");
        updateDTO.setEmail("updated@example.com");
        updateDTO.setEmergencyContact("987-654-3210");
        updateDTO.setAddress(createDefaultAddressDTO());
        updateDTO.setInsurance(createDefaultInsuranceDTO());
        return updateDTO;
    }
}