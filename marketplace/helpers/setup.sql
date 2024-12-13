CREATE DATABASE marketplace;
USE marketplace;

CREATE TABLE user_profile (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    role ENUM('USER', 'SUPPORT', 'ADMIN') NOT NULL
);

CREATE TABLE user_security (
    user_id INT PRIMARY KEY,
    password_hash VARCHAR(255),
    two_factor_enabled BOOLEAN,
    two_factor_secret_key VARCHAR(255),
    two_factor_backup_codes_hash JSON,
    FOREIGN KEY (user_id) REFERENCES user_profile(user_id) ON DELETE CASCADE
);

CREATE TABLE user_status (
    user_id INT PRIMARY KEY,
    is_banned BOOLEAN,
    is_inactive BOOLEAN,
    ban_type VARCHAR(50),
    ban_reason TEXT,
    ban_duration INT,
    ban_start_time DATETIME,
    ban_end_time DATETIME,
    FOREIGN KEY (user_id) REFERENCES user_profile(user_id) ON DELETE CASCADE
);

CREATE TABLE user_history (
    user_id INT PRIMARY KEY,
    login_count INT,
    last_login DATETIME,
    failed_login_count INT,
    last_failed_login DATETIME,
    created_at DATETIME,
    updated_at DATETIME,
    FOREIGN KEY (user_id) REFERENCES user_profile(user_id) ON DELETE CASCADE
);

CREATE TABLE user_fingerprint (
    user_id INT PRIMARY KEY,
    username_history JSON,
    email_address_history JSON,
    mac_address VARCHAR(255),
    associated_ips JSON,
    avg_login_frequency JSON,
    avg_session_duration JSON,
    geolocation_country VARCHAR(100),
    geolocation_city VARCHAR(100),
    geolocation_latitude DOUBLE,
    geolocation_longitude DOUBLE,
    browser_info VARCHAR(255),
    os_name VARCHAR(100),
    os_version VARCHAR(50),
    device_type VARCHAR(50),
    device_manufacturer VARCHAR(100),
    device_model VARCHAR(100),
    user_preferences JSON,
    user_agent VARCHAR(255),
    device_id VARCHAR(255),
    screen_resolution VARCHAR(100),
    two_factor_enabled BOOLEAN,
    transaction_history JSON,
    vpn_usage BOOLEAN,
    behavioral_biometrics JSON,
    FOREIGN KEY (user_id) REFERENCES user_profile(user_id) ON DELETE CASCADE
);

