package com.ehrblockchain.patient.dto;

import java.time.LocalDate;

import com.ehrblockchain.healthrecord.dto.HealthRecordCreateDTO;

public class PatientCreateDTO {

    private String firstName;
    private String lastName;
    private LocalDate dateOfBirth;
    private String gender;
    private Double height;
    private Double weight;
    private String bloodType;
    private String phoneNumber;
    private String email;
    private String emergencyContact;
    private AddressDTO address;
    private InsuranceDTO insurance;
    private HealthRecordCreateDTO healthRecord;

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

    public LocalDate getDateOfBirth() {
        return dateOfBirth;
    }

    public void setDateOfBirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }

    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    public Double getHeight() {
        return height;
    }

    public void setHeight(Double height) {
        this.height = height;
    }

    public Double getWeight() {
        return weight;
    }

    public void setWeight(Double weight) {
        this.weight = weight;
    }

    public String getBloodType() {
        return bloodType;
    }

    public void setBloodType(String bloodType) {
        this.bloodType = bloodType;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getEmergencyContact() {
        return emergencyContact;
    }

    public void setEmergencyContact(String emergencyContact) {
        this.emergencyContact = emergencyContact;
    }

    public AddressDTO getAddress() {
        return address;
    }

    public void setAddress(AddressDTO address) {
        this.address = address;
    }

    public InsuranceDTO getInsurance() {
        return insurance;
    }

    public void setInsurance(InsuranceDTO insurance) {
        this.insurance = insurance;
    }

    public HealthRecordCreateDTO getHealthRecord() {
        return healthRecord;
    }

    public void setHealthRecord(HealthRecordCreateDTO healthRecord) {
        this.healthRecord = healthRecord;
    }

}