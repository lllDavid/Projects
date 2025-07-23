package com.ehrblockchain.healthrecord.service;

import com.ehrblockchain.healthrecord.model.HealthRecord;
import com.ehrblockchain.healthrecord.repository.HealthRecordRepository;
import com.ehrblockchain.patient.repository.PatientRepository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
public class HealthRecordService {

    private final HealthRecordRepository healthRecordRepository;
    private final PatientRepository patientRepository;

    public HealthRecordService(HealthRecordRepository healthRecordRepository, PatientRepository patientRepository) {
        this.healthRecordRepository = healthRecordRepository;
        this.patientRepository = patientRepository;
    }

    @Transactional(readOnly = true)
    public HealthRecord getHealthRecordById(Long patientId) {
        Long ehrId = patientRepository.findById(patientId)
                .orElseThrow(() -> new RuntimeException("Patient not found"))
                .getEhrId();

        if (ehrId == null) throw new RuntimeException("HealthRecord not found for patient");

        return healthRecordRepository.findById(ehrId)
                .orElseThrow(() -> new RuntimeException("HealthRecord not found"));
    }

    @Transactional
    public HealthRecord updateHealthRecord(Long patientId, HealthRecord updatedHealthRecord) {
        Long ehrId = patientRepository.findById(patientId)
                .orElseThrow(() -> new RuntimeException("Patient not found"))
                .getEhrId();

        if (ehrId == null) throw new RuntimeException("HealthRecord not found for patient");

        HealthRecord existingHealthRecord = healthRecordRepository.findById(ehrId)
                .orElseThrow(() -> new RuntimeException("HealthRecord not found"));
        existingHealthRecord.updateFrom(updatedHealthRecord);
        return existingHealthRecord;
    }

    @Transactional
    public void deleteHealthRecordById(Long patientId) {
        Long ehrId = patientRepository.findById(patientId)
                .orElseThrow(() -> new RuntimeException("Patient not found"))
                .getEhrId();

        if (ehrId == null) throw new RuntimeException("HealthRecord not found for patient");

        healthRecordRepository.deleteById(ehrId);
    }
}
