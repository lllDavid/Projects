package com.ehrblockchain.healthrecord.model;

import java.time.LocalDate;

import jakarta.persistence.*;

import jakarta.validation.constraints.Size;

import com.fasterxml.jackson.annotation.JsonBackReference;

import com.ehrblockchain.security.encryption.ColumnEncryptionConverter;

@Entity
@Table(name = "encounters")
public class Encounter {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "encounter_date")
    private LocalDate encounterDate;

    @Size(max = 255)
    @Convert(converter = ColumnEncryptionConverter.class)
    private String provider;

    @Size(max = 1000)
    @Convert(converter = ColumnEncryptionConverter.class)
    private String reason;

    @ManyToOne(fetch = FetchType.LAZY)
    @JsonBackReference
    @JoinColumn(name = "health_record_id", nullable = false)
    private HealthRecord healthRecord;

    public Encounter() {
    }

    public Encounter(LocalDate encounterDate, String provider, String reason) {
        this.encounterDate = encounterDate;
        this.provider = provider;
        this.reason = reason;
    }

    public Long getId() {
        return id;
    }

    public LocalDate getEncounterDate() {
        return encounterDate;
    }

    public void setEncounterDate(LocalDate encounterDate) {
        this.encounterDate = encounterDate;
    }

    public String getProvider() {
        return provider;
    }

    public void setProvider(String provider) {
        this.provider = provider;
    }

    public String getReason() {
        return reason;
    }

    public void setReason(String reason) {
        this.reason = reason;
    }

    public HealthRecord getHealthRecord() {
        return healthRecord;
    }

    public void setHealthRecord(HealthRecord healthRecord) {
        this.healthRecord = healthRecord;
    }

    @Override
    public String toString() {
        return "Encounter{" +
                "id=" + id +
                ", encounterDate=" + encounterDate +
                ", provider='" + provider + '\'' +
                ", reason='" + reason + '\'' +
                '}';
    }
}