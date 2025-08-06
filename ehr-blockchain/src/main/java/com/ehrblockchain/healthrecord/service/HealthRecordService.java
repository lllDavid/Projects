package com.ehrblockchain.healthrecord.service;

import java.time.LocalDateTime;
import java.util.Optional;

import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.ehrblockchain.healthrecord.dto.HealthRecordUpdateDTO;
import com.ehrblockchain.healthrecord.model.HealthRecord;
import com.ehrblockchain.healthrecord.repository.HealthRecordRepository;
import com.ehrblockchain.healthrecord.mapper.HealthRecordMapperHelper;

import com.ehrblockchain.patient.model.Patient;
import com.ehrblockchain.patient.repository.PatientRepository;

@Service
public class HealthRecordService {

    private final HealthRecordRepository healthRecordRepository;
    private final PatientRepository patientRepository;
    private final HealthRecordMapperHelper mapperHelper;

    public HealthRecordService(HealthRecordRepository healthRecordRepository, PatientRepository patientRepository, HealthRecordMapperHelper mapperHelper) {
        this.healthRecordRepository = healthRecordRepository;
        this.patientRepository = patientRepository;
        this.mapperHelper = mapperHelper;
    }

    @Transactional(readOnly = true)
    public Optional<HealthRecord> getHealthRecordById(Long patientId) {
        return patientRepository.findById(patientId)
                .map(Patient::getEhrId)
                .flatMap(healthRecordRepository::findById);
    }

    @Transactional
    public HealthRecord updateHealthRecord(Long patientId, HealthRecordUpdateDTO updateDto) {
        Patient patient = patientRepository.findById(patientId)
                .orElseThrow(() -> new RuntimeException("Patient not found"));

        Long ehrId = patient.getEhrId();

        if (ehrId == null) throw new RuntimeException("HealthRecord not found for patient");

        HealthRecord existingHealthRecord = healthRecordRepository.findById(ehrId)
                .orElseThrow(() -> new RuntimeException("HealthRecord not found"));

        mapperHelper.updateWithDto(updateDto, existingHealthRecord);

        existingHealthRecord.setUpdatedAt(LocalDateTime.now());

        return existingHealthRecord;
    }

    @Transactional
    public void deleteHealthRecord(Long patientId) {
        Patient patient = patientRepository.findById(patientId)
                .orElseThrow(() -> new RuntimeException("Patient not found"));

        if (patient.getHealthRecord() == null) {
            throw new RuntimeException("HealthRecord not found for patient");
        }
        patient.setHealthRecord(null);
    }
}