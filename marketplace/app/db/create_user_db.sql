CREATE DATABASE marketplace_users;
USE marketplace_users;

-- Table for storing basic user information
CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for the user
    username VARCHAR(255),                    -- User's username
    email VARCHAR(255),                       -- User's email
    role INT,                                 -- Role: 1=User, 2=Support, 3=Admin
    CHECK (role IN (1, 2, 3))                 -- Validates that the role is 1, 2, or 3
);

-- Table for storing user's bank information
CREATE TABLE user_bank (
    id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for the bank record
    user_id INT,                            -- Foreign key reference to the user table
    bank_name VARCHAR(255),                 -- Bank name
    account_holder VARCHAR(255),            -- Name of the account holder
    account_number VARCHAR(50),             -- Bank account number
    routing_number VARCHAR(50),             -- Routing number
    iban VARCHAR(50),                       -- IBAN number
    swift_bic VARCHAR(50),                  -- SWIFT/BIC code
    date_linked TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- When the bank account was linked
    FOREIGN KEY (user_id) REFERENCES user(id) -- Foreign key to user table
);

-- Table for storing user's status information (ban, inactivity, etc.)
CREATE TABLE user_status (
    id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for the status record
    user_id INT,                            -- Foreign key reference to the user table
    is_banned BOOLEAN DEFAULT FALSE,        -- Whether the user is banned
    is_inactive BOOLEAN DEFAULT FALSE,      -- Whether the user is inactive
    ban_type VARCHAR(50),                   -- Type of ban (if any)
    ban_reason TEXT,                        -- Reason for the ban
    ban_duration INT,                       -- Duration of the ban (in seconds, or NULL for permanent)
    ban_start_time TIMESTAMP,               -- When the ban started
    ban_end_time TIMESTAMP,                 -- When the ban ends (if applicable)
    FOREIGN KEY (user_id) REFERENCES user(id) -- Foreign key to user table
);

-- Table for storing user's login history
CREATE TABLE user_history (
    id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for the history record
    user_id INT,                            -- Foreign key reference to the user table
    login_count INT DEFAULT 0,              -- Number of times the user has logged in
    last_login TIMESTAMP,                   -- Last login timestamp
    failed_login_count INT DEFAULT 0,       -- Number of failed login attempts
    last_failed_login TIMESTAMP,            -- Timestamp of the last failed login attempt
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- When the history record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- When the record was last updated
    transaction_history JSON,               -- User's transaction history (stored as JSON)
    FOREIGN KEY (user_id) REFERENCES user(id) -- Foreign key to user table
);

-- Table for storing user's security-related information (password hash, 2FA, etc.)
CREATE TABLE user_security (
    id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for the security record
    user_id INT,                            -- Foreign key reference to the user table
    password_hash VARCHAR(255),             -- Password hash
    two_factor_enabled BOOLEAN DEFAULT FALSE, -- Whether two-factor authentication is enabled
    two_factor_secret_key VARCHAR(255),      -- Secret key for two-factor authentication
    two_factor_backup_codes_hash JSON,      -- Backup codes for two-factor authentication, stored as JSON
    FOREIGN KEY (user_id) REFERENCES user(id) -- Foreign key to user table
);

-- Table for storing user's fingerprint data and other behavioral attributes
CREATE TABLE user_fingerprint (
    id INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for the fingerprint record
    user_id INT,                            -- Foreign key reference to the user table
    username_history JSON,                  -- List of previous usernames (stored as JSON)
    email_address_history JSON,             -- List of previous email addresses (stored as JSON)
    mac_address VARCHAR(50),                -- MAC address of the user's device
    associated_ips JSON,                    -- List of IPs associated with the user (stored as JSON)
    avg_login_frequency JSON,               -- Average login frequency data (stored as JSON)
    avg_session_duration JSON,              -- Average session duration data (stored as JSON)
    geolocation_country VARCHAR(255),       -- Country of the user (based on IP or other data)
    geolocation_city VARCHAR(255),          -- City of the user (based on IP or other data)
    geolocation_latitude DECIMAL(9, 6),     -- Latitude of the user (if available)
    geolocation_longitude DECIMAL(9, 6),    -- Longitude of the user (if available)
    browser_info VARCHAR(255),              -- Browser info (e.g., User-Agent string)
    os_name VARCHAR(255),                   -- Operating system name (e.g., Windows, macOS)
    os_version VARCHAR(50),                 -- Operating system version
    device_type VARCHAR(50),                -- Type of device (e.g., desktop, mobile)
    device_manufacturer VARCHAR(255),       -- Device manufacturer (e.g., Apple, Samsung)
    device_model VARCHAR(255),              -- Device model (e.g., iPhone 13, Galaxy S21)
    user_preferences JSON,                  -- User preferences (stored as JSON)
    user_agent VARCHAR(255),                -- User-Agent string
    device_id VARCHAR(50),                  -- Unique identifier for the device
    screen_resolution VARCHAR(50),          -- Screen resolution of the user's device
    two_factor_enabled BOOLEAN,             -- Whether two-factor is enabled for the user
    vpn_usage BOOLEAN,                       -- Whether the user uses a VPN
    behavioral_biometrics JSON,             -- Behavioral biometrics data (stored as JSON)
    FOREIGN KEY (user_id) REFERENCES user(id) -- Foreign key to user table
);
