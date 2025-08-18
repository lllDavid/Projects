package com.ehrblockchain.healthrecord.model;

import java.time.LocalDate;
import java.time.LocalDateTime;

import java.util.ArrayList;
import java.util.List;

import jakarta.persistence.*;

import jakarta.validation.Valid;

import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.UpdateTimestamp;

import com.fasterxml.jackson.annotation.JsonManagedReference;

import com.ehrblockchain.patient.model.Patient;

@Entity
@Table(name = "health_records")
public class HealthRecord {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id", nullable = false, unique = true)
    private Long id;

    @OneToOne(mappedBy = "healthRecord")
    private Patient patient;

    @CreationTimestamp
    @Column(name = "created_at", nullable = false, updatable = false)
    private LocalDateTime createdAt;

    @UpdateTimestamp
    @Column(name = "updated_at")
    private LocalDateTime updatedAt;

    @Column(name = "record_date", nullable = false)
    private LocalDate recordDate;

    @OneToMany(mappedBy = "healthRecord", cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.LAZY)
    @JsonManagedReference
    @Valid
    private List<Note> notes = new ArrayList<>();

    @OneToMany(mappedBy = "healthRecord", cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.LAZY)
    @JsonManagedReference
    @Valid
    private List<Diagnosis> diagnoses = new ArrayList<>();

    @OneToMany(mappedBy = "healthRecord", cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.LAZY)
    @JsonManagedReference
    @Valid
    private List<TreatmentPlan> treatmentPlans = new ArrayList<>();

    @OneToMany(mappedBy = "healthRecord", cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.LAZY)
    @JsonManagedReference
    @Valid
    private List<Prescription> prescriptions = new ArrayList<>();

    @OneToMany(mappedBy = "healthRecord", cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.LAZY)
    @JsonManagedReference
    @Valid
    private List<Vitals> vitals = new ArrayList<>();

    @OneToMany(mappedBy = "healthRecord", cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.LAZY)
    @JsonManagedReference
    @Valid
    private List<CBC> cbcTests = new ArrayList<>();

    @OneToMany(mappedBy = "healthRecord", cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.LAZY)
    @JsonManagedReference
    @Valid
    private List<Allergy> allergies = new ArrayList<>();

    @OneToMany(mappedBy = "healthRecord", cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.LAZY)
    @JsonManagedReference
    @Valid
    private List<LabResult> labResults = new ArrayList<>();

    @OneToMany(mappedBy = "healthRecord", cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.LAZY)
    @JsonManagedReference
    @Valid
    private List<Immunization> immunizations = new ArrayList<>();

    @OneToMany(mappedBy = "healthRecord", cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.LAZY)
    @JsonManagedReference
    @Valid
    private List<MedicalHistory> medicalHistory = new ArrayList<>();

    @OneToMany(mappedBy = "healthRecord", cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.LAZY)
    @JsonManagedReference
    @Valid
    private List<FamilyHistory> familyHistory = new ArrayList<>();

    @OneToMany(mappedBy = "healthRecord", cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.LAZY)
    @JsonManagedReference
    @Valid
    private List<Encounter> encounters = new ArrayList<>();

    @OneToMany(mappedBy = "healthRecord", cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.LAZY)
    @JsonManagedReference
    @Valid
    private List<Procedure> procedures = new ArrayList<>();

    public HealthRecord() {
    }

    public HealthRecord(Patient patient, LocalDate recordDate,
                        List<Diagnosis> diagnoses,
                        List<TreatmentPlan> treatmentPlans,
                        List<Prescription> prescriptions,
                        List<Allergy> allergies,
                        List<Note> notes,
                        List<LabResult> labResults,
                        List<Vitals> vitals,
                        List<CBC> cbcTests,
                        List<Immunization> immunizations,
                        List<MedicalHistory> medicalHistory,
                        List<FamilyHistory> familyHistory,
                        List<Encounter> encounters,
                        List<Procedure> procedures) {
        this.patient = patient;
        this.recordDate = recordDate;
        this.diagnoses = diagnoses;
        this.treatmentPlans = treatmentPlans;
        this.prescriptions = prescriptions;
        this.allergies = allergies;
        this.notes = notes;
        this.labResults = labResults;
        this.vitals = vitals;
        this.cbcTests = cbcTests;
        this.immunizations = immunizations;
        this.medicalHistory = medicalHistory;
        this.familyHistory = familyHistory;
        this.encounters = encounters;
        this.procedures = procedures;
    }

    public Long getId() {
        return id;
    }

    public Long getPatientId() {
        return patient != null ? patient.getId() : null;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }

    public LocalDate getRecordDate() {
        return recordDate;
    }

    public void setRecordDate(LocalDate recordDate) {
        this.recordDate = recordDate;
    }

    public List<Diagnosis> getDiagnoses() {
        return diagnoses;
    }

    public void setDiagnoses(List<Diagnosis> diagnoses) {
        this.diagnoses = diagnoses;
    }

    public List<TreatmentPlan> getTreatmentPlans() {
        return treatmentPlans;
    }

    public void setTreatmentPlans(List<TreatmentPlan> treatmentPlans) {
        this.treatmentPlans = treatmentPlans;
    }

    public List<Prescription> getPrescriptions() {
        return prescriptions;
    }

    public void setPrescriptions(List<Prescription> prescriptions) {
        this.prescriptions = prescriptions;
    }

    public List<Vitals> getVitals() {
        return vitals;
    }

    public void setVitals(List<Vitals> vitals) {
        this.vitals = vitals;
    }

    public List<CBC> getCbcTests() {
        return cbcTests;
    }

    public void setCbcTests(List<CBC> cbcTests) {
        this.cbcTests = cbcTests;
    }

    public List<Note> getNotes() {
        return notes;
    }

    public void setNotes(List<Note> notes) {
        this.notes = notes;
    }

    public List<Allergy> getAllergies() {
        return allergies;
    }

    public void setAllergies(List<Allergy> allergies) {
        this.allergies = allergies;
    }

    public List<LabResult> getLabResults() {
        return labResults;
    }

    public void setLabResults(List<LabResult> labResults) {
        this.labResults = labResults;
    }

    public List<Immunization> getImmunizations() {
        return immunizations;
    }

    public void setImmunizations(List<Immunization> immunizations) {
        this.immunizations = immunizations;
    }

    public List<MedicalHistory> getMedicalHistory() {
        return medicalHistory;
    }

    public void setMedicalHistory(List<MedicalHistory> medicalHistory) {
        this.medicalHistory = medicalHistory;
    }

    public List<FamilyHistory> getFamilyHistory() {
        return familyHistory;
    }

    public void setFamilyHistory(List<FamilyHistory> familyHistory) {
        this.familyHistory = familyHistory;
    }

    public List<Encounter> getEncounters() {
        return encounters;
    }

    public void setEncounters(List<Encounter> encounters) {
        this.encounters = encounters;
    }

    public List<Procedure> getProcedures() {
        return procedures;
    }

    public void setProcedures(List<Procedure> procedures) {
        this.procedures = procedures;
    }

    public LocalDateTime getCreatedAt() {
        return createdAt;
    }

    public void setCreatedAt(LocalDateTime createdAt) {
        this.createdAt = createdAt;
    }

    public LocalDateTime getUpdatedAt() {
        return updatedAt;
    }

    public void setUpdatedAt(LocalDateTime updatedAt) {
        this.updatedAt = updatedAt;
    }

    @Override
    public String toString() {
        return "HealthRecord{" +
                ", patientId=" + (patient != null ? patient.getId() : null) +
                ", recordDate=" + recordDate +
                ", diagnoses=" + diagnoses +
                ", treatmentPlans=" + treatmentPlans +
                ", prescriptions=" + prescriptions +
                ", allergies=" + allergies +
                ", notes='" + notes + '\'' +
                ", labResults=" + labResults +
                ", vitals=" + vitals +
                ", cbcTests=" + cbcTests +
                ", immunizations=" + immunizations +
                ", medicalHistory=" + medicalHistory +
                ", familyHistory=" + familyHistory +
                ", encounters=" + encounters +
                ", procedures=" + procedures +
                ", createdAt=" + (createdAt != null ? createdAt.toString() : null) +
                ", updatedAt=" + (updatedAt != null ? updatedAt.toString() : null) +
                '}';
    }
}