package com.ehrblockchain.patient.model;

import java.time.LocalDate;
import java.time.LocalDateTime;

import jakarta.persistence.*;

import jakarta.validation.constraints.*;

import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.UpdateTimestamp;

import com.ehrblockchain.healthrecord.model.HealthRecord;
import com.ehrblockchain.user.model.User;
import com.ehrblockchain.security.encryption.ColumnEncryptionConverter;

@Entity
@Table(name = "patients",
        indexes = {@Index(name = "idx_patient_email", columnList = "email")}
)
public class Patient {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id", nullable = false, unique = true)
    private Long id;

    @OneToOne(cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.LAZY)
    @JoinColumn(name = "ehr_id", referencedColumnName = "id")
    private HealthRecord healthRecord;

    @OneToOne(mappedBy = "patient", fetch = FetchType.LAZY)
    private User user;

    @CreationTimestamp
    @Column(name = "created_at", nullable = false, updatable = false)
    private LocalDateTime createdAt;

    @UpdateTimestamp
    @Column(name = "updated_at")
    private LocalDateTime updatedAt;

    @Size(max = 100)
    @Column(name = "first_name")
    @Convert(converter = ColumnEncryptionConverter.class)
    private String firstName;

    @Size(max = 100)
    @Column(name = "last_name")
    @Convert(converter = ColumnEncryptionConverter.class)
    private String lastName;

    @Past
    @Column(name = "date_of_birth")
    private LocalDate dateOfBirth;

    @Size(max = 100)
    @Column(name = "gender")
    @Convert(converter = ColumnEncryptionConverter.class)
    private String gender;

    @Min(0)
    @Max(300)
    @Column(name = "height")
    private Double height;

    @Min(0)
    @Max(500)
    @Column(name = "weight")
    private Double weight;

    // Matches one of the blood types A, B, AB, or O followed by either a - or +
    @Pattern(regexp = "^(A|B|AB|O)[-+]$")
    @Column(name = "blood_type")
    @Convert(converter = ColumnEncryptionConverter.class)
    private String bloodType;

    // Matches a phone number of 7–15 digits, optionally starting with a +
    @Pattern(regexp = "\\+?[0-9]{7,15}")
    @Column(name = "phone_number")
    @Convert(converter = ColumnEncryptionConverter.class)
    private String phoneNumber;

    @Email
    @Size(min = 5, max = 254)
    @Column(name = "email", unique = true)
    private String email;

    @Size(max = 100)
    @Column(name = "emergency_contact")
    @Convert(converter = ColumnEncryptionConverter.class)
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

    public void setHealthRecord(HealthRecord healthRecord) {
        this.healthRecord = healthRecord;
    }

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

    public Address getAddress() {
        return address;
    }

    public void setAddress(Address address) {
        this.address = address;
    }

    public Insurance getInsurance() {
        return insurance;
    }

    public void setInsurance(Insurance insurance) {
        this.insurance = insurance;
    }

    public String getBloodType() {
        return bloodType;
    }

    public void setBloodType(String bloodType) {
        this.bloodType = bloodType;
    }

    public LocalDateTime getCreatedAt() {
        return createdAt;
    }

    public LocalDateTime getUpdatedAt() {
        return updatedAt;
    }

    public void setCreatedAt(LocalDateTime createdAt) {
        this.createdAt = createdAt;
    }

    public void setUpdatedAt(LocalDateTime updatedAt) {
        this.updatedAt = updatedAt;
    }

    @Override
    public String toString() {
        return "Patient{" +
                "firstName='" + firstName + '\'' +
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
                ", createdAt=" + (createdAt != null ? createdAt.toString() : null) +
                ", updatedAt=" + (updatedAt != null ? updatedAt.toString() : null) +
                '}';
    }
}