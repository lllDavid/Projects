package com.ehrblockchain.config;

import org.springdoc.core.customizers.OpenApiCustomizer;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import io.swagger.v3.oas.models.Components;
import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.Operation;
import io.swagger.v3.oas.models.PathItem;
import io.swagger.v3.oas.models.examples.Example;
import io.swagger.v3.oas.models.info.Info;
import io.swagger.v3.oas.models.media.Content;
import io.swagger.v3.oas.models.security.SecurityRequirement;
import io.swagger.v3.oas.models.security.SecurityScheme;

@Configuration
public class OpenApiConfig {

    private static final String SECURITY_SCHEME_NAME = "bearerAuth";

    @Bean
    public OpenAPI customOpenAPI() {
        return new OpenAPI()
                .info(new Info().title("EHR Blockchain"))
                .addSecurityItem(new SecurityRequirement().addList(SECURITY_SCHEME_NAME))
                .components(new Components()
                        .addSecuritySchemes(SECURITY_SCHEME_NAME,
                                new SecurityScheme()
                                        .name("Authorization")
                                        .type(SecurityScheme.Type.HTTP)
                                        .scheme("bearer")
                                        .bearerFormat("JWT")));
    }

    @Bean
    public OpenApiCustomizer addExamples() {
        return openApi -> {

            addExample(openApi, "/auth/register", """
                    {
                      "firstName": "admin",
                      "lastName": "admin",
                      "email": "admin.admin@example.com",
                      "password": "hJ2$wQ6&nR5!pVz8yDf"
                    }
                    """, "registerExample");

            addExample(openApi, "/auth/login", """
                    {
                       "email": "admin.admin@example.com",
                      "password": "hJ2$wQ6&nR5!pVz8yDf"
                    }
                    """, "loginExample");

            addExample(openApi, "/users", """
                    {
                       "firstName": "John",
                      "lastName": "Doe",
                      "email": "john.doe@example.com",
                      "password": "sM9!vH2$gN6@cXj4qRb"
                    }
                    """, "usersCreateExample");

            addExample(openApi, "/users/{id}", """
                    {
                       "firstName": "John",
                      "lastName": "Doe",
                      "email": "john.doe1987@example.com",
                      "password": "sM9!vH2$gN6@cXj4qRb"
                    }
                    """, "usersUpdateExample");

            addExample(openApi, "/users/create-elevated", """
                    {
                      "firstName": "Jane",
                      "lastName": "Smith",
                      "email": "jane.smith@example.com",
                      "password": "dQ3#bZ8&yT5!fKp7wLg"
                    }
                    """, "usersCreateElevatedExample");

            setDescription(openApi, "/chain",
                    "The chain's max transactions per block is 3 for development. After 3 transactions (via GET, PATCH or DELETE requests) on a health record, a block is created.");

            setPostDescription(openApi, "/users",
                    "For development every user is created with role ADMIN. Role is determined by the active profile in resources/application.yml:");

            setDescription(openApi, "/auth/register",
                    "For development every user is created with role ADMIN. Role is determined by the active profile in resources/application.yml:");

            addExample(openApi, "/patients", """
                    {
                      "recordDate": "2025-08-28",
                      "firstName": "Alice",
                      "lastName": "Smith",
                      "dateOfBirth": "1990-04-22",
                      "gender": "Female",
                      "height": 165.0,
                      "weight": 60.0,
                      "bloodType": "A+",
                      "phoneNumber": "+15551234567",
                      "email": "alice.smith@example.com",
                      "emergencyContact": "Bob Smith",
                      "address": {
                        "street": "456 Elm St",
                        "city": "Metropolis",
                        "state": "NY",
                        "postalCode": "10001",
                        "country": "USA"
                      },
                      "insurance": {
                        "providerName": "HealthPlan Inc.",
                        "policyNumber": "HP123456",
                        "groupNumber": "GRP001",
                        "coverageStartDate": "2023-01-01",
                        "coverageEndDate": "2026-12-31"
                      }
                    }
                    """, "patientsCreateExample");

            addExample(openApi, "/patients/{id}", """
                    {
                      "recordDate": "2025-08-28",
                      "firstName": "Alice",
                      "lastName": "Smith",
                      "dateOfBirth": "1990-04-22",
                      "gender": "Female",
                      "height": 165.0,
                      "weight": 60.0,
                      "bloodType": "A+",
                      "phoneNumber": "+123456789",
                      "email": "alice.smith1996@example.com",
                      "emergencyContact": "Martin Smith",
                      "address": {
                        "street": "456 New Street",
                        "city": "New York",
                        "state": "NY",
                        "postalCode": "10001",
                        "country": "USA"
                      },
                      "insurance": {
                        "providerName": "HealthPlan Inc.",
                        "policyNumber": "HP123456",
                        "groupNumber": "GRP001",
                        "coverageStartDate": "2023-01-01",
                        "coverageEndDate": "2026-12-31"
                      }
                    }
                    """, "patientsUpdateExample");

            addExample(openApi, "/patients/{patientId}/healthrecord", """
                    {
                      "notes": [
                        { "content": "Patient is recovering well from surgery." }
                      ],
                      "diagnoses": [
                        { "code": "I10", "description": "Hypertension", "severity": "Moderate", "diagnosedDate": "2023-05-15" }
                      ],
                      "treatmentPlans": [
                        { "type": "Physical Therapy", "startDate": "2025-08-01", "endDate": "2025-09-01", "notes": "Focus on lower back exercises" }
                      ],
                      "prescriptions": [
                        { "drugName": "Lisinopril", "dosage": "10mg", "frequency": "Once daily", "duration": "30 days" }
                      ],
                      "vitals": [
                        { "bloodPressure": "120/80", "temperature": 36.6, "heartRate": 72, "respiratoryRate": 16, "oxygenSaturation": 98 }
                      ],
                      "cbcTests": [
                        { "testDate": "2025-08-20", "redBloodCellCount": 4500000, "whiteBloodCellCount": 7000, "hemoglobin": 14.0, "hematocrit": 42.0, "plateletCount": 250000 }
                      ],
                      "allergies": [
                        { "allergen": "Peanuts", "reaction": "Hives", "severity": "Severe" }
                      ],
                      "labResults": [
                        { "testName": "Blood Glucose", "testDate": "2025-08-22", "result": "95 mg/dL" }
                      ],
                      "immunizations": [
                        { "vaccineName": "Influenza", "dateAdministered": "2024-10-01", "provider": "Health Clinic" }
                      ],
                      "medicalHistory": [
                        { "condition": "Asthma", "diagnosisDate": "2010-04-15", "notes": "Mild, controlled with inhaler" }
                      ],
                      "familyHistory": [
                        { "relative": "Father", "condition": "Diabetes", "notes": "Type 2" }
                      ],
                      "encounters": [
                        { "encounterDate": "2025-08-25", "provider": "Dr. Smith", "reason": "Routine checkup" }
                      ],
                      "procedures": [
                        { "procedureName": "Appendectomy", "procedureDate": "2015-06-10", "notes": "No complications" }
                      ]
                    }
                    """, "healthRecordUpdateExample");

        };
    }

    public void addExample(OpenAPI api, String path, String json, String name) {
        if (api.getPaths() == null) return;
        PathItem p = api.getPaths().get(path);
        if (p == null) return;

        Operation get = p.getGet();
        if (get != null && get.getResponses() != null)
            get.getResponses().forEach((s, r) -> {
                if (r.getContent() == null) r.setContent(new Content());
                r.getContent().computeIfAbsent("application/json", k -> new io.swagger.v3.oas.models.media.MediaType())
                        .addExamples(name, new Example().value(json));
            });

        for (Operation op : new Operation[]{p.getPost(), p.getPut(), p.getPatch()})
            if (op != null && op.getRequestBody() != null) {
                Content c = op.getRequestBody().getContent();
                if (c != null && c.get("application/json") != null)
                    c.get("application/json").addExamples(name, new Example().value(json));
            }
    }

    public void setDescription(OpenAPI api, String path, String desc) {
        if (api.getPaths() == null) return;
        PathItem p = api.getPaths().get(path);
        if (p == null) return;

        for (Operation op : new Operation[]{p.getGet(), p.getPost(), p.getPut(), p.getPatch()}) {
            if (op != null) op.setDescription(desc);
        }
    }

    public void setPostDescription(OpenAPI api, String path, String desc) {
        if (api.getPaths() == null) return;
        PathItem p = api.getPaths().get(path);
        if (p == null) return;

        Operation post = p.getPost();
        if (post != null) post.setDescription(desc);
    }
}