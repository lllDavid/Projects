package com.ehrblockchain.patient.service;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.ehrblockchain.patient.model.Patient;
import com.ehrblockchain.patient.repository.PatientRepository;

@Service
public class PatientService {

    private final PatientRepository patientRepository;

    public PatientService(PatientRepository patientRepository) {
        this.patientRepository = patientRepository;
    }

    @Transactional
    public Patient savePatientWithHealthRecord(Patient patient) {
        patientRepository.findByEmail(patient.getEmail()).ifPresent(p -> {
            throw new RuntimeException("Email already exists");
        });
        return patientRepository.save(patient);
    }

    @Transactional
    public Patient updatePatient(Long patientId, Patient updatedPatient) {
        Patient existingPatient = patientRepository.findById(patientId).orElseThrow(() -> new RuntimeException("Patient not found"));
        existingPatient.updateFrom(updatedPatient);
        return existingPatient;
    }

    @Transactional(readOnly = true)
    public Optional<Patient> getPatientById(Long patientId) {
        return patientRepository.findById(patientId);
    }

    @Transactional(readOnly = true)
    public Optional<Patient> getPatientByEmail(String email) {
        return patientRepository.findByEmail(email);
    }

    @Transactional(readOnly = true)
    public List<Patient> getAllPatients() {
        return patientRepository.findAll();
    }

    @Transactional
    public void deletePatientById(Long patientId) {
        patientRepository.deleteById(patientId);
    }
}