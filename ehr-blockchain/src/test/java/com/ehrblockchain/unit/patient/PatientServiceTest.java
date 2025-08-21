package com.ehrblockchain.unit.patient;

import java.util.List;
import java.util.Optional;

import com.ehrblockchain.patient.service.PatientService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;

import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import static org.assertj.core.api.Assertions.assertThat;
import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.*;

import com.ehrblockchain.patient.mapper.PatientMapper;
import com.ehrblockchain.patient.dto.PatientDTO;
import com.ehrblockchain.patient.dto.PatientUpdateDTO;
import com.ehrblockchain.patient.repository.PatientRepository;
import com.ehrblockchain.patient.dto.PatientCreateDTO;
import com.ehrblockchain.patient.model.Patient;
import com.ehrblockchain.exception.EmailAlreadyExistsException;
import com.ehrblockchain.exception.PatientNotFoundException;
import com.ehrblockchain.fixtures.fixtures;

@ExtendWith(MockitoExtension.class)
class PatientServiceTest {
    @Mock
    private PatientRepository patientRepository;

    @Mock
    private PatientMapper patientMapper;

    private PatientService underTest;

    @BeforeEach
    void setUp() {
        underTest = new PatientService(patientRepository, patientMapper);
    }

    @Test
    void shouldSavePatient() {
        Patient patient = fixtures.createDefaultPatient();
        PatientDTO patientDTO = fixtures.createDefaultPatientDTO();

        when(patientRepository.findByEmail(patient.getEmail())).thenReturn(Optional.empty());
        when(patientRepository.save(patient)).thenReturn(patient);
        when(patientMapper.toDto(patient)).thenReturn(patientDTO);

        PatientDTO result = underTest.savePatient(patient);

        assertNotNull(result);
        assertThat(result).usingRecursiveComparison().isEqualTo(patientDTO);

        verify(patientRepository).findByEmail(patient.getEmail());
        verify(patientRepository).save(patient);
        verify(patientMapper).toDto(patient);
    }

    @Test
    void shouldCreatePatient() {
        PatientCreateDTO createDTO = fixtures.createDefaultPatientCreateDTO();
        Patient patient = fixtures.createDefaultPatient();
        PatientDTO patientDTO = fixtures.createDefaultPatientDTO();

        when(patientMapper.toEntity(createDTO)).thenReturn(patient);
        when(patientRepository.findByEmail(patient.getEmail())).thenReturn(Optional.empty());
        when(patientRepository.save(patient)).thenReturn(patient);
        when(patientMapper.toDto(patient)).thenReturn(patientDTO);

        PatientDTO result = underTest.createPatient(createDTO);

        assertNotNull(result);
        assertThat(result).usingRecursiveComparison().isEqualTo(patientDTO);

        verify(patientMapper).toEntity(createDTO);
        verify(patientRepository).findByEmail(patient.getEmail());
        verify(patientRepository).save(patient);
        verify(patientMapper).toDto(patient);
    }

    @Test
    void shouldUpdatePatient() {
        Patient existingPatient = fixtures.createDefaultPatient();
        PatientUpdateDTO updateDTO = fixtures.createDefaultPatientUpdateDTO();
        PatientDTO updatedPatientDTO = fixtures.createDefaultPatientDTO();

        when(patientRepository.findById(existingPatient.getId())).thenReturn(Optional.of(existingPatient));
        doAnswer(invocation -> {
            PatientUpdateDTO dto = invocation.getArgument(0);
            Patient patient = invocation.getArgument(1);
            patient.setFirstName(dto.getFirstName());
            patient.setLastName(dto.getLastName());
            return null;
        }).when(patientMapper).updateFromDto(updateDTO, existingPatient);

        doNothing().when(patientMapper).updateNestedEntitiesFromDto(updateDTO, existingPatient);
        when(patientMapper.toDto(existingPatient)).thenReturn(updatedPatientDTO);

        PatientDTO result = underTest.updatePatient(existingPatient.getId(), updateDTO);

        assertNotNull(result);
        assertThat(result).usingRecursiveComparison().isEqualTo(updatedPatientDTO);

        verify(patientRepository).findById(existingPatient.getId());
        verify(patientMapper).updateFromDto(updateDTO, existingPatient);
        verify(patientMapper).updateNestedEntitiesFromDto(updateDTO, existingPatient);
        verify(patientMapper).toDto(existingPatient);
    }

    @Test
    void shouldDeletePatient() {
        Long patientId = 1L;

        underTest.deletePatient(patientId);

        verify(patientRepository).deleteById(patientId);
        verifyNoMoreInteractions(patientRepository);
    }

    @Test
    void shouldGetAllPatients() {
        List<Patient> patients = List.of(fixtures.createDefaultPatient());
        List<PatientDTO> patientDTOs = List.of(fixtures.createDefaultPatientDTO());

        when(patientRepository.findAll()).thenReturn(patients);
        when(patientMapper.toDto(any(Patient.class)))
                .thenAnswer(invocation -> fixtures.createDefaultPatientDTO());

        List<PatientDTO> result = underTest.getAllPatients();

        assertNotNull(result);
        assertEquals(patientDTOs.size(), result.size());
        assertThat(result).usingRecursiveComparison().isEqualTo(patientDTOs);

        verify(patientRepository).findAll();
        verify(patientMapper).toDto(any(Patient.class));
    }

    @Test
    void shouldGetPatientById() {
        Long patientId = 1L;

        when(patientRepository.findById(patientId)).thenReturn(Optional.of(fixtures.createDefaultPatient()));
        when(patientMapper.toDto(any(Patient.class))).thenReturn(fixtures.createDefaultPatientDTO());

        PatientDTO result = underTest.getPatientById(patientId);

        assertThat(result).isNotNull();
        assertThat(result).usingRecursiveComparison().isEqualTo(fixtures.createDefaultPatientDTO());

        verify(patientRepository).findById(patientId);
        verify(patientMapper).toDto(any(Patient.class));
    }

    @Test
    void shouldGetPatientByEmail() {
        String email = "test@example.com";
        Patient patient = fixtures.createDefaultPatient();
        PatientDTO patientDTO = fixtures.createDefaultPatientDTO();

        when(patientRepository.findByEmail(email)).thenReturn(Optional.of(patient));
        when(patientMapper.toDto(patient)).thenReturn(patientDTO);

        PatientDTO result = underTest.getPatientByEmail(email);

        assertNotNull(result);
        assertThat(result).usingRecursiveComparison().isEqualTo(patientDTO);

        verify(patientRepository).findByEmail(email);
        verify(patientMapper).toDto(patient);
    }

    @Test
    void shouldThrowWhenSavingPatientIfEmailExists() {
        Patient patient = fixtures.createDefaultPatient();

        when(patientRepository.findByEmail(patient.getEmail())).thenReturn(Optional.of(patient));

        assertThrows(EmailAlreadyExistsException.class, () -> underTest.savePatient(patient));

        verify(patientRepository).findByEmail(patient.getEmail());
        verify(patientRepository, never()).save(any());
        verify(patientMapper, never()).toDto(any(Patient.class));
    }

    @Test
    void shouldThrowWhenCreatingPatientIfEmailExists() {
        PatientCreateDTO createDTO = fixtures.createDefaultPatientCreateDTO();
        Patient patient = fixtures.createDefaultPatient();

        when(patientMapper.toEntity(createDTO)).thenReturn(patient);
        when(patientRepository.findByEmail(patient.getEmail())).thenReturn(Optional.of(patient));

        assertThrows(EmailAlreadyExistsException.class, () -> underTest.createPatient(createDTO));

        verify(patientMapper).toEntity(createDTO);
        verify(patientRepository).findByEmail(patient.getEmail());
        verify(patientRepository, never()).save(any());
        verify(patientMapper, never()).toDto(any());
    }

    @Test
    void shouldThrowWhenUpdatingPatientIfNotFound() {
        Long patientId = 1L;
        PatientUpdateDTO updateDTO = fixtures.createDefaultPatientUpdateDTO();

        when(patientRepository.findById(patientId)).thenReturn(Optional.empty());

        assertThrows(PatientNotFoundException.class, () -> underTest.updatePatient(patientId, updateDTO));

        verify(patientRepository).findById(patientId);
        verify(patientMapper, never()).updateFromDto(any(), any());
        verify(patientMapper, never()).updateNestedEntitiesFromDto(any(), any());
        verify(patientRepository, never()).save(any());
        verify(patientMapper, never()).toDto(any());
    }

    @Test
    void shouldPropagateWhenMapperThrowsOnUpdate() {
        Patient existingPatient = fixtures.createDefaultPatient();
        PatientUpdateDTO updateDTO = fixtures.createDefaultPatientUpdateDTO();

        when(patientRepository.findById(existingPatient.getId())).thenReturn(Optional.of(existingPatient));
        doThrow(new RuntimeException("mapper failure")).when(patientMapper).updateFromDto(updateDTO, existingPatient);

        assertThrows(RuntimeException.class, () -> underTest.updatePatient(existingPatient.getId(), updateDTO));

        verify(patientRepository).findById(existingPatient.getId());
        verify(patientMapper).updateFromDto(updateDTO, existingPatient);
        verify(patientRepository, never()).save(any());
    }

    @Test
    void shouldPropagateWhenRepositoryThrowsOnDelete() {
        Long patientId = 1L;

        doThrow(new RuntimeException("delete failed")).when(patientRepository).deleteById(patientId);

        assertThrows(RuntimeException.class, () -> underTest.deletePatient(patientId));

        verify(patientRepository).deleteById(patientId);
    }

    @Test
    void shouldPropagateWhenMapperThrowsOnGetAll() {
        List<Patient> patients = List.of(fixtures.createDefaultPatient());

        when(patientRepository.findAll()).thenReturn(patients);
        when(patientMapper.toDto(any(Patient.class))).thenThrow(new RuntimeException("map fail"));

        assertThrows(RuntimeException.class, () -> underTest.getAllPatients());

        verify(patientRepository).findAll();
        verify(patientMapper).toDto(any(Patient.class));
    }

    @Test
    void shouldThrowWhenGetPatientByIdNotFound() {
        Long patientId = 1L;

        when(patientRepository.findById(patientId)).thenReturn(Optional.empty());

        assertThrows(PatientNotFoundException.class, () -> underTest.getPatientById(patientId));

        verify(patientRepository).findById(patientId);
        verify(patientMapper, never()).toDto(any());
    }

    @Test
    void shouldThrowWhenGetPatientByEmailNotFound() {
        String email = "notfound@example.com";

        when(patientRepository.findByEmail(email)).thenReturn(Optional.empty());

        assertThrows(PatientNotFoundException.class, () -> underTest.getPatientByEmail(email));

        verify(patientRepository).findByEmail(email);
        verify(patientMapper, never()).toDto(any());
    }
}