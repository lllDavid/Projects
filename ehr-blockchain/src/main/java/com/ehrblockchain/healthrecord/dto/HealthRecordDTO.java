package com.ehrblockchain.healthrecord.dto;

import com.fasterxml.jackson.annotation.JsonInclude;

import java.util.List;

@JsonInclude(JsonInclude.Include.NON_NULL)
public class HealthRecordDTO {

    private List<NoteDTO> notes;
    private List<DiagnosisDTO> diagnoses;
    private List<TreatmentPlanDTO> treatmentPlans;
    private List<PrescriptionDTO> prescriptions;
    private List<VitalsDTO> vitals;
    private List<CBCDTO> cbcTests;
    private List<AllergyDTO> allergies;
    private List<LabResultDTO> labResults;
    private List<ImmunizationDTO> immunizations;
    private List<MedicalHistoryDTO> medicalHistory;
    private List<FamilyHistoryDTO> familyHistory;
    private List<EncounterDTO> encounters;
    private List<ProcedureDTO> procedures;


    public List<NoteDTO> getNotes() {
        return notes;
    }

    public void setNotes(List<NoteDTO> notes) {
        this.notes = notes;
    }

    public List<DiagnosisDTO> getDiagnoses() {
        return diagnoses;
    }

    public void setDiagnoses(List<DiagnosisDTO> diagnoses) {
        this.diagnoses = diagnoses;
    }

    public List<TreatmentPlanDTO> getTreatmentPlans() {
        return treatmentPlans;
    }

    public void setTreatmentPlans(List<TreatmentPlanDTO> treatmentPlans) {
        this.treatmentPlans = treatmentPlans;
    }

    public List<PrescriptionDTO> getPrescriptions() {
        return prescriptions;
    }

    public void setPrescriptions(List<PrescriptionDTO> prescriptions) {
        this.prescriptions = prescriptions;
    }

    public List<VitalsDTO> getVitals() {
        return vitals;
    }

    public void setVitals(List<VitalsDTO> vitals) {
        this.vitals = vitals;
    }

    public List<CBCDTO> getCbcTests() {
        return cbcTests;
    }

    public void setCbcTests(List<CBCDTO> cbcTests) {
        this.cbcTests = cbcTests;
    }

    public List<AllergyDTO> getAllergies() {
        return allergies;
    }

    public void setAllergies(List<AllergyDTO> allergies) {
        this.allergies = allergies;
    }

    public List<LabResultDTO> getLabResults() {
        return labResults;
    }

    public void setLabResults(List<LabResultDTO> labResults) {
        this.labResults = labResults;
    }

    public List<ImmunizationDTO> getImmunizations() {
        return immunizations;
    }

    public void setImmunizations(List<ImmunizationDTO> immunizations) {
        this.immunizations = immunizations;
    }

    public List<MedicalHistoryDTO> getMedicalHistory() {
        return medicalHistory;
    }

    public void setMedicalHistory(List<MedicalHistoryDTO> medicalHistory) {
        this.medicalHistory = medicalHistory;
    }

    public List<FamilyHistoryDTO> getFamilyHistory() {
        return familyHistory;
    }

    public void setFamilyHistory(List<FamilyHistoryDTO> familyHistory) {
        this.familyHistory = familyHistory;
    }

    public List<EncounterDTO> getEncounters() {
        return encounters;
    }

    public void setEncounters(List<EncounterDTO> encounters) {
        this.encounters = encounters;
    }

    public List<ProcedureDTO> getProcedures() {
        return procedures;
    }

    public void setProcedures(List<ProcedureDTO> procedures) {
        this.procedures = procedures;
    }
}
