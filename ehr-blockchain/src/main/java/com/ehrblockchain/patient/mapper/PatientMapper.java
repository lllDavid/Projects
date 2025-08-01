package com.ehrblockchain.patient.mapper;

import org.mapstruct.AfterMapping;
import org.mapstruct.Mapper;
import org.mapstruct.MappingTarget;
import org.mapstruct.NullValuePropertyMappingStrategy;

import com.ehrblockchain.healthrecord.dto.HealthRecordCreateDTO;
import com.ehrblockchain.healthrecord.model.HealthRecord;
import com.ehrblockchain.patient.dto.AddressDTO;
import com.ehrblockchain.patient.dto.InsuranceDTO;
import com.ehrblockchain.patient.dto.PatientCreateDTO;
import com.ehrblockchain.patient.dto.PatientUpdateDTO;
import com.ehrblockchain.patient.model.Address;
import com.ehrblockchain.patient.model.Insurance;
import com.ehrblockchain.patient.model.Patient;


@Mapper(
        componentModel = "spring",
        nullValuePropertyMappingStrategy = NullValuePropertyMappingStrategy.IGNORE
)
public interface PatientMapper {

    void updateFromDto(PatientUpdateDTO dto, @MappingTarget Patient patient);

    void updateAddressFromDto(AddressDTO dto, @MappingTarget Address address);

    void updateInsuranceFromDto(InsuranceDTO dto, @MappingTarget Insurance insurance);

    Patient toEntity(PatientCreateDTO dto);

    HealthRecord toEntity(HealthRecordCreateDTO dto);

    @AfterMapping
    default void linkHealthRecordChildren(HealthRecordCreateDTO dto, @MappingTarget HealthRecord entity) {
        entity.getAllergies().forEach(allergy -> allergy.setHealthRecord(entity));
        entity.getDiagnoses().forEach(diagnosis -> diagnosis.setHealthRecord(entity));
        entity.getNotes().forEach(note -> note.setHealthRecord(entity));
        entity.getTreatmentPlans().forEach(treatmentPlan -> treatmentPlan.setHealthRecord(entity));
        entity.getPrescriptions().forEach(prescription -> prescription.setHealthRecord(entity));
        entity.getVitals().forEach(vitals -> vitals.setHealthRecord(entity));
        entity.getCbcTests().forEach(cbc -> cbc.setHealthRecord(entity));
        entity.getLabResults().forEach(labResult -> labResult.setHealthRecord(entity));
        entity.getImmunizations().forEach(immunization -> immunization.setHealthRecord(entity));
        entity.getMedicalHistory().forEach(medicalHistory -> medicalHistory.setHealthRecord(entity));
        entity.getFamilyHistory().forEach(familyHistory -> familyHistory.setHealthRecord(entity));
        entity.getEncounters().forEach(encounter -> encounter.setHealthRecord(entity));
        entity.getProcedures().forEach(procedure -> procedure.setHealthRecord(entity));
    }
}