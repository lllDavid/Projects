ALTER TABLE marketplace_wallets.crypto_wallet
ADD CONSTRAINT fk_user_id
FOREIGN KEY (user_id)
REFERENCES marketplace.marketplace_users(id)
ON DELETE CASCADE;

ALTER TABLE marketplace_wallets.fiat_wallet
ADD CONSTRAINT fk_user_id
FOREIGN KEY (user_id)
REFERENCES marketplace.marketplace_users(id)
ON DELETE CASCADE;
