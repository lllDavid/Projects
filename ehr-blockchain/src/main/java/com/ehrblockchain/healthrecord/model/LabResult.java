package com.ehrblockchain.healthrecord.model;

import java.time.LocalDate;

import jakarta.persistence.*;

import jakarta.validation.constraints.Size;

import com.fasterxml.jackson.annotation.JsonBackReference;

import com.ehrblockchain.security.encryption.ColumnEncryptionConverter;

@Entity
@Table(name = "lab_results")
public class LabResult {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Size(max = 255)
    @Convert(converter = ColumnEncryptionConverter.class)
    private String testName;

    private LocalDate testDate;

    @Size(max = 500)
    @Convert(converter = ColumnEncryptionConverter.class)
    private String result;

    @ManyToOne(fetch = FetchType.LAZY)
    @JsonBackReference
    @JoinColumn(name = "health_record_id", nullable = false)
    private HealthRecord healthRecord;

    public LabResult() {
    }

    public LabResult(String testName, LocalDate testDate, String result) {
        this.testName = testName;
        this.testDate = testDate;
        this.result = result;
    }

    public Long getId() {
        return id;
    }

    public String getTestName() {
        return testName;
    }

    public void setTestName(String testName) {
        this.testName = testName;
    }

    public LocalDate getTestDate() {
        return testDate;
    }

    public void setTestDate(LocalDate testDate) {
        this.testDate = testDate;
    }

    public String getResult() {
        return result;
    }

    public void setResult(String result) {
        this.result = result;
    }

    public HealthRecord getHealthRecord() {
        return healthRecord;
    }

    public void setHealthRecord(HealthRecord healthRecord) {
        this.healthRecord = healthRecord;
    }

    @Override
    public String toString() {
        return "LabResult{" +
                "id=" + id +
                ", testName='" + testName + '\'' +
                ", testDate=" + testDate +
                ", result='" + result + '\'' +
                '}';
    }
}