package com.ehrblockchain.patient.controller;

import java.util.List;

import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;

import com.ehrblockchain.patient.service.PatientService;
import com.ehrblockchain.patient.dto.PatientUpdateDTO;
import com.ehrblockchain.patient.dto.PatientCreateDTO;
import com.ehrblockchain.patient.dto.PatientDTO;

@RestController
@RequestMapping("/patients")
public class PatientController {

    private final PatientService patientService;

    public PatientController(PatientService patientService) {
        this.patientService = patientService;
    }

    @PreAuthorize("hasAnyRole('ADMIN', 'RECEPTION', 'DOCTOR', 'FINANCE')")
    @GetMapping
    public ResponseEntity<List<PatientDTO>> getAllPatients() {
        return ResponseEntity.ok(patientService.getAllPatients());
    }

    @PreAuthorize("hasAnyRole('ADMIN', 'RECEPTION', 'DOCTOR', 'NURSE', 'FINANCE')")
    @GetMapping("/{id}")
    public ResponseEntity<PatientDTO> getPatientById(@PathVariable Long id) {
        PatientDTO patient = patientService.getPatientById(id);
        return ResponseEntity.ok(patient);
    }

    @PreAuthorize("hasAnyRole('ADMIN', 'RECEPTION', 'NURSE')")
    @PostMapping
    public ResponseEntity<PatientDTO> createPatient(@RequestBody PatientCreateDTO patientCreateDTO) {
        PatientDTO savedPatientDTO = patientService.createPatient(patientCreateDTO);
        return ResponseEntity.status(HttpStatus.CREATED).body(savedPatientDTO);
    }

    @PreAuthorize("hasAnyRole('ADMIN', 'RECEPTION', 'DOCTOR', 'NURSE')")
    @PatchMapping("/{id}")
    public ResponseEntity<PatientDTO> updatePatient(@PathVariable Long id,
                                                    @RequestBody PatientUpdateDTO updateDTO) {
        PatientDTO updatedPatientDto = patientService.updatePatient(id, updateDTO);
        return ResponseEntity.ok(updatedPatientDto);
    }

    @PreAuthorize("hasAnyRole('ADMIN')")
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deletePatient(@PathVariable Long id) {
        patientService.deletePatient(id);
        return ResponseEntity.noContent().build();
    }
}