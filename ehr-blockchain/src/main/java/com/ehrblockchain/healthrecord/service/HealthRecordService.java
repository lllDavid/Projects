package com.ehrblockchain.healthrecord.service;

import java.time.LocalDateTime;
import java.util.UUID;

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
import com.ehrblockchain.auth.service.AuthService;
import com.ehrblockchain.blockchain.model.Transaction;
import com.ehrblockchain.user.dto.UserDTO;
import com.ehrblockchain.blockchain.model.Blockchain;

import static com.ehrblockchain.blockchain.util.MerkleUtils.computeTransactionHash;

@Service
// TODO: refactor repeated logic into helper methods
public class HealthRecordService {

    private final HealthRecordRepository healthRecordRepository;
    private final PatientRepository patientRepository;
    private final HealthRecordMapperHelper mapperHelper;
    private final HealthRecordMapper healthRecordMapper;
    private final AuthService authService;
    private final Blockchain blockchain;

    public HealthRecordService(HealthRecordRepository healthRecordRepository,
                               PatientRepository patientRepository,
                               HealthRecordMapperHelper mapperHelper,
                               HealthRecordMapper healthRecordMapper, AuthService authService, Blockchain blockchain) {
        this.healthRecordRepository = healthRecordRepository;
        this.patientRepository = patientRepository;
        this.mapperHelper = mapperHelper;
        this.healthRecordMapper = healthRecordMapper;
        this.authService = authService;
        this.blockchain = blockchain;
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

        // Blockchain related
        UserDTO currentUser = authService.getCurrentUser();
        Long actorId = (currentUser != null) ? currentUser.id() : 0L;

        HealthRecordDTO healthRecordDTO = healthRecordMapper.toDto(healthRecord);

        Transaction accessTx = new Transaction(
                UUID.randomUUID(),
                patientId,
                "readRecord",
                actorId,
                computeTransactionHash(healthRecordDTO),
                System.currentTimeMillis(),
                "unsigned"
        );

        blockchain.addTransaction(accessTx, String.valueOf(actorId));

        return healthRecordDTO;
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

        // Blockchain related
        UserDTO currentUser = authService.getCurrentUser();
        Long actorId = (currentUser != null) ? currentUser.id() : 0L;

        HealthRecordDTO healthRecordDTO = healthRecordMapper.toDto(existingHealthRecord);

        Transaction accessTx = new Transaction(
                UUID.randomUUID(),
                patientId,
                "writeRecord",
                actorId,
                computeTransactionHash(healthRecordDTO),
                System.currentTimeMillis(),
                "unsigned"
        );

        blockchain.addTransaction(accessTx, String.valueOf(actorId));

        return healthRecordDTO;
    }

    @Transactional
    public void deleteHealthRecord(Long patientId) {
        Patient patient = patientRepository.findById(patientId)
                .orElseThrow(() -> new HealthRecordNotFoundException(patientId));

        if (patient.getHealthRecord() == null) {
            throw new HealthRecordNotFoundException(patientId);
        }

        HealthRecord existingHealthRecord = patient.getHealthRecord();

        // Blockchain related
        UserDTO currentUser = authService.getCurrentUser();
        Long actorId = (currentUser != null) ? currentUser.id() : 0L;

        HealthRecordDTO healthRecordDTO = healthRecordMapper.toDto(existingHealthRecord);

        Transaction accessTx = new Transaction(
                UUID.randomUUID(),
                patientId,
                "deleteRecord",
                actorId,
                computeTransactionHash(healthRecordDTO),
                System.currentTimeMillis(),
                "unsigned"
        );

        blockchain.addTransaction(accessTx, String.valueOf(actorId));

        patient.setHealthRecord(null);
    }
}