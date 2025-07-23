package com.ehrblockchain.healthrecord.model;

import com.fasterxml.jackson.annotation.JsonBackReference;
import jakarta.persistence.*;

@Entity
@Table(name = "vitals")
public class Vitals {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String bloodPressure;
    private Double temperature;
    private Integer heartRate;
    private Integer respiratoryRate;
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
