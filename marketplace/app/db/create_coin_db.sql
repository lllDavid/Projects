CREATE DATABASE marketplace_coins;
USE marketplace_coins;

-- Table for storing basic coin specifications
CREATE TABLE coin_specs (
    id INT AUTO_INCREMENT PRIMARY KEY,           -- Unique identifier for the coin specs
    algorithm VARCHAR(255),                     -- Algorithm used by the coin
    consensus_mechanism VARCHAR(255),           -- Consensus mechanism (e.g., PoW, PoS)
    blockchain_network VARCHAR(255),            -- Blockchain network name
    average_block_time FLOAT,                   -- Average block time in seconds
    security_features VARCHAR(255),            -- Security features of the coin
    privacy_features VARCHAR(255),             -- Privacy features of the coin
    max_supply DECIMAL(20, 8),                  -- Maximum supply of the coin
    genesis_block_date DATE,                    -- Genesis block date
    token_type VARCHAR(255),                    -- Token type (e.g., utility, security)
    governance_model VARCHAR(255),             -- Governance model of the coin
    development_activity VARCHAR(255),         -- Description of development activity
    hard_cap DECIMAL(20, 8),                   -- Hard cap of the coin
    forking_coin VARCHAR(255),                 -- Forking coin (if applicable)
    tokenomics VARCHAR(255)                    -- Tokenomics details
);

-- Table for storing coin market data
CREATE TABLE coin_market_data (
    id INT AUTO_INCREMENT PRIMARY KEY,           -- Unique identifier for the market data
    rank INT,                                    -- Rank of the coin in the market
    price_usd DECIMAL(20, 8),                    -- Current price in USD
    market_cap_usd DECIMAL(20, 8),               -- Market capitalization in USD
    volume_24h_usd DECIMAL(20, 8),               -- Trading volume in the last 24 hours
    high_24h_usd DECIMAL(20, 8),                 -- Highest price in the last 24 hours
    low_24h_usd DECIMAL(20, 8),                  -- Lowest price in the last 24 hours
    change_24h_percent DECIMAL(10, 4),           -- Percentage change in the last 24 hours
    all_time_high DECIMAL(20, 8),                -- All-time high price
    all_time_low DECIMAL(20, 8),                 -- All-time low price
    circulating_supply DECIMAL(20, 8),           -- Circulating supply of the coin
    market_dominance DECIMAL(10, 4),             -- Market dominance percentage
    last_updated DATETIME                        -- Timestamp of the last update
);

-- Table for storing coin information
CREATE TABLE coin (
    id INT AUTO_INCREMENT PRIMARY KEY,           -- Unique identifier for the coin
    name VARCHAR(255),                           -- Name of the coin
    symbol VARCHAR(50),                          -- Symbol of the coin
    category VARCHAR(255),                       -- Category of the coin
    description VARCHAR(255),                    -- Description of the coin
    price DECIMAL(20, 8),                        -- Current price of the coin
    coin_specs_id INT,                           -- Foreign key reference to CoinSpecs table
    coin_market_data_id INT,                     -- Foreign key reference to CoinMarketData table
    FOREIGN KEY (coin_specs_id) REFERENCES coin_specs(id) ON DELETE CASCADE, -- Reference to CoinSpecs
    FOREIGN KEY (coin_market_data_id) REFERENCES coin_market_data(id) ON DELETE CASCADE -- Reference to CoinMarketData
);
