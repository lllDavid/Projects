package com.ehrblockchain.patient.model;

import java.time.LocalDate;

import jakarta.persistence.Embeddable;

@Embeddable
public class Insurance {
    private String providerName;
    private String policyNumber;
    private String groupNumber;
    private LocalDate coverageStartDate;
    private LocalDate coverageEndDate;

    public Insurance() {
    }

    public Insurance(String providerName, String policyNumber, String groupNumber,
                     LocalDate coverageStartDate, LocalDate coverageEndDate) {
        this.providerName = providerName;
        this.policyNumber = policyNumber;
        this.groupNumber = groupNumber;
        this.coverageStartDate = coverageStartDate;
        this.coverageEndDate = coverageEndDate;
    }

    public String getProviderName() {
        return providerName;
    }

    public String getPolicyNumber() {
        return policyNumber;
    }

    public String getGroupNumber() {
        return groupNumber;
    }

    public LocalDate getCoverageStartDate() {
        return coverageStartDate;
    }

    public LocalDate getCoverageEndDate() {
        return coverageEndDate;
    }

    public void setProviderName(String providerName) {
        this.providerName = providerName;
    }

    public void setPolicyNumber(String policyNumber) {
        this.policyNumber = policyNumber;
    }

    public void setGroupNumber(String groupNumber) {
        this.groupNumber = groupNumber;
    }

    public void setCoverageStartDate(LocalDate coverageStartDate) {
        this.coverageStartDate = coverageStartDate;
    }

    public void setCoverageEndDate(LocalDate coverageEndDate) {
        this.coverageEndDate = coverageEndDate;
    }

    @Override
    public String toString() {
        return "Insurance{" +
                "providerName='" + providerName + '\'' +
                ", policyNumber='" + policyNumber + '\'' +
                ", groupNumber='" + groupNumber + '\'' +
                ", coverageStartDate=" + coverageStartDate +
                ", coverageEndDate=" + coverageEndDate +
                '}';
    }
}