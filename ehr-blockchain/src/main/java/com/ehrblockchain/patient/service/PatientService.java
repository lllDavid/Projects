package com.ehrblockchain.patient.service;

import java.util.List;
import java.util.stream.Collectors;

import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.ehrblockchain.exception.EmailAlreadyExistsException;
import com.ehrblockchain.exception.PatientNotFoundException;

import com.ehrblockchain.patient.mapper.PatientMapper;
import com.ehrblockchain.patient.model.Patient;
import com.ehrblockchain.patient.repository.PatientRepository;
import com.ehrblockchain.patient.dto.PatientCreateDTO;
import com.ehrblockchain.patient.dto.PatientDTO;
import com.ehrblockchain.patient.dto.PatientUpdateDTO;

@Service
public class PatientService {

    private final PatientRepository patientRepository;
    private final PatientMapper patientMapper;

    public PatientService(PatientRepository patientRepository, PatientMapper patientMapper) {
        this.patientRepository = patientRepository;
        this.patientMapper = patientMapper;
    }

    @Transactional
    public PatientDTO savePatient(Patient patient) {
        patientRepository.findByEmail(patient.getEmail()).ifPresent(p -> {
            throw new EmailAlreadyExistsException(patient.getEmail());
        });
        Patient savedPatient = patientRepository.save(patient);

        return patientMapper.toDto(savedPatient);
    }

    @Transactional
    public PatientDTO createPatient(PatientCreateDTO createDTO) {
        Patient patient = patientMapper.toEntity(createDTO);

        return savePatient(patient);
    }

    @Transactional
    public PatientDTO updatePatient(Long id, PatientUpdateDTO updateDTO) {
        Patient existingPatient = patientRepository.findById(id)
                .orElseThrow(() -> new PatientNotFoundException(id));

        patientMapper.updateFromDto(updateDTO, existingPatient);
        patientMapper.updateNestedEntitiesFromDto(updateDTO, existingPatient);

        return patientMapper.toDto(existingPatient);
    }

    @Transactional
    public void deletePatient(Long patientId) {
        patientRepository.deleteById(patientId);
    }

    @Transactional(readOnly = true)
    public List<PatientDTO> getAllPatients() {
        return patientRepository.findAll().stream()
                .map(patientMapper::toDto)
                .collect(Collectors.toList());
    }

    @Transactional(readOnly = true)
    public PatientDTO getPatientById(Long patientId) {
        return patientRepository.findById(patientId)
                .map(patientMapper::toDto)
                .orElseThrow(() -> new PatientNotFoundException(patientId));
    }

    @Transactional(readOnly = true)
    public PatientDTO getPatientByEmail(String email) {
        return patientRepository.findByEmail(email)
                .map(patientMapper::toDto)
                .orElseThrow(() -> new PatientNotFoundException(email));
    }
}