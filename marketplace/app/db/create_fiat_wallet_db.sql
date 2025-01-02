CREATE DATABASE marketplace_wallets;
USE marketplace_wallets;

CREATE TABLE fiat_wallets (
    wallet_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for the wallet
    user_id INT,                              -- Foreign key to link to the user (referencing `marketplace_users.id`)
    balance DECIMAL(20, 8),                    -- Wallet balance
    iban VARCHAR(34),                          -- IBAN (for fiat wallets)
    swift_code VARCHAR(11),                    -- SWIFT code for international transfers
    routing_number VARCHAR(9),                 -- Routing number for bank transfers (U.S.)
    last_accessed TIMESTAMP,                   -- Last accessed timestamp
    encryption_key VARCHAR(255),               -- Encryption key for securing wallet information
    deposit_history JSON DEFAULT '{}',         -- Deposit history (stored as JSON for flexibility)
    withdrawal_history JSON DEFAULT '{}',      -- Withdrawal history (stored as JSON for flexibility)
    FOREIGN KEY (user_id) REFERENCES marketplace_users.user(id)  -- Link to the `marketplace_users` table
);
