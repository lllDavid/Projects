package com.ehrblockchain.healthrecord.dto;

import java.time.LocalDate;

public class CBCDTO {

    private Long id;
    private LocalDate testDate;
    private Integer redBloodCellCount;
    private Integer whiteBloodCellCount;
    private Double hemoglobin;
    private Double hematocrit;
    private Integer plateletCount;

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
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
}