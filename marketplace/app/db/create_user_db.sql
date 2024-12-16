CREATE DATABASE marketplace_users;
USE marketplace_users;

-- Create user_profile table
CREATE TABLE user_profile (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- User ID (Primary Key)
    username VARCHAR(255),              -- Username
    email VARCHAR(255),                 -- Email
    role ENUM('user', 'admin', 'moderator')  -- Role (Assuming role types)
);

-- Create user_bank table
CREATE TABLE user_bank (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Bank ID (Primary Key)
    user_id INT,                        -- Foreign Key to user_profile
    bank_name VARCHAR(255),             -- Bank Name
    account_holder VARCHAR(255),        -- Account Holder's Name
    account_number VARCHAR(255),        -- Account Number
    routing_number VARCHAR(255),        -- Routing Number
    iban VARCHAR(255),                  -- IBAN
    swift_bic VARCHAR(255),             -- SWIFT/BIC Code
    date_linked DATE,                   -- Date when the account was linked
    FOREIGN KEY (user_id) REFERENCES user_profile(id)
);

-- Create user_status table
CREATE TABLE user_status (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Status ID (Primary Key)
    user_id INT,                        -- Foreign Key to user_profile
    is_banned BOOLEAN DEFAULT FALSE,    -- Is the user banned?
    is_inactive BOOLEAN DEFAULT FALSE,  -- Is the user inactive?
    ban_type ENUM('temporary', 'permanent') DEFAULT 'temporary',  -- Ban type
    ban_reason TEXT,                    -- Reason for the ban
    ban_duration INT,                   -- Duration of the ban in days (if applicable)
    ban_start_time DATETIME,            -- When the ban started
    ban_end_time DATETIME,              -- When the ban ends
    FOREIGN KEY (user_id) REFERENCES user_profile(id)
);

-- Create user_history table
CREATE TABLE user_history (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- History ID (Primary Key)
    user_id INT,                        -- Foreign Key to user_profile
    login_count INT DEFAULT 0,          -- Login Count
    last_login DATETIME,                -- Last login timestamp
    failed_login_count INT DEFAULT 0,   -- Failed login attempts
    last_failed_login DATETIME,         -- Last failed login timestamp
    created_at DATETIME,                -- Account creation time
    updated_at DATETIME,                -- Last account update time
    FOREIGN KEY (user_id) REFERENCES user_profile(id)
);

-- Create user_security table
CREATE TABLE user_security (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Security ID (Primary Key)
    user_id INT,                        -- Foreign Key to user_profile
    password_hash VARCHAR(255),         -- Hashed password
    two_factor_enabled BOOLEAN DEFAULT FALSE,  -- Whether 2FA is enabled
    two_factor_secret_key VARCHAR(255), -- Secret key for 2FA (if enabled)
    two_factor_backup_codes_hash JSON,  -- Backup codes for 2FA in JSON format
    FOREIGN KEY (user_id) REFERENCES user_profile(id)
);

-- Create user_fingerprint table
CREATE TABLE user_fingerprint (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Fingerprint ID (Primary Key)
    user_id INT,                        -- Foreign Key to user_profile
    username_history JSON,              -- Username history (in JSON format)
    email_address_history JSON,         -- Email address history (in JSON format)
    mac_address VARCHAR(255),           -- MAC Address
    associated_ips JSON,                -- Associated IPs (in JSON format)
    avg_login_frequency FLOAT,          -- Average login frequency
    avg_session_duration FLOAT,         -- Average session duration
    geolocation_country VARCHAR(255),   -- Country of user (geolocation)
    geolocation_city VARCHAR(255),      -- City of user (geolocation)
    geolocation_latitude FLOAT,         -- Latitude of user
    geolocation_longitude FLOAT,        -- Longitude of user
    browser_info VARCHAR(255),          -- Browser Information
    os_name VARCHAR(255),               -- OS Name
    os_version VARCHAR(255),            -- OS Version
    device_type VARCHAR(255),           -- Device Type (mobile, desktop, etc.)
    device_manufacturer VARCHAR(255),   -- Device Manufacturer
    device_model VARCHAR(255),          -- Device Model
    user_preferences JSON,              -- User preferences (in JSON format)
    user_agent VARCHAR(255),            -- User Agent string
    device_id VARCHAR(255),             -- Device ID
    screen_resolution VARCHAR(255),     -- Screen resolution
    two_factor_enabled BOOLEAN DEFAULT FALSE,  -- Whether 2FA is enabled
    transaction_history JSON,           -- User's transaction history (in JSON format)
    vpn_usage BOOLEAN DEFAULT FALSE,    -- Whether VPN usage is detected
    behavioral_biometrics JSON,         -- Behavioral biometrics (in JSON format)
    FOREIGN KEY (user_id) REFERENCES user_profile(id)
);
