package com.ehrblockchain.healthrecord.model;

import jakarta.persistence.*;

import jakarta.validation.constraints.Size;

import com.fasterxml.jackson.annotation.JsonBackReference;

import com.ehrblockchain.security.encryption.ColumnEncryptionConverter;

@Entity
@Table(name = "allergies")
public class Allergy {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Size(max = 200)
    @Column(name = "allergen")
    @Convert(converter = ColumnEncryptionConverter.class)
    private String allergen;

    @Size(max = 300)
    @Column(name = "reaction")
    @Convert(converter = ColumnEncryptionConverter.class)
    private String reaction;

    @Size(max = 100)
    @Column(name = "severity")
    @Convert(converter = ColumnEncryptionConverter.class)
    private String severity;

    @ManyToOne(fetch = FetchType.LAZY)
    @JsonBackReference
    @JoinColumn(name = "health_record_id", nullable = false)
    private HealthRecord healthRecord;

    public Allergy() {
    }

    public Allergy(String allergen, String reaction, String severity) {
        this.allergen = allergen;
        this.reaction = reaction;
        this.severity = severity;
    }

    public Long getId() {
        return id;
    }

    public HealthRecord getHealthRecord() {
        return healthRecord;
    }

    public void setHealthRecord(HealthRecord healthRecord) {
        this.healthRecord = healthRecord;
    }

    public String getAllergen() {
        return allergen;
    }

    public void setAllergen(String allergen) {
        this.allergen = allergen;
    }

    public String getReaction() {
        return reaction;
    }

    public void setReaction(String reaction) {
        this.reaction = reaction;
    }

    public String getSeverity() {
        return severity;
    }

    public void setSeverity(String severity) {
        this.severity = severity;
    }

    @Override
    public String toString() {
        return "Allergy{" +
                "id=" + id +
                ", allergen='" + allergen + '\'' +
                ", reaction='" + reaction + '\'' +
                ", severity='" + severity + '\'' +
                '}';
    }
}