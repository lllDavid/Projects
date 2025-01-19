ALTER TABLE crypto_wallet
ADD CONSTRAINT fk_user_id
FOREIGN KEY (user_id)
REFERENCES marketplace_users(id)
ON DELETE CASCADE; 

ALTER TABLE fiat_wallet
ADD CONSTRAINT fk_user_id
FOREIGN KEY (user_id)
REFERENCES marketplace_users(id)
ON DELETE CASCADE; 

