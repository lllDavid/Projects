package com.ehrblockchain.healthrecord.model;

import com.fasterxml.jackson.annotation.JsonBackReference;
import jakarta.persistence.*;

import java.time.LocalDate;

@Entity
@Table(name = "medical_history")
public class MedicalHistory {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String condition;
    private LocalDate diagnosisDate;
    private String notes;

    @ManyToOne(fetch = FetchType.LAZY)
    @JsonBackReference
    @JoinColumn(name = "health_record_id", nullable = false)
    private HealthRecord healthRecord;

    public MedicalHistory() {
    }

    public MedicalHistory(String condition, LocalDate diagnosisDate, String notes) {
        this.condition = condition;
        this.diagnosisDate = diagnosisDate;
        this.notes = notes;
    }

    public Long getId() {
        return id;
    }

    public String getCondition() {
        return condition;
    }

    public void setCondition(String condition) {
        this.condition = condition;
    }

    public LocalDate getDiagnosisDate() {
        return diagnosisDate;
    }

    public void setDiagnosisDate(LocalDate diagnosisDate) {
        this.diagnosisDate = diagnosisDate;
    }

    public String getNotes() {
        return notes;
    }

    public void setNotes(String notes) {
        this.notes = notes;
    }

    public HealthRecord getHealthRecord() {
        return healthRecord;
    }

    public void setHealthRecord(HealthRecord healthRecord) {
        this.healthRecord = healthRecord;
    }

    @Override
    public String toString() {
        return "MedicalHistory{" +
                "id=" + id +
                ", condition='" + condition + '\'' +
                ", diagnosisDate=" + diagnosisDate +
                ", notes='" + notes + '\'' +
                '}';
    }
}
