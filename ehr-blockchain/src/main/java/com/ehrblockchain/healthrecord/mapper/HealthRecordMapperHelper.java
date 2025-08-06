package com.ehrblockchain.healthrecord.mapper;

import java.util.List;
import java.util.Objects;
import java.util.Set;
import java.util.function.BiConsumer;
import java.util.function.Function;
import java.util.stream.Collectors;

import org.springframework.stereotype.Component;
import org.springframework.transaction.annotation.Transactional;

import com.ehrblockchain.healthrecord.dto.*;
import com.ehrblockchain.healthrecord.model.*;

@Component
public class HealthRecordMapperHelper {
    private final HealthRecordMapper mapper;

    public HealthRecordMapperHelper(HealthRecordMapper mapper) {
        this.mapper = mapper;
    }

    @Transactional
    public void updateWithDto(HealthRecordUpdateDTO dto, HealthRecord entity) {

        mergeList(
                dto.getDiagnoses(),
                entity.getDiagnoses(),
                DiagnosisDTO::getId,
                Diagnosis::getId,
                mapper::updateDiagnosisFromDto,
                mapper::mapToDiagnosis,
                Diagnosis::setHealthRecord,
                entity
        );

        mergeList(
                dto.getTreatmentPlans(),
                entity.getTreatmentPlans(),
                TreatmentPlanDTO::getId,
                TreatmentPlan::getId,
                mapper::updateTreatmentPlanFromDto,
                mapper::mapToTreatmentPlan,
                TreatmentPlan::setHealthRecord,
                entity
        );

        mergeList(
                dto.getPrescriptions(),
                entity.getPrescriptions(),
                PrescriptionDTO::getId,
                Prescription::getId,
                mapper::updatePrescriptionFromDto,
                mapper::mapToPrescription,
                Prescription::setHealthRecord,
                entity
        );

        mergeList(
                dto.getVitals(),
                entity.getVitals(),
                VitalsDTO::getId,
                Vitals::getId,
                mapper::updateVitalsFromDto,
                mapper::mapToVitals,
                Vitals::setHealthRecord,
                entity
        );

        mergeList(
                dto.getCbcTests(),
                entity.getCbcTests(),
                CBCDTO::getId,
                CBC::getId,
                mapper::updateCBCFromDto,
                mapper::mapToCBC,
                CBC::setHealthRecord,
                entity
        );

        mergeList(
                dto.getAllergies(),
                entity.getAllergies(),
                AllergyDTO::getId,
                Allergy::getId,
                mapper::updateAllergyFromDto,
                mapper::mapToAllergy,
                Allergy::setHealthRecord,
                entity
        );

        mergeList(
                dto.getLabResults(),
                entity.getLabResults(),
                LabResultDTO::getId,
                LabResult::getId,
                mapper::updateLabResultFromDto,
                mapper::mapToLabResult,
                LabResult::setHealthRecord,
                entity
        );

        mergeList(
                dto.getImmunizations(),
                entity.getImmunizations(),
                ImmunizationDTO::getId,
                Immunization::getId,
                mapper::updateImmunizationFromDto,
                mapper::mapToImmunization,
                Immunization::setHealthRecord,
                entity
        );

        mergeList(
                dto.getMedicalHistory(),
                entity.getMedicalHistory(),
                MedicalHistoryDTO::getId,
                MedicalHistory::getId,
                mapper::updateMedicalHistoryFromDto,
                mapper::mapToMedicalHistory,
                MedicalHistory::setHealthRecord,
                entity
        );

        mergeList(
                dto.getFamilyHistory(),
                entity.getFamilyHistory(),
                FamilyHistoryDTO::getId,
                FamilyHistory::getId,
                mapper::updateFamilyHistoryFromDto,
                mapper::mapToFamilyHistory,
                FamilyHistory::setHealthRecord,
                entity
        );

        mergeList(
                dto.getEncounters(),
                entity.getEncounters(),
                EncounterDTO::getId,
                Encounter::getId,
                mapper::updateEncounterFromDto,
                mapper::mapToEncounter,
                Encounter::setHealthRecord,
                entity
        );

        mergeList(
                dto.getProcedures(),
                entity.getProcedures(),
                ProcedureDTO::getId,
                Procedure::getId,
                mapper::updateProcedureFromDto,
                mapper::mapToProcedure,
                Procedure::setHealthRecord,
                entity
        );

        mergeList(
                dto.getNotes(),
                entity.getNotes(),
                NoteDTO::getId,
                Note::getId,
                mapper::updateNoteFromDto,
                mapper::mapToNote,
                Note::setHealthRecord,
                entity
        );
    }

    private <D, E> void mergeList(
            List<D> dtos,
            List<E> existing,
            Function<D, Long> getDtoId,
            Function<E, Long> getEntityId,
            BiConsumer<D, E> updateFn,
            Function<D, E> createFn,
            BiConsumer<E, HealthRecord> setParentFn,
            HealthRecord parent
    ) {
        if (dtos == null) {
            return;
        }

        Set<Long> dtoIds = dtos.stream()
                .map(getDtoId)
                .filter(Objects::nonNull)
                .collect(Collectors.toSet());

        existing.removeIf(e -> {
            Long id = getEntityId.apply(e);
            return id != null && !dtoIds.contains(id);
        });

        for (D dto : dtos) {
            Long id = getDtoId.apply(dto);
            E found = (id != null)
                    ? existing.stream()
                    .filter(e -> id.equals(getEntityId.apply(e)))
                    .findFirst()
                    .orElse(null)
                    : null;

            if (found != null) {
                updateFn.accept(dto, found);
            } else {
                E created = createFn.apply(dto);
                setParentFn.accept(created, parent);
                existing.add(created);
            }
        }
    }
}