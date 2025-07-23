package com.ehrblockchain.healthrecord.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.ehrblockchain.healthrecord.model.HealthRecord;

public interface HealthRecordRepository extends JpaRepository<HealthRecord, Long> {
}

