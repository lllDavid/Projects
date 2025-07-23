package com.ehrblockchain;

import java.time.LocalDate;
import java.util.List;

import com.ehrblockchain.healthrecord.service.HealthRecordService;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;

import com.ehrblockchain.patient.model.Patient;
import com.ehrblockchain.patient.model.Address;
import com.ehrblockchain.patient.model.Insurance;
import com.ehrblockchain.patient.service.PatientService;

import com.ehrblockchain.healthrecord.model.*;

@SpringBootApplication
public class EhrBlockchainApplication {

    public static void main(String[] args) {
        ApplicationContext context = SpringApplication.run(EhrBlockchainApplication.class, args);
        PatientService patientService = context.getBean(PatientService.class);

        // ---------- Create Address ----------
        Address address = new Address();
        address.setStreet("123 Main St");
        address.setCity("Springfield");
        address.setState("IL");
        address.setPostalCode("62704");
        address.setCountry("USA");

        // ---------- Create Insurance ----------
        Insurance insurance = new Insurance();
        insurance.setProviderName("Acme Insurance");
        insurance.setPolicyNumber("POL123456789");
        insurance.setGroupNumber("GRP98765");
        insurance.setCoverageStartDate(LocalDate.of(2024, 1, 1));
        insurance.setCoverageEndDate(LocalDate.of(2025, 1, 1));

        // ---------- Create Patient ----------
        Patient patient = new Patient();
        patient.setFirstName("Robert");
        patient.setLastName("Jensen");
        patient.setDateOfBirth(LocalDate.of(1985, 4, 12));
        patient.setGender("Male");
        patient.setHeight(180.00);
        patient.setWeight(80.00);
        patient.setPhoneNumber("555-123-4567");
        patient.setEmail("robert.jensen3@gmail.com");
        patient.setEmergencyContact("Sarah Jensen");
        patient.setAddress(address);
        patient.setInsurance(insurance);

        // ---------- Create HealthRecord ----------
        HealthRecord healthRecord = new HealthRecord();
        healthRecord.setRecordDate(LocalDate.now());

        // ---------- Create Individual Health Details ----------
        Allergy allergy = new Allergy();
        allergy.setAllergen("Peanuts");
        allergy.setReaction("Anaphylaxis");
        allergy.setSeverity("High");
        allergy.setHealthRecord(healthRecord);

        Diagnosis diagnosis = new Diagnosis();
        diagnosis.setCode("J45");
        diagnosis.setDescription("Asthma");
        diagnosis.setSeverity("Moderate");
        diagnosis.setDiagnosedDate(LocalDate.of(2020, 5, 20));
        diagnosis.setHealthRecord(healthRecord);

        Encounter encounter = new Encounter();
        encounter.setEncounterDate(LocalDate.of(2024, 3, 15));
        encounter.setProvider("Dr. Smith");
        encounter.setReason("Annual check-up");
        encounter.setHealthRecord(healthRecord);

        FamilyHistory familyHistory = new FamilyHistory();
        familyHistory.setRelative("Mother");
        familyHistory.setCondition("Hypertension");
        familyHistory.setNotes("Diagnosed at age 50");
        familyHistory.setHealthRecord(healthRecord);

        Immunization immunization = new Immunization();
        immunization.setVaccineName("Influenza");
        immunization.setDateAdministered(LocalDate.of(2023, 10, 15));
        immunization.setProvider("City Health Clinic");
        immunization.setHealthRecord(healthRecord);

        LabResult labResult = new LabResult();
        labResult.setTestName("CBC");
        labResult.setTestDate(LocalDate.of(2024, 2, 10));
        labResult.setResult("Normal");
        labResult.setHealthRecord(healthRecord);

        MedicalHistory medicalHistory = new MedicalHistory();
        medicalHistory.setCondition("Type 2 Diabetes");
        medicalHistory.setDiagnosisDate(LocalDate.of(2018, 6, 1));
        medicalHistory.setNotes("Managed with diet and exercise");
        medicalHistory.setHealthRecord(healthRecord);

        Prescription prescription = new Prescription();
        prescription.setDrugName("Metformin");
        prescription.setDosage("500mg");
        prescription.setFrequency("Twice daily");
        prescription.setDuration("6 months");
        prescription.setHealthRecord(healthRecord);

        Procedure procedure = new Procedure();
        procedure.setProcedureName("Appendectomy");
        procedure.setProcedureDate(LocalDate.of(2023, 11, 20));
        procedure.setNotes("No complications");
        procedure.setHealthRecord(healthRecord);

        TreatmentPlan treatmentPlan = new TreatmentPlan();
        treatmentPlan.setType("Physical Therapy");
        treatmentPlan.setStartDate(LocalDate.of(2024, 7, 1));
        treatmentPlan.setEndDate(LocalDate.of(2024, 9, 30));
        treatmentPlan.setNotes("Focus on lower back pain");
        treatmentPlan.setHealthRecord(healthRecord);

        Vitals vitals = new Vitals();
        vitals.setBloodPressure("120/80");
        vitals.setTemperature(98.6);
        vitals.setHeartRate(72);
        vitals.setRespiratoryRate(16);
        vitals.setOxygenSaturation(98);
        vitals.setHealthRecord(healthRecord);

        CBC cbc = new CBC();
        cbc.setTestDate(LocalDate.of(2025, 7, 11));
        cbc.setRedBloodCellCount(4500000);
        cbc.setWhiteBloodCellCount(7000);
        cbc.setHemoglobin(14.5);
        cbc.setHematocrit(42.0);
        cbc.setPlateletCount(250000);
        cbc.setHealthRecord(healthRecord);

        Note note = new Note();
        note.setContent("Focus on lower back pain");
        note.setHealthRecord(healthRecord);


        // ---------- Aggregate all health data into HealthRecord ----------
        healthRecord.setDiagnoses(List.of(diagnosis));
        healthRecord.setTreatmentPlans(List.of(treatmentPlan));
        healthRecord.setPrescriptions(List.of(prescription));
        healthRecord.setAllergies(List.of(allergy));
        healthRecord.setNotes(List.of(note));
        healthRecord.setLabResults(List.of(labResult));
        healthRecord.setVitals(List.of(vitals));
        healthRecord.setCbcTests(List.of(cbc));
        healthRecord.setImmunizations(List.of(immunization));
        healthRecord.setMedicalHistory(List.of(medicalHistory));
        healthRecord.setFamilyHistory(List.of(familyHistory));
        healthRecord.setEncounters(List.of(encounter));
        healthRecord.setProcedures(List.of(procedure));

        // ---------- Associate patient and health record ----------
        patient.setHealthRecord(healthRecord);
        healthRecord.setPatient(patient);

        // ---------- Persist patient with associated records ----------
        patientService.savePatientWithHealthRecord(patient);

        // ---------- Fetch and log patient data ----------
        System.out.println("! GetByID: " + patientService.getPatientById(patient.getId()));
        System.out.println("! GetByEmail: " + patientService.getPatientByEmail(patient.getEmail()));
        System.out.println("! GetAllPatients: " + patientService.getAllPatients());
        System.out.println("! GetHealthRecord: " + patient.getHealthRecord());


        // ---------- Update patient ----------
        Long patientId = patient.getId();
        Patient updatedPatient = new Patient();
        updatedPatient.setFirstName("Daniel");
        updatedPatient.setLastName("Johnson");
        Patient updated = patientService.updatePatient(patientId, updatedPatient);
        System.out.println("Updated: " + updated);

        // ---------- Delete patient ----------
        // patientService.deletePatientById(patient.getId());

    }
}