package com.ehrblockchain.healthrecord.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import com.ehrblockchain.healthrecord.dto.HealthRecordUpdateDTO;
import com.ehrblockchain.healthrecord.model.HealthRecord;
import com.ehrblockchain.healthrecord.service.HealthRecordService;

@RestController
@RequestMapping("/patients/{patientId}/healthrecord")
public class HealthRecordController {

    private final HealthRecordService healthRecordService;

    public HealthRecordController(HealthRecordService healthRecordService) {
        this.healthRecordService = healthRecordService;
    }

    @GetMapping
    public ResponseEntity<HealthRecord> getHealthRecordById(@PathVariable Long patientId) {
        return healthRecordService.getHealthRecordById(patientId)
                .map(ResponseEntity::ok)
                .orElseGet(() -> ResponseEntity.notFound().build());
    }

    @PatchMapping
    public ResponseEntity<HealthRecord> updateHealthRecord(@PathVariable Long patientId, @RequestBody HealthRecordUpdateDTO updateDto) {
        try {
            HealthRecord updatedHealthRecord = healthRecordService.updateHealthRecord(patientId, updateDto);
            return ResponseEntity.ok(updatedHealthRecord);
        } catch (RuntimeException e) {
            return ResponseEntity.notFound().build();
        }
    }

    @DeleteMapping
    public ResponseEntity<Void> deleteHealthRecord(@PathVariable Long patientId) {
        try {
            healthRecordService.deleteHealthRecord(patientId);
            return ResponseEntity.noContent().build();
        } catch (RuntimeException e) {
            return ResponseEntity.notFound().build();
        }
    }
}