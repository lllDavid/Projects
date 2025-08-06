package com.ehrblockchain.patient.service;

import java.util.List;
import java.util.Optional;

import jakarta.persistence.EntityNotFoundException;

import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.ehrblockchain.patient.dto.PatientUpdateDTO;
import com.ehrblockchain.patient.model.Address;
import com.ehrblockchain.patient.model.Insurance;
import com.ehrblockchain.patient.model.Patient;
import com.ehrblockchain.patient.repository.PatientRepository;
import com.ehrblockchain.patient.dto.PatientCreateDTO;
import com.ehrblockchain.patient.mapper.PatientMapper;


@Service
public class PatientService {

    private final PatientRepository patientRepository;
    private final PatientMapper patientMapper;

    public PatientService(PatientRepository patientRepository, PatientMapper patientMapper) {
        this.patientRepository = patientRepository;
        this.patientMapper = patientMapper;
    }

    @Transactional
    public Patient savePatient(Patient patient) {
        patientRepository.findByEmail(patient.getEmail()).ifPresent(p -> {
            throw new RuntimeException("Email already exists");
        });
        return patientRepository.save(patient);
    }

    @Transactional
    public Patient createPatient(PatientCreateDTO createDTO) {
        Patient patient = patientMapper.toEntity(createDTO);
        return savePatient(patient);
    }

    @Transactional
    public Patient updatePatient(Long id, PatientUpdateDTO updateDTO) {
        Patient existingPatient = patientRepository.findById(id)
                .orElseThrow(() -> new EntityNotFoundException("Patient not found with id: " + id));

        patientMapper.updateFromDto(updateDTO, existingPatient);

        if (updateDTO.getAddress() != null) {
            Address existingAddress = existingPatient.getAddress();
            if (existingAddress == null) {
                existingAddress = new Address();
                existingPatient.setAddress(existingAddress);
            }
            patientMapper.updateAddressFromDto(updateDTO.getAddress(), existingAddress);
        }

        if (updateDTO.getInsurance() != null) {
            Insurance existingInsurance = existingPatient.getInsurance();
            if (existingInsurance == null) {
                existingInsurance = new Insurance();
                existingPatient.setInsurance(existingInsurance);
            }
            patientMapper.updateInsuranceFromDto(updateDTO.getInsurance(), existingInsurance);
        }

        return existingPatient;
    }

    @Transactional
    public void deletePatient(Long patientId) {
        patientRepository.deleteById(patientId);
    }

    @Transactional(readOnly = true)
    public List<Patient> getAllPatients() {
        return patientRepository.findAll();
    }

    @Transactional(readOnly = true)
    public Optional<Patient> getPatientById(Long patientId) {
        return patientRepository.findById(patientId);
    }

    @Transactional(readOnly = true)
    public Optional<Patient> getPatientByEmail(String email) {
        return patientRepository.findByEmail(email);
    }
}