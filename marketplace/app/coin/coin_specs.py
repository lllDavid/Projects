from dataclasses import dataclass

@dataclass
class CoinSpecs:
    algorithm: str
    consensus_mechanism: str
    blockchain_network: str
    block_time: float
    transaction_speed: float
    security_features: str
    privacy_features: str
    max_supply: float | None = None  # max_supply can be a float or None
    genesis_block_date: str | None = None  # genesis_block_date can be a string or None
    token_type: str | None = None  # token_type can be a string or None
    governance_model: str | None = None  # governance_model can be a string or None
    development_activity: str | None = None  # development_activity can be a string or None
    hard_cap: float | None = None  # hard_cap can be a float or None
    forking_coin: str | None = None  # forking_coin can be a string or None
    economic_model: str | None = None  # economic_model can be a string or None

    # Update methods (same as before, but also for the new fields)

    def update_algorithm(self, new_algorithm: str):
        self.algorithm = new_algorithm

    def update_consensus_mechanism(self, new_consensus_mechanism: str):
        self.consensus_mechanism = new_consensus_mechanism

    def update_blockchain_network(self, new_blockchain_network: str):
        self.blockchain_network = new_blockchain_network

    def update_block_time(self, new_block_time: float):
        self.block_time = new_block_time

    def update_transaction_speed(self, new_transaction_speed: float):
        self.transaction_speed = new_transaction_speed

    def update_security_features(self, new_security_features: str):
        self.security_features = new_security_features

    def update_privacy_features(self, new_privacy_features: str):
        self.privacy_features = new_privacy_features

    def update_max_supply(self, new_max_supply: float):
        self.max_supply = new_max_supply

    def update_genesis_block_date(self, new_genesis_block_date: str):
        self.genesis_block_date = new_genesis_block_date

    def update_token_type(self, new_token_type: str):
        self.token_type = new_token_type

    def update_governance_model(self, new_governance_model: str):
        self.governance_model = new_governance_model

    def update_development_activity(self, new_development_activity: str):
        self.development_activity = new_development_activity

    def update_hard_cap(self, new_hard_cap: float):
        self.hard_cap = new_hard_cap

    def update_forking_coin(self, new_forking_coin: str):
        self.forking_coin = new_forking_coin

    def update_economic_model(self, new_economic_model: str):
        self.economic_model = new_economic_model


    def __str__(self):
            return (f"Algorithm: {self.algorithm}\n"
                    f"Consensus Mechanism: {self.consensus_mechanism}\n"
                    f"Block Time: {self.block_time} seconds\n"
                    f"Transaction Speed: {self.transaction_speed} transactions/second\n"
                    f"Security Features: {self.security_features}\n"
                    f"Privacy Features: {self.privacy_features}")