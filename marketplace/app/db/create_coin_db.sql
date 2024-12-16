CREATE DATABASE marketplace_coins;
USE marketplace_coins;

-- Create coin table
CREATE TABLE coin (
    id INT AUTO_INCREMENT PRIMARY KEY,         -- Coin ID (Primary Key)
    name VARCHAR(255),                          -- Coin Name
    symbol VARCHAR(20),                         -- Coin Symbol (e.g., BTC, ETH)
    category VARCHAR(100),                      -- Coin Category (e.g., DeFi, Stablecoin, etc.)
    description TEXT,                           -- Coin Description
    price DECIMAL(20, 8),                       -- Coin Price in USD
    last_updated DATETIME                       -- Last updated timestamp
);

-- Create coin_specs table
CREATE TABLE coin_specs (
    id INT AUTO_INCREMENT PRIMARY KEY,          -- Specs ID (Primary Key)
    coin_id INT,                                -- Foreign Key to coin table
    algorithm VARCHAR(100),                     -- Coin Algorithm (e.g., SHA-256, Proof of Work)
    consensus_mechanism VARCHAR(100),           -- Consensus Mechanism (e.g., Proof of Stake)
    block_time DECIMAL(10, 2),                  -- Block Time in seconds
    max_supply DECIMAL(20, 8),                  -- Maximum Supply of the coin
    circulating_supply DECIMAL(20, 8),         -- Current Circulating Supply
    transaction_speed DECIMAL(10, 2),           -- Transaction Speed (transactions per second)
    security_features TEXT,                     -- Security Features of the coin
    privacy_features TEXT,                      -- Privacy Features (e.g., ZK-Snarks, Ring Signatures)
    FOREIGN KEY (coin_id) REFERENCES coin(id)  -- Link to coin table
);

-- Create coin_market_data table
CREATE TABLE coin_market_data (
    id INT AUTO_INCREMENT PRIMARY KEY,          -- Market Data ID (Primary Key)
    coin_id INT,                                -- Foreign Key to coin table
    price_usd DECIMAL(20, 8),                   -- Coin Price in USD
    market_cap_usd DECIMAL(20, 8),              -- Market Capitalization in USD
    volume_24h_usd DECIMAL(20, 8),              -- 24 Hour Trading Volume in USD
    high_24h_usd DECIMAL(20, 8),                -- 24 Hour High Price in USD
    low_24h_usd DECIMAL(20, 8),                 -- 24 Hour Low Price in USD
    price_change_24h DECIMAL(20, 8),            -- Price Change in 24 Hours in USD
    circulating_supply DECIMAL(20, 8),          -- Circulating Supply of the coin
    max_supply DECIMAL(20, 8),                  -- Maximum Supply of the coin
    FOREIGN KEY (coin_id) REFERENCES coin(id)  -- Link to coin table
);

-- Create coin_details table (optional, if you want to store it separately)
-- This table could either store foreign keys to the other tables or be used as a view.
CREATE TABLE coin_details (
    id INT AUTO_INCREMENT PRIMARY KEY,          -- Details ID (Primary Key)
    coin_id INT,                                -- Foreign Key to coin table
    coin_specs_id INT,                          -- Foreign Key to coin_specs table
    coin_market_data_id INT,                    -- Foreign Key to coin_market_data table
    FOREIGN KEY (coin_id) REFERENCES coin(id), 
    FOREIGN KEY (coin_specs_id) REFERENCES coin_specs(id),
    FOREIGN KEY (coin_market_data_id) REFERENCES coin_market_data(id)
);
