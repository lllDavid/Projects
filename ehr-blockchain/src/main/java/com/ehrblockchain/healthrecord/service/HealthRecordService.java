package com.ehrblockchain.healthrecord.service;

import java.time.LocalDateTime;

import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.ehrblockchain.exception.HealthRecordNotFoundException;

import com.ehrblockchain.patient.model.Patient;
import com.ehrblockchain.patient.repository.PatientRepository;

import com.ehrblockchain.healthrecord.dto.HealthRecordUpdateDTO;
import com.ehrblockchain.healthrecord.model.HealthRecord;
import com.ehrblockchain.healthrecord.repository.HealthRecordRepository;
import com.ehrblockchain.healthrecord.mapper.HealthRecordMapperHelper;
import com.ehrblockchain.healthrecord.dto.HealthRecordDTO;
import com.ehrblockchain.healthrecord.mapper.HealthRecordMapper;

@Service
public class HealthRecordService {

    private final HealthRecordRepository healthRecordRepository;
    private final PatientRepository patientRepository;
    private final HealthRecordMapperHelper mapperHelper;
    private final HealthRecordMapper healthRecordMapper;

    public HealthRecordService(HealthRecordRepository healthRecordRepository,
                               PatientRepository patientRepository,
                               HealthRecordMapperHelper mapperHelper,
                               HealthRecordMapper healthRecordMapper) {
        this.healthRecordRepository = healthRecordRepository;
        this.patientRepository = patientRepository;
        this.mapperHelper = mapperHelper;
        this.healthRecordMapper = healthRecordMapper;
    }

    @Transactional(readOnly = true)
    public HealthRecordDTO getHealthRecordById(Long patientId) {
        Patient patient = patientRepository.findById(patientId)
                .orElseThrow(() -> new HealthRecordNotFoundException(patientId));

        Long ehrId = patient.getEhrId();
        if (ehrId == null) {
            throw new HealthRecordNotFoundException(patientId);
        }

        HealthRecord healthRecord = healthRecordRepository.findById(ehrId)
                .orElseThrow(() -> new HealthRecordNotFoundException(ehrId));

        return healthRecordMapper.toDto(healthRecord);
    }

    @Transactional
    public HealthRecordDTO updateHealthRecord(Long patientId, HealthRecordUpdateDTO updateDto) {
        Patient patient = patientRepository.findById(patientId)
                .orElseThrow(() -> new HealthRecordNotFoundException(patientId));

        Long ehrId = patient.getEhrId();
        if (ehrId == null) {
            throw new HealthRecordNotFoundException("HealthRecord not found for patient with id: " + patientId);
        }

        HealthRecord existingHealthRecord = healthRecordRepository.findById(ehrId)
                .orElseThrow(() -> new HealthRecordNotFoundException(ehrId));

        mapperHelper.updateWithDto(updateDto, existingHealthRecord);
        existingHealthRecord.setUpdatedAt(LocalDateTime.now());

        return healthRecordMapper.toDto(existingHealthRecord);
    }

    @Transactional
    public void deleteHealthRecord(Long patientId) {
        Patient patient = patientRepository.findById(patientId)
                .orElseThrow(() -> new HealthRecordNotFoundException(patientId));

        if (patient.getHealthRecord() == null) {
            throw new HealthRecordNotFoundException(patientId);
        }

        patient.setHealthRecord(null);
    }
}