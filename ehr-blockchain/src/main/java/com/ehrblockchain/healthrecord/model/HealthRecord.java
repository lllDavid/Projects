package com.ehrblockchain.healthrecord.model;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import com.fasterxml.jackson.annotation.JsonManagedReference;
import jakarta.persistence.*;

import com.ehrblockchain.patient.model.Patient;
import org.hibernate.annotations.CreationTimestamp;
import org.hibernate.annotations.UpdateTimestamp;
import org.springframework.http.ResponseEntity;

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
    private List<Note> notes = new ArrayList<>();

    @OneToMany(mappedBy = "healthRecord", cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.LAZY)
    @JsonManagedReference
    private List<Diagnosis> diagnoses = new ArrayList<>();

    @OneToMany(mappedBy = "healthRecord", cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.LAZY)
    @JsonManagedReference
    private List<TreatmentPlan> treatmentPlans = new ArrayList<>();

    @OneToMany(mappedBy = "healthRecord", cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.LAZY)
    @JsonManagedReference
    private List<Prescription> prescriptions = new ArrayList<>();

    @OneToMany(mappedBy = "healthRecord", cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.LAZY)
    @JsonManagedReference
    private List<Vitals> vitals = new ArrayList<>();

    @OneToMany(mappedBy = "healthRecord", cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.LAZY)
    @JsonManagedReference
    private List<CBC> cbcTests = new ArrayList<>();

    @OneToMany(mappedBy = "healthRecord", cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.LAZY)
    @JsonManagedReference
    private List<Allergy> allergies = new ArrayList<>();

    @OneToMany(mappedBy = "healthRecord", cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.LAZY)
    @JsonManagedReference
    private List<LabResult> labResults = new ArrayList<>();

    @OneToMany(mappedBy = "healthRecord", cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.LAZY)
    @JsonManagedReference
    private List<Immunization> immunizations = new ArrayList<>();

    @OneToMany(mappedBy = "healthRecord", cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.LAZY)
    @JsonManagedReference
    private List<MedicalHistory> medicalHistory = new ArrayList<>();

    @OneToMany(mappedBy = "healthRecord", cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.LAZY)
    @JsonManagedReference
    private List<FamilyHistory> familyHistory = new ArrayList<>();

    @OneToMany(mappedBy = "healthRecord", cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.LAZY)
    @JsonManagedReference
    private List<Encounter> encounters = new ArrayList<>();

    @OneToMany(mappedBy = "healthRecord", cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.LAZY)
    @JsonManagedReference
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

    public LocalDate getRecordDate() {
        return recordDate;
    }

    public List<Diagnosis> getDiagnoses() {
        return diagnoses;
    }

    public List<TreatmentPlan> getTreatmentPlans() {
        return treatmentPlans;
    }

    public List<Prescription> getPrescriptions() {
        return prescriptions;
    }

    public List<Vitals> getVitals() {
        return vitals;
    }

    public List<CBC> getCbcTests() {
        return cbcTests;
    }

    public List<Note> getNotes() {
        return notes;
    }

    public List<Allergy> getAllergies() {
        return allergies;
    }

    public List<LabResult> getLabResults() {
        return labResults;
    }

    public List<Immunization> getImmunizations() {
        return immunizations;
    }

    public List<MedicalHistory> getMedicalHistory() {
        return medicalHistory;
    }

    public List<FamilyHistory> getFamilyHistory() {
        return familyHistory;
    }

    public List<Encounter> getEncounters() {
        return encounters;
    }

    public List<Procedure> getProcedures() {
        return procedures;
    }

    public LocalDateTime getCreatedAt() {
        return createdAt;
    }

    public LocalDateTime getUpdatedAt() {
        return updatedAt;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }

    public void setRecordDate(LocalDate recordDate) {
        this.recordDate = recordDate;
    }

    public void setDiagnoses(List<Diagnosis> diagnoses) {
        this.diagnoses = diagnoses;
    }

    public void setTreatmentPlans(List<TreatmentPlan> treatmentPlans) {
        this.treatmentPlans = treatmentPlans;
    }

    public void setPrescriptions(List<Prescription> prescriptions) {
        this.prescriptions = prescriptions;
    }

    public void setVitals(List<Vitals> vitals) {
        this.vitals = vitals;
    }

    public void setCbcTests(List<CBC> cbcTests) {
        this.cbcTests = cbcTests;
    }

    public void setNotes(List<Note> notes) {
        this.notes = notes;
    }

    public void setAllergies(List<Allergy> allergies) {
        this.allergies = allergies;
    }

    public void setLabResults(List<LabResult> labResults) {
        this.labResults = labResults;
    }

    public void setImmunizations(List<Immunization> immunizations) {
        this.immunizations = immunizations;
    }

    public void setMedicalHistory(List<MedicalHistory> medicalHistory) {
        this.medicalHistory = medicalHistory;
    }

    public void setFamilyHistory(List<FamilyHistory> familyHistory) {
        this.familyHistory = familyHistory;
    }

    public void setEncounters(List<Encounter> encounters) {
        this.encounters = encounters;
    }

    public void setProcedures(List<Procedure> procedures) {
        this.procedures = procedures;
    }

    public void setUpdatedAt(LocalDateTime updatedAt) {
        this.updatedAt = updatedAt;
    }

    @Override
    public String toString() {
        return "HealthRecord{" +
                "id=" + id +
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