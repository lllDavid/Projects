package com.ehrblockchain.patient.model;

import java.time.LocalDate;

import jakarta.persistence.*;

import com.fasterxml.jackson.annotation.JsonIgnore;
import com.ehrblockchain.healthrecord.model.HealthRecord;

@Entity
@Table(name = "patients",
        indexes = {@Index(name = "idx_patient_email", columnList = "email")}
)
public class Patient {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id", nullable = false, unique = true)
    private Long id;

    @OneToOne(cascade = CascadeType.ALL, orphanRemoval = true)
    @JoinColumn(name = "ehr_id", referencedColumnName = "id")
    private HealthRecord healthRecord;

    @Column(name = "first_name")
    private String firstName;

    @Column(name = "last_name")
    private String lastName;

    @Column(name = "date_of_birth")
    private LocalDate dateOfBirth;

    @Column(name = "gender")
    private String gender;

    @Column(name = "height")
    private Double height;

    @Column(name = "weight")
    private Double weight;

    @Column(name = "blood_type")
    private String bloodType;

    @Column(name = "phone_number")
    private String phoneNumber;

    @Column(name = "email", unique = true)
    private String email;

    @Column(name = "emergency_contact")
    private String emergencyContact;

    @Embedded
    private Address address;

    @Embedded
    private Insurance insurance;

    public Patient() {
    }

    public Patient(HealthRecord healthRecord, String firstName, String lastName,
                   LocalDate dateOfBirth, String gender, String phoneNumber, String email,
                   Address address, Insurance insurance,
                   Double height, Double weight, String bloodType, String emergencyContact) {
        this.healthRecord = healthRecord;
        this.firstName = firstName;
        this.lastName = lastName;
        this.dateOfBirth = dateOfBirth;
        this.gender = gender;
        this.height = height;
        this.weight = weight;
        this.phoneNumber = phoneNumber;
        this.email = email;
        this.emergencyContact = emergencyContact;
        this.address = address;
        this.insurance = insurance;
        this.bloodType = bloodType;
    }

    public Long getId() {
        return id;
    }

    public Long getEhrId() {
        return healthRecord != null ? healthRecord.getId() : null;
    }

    public HealthRecord getHealthRecord() {
        return healthRecord;
    }

    public String getFirstName() {
        return firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public LocalDate getDateOfBirth() {
        return dateOfBirth;
    }

    public String getGender() {
        return gender;
    }

    public Double getHeight() {
        return height;
    }

    public Double getWeight() {
        return weight;
    }

    public String getPhoneNumber() {
        return phoneNumber;
    }

    public String getEmail() {
        return email;
    }

    public String getEmergencyContact() {
        return emergencyContact;
    }

    public Address getAddress() {
        return address;
    }

    public Insurance getInsurance() {
        return insurance;
    }

    public void setHealthRecord(HealthRecord healthRecord) {
        this.healthRecord = healthRecord;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public void setDateOfBirth(LocalDate dateOfBirth) {
        this.dateOfBirth = dateOfBirth;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    public void setHeight(Double height) {
        this.height = height;
    }

    public void setWeight(Double weight) {
        this.weight = weight;
    }

    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public void setEmergencyContact(String emergencyContact) {
        this.emergencyContact = emergencyContact;
    }

    public void setAddress(Address address) {
        this.address = address;
    }

    public void setInsurance(Insurance insurance) {
        this.insurance = insurance;
    }

    public void updateFrom(Patient updatedPatient) {
        if (updatedPatient.firstName != null) this.firstName = updatedPatient.firstName;
        if (updatedPatient.lastName != null) this.lastName = updatedPatient.lastName;
        if (updatedPatient.dateOfBirth != null) this.dateOfBirth = updatedPatient.dateOfBirth;
        if (updatedPatient.gender != null) this.gender = updatedPatient.gender;
        if (updatedPatient.height != null) this.height = updatedPatient.height;
        if (updatedPatient.weight != null) this.weight = updatedPatient.weight;
        if (updatedPatient.bloodType != null) this.bloodType = updatedPatient.bloodType;
        if (updatedPatient.phoneNumber != null) this.phoneNumber = updatedPatient.phoneNumber;
        if (updatedPatient.email != null) this.email = updatedPatient.email;
        if (updatedPatient.emergencyContact != null) this.emergencyContact = updatedPatient.emergencyContact;
        if (updatedPatient.address != null) this.address = updatedPatient.address;
        if (updatedPatient.insurance != null) this.insurance = updatedPatient.insurance;
        if (updatedPatient.healthRecord != null) this.healthRecord = updatedPatient.healthRecord;
    }

    @Override
    public String toString() {
        return "Patient{" +
                "id='" + id + '\'' +
                ", ehrId='" + (healthRecord != null ? healthRecord.getId() : null) + '\'' +
                ", firstName='" + firstName + '\'' +
                ", lastName='" + lastName + '\'' +
                ", dateOfBirth=" + dateOfBirth +
                ", gender='" + gender + '\'' +
                ", height=" + height +
                ", weight=" + weight +
                ", phoneNumber='" + phoneNumber + '\'' +
                ", email='" + email + '\'' +
                ", emergencyContact='" + emergencyContact + '\'' +
                ", address=" + address +
                ", insurance=" + insurance +
                ", bloodType='" + bloodType + '\'' +
                '}';
    }
}