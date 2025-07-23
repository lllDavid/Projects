package com.ehrblockchain.healthrecord.model;

import com.fasterxml.jackson.annotation.JsonBackReference;
import jakarta.persistence.*;

import java.time.LocalDate;

@Entity
@Table(name = "cbc_tests")
public class CBC {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private LocalDate testDate;
    private Integer redBloodCellCount;
    private Integer whiteBloodCellCount;
    private Double hemoglobin;
    private Double hematocrit;
    private Integer plateletCount;

    @ManyToOne(fetch = FetchType.LAZY)
    @JsonBackReference
    @JoinColumn(name = "health_record_id", nullable = false)
    private HealthRecord healthRecord;

    public CBC() {
    }

    public CBC(LocalDate testDate, Integer redBloodCellCount, Integer whiteBloodCellCount,
               Double hemoglobin, Double hematocrit, Integer plateletCount, HealthRecord healthRecord) {
        this.testDate = testDate;
        this.redBloodCellCount = redBloodCellCount;
        this.whiteBloodCellCount = whiteBloodCellCount;
        this.hemoglobin = hemoglobin;
        this.hematocrit = hematocrit;
        this.plateletCount = plateletCount;
        this.healthRecord = healthRecord;
    }

    public Long getId() {
        return id;
    }

    public LocalDate getTestDate() {
        return testDate;
    }

    public void setTestDate(LocalDate testDate) {
        this.testDate = testDate;
    }

    public Integer getRedBloodCellCount() {
        return redBloodCellCount;
    }

    public void setRedBloodCellCount(Integer redBloodCellCount) {
        this.redBloodCellCount = redBloodCellCount;
    }

    public Integer getWhiteBloodCellCount() {
        return whiteBloodCellCount;
    }

    public void setWhiteBloodCellCount(Integer whiteBloodCellCount) {
        this.whiteBloodCellCount = whiteBloodCellCount;
    }

    public Double getHemoglobin() {
        return hemoglobin;
    }

    public void setHemoglobin(Double hemoglobin) {
        this.hemoglobin = hemoglobin;
    }

    public Double getHematocrit() {
        return hematocrit;
    }

    public void setHematocrit(Double hematocrit) {
        this.hematocrit = hematocrit;
    }

    public Integer getPlateletCount() {
        return plateletCount;
    }

    public void setPlateletCount(Integer plateletCount) {
        this.plateletCount = plateletCount;
    }

    public HealthRecord getHealthRecord() {
        return healthRecord;
    }

    public void setHealthRecord(HealthRecord healthRecord) {
        this.healthRecord = healthRecord;
    }

    @Override
    public String toString() {
        return "CBC{" +
                "id=" + id +
                ", testDate=" + testDate +
                ", redBloodCellCount=" + redBloodCellCount +
                ", whiteBloodCellCount=" + whiteBloodCellCount +
                ", hemoglobin=" + hemoglobin +
                ", hematocrit=" + hematocrit +
                ", plateletCount=" + plateletCount +
                '}';
    }
}