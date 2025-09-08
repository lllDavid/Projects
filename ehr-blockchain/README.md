# Electronic Health Record Blockchain
- This backend manages users, patient information and health records, providing secure, controlled access. Encryption and a custom blockchain ensure data integrity, prevent tampering, and maintain a complete log of all access and changes.

## Features
- RESTful CRUD APIs for Users, Patients, and Health Records
- Custom Blockchain with Merkle Tree for data integrity
- Data Transfer Objects (DTOs) for create, update, and response operations
- OAuth2 and JWT-based Authentication for secure access
- Role-Based Access Control (RBAC)
- Input Validation and Custom Error Handling
- Unit and Integration Tests for controllers, services, and repositories
- Token Bucket-based Rate Limiting on APIs
- Password Hashing with Argon2id
- AES-256 Encryption for Health Records
- Swagger/OpenAPI Documentation for all endpoints

## Prerequisites
- Java JDK 21 or higher
- PostgreSQL 17.5 or higher
- IDE with Maven support or Apache Maven installed

## Setting Up The Environment
- Create a Database `ehr` in PostgreSQL
- For testing create a Database `ehr_test`

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/lllDavid/ehr-blockchain
```

### 2. Navigate to the directory
```text
cd ehr-blockchain
```

### 3. Create .env file
- Place a .env file at the project root before building or running the app
- Provide credentials for the DB configuration and JWT secret key, following the .env.example

### 4. Build the app
```bash
./mvnw clean install (Maven Wrapper) or mvn clean install (Global Maven)
```

### 5. Run the app
```bash
./mvnw spring-boot:run (Maven Wrapper) or mvn spring-boot:run (Global Maven)
```

## Swagger Documentation
- API spec: [http://localhost:8080/v3/api-docs](http://localhost:8080/v3/api-docs)
- Swagger UI: [http://localhost:8080/swagger-ui/index.html](http://localhost:8080/swagger-ui/index.html)

## API Quickstart

### 1. Open Swagger UI
- Go to: [http://localhost:8080/swagger-ui/index.html](http://localhost:8080/swagger-ui/index.html)

### 2. Register a User
- Send a `POST` request to `/auth/register` with required credentials

### 3. Authenticate
- Send a `POST` request to `/auth/login` with required credentials

### 4. Copy the JWT token
- From the response body, copy the string inside the quotes after `"token"`

### 5. Authorize Swagger
- Click the **Authorize** button in the top-right corner and paste the token

### 6. Access secured APIs
- After authorizing, you can make requests to all endpoints