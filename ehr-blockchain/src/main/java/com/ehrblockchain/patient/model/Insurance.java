package com.ehrblockchain.patient.model;

import java.time.LocalDate;

import jakarta.persistence.Column;
import jakarta.persistence.Convert;
import jakarta.persistence.Embeddable;

import jakarta.validation.constraints.FutureOrPresent;
import jakarta.validation.constraints.PastOrPresent;
import jakarta.validation.constraints.Size;

import com.ehrblockchain.security.encryption.ColumnEncryptionConverter;

@Embeddable
public class Insurance {
    @Size(max = 100)
    @Column(name = "provider_name")
    @Convert(converter = ColumnEncryptionConverter.class)
    private String providerName;

    @Size(max = 100)
    @Column(name = "policy_number")
    @Convert(converter = ColumnEncryptionConverter.class)
    private String policyNumber;

    @Size(max = 100)
    @Column(name = "group_number")
    @Convert(converter = ColumnEncryptionConverter.class)
    private String groupNumber;

    @PastOrPresent()
    @Column(name = "coverage_start_date")
    private LocalDate coverageStartDate;

    @FutureOrPresent()
    @Column(name = "coverage_end_date")
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

    public void setProviderName(String providerName) {
        this.providerName = providerName;
    }

    public String getPolicyNumber() {
        return policyNumber;
    }

    public void setPolicyNumber(String policyNumber) {
        this.policyNumber = policyNumber;
    }

    public String getGroupNumber() {
        return groupNumber;
    }

    public void setGroupNumber(String groupNumber) {
        this.groupNumber = groupNumber;
    }

    public LocalDate getCoverageStartDate() {
        return coverageStartDate;
    }

    public void setCoverageStartDate(LocalDate coverageStartDate) {
        this.coverageStartDate = coverageStartDate;
    }

    public LocalDate getCoverageEndDate() {
        return coverageEndDate;
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