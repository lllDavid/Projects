package com.ehrblockchain.patient.controller;

import java.util.List;

import com.ehrblockchain.patient.dto.PatientCreateDTO;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import com.ehrblockchain.patient.model.Patient;
import com.ehrblockchain.patient.service.PatientService;
import com.ehrblockchain.patient.dto.PatientUpdateDTO;

@RestController
@RequestMapping("/patients")
public class PatientController {

    private final PatientService patientService;

    public PatientController(PatientService patientService) {
        this.patientService = patientService;
    }

    @GetMapping
    public List<Patient> getAllPatients() {
        return patientService.getAllPatients();
    }

    @GetMapping("/{id}")
    public ResponseEntity<Patient> getPatientById(@PathVariable Long id) {
        return patientService.getPatientById(id)
                .map(ResponseEntity::ok)
                .orElseGet(() -> ResponseEntity.notFound().build());
    }

    @PostMapping
    public ResponseEntity<Patient> createPatient(@RequestBody PatientCreateDTO patientCreateDTO) {
        Patient savedPatient = patientService.createPatient(patientCreateDTO);
        return new ResponseEntity<>(savedPatient, HttpStatus.CREATED);
    }

    @PatchMapping("/{id}")
    public ResponseEntity<Patient> updatePatient(@PathVariable Long id,
                                                 @RequestBody PatientUpdateDTO updateDTO) {
        Patient updatedPatient = patientService.updatePatient(id, updateDTO);
        return ResponseEntity.ok(updatedPatient);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deletePatient(@PathVariable Long id) {
        try {
            patientService.deletePatientById(id);
            return ResponseEntity.noContent().build();
        } catch (RuntimeException e) {
            return ResponseEntity.notFound().build();
        }
    }
}