CREATE DATABASE marketplace_wallets;
USE marketplace_wallets;

CREATE TABLE crypto_wallet (
    wallet_id INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for the wallet
    user_id INT,                                    -- Foreign key to link to the user (referencing `marketplace_users.id`)
    wallet_address VARCHAR(255),                     -- Wallet address (string)
    balance DECIMAL(20, 8),                          -- Wallet balance stored as JSON for flexibility
    total_coin_value DECIMAL(20, 8),                 -- Total coin value (stored as a DECIMAL)
    last_accessed TIMESTAMP,                         -- Timestamp for last accessed date and time
    encryption_key VARCHAR(255),                     -- Encryption key to secure wallet info
    deposit_history JSON DEFAULT '{}',               -- Deposit history stored as JSON for flexibility
    withdrawal_history JSON DEFAULT '{}',            -- Withdrawal history stored as JSON for flexibility
    FOREIGN KEY (user_id) REFERENCES marketplace_users.user(id)  -- Link to the `marketplace_users` table
);
