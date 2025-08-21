package com.ehrblockchain.healthrecord.dto;

import com.fasterxml.jackson.annotation.JsonInclude;

import java.util.List;

@JsonInclude(JsonInclude.Include.NON_NULL)
public record HealthRecordDTO(
        List<NoteDTO> notes,
        List<DiagnosisDTO> diagnoses,
        List<TreatmentPlanDTO> treatmentPlans,
        List<PrescriptionDTO> prescriptions,
        List<VitalsDTO> vitals,
        List<CBCDTO> cbcTests,
        List<AllergyDTO> allergies,
        List<LabResultDTO> labResults,
        List<ImmunizationDTO> immunizations,
        List<MedicalHistoryDTO> medicalHistory,
        List<FamilyHistoryDTO> familyHistory,
        List<EncounterDTO> encounters,
        List<ProcedureDTO> procedures
) {}