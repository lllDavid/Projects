from dataclasses import dataclass

@dataclass
class CoinDetails:
    algorithm: str
    consensus_mechanism: str
    block_time: float
    max_supply: float
    circulating_supply: float
    transaction_speed: float
    security_features: str
    privacy_features: str

    def update_supply(self, new_circulating_supply: float, new_max_supply: float):
        self.circulating_supply = new_circulating_supply
        self.max_supply = new_max_supply

    def calculate_remaining_supply(self) -> float:
        return self.max_supply - self.circulating_supply

    def update_security_features(self, new_security_features: str):
        self.security_features = new_security_features

    def update_privacy_features(self, new_privacy_features: str):
        self.privacy_features = new_privacy_features

    def __str__(self):
            return (f"Algorithm: {self.algorithm}\n"
                    f"Consensus Mechanism: {self.consensus_mechanism}\n"
                    f"Block Time: {self.block_time} seconds\n"
                    f"Max Supply: {self.max_supply}\n"
                    f"Circulating Supply: {self.circulating_supply}\n"
                    f"Transaction Speed: {self.transaction_speed} transactions/second\n"
                    f"Security Features: {self.security_features}\n"
                    f"Privacy Features: {self.privacy_features}")