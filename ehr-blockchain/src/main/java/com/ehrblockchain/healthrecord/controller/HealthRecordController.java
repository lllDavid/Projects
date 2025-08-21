package com.ehrblockchain.healthrecord.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import com.ehrblockchain.healthrecord.dto.HealthRecordUpdateDTO;
import com.ehrblockchain.healthrecord.service.HealthRecordService;
import com.ehrblockchain.healthrecord.dto.HealthRecordDTO;

@RestController
@RequestMapping("/patients/{patientId}/healthrecord")
public class HealthRecordController {

    private final HealthRecordService healthRecordService;

    public HealthRecordController(HealthRecordService healthRecordService) {
        this.healthRecordService = healthRecordService;
    }

    @GetMapping
    public ResponseEntity<HealthRecordDTO> getHealthRecordById(@PathVariable Long patientId) {
        HealthRecordDTO healthRecord = healthRecordService.getHealthRecordById(patientId);
        return ResponseEntity.ok(healthRecord);
    }

    @PatchMapping
    public ResponseEntity<HealthRecordDTO> updateHealthRecord(@PathVariable Long patientId,
                                                              @RequestBody HealthRecordUpdateDTO updateDto) {
        HealthRecordDTO updatedHealthRecord = healthRecordService.updateHealthRecord(patientId, updateDto);
        return ResponseEntity.ok(updatedHealthRecord);
    }

    @DeleteMapping
    public ResponseEntity<Void> deleteHealthRecord(@PathVariable Long patientId) {
        healthRecordService.deleteHealthRecord(patientId);
        return ResponseEntity.noContent().build();
    }
}