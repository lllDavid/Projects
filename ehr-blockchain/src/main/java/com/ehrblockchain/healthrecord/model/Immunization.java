package com.ehrblockchain.healthrecord.model;

import java.time.LocalDate;

import jakarta.persistence.*;

import jakarta.validation.constraints.Size;

import com.fasterxml.jackson.annotation.JsonBackReference;

@Entity
@Table(name = "immunizations")
public class Immunization {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Size(max = 255)
    private String vaccineName;

    private LocalDate dateAdministered;

    @Size(max = 255)
    private String provider;

    @ManyToOne(fetch = FetchType.LAZY)
    @JsonBackReference
    @JoinColumn(name = "health_record_id", nullable = false)
    private HealthRecord healthRecord;

    public Immunization() {
    }

    public Immunization(String vaccineName, LocalDate dateAdministered, String provider) {
        this.vaccineName = vaccineName;
        this.dateAdministered = dateAdministered;
        this.provider = provider;
    }

    public Long getId() {
        return id;
    }

    public String getVaccineName() {
        return vaccineName;
    }

    public void setVaccineName(String vaccineName) {
        this.vaccineName = vaccineName;
    }

    public LocalDate getDateAdministered() {
        return dateAdministered;
    }

    public void setDateAdministered(LocalDate dateAdministered) {
        this.dateAdministered = dateAdministered;
    }

    public String getProvider() {
        return provider;
    }

    public void setProvider(String provider) {
        this.provider = provider;
    }

    public HealthRecord getHealthRecord() {
        return healthRecord;
    }

    public void setHealthRecord(HealthRecord healthRecord) {
        this.healthRecord = healthRecord;
    }

    @Override
    public String toString() {
        return "Immunization{" +
                "id=" + id +
                ", vaccineName='" + vaccineName + '\'' +
                ", dateAdministered=" + dateAdministered +
                ", provider='" + provider + '\'' +
                '}';
    }
}