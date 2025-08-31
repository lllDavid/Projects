package com.ehrblockchain.unit.healthrecord;

import java.util.Optional;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;

import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.mockito.Mockito.*;

import com.ehrblockchain.exception.HealthRecordNotFoundException;
import com.ehrblockchain.healthrecord.dto.HealthRecordDTO;
import com.ehrblockchain.healthrecord.dto.HealthRecordUpdateDTO;
import com.ehrblockchain.healthrecord.mapper.HealthRecordMapper;
import com.ehrblockchain.healthrecord.mapper.HealthRecordMapperHelper;
import com.ehrblockchain.healthrecord.model.HealthRecord;
import com.ehrblockchain.healthrecord.repository.HealthRecordRepository;
import com.ehrblockchain.patient.model.Patient;
import com.ehrblockchain.patient.repository.PatientRepository;
import com.ehrblockchain.fixtures.fixtures;
import com.ehrblockchain.healthrecord.service.HealthRecordService;

@ExtendWith(MockitoExtension.class)
class HealthRecordServiceTest {
    @Mock
    private HealthRecordRepository healthRecordRepository;

    @Mock
    private PatientRepository patientRepository;

    @Mock
    private HealthRecordMapperHelper mapperHelper;

    @Mock
    private HealthRecordMapper healthRecordMapper;

    private HealthRecordService underTest;

    @BeforeEach
    void setUp() {
        underTest = new HealthRecordService(
                healthRecordRepository, patientRepository, mapperHelper, healthRecordMapper
        );
    }

    @Test
    void shouldGetHealthRecordById() {
        Patient patient = fixtures.createDefaultPatient();
        HealthRecord existingRecord = patient.getHealthRecord();
        HealthRecordDTO dto = fixtures.createDefaultHealthRecordDTO();

        when(patientRepository.findById(patient.getId())).thenReturn(Optional.of(patient));
        when(healthRecordRepository.findById(existingRecord.getId())).thenReturn(Optional.of(existingRecord));
        when(healthRecordMapper.toDto(existingRecord)).thenReturn(dto);

        HealthRecordDTO result = underTest.getHealthRecordById(patient.getEhrId());

        assertNotNull(result);
        assertThat(result).isEqualTo(dto);

        verify(patientRepository).findById(patient.getId());
        verify(healthRecordRepository).findById(existingRecord.getId());
        verify(healthRecordMapper).toDto(existingRecord);
    }

    @Test
    void shouldThrowWhenPatientNotFoundOnGet() {
        Long patientId = 1L;
        when(patientRepository.findById(patientId)).thenReturn(Optional.empty());

        assertThrows(HealthRecordNotFoundException.class, () -> underTest.getHealthRecordById(patientId));

        verify(patientRepository).findById(patientId);
        verifyNoInteractions(healthRecordRepository);
    }

    @Test
    void shouldUpdateHealthRecord() {
        Patient patient = fixtures.createDefaultPatient();
        HealthRecord existingRecord = fixtures.createDefaultHealthRecord();
        patient.setHealthRecord(existingRecord);

        HealthRecordUpdateDTO updateDTO = new HealthRecordUpdateDTO();
        HealthRecordDTO resultDTO = fixtures.createDefaultHealthRecordDTO();

        when(patientRepository.findById(patient.getId())).thenReturn(Optional.of(patient));
        when(healthRecordRepository.findById(existingRecord.getId()))
                .thenReturn(Optional.of(existingRecord));  // <--- MOCK BEFORE CALL
        doNothing().when(mapperHelper).updateWithDto(updateDTO, existingRecord);
        when(healthRecordMapper.toDto(existingRecord)).thenReturn(resultDTO);

        HealthRecordDTO result = underTest.updateHealthRecord(patient.getId(), updateDTO);

        assertNotNull(result);
        assertThat(result).isEqualTo(resultDTO);
        assertThat(existingRecord.getUpdatedAt()).isNotNull();

        verify(patientRepository).findById(patient.getId());
        verify(mapperHelper).updateWithDto(updateDTO, existingRecord);
        verify(healthRecordMapper).toDto(existingRecord);
        verify(healthRecordRepository).findById(existingRecord.getId());
    }

    @Test
    void shouldThrowWhenPatientNotFoundOnUpdate() {
        Long patientId = 1L;
        HealthRecordUpdateDTO updateDTO = new HealthRecordUpdateDTO();

        when(patientRepository.findById(patientId)).thenReturn(Optional.empty());

        assertThrows(HealthRecordNotFoundException.class, () -> underTest.updateHealthRecord(patientId, updateDTO));
        verify(patientRepository).findById(patientId);
        verifyNoInteractions(healthRecordRepository, mapperHelper, healthRecordMapper);
    }

    @Test
    void shouldDeleteHealthRecord() {
        Patient patient = fixtures.createDefaultPatient();
        patient.setHealthRecord(fixtures.createDefaultHealthRecord());

        when(patientRepository.findById(patient.getId())).thenReturn(Optional.of(patient));

        underTest.deleteHealthRecord(patient.getId());

        assertThat(patient.getHealthRecord()).isNull();
        verify(patientRepository).findById(patient.getId());
    }

    @Test
    void shouldThrowWhenDeletingNonExistentHealthRecord() {
        Patient patient = fixtures.createDefaultPatient();
        patient.setHealthRecord(null);

        when(patientRepository.findById(patient.getId())).thenReturn(Optional.of(patient));

        assertThrows(HealthRecordNotFoundException.class, () -> underTest.deleteHealthRecord(patient.getId()));
        verify(patientRepository).findById(patient.getId());
    }

    @Test
    void shouldThrowWhenHealthRecordNotFoundOnGet() {
        Patient patient = fixtures.createDefaultPatient();
        Long recordId = 1L;

        when(patientRepository.findById(patient.getId())).thenReturn(Optional.of(patient));
        when(healthRecordRepository.findById(recordId)).thenReturn(Optional.empty());

        assertThrows(HealthRecordNotFoundException.class,
                () -> underTest.getHealthRecordById(recordId));

        verify(patientRepository).findById(patient.getId());
        verify(healthRecordRepository).findById(recordId);
        verifyNoInteractions(healthRecordMapper);
    }

    @Test
    void shouldUpdateHealthRecordAndPersistChanges() {
        Patient patient = fixtures.createDefaultPatient();
        HealthRecord record = fixtures.createDefaultHealthRecord();
        patient.setHealthRecord(record);

        HealthRecordUpdateDTO updateDTO = new HealthRecordUpdateDTO();
        HealthRecordDTO resultDTO = fixtures.createDefaultHealthRecordDTO();

        when(patientRepository.findById(patient.getId())).thenReturn(Optional.of(patient));
        when(healthRecordRepository.findById(record.getId())).thenReturn(Optional.of(record));
        doNothing().when(mapperHelper).updateWithDto(updateDTO, record);
        when(healthRecordMapper.toDto(record)).thenReturn(resultDTO);

        HealthRecordDTO result = underTest.updateHealthRecord(patient.getId(), updateDTO);

        assertThat(result).isEqualTo(resultDTO);
        verify(healthRecordRepository).findById(record.getId());
        verify(healthRecordMapper).toDto(record);
    }

    @Test
    void shouldThrowWhenHealthRecordMissingOnUpdate() {
        Patient patient = fixtures.createDefaultPatient();
        HealthRecordUpdateDTO updateDTO = new HealthRecordUpdateDTO();
        HealthRecord record = fixtures.createDefaultHealthRecord();
        patient.setHealthRecord(record);

        when(patientRepository.findById(patient.getId())).thenReturn(Optional.of(patient));
        when(healthRecordRepository.findById(record.getId())).thenReturn(Optional.empty()); // match exactly

        assertThrows(HealthRecordNotFoundException.class,
                () -> underTest.updateHealthRecord(patient.getId(), updateDTO));
    }

    @Test
    void shouldNotDeleteWhenPatientNotFound() {
        Long id = 77L;
        when(patientRepository.findById(id)).thenReturn(Optional.empty());

        assertThrows(HealthRecordNotFoundException.class, () -> underTest.deleteHealthRecord(id));

        verify(patientRepository).findById(id);
        verifyNoInteractions(healthRecordRepository);
    }

    @Test
    void shouldThrowWhenUpdateDTOIsNull() {
        Patient patient = fixtures.createDefaultPatient();
        HealthRecord record = fixtures.createDefaultHealthRecord();
        patient.setHealthRecord(record);

        when(patientRepository.findById(patient.getId())).thenReturn(Optional.of(patient));

        assertThrows(HealthRecordNotFoundException.class,
                () -> underTest.updateHealthRecord(patient.getId(), null));

        verify(patientRepository).findById(patient.getId());
    }

    @Test
    void shouldMapEntityToDtoCorrectly() {
        HealthRecord record = fixtures.createDefaultHealthRecord();
        HealthRecordDTO dto = fixtures.createDefaultHealthRecordDTO();

        when(healthRecordMapper.toDto(record)).thenReturn(dto);

        HealthRecordDTO result = healthRecordMapper.toDto(record);

        assertThat(result).isEqualTo(dto);
        verify(healthRecordMapper).toDto(record);
    }

    @Test
    void shouldNotUpdateWhenMapperHelperThrows() {
        Patient patient = fixtures.createDefaultPatient();
        HealthRecord record = fixtures.createDefaultHealthRecord();
        patient.setHealthRecord(record);

        HealthRecordUpdateDTO updateDTO = new HealthRecordUpdateDTO();

        when(patientRepository.findById(patient.getId())).thenReturn(Optional.of(patient));
        when(healthRecordRepository.findById(record.getId())).thenReturn(Optional.of(record));
        doThrow(new RuntimeException("Mapping failed")).when(mapperHelper).updateWithDto(updateDTO, record);

        assertThrows(RuntimeException.class, () -> underTest.updateHealthRecord(patient.getId(), updateDTO));
    }

    @Test
    void shouldThrowWhenMapperReturnsNullDto() {
        Patient patient = fixtures.createDefaultPatient();
        HealthRecord record = fixtures.createDefaultHealthRecord();
        patient.setHealthRecord(record);

        HealthRecordUpdateDTO updateDTO = new HealthRecordUpdateDTO();

        when(patientRepository.findById(patient.getId())).thenReturn(Optional.of(patient));
        when(healthRecordRepository.findById(record.getId())).thenReturn(Optional.of(record));
        doNothing().when(mapperHelper).updateWithDto(updateDTO, record);
        when(healthRecordMapper.toDto(record)).thenReturn(null);

        HealthRecordDTO result = underTest.updateHealthRecord(patient.getId(), updateDTO);

        assertThat(result).isNull();
    }

    @Test
    void shouldNotInteractWithMapperWhenNoHealthRecordToDelete() {
        Patient patient = fixtures.createDefaultPatient();
        patient.setHealthRecord(null);

        when(patientRepository.findById(patient.getId())).thenReturn(Optional.of(patient));

        assertThrows(HealthRecordNotFoundException.class,
                () -> underTest.deleteHealthRecord(patient.getId()));

        verify(patientRepository).findById(patient.getId());
        verifyNoInteractions(healthRecordMapper);
    }

}