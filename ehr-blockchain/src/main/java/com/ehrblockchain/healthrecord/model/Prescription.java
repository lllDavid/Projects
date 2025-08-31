package com.ehrblockchain.healthrecord.model;

import jakarta.persistence.*;

import jakarta.validation.constraints.Size;

import com.fasterxml.jackson.annotation.JsonBackReference;

import com.ehrblockchain.security.encryption.ColumnEncryptionConverter;

@Entity
@Table(name = "prescriptions")
public class Prescription {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Size(max = 255)
    @Convert(converter = ColumnEncryptionConverter.class)
    private String drugName;

    @Size(max = 100)
    @Convert(converter = ColumnEncryptionConverter.class)
    private String dosage;

    @Size(max = 100)
    @Convert(converter = ColumnEncryptionConverter.class)
    private String frequency;

    @Size(max = 100)
    @Convert(converter = ColumnEncryptionConverter.class)
    private String duration;

    @ManyToOne(fetch = FetchType.LAZY)
    @JsonBackReference
    @JoinColumn(name = "health_record_id", nullable = false)
    private HealthRecord healthRecord;

    public Prescription() {
    }

    public Prescription(String drugName, String dosage, String frequency, String duration) {
        this.drugName = drugName;
        this.dosage = dosage;
        this.frequency = frequency;
        this.duration = duration;
    }

    public Long getId() {
        return id;
    }

    public String getDrugName() {
        return drugName;
    }

    public void setDrugName(String drugName) {
        this.drugName = drugName;
    }

    public String getDosage() {
        return dosage;
    }

    public void setDosage(String dosage) {
        this.dosage = dosage;
    }

    public String getFrequency() {
        return frequency;
    }

    public void setFrequency(String frequency) {
        this.frequency = frequency;
    }

    public String getDuration() {
        return duration;
    }

    public void setDuration(String duration) {
        this.duration = duration;
    }

    public HealthRecord getHealthRecord() {
        return healthRecord;
    }

    public void setHealthRecord(HealthRecord healthRecord) {
        this.healthRecord = healthRecord;
    }

    @Override
    public String toString() {
        return "Prescription{" +
                "id=" + id +
                ", drugName='" + drugName + '\'' +
                ", dosage='" + dosage + '\'' +
                ", frequency='" + frequency + '\'' +
                ", duration='" + duration + '\'' +
                '}';
    }
}