package com.ehrblockchain.healthrecord.mapper;

import org.mapstruct.*;

import com.ehrblockchain.healthrecord.dto.*;
import com.ehrblockchain.healthrecord.model.*;

@Mapper(componentModel = "spring", nullValuePropertyMappingStrategy = NullValuePropertyMappingStrategy.IGNORE)
public interface HealthRecordMapper {

    Diagnosis mapToDiagnosis(DiagnosisDTO dto);

    Note mapToNote(NoteDTO dto);

    TreatmentPlan mapToTreatmentPlan(TreatmentPlanDTO dto);

    Prescription mapToPrescription(PrescriptionDTO dto);

    Vitals mapToVitals(VitalsDTO dto);

    CBC mapToCBC(CBCDTO dto);

    Allergy mapToAllergy(AllergyDTO dto);

    LabResult mapToLabResult(LabResultDTO dto);

    Immunization mapToImmunization(ImmunizationDTO dto);

    MedicalHistory mapToMedicalHistory(MedicalHistoryDTO dto);

    FamilyHistory mapToFamilyHistory(FamilyHistoryDTO dto);

    Encounter mapToEncounter(EncounterDTO dto);

    Procedure mapToProcedure(ProcedureDTO dto);

    void updateDiagnosisFromDto(DiagnosisDTO dto, @MappingTarget Diagnosis entity);

    void updateNoteFromDto(NoteDTO dto, @MappingTarget Note entity);

    void updateTreatmentPlanFromDto(TreatmentPlanDTO dto, @MappingTarget TreatmentPlan entity);

    void updatePrescriptionFromDto(PrescriptionDTO dto, @MappingTarget Prescription entity);

    void updateVitalsFromDto(VitalsDTO dto, @MappingTarget Vitals entity);

    void updateCBCFromDto(CBCDTO dto, @MappingTarget CBC entity);

    void updateAllergyFromDto(AllergyDTO dto, @MappingTarget Allergy entity);

    void updateLabResultFromDto(LabResultDTO dto, @MappingTarget LabResult entity);

    void updateImmunizationFromDto(ImmunizationDTO dto, @MappingTarget Immunization entity);

    void updateMedicalHistoryFromDto(MedicalHistoryDTO dto, @MappingTarget MedicalHistory entity);

    void updateFamilyHistoryFromDto(FamilyHistoryDTO dto, @MappingTarget FamilyHistory entity);

    void updateEncounterFromDto(EncounterDTO dto, @MappingTarget Encounter entity);

    void updateProcedureFromDto(ProcedureDTO dto, @MappingTarget Procedure entity);

}