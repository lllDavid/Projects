package com.ehrblockchain.healthrecord.model;

import jakarta.persistence.*;

import jakarta.validation.constraints.*;

import com.fasterxml.jackson.annotation.JsonBackReference;

import com.ehrblockchain.security.encryption.ColumnEncryptionConverter;

@Entity
@Table(name = "vitals")
public class Vitals {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Size(max = 200)
    @Convert(converter = ColumnEncryptionConverter.class)
    private String bloodPressure;

    @DecimalMin(value = "25.0")
    @DecimalMax(value = "110.0")
    private Double temperature;

    @Min(30)
    @Max(200)
    private Integer heartRate;

    @Min(5)
    @Max(60)
    private Integer respiratoryRate;

    @Min(50)
    @Max(100)
    private Integer oxygenSaturation;

    @ManyToOne(fetch = FetchType.LAZY)
    @JsonBackReference
    @JoinColumn(name = "health_record_id", nullable = false)
    private HealthRecord healthRecord;

    public Vitals() {
    }

    public Vitals(HealthRecord healthRecord, String bloodPressure, Double temperature, Integer heartRate, Integer respiratoryRate, Integer oxygenSaturation) {
        this.healthRecord = healthRecord;
        this.bloodPressure = bloodPressure;
        this.temperature = temperature;
        this.heartRate = heartRate;
        this.respiratoryRate = respiratoryRate;
        this.oxygenSaturation = oxygenSaturation;
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

    public String getBloodPressure() {
        return bloodPressure;
    }

    public void setBloodPressure(String bloodPressure) {
        this.bloodPressure = bloodPressure;
    }

    public Double getTemperature() {
        return temperature;
    }

    public void setTemperature(Double temperature) {
        this.temperature = temperature;
    }

    public Integer getHeartRate() {
        return heartRate;
    }

    public void setHeartRate(Integer heartRate) {
        this.heartRate = heartRate;
    }

    public Integer getRespiratoryRate() {
        return respiratoryRate;
    }

    public void setRespiratoryRate(Integer respiratoryRate) {
        this.respiratoryRate = respiratoryRate;
    }

    public Integer getOxygenSaturation() {
        return oxygenSaturation;
    }

    public void setOxygenSaturation(Integer oxygenSaturation) {
        this.oxygenSaturation = oxygenSaturation;
    }

    @Override
    public String toString() {
        return "Vitals{" +
                "id=" + id +
                ", bloodPressure='" + bloodPressure + '\'' +
                ", temperature=" + temperature +
                ", heartRate=" + heartRate +
                ", respiratoryRate=" + respiratoryRate +
                ", oxygenSaturation=" + oxygenSaturation +
                '}';
    }
}