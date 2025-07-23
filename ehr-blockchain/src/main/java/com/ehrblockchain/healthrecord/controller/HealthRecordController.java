package com.ehrblockchain.healthrecord.controller;

import com.ehrblockchain.healthrecord.model.HealthRecord;
import com.ehrblockchain.healthrecord.service.HealthRecordService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/patients/{patientId}/healthrecord")
public class HealthRecordController {

    private final HealthRecordService healthRecordService;

    public HealthRecordController(HealthRecordService healthRecordService) {
        this.healthRecordService = healthRecordService;
    }

    @GetMapping
    public ResponseEntity<HealthRecord> getHealthRecordById(@PathVariable Long patientId) {
        try {
            HealthRecord record = healthRecordService.getHealthRecordById(patientId);
            return ResponseEntity.ok(record);
        } catch (RuntimeException e) {
            return ResponseEntity.notFound().build();
        }
    }

    @PutMapping
    public ResponseEntity<HealthRecord> updateHealthRecord(@PathVariable Long patientId, @RequestBody HealthRecord updatedRecord) {
        try {
            HealthRecord updated = healthRecordService.updateHealthRecord(patientId, updatedRecord);
            return ResponseEntity.ok(updated);
        } catch (RuntimeException e) {
            return ResponseEntity.notFound().build();
        }
    }

    @DeleteMapping
    public ResponseEntity<Void> deleteHealthRecord(@PathVariable Long patientId) {
        try {
            healthRecordService.deleteHealthRecordById(patientId);
            return ResponseEntity.noContent().build();
        } catch (RuntimeException e) {
            return ResponseEntity.notFound().build();
        }
    }
}
