CREATE DATABASE marketplace;
USE marketplace;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    role ENUM('User', 'Support', 'Admin') NOT NULL
);

CREATE TABLE user_security (
    user_id INT PRIMARY KEY,
    password_hash VARCHAR(255),
    two_factor_enabled BOOLEAN,
    two_factor_backup_codes_hash JSON,
    two_factor_secret_key VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
    ON DELETE CASCADE
);

CREATE TABLE user_status (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    is_banned BOOLEAN DEFAULT FALSE,
    ban_reason TEXT,
    ban_duration INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE user_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    login_count INT DEFAULT 0,
    last_login TIMESTAMP,
    failed_login_count INT DEFAULT 0,
    last_failed_login TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);
