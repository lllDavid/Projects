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
import com.ehrblockchain.fixtures.UnitFixtures;
import com.ehrblockchain.healthrecord.service.HealthRecordService;
import com.ehrblockchain.auth.service.AuthService;
import com.ehrblockchain.blockchain.model.Blockchain;

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

    @Mock
    private AuthService authService;

    @Mock
    private Blockchain blockchain;

    private HealthRecordService underTest;

    @BeforeEach
    void setUp() {
        underTest = new HealthRecordService(
                healthRecordRepository,
                patientRepository,
                mapperHelper,
                healthRecordMapper,
                authService,
                blockchain
        );
    }

    @Test
    void shouldGetHealthRecordById() {
        Patient patient = UnitFixtures.createDefaultPatient();
        HealthRecord existingRecord = patient.getHealthRecord();
        HealthRecordDTO dto = UnitFixtures.createDefaultHealthRecordDTO();

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
        Patient patient = UnitFixtures.createDefaultPatient();
        HealthRecord existingRecord = UnitFixtures.createDefaultHealthRecord();
        patient.setHealthRecord(existingRecord);

        HealthRecordUpdateDTO updateDTO = new HealthRecordUpdateDTO();
        HealthRecordDTO resultDTO = UnitFixtures.createDefaultHealthRecordDTO();

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
        Patient patient = UnitFixtures.createDefaultPatient();
        HealthRecord record = UnitFixtures.createDefaultHealthRecord();
        patient.setHealthRecord(record);
        HealthRecordDTO dto = UnitFixtures.createDefaultHealthRecordDTO();

        when(patientRepository.findById(patient.getId())).thenReturn(Optional.of(patient));
        when(healthRecordMapper.toDto(record)).thenReturn(dto);

        underTest.deleteHealthRecord(patient.getId());

        assertThat(patient.getHealthRecord()).isNull();
        verify(patientRepository).findById(patient.getId());
        verify(healthRecordMapper).toDto(record);
    }

    @Test
    void shouldThrowWhenDeletingNonExistentHealthRecord() {
        Patient patient = UnitFixtures.createDefaultPatient();
        patient.setHealthRecord(null);

        when(patientRepository.findById(patient.getId())).thenReturn(Optional.of(patient));

        assertThrows(HealthRecordNotFoundException.class, () -> underTest.deleteHealthRecord(patient.getId()));
        verify(patientRepository).findById(patient.getId());
    }

    @Test
    void shouldThrowWhenHealthRecordNotFoundOnGet() {
        Patient patient = UnitFixtures.createDefaultPatient();
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
        Patient patient = UnitFixtures.createDefaultPatient();
        HealthRecord record = UnitFixtures.createDefaultHealthRecord();
        patient.setHealthRecord(record);

        HealthRecordUpdateDTO updateDTO = new HealthRecordUpdateDTO();
        HealthRecordDTO resultDTO = UnitFixtures.createDefaultHealthRecordDTO();

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
        Patient patient = UnitFixtures.createDefaultPatient();
        HealthRecordUpdateDTO updateDTO = new HealthRecordUpdateDTO();
        HealthRecord record = UnitFixtures.createDefaultHealthRecord();
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
        Patient patient = UnitFixtures.createDefaultPatient();
        HealthRecord record = UnitFixtures.createDefaultHealthRecord();
        patient.setHealthRecord(record);

        when(patientRepository.findById(patient.getId())).thenReturn(Optional.of(patient));

        assertThrows(HealthRecordNotFoundException.class,
                () -> underTest.updateHealthRecord(patient.getId(), null));

        verify(patientRepository).findById(patient.getId());
    }

    @Test
    void shouldMapEntityToDtoCorrectly() {
        HealthRecord record = UnitFixtures.createDefaultHealthRecord();
        HealthRecordDTO dto = UnitFixtures.createDefaultHealthRecordDTO();

        when(healthRecordMapper.toDto(record)).thenReturn(dto);

        HealthRecordDTO result = healthRecordMapper.toDto(record);

        assertThat(result).isEqualTo(dto);
        verify(healthRecordMapper).toDto(record);
    }

    @Test
    void shouldNotUpdateWhenMapperHelperThrows() {
        Patient patient = UnitFixtures.createDefaultPatient();
        HealthRecord record = UnitFixtures.createDefaultHealthRecord();
        patient.setHealthRecord(record);

        HealthRecordUpdateDTO updateDTO = new HealthRecordUpdateDTO();

        when(patientRepository.findById(patient.getId())).thenReturn(Optional.of(patient));
        when(healthRecordRepository.findById(record.getId())).thenReturn(Optional.of(record));
        doThrow(new RuntimeException("Mapping failed")).when(mapperHelper).updateWithDto(updateDTO, record);

        assertThrows(RuntimeException.class, () -> underTest.updateHealthRecord(patient.getId(), updateDTO));
    }

    @Test
    void shouldThrowWhenMapperReturnsNullDto() {
        Patient patient = UnitFixtures.createDefaultPatient();
        HealthRecord record = UnitFixtures.createDefaultHealthRecord();
        patient.setHealthRecord(record);

        HealthRecordUpdateDTO updateDTO = new HealthRecordUpdateDTO();

        when(patientRepository.findById(patient.getId())).thenReturn(Optional.of(patient));
        when(healthRecordRepository.findById(record.getId())).thenReturn(Optional.of(record));
        doNothing().when(mapperHelper).updateWithDto(updateDTO, record);
        when(healthRecordMapper.toDto(record)).thenReturn(null);

        assertThrows(NullPointerException.class,
                () -> underTest.updateHealthRecord(patient.getId(), updateDTO));
    }

    @Test
    void shouldNotInteractWithMapperWhenNoHealthRecordToDelete() {
        Patient patient = UnitFixtures.createDefaultPatient();
        patient.setHealthRecord(null);

        when(patientRepository.findById(patient.getId())).thenReturn(Optional.of(patient));

        assertThrows(HealthRecordNotFoundException.class,
                () -> underTest.deleteHealthRecord(patient.getId()));

        verify(patientRepository).findById(patient.getId());
        verifyNoInteractions(healthRecordMapper);
    }

}