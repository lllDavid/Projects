from dataclasses import dataclass
from typing import Dict, Set

@dataclass
class UserFingerprint:
    username_history: Set[str]  
    email_address_history: Set[str]  
    mac_address: str | None = None
    associated_ips: dict[str, int] | None = None
    avg_login_frequency: dict[str, float] | None = None 
    avg_session_duration: dict[str, float] | None = None 
    geolocation_country: str | None = None
    geolocation_city: str | None = None
    geolocation_latitude: float | None = None  
    geolocation_longitude: float | None = None  
    browser_info: str | None = None
    os_name: str | None = None  
    os_version: str | None = None  
    device_type: str | None = None 
    device_manufacturer: str | None = None 
    device_model: str | None = None  
    user_preferences: dict[str, str] | None = None  
    user_agent: str | None = None
    device_id: str | None = None  
    screen_resolution: str | None = None  
    two_factor_enabled: bool | None = None  
    transaction_history: dict[str, float] | None = None  
    vpn_usage: bool | None = None  
    behavioral_biometrics: dict[str, float] | None = None

    def update_username_history(self, username: str):
        self.username_history.add(username)

    def update_email_address_history(self, email: str):
        self.email_address_history.add(email)

    def update_mac_address(self, mac_address: str):
        self.mac_address = mac_address

    def update_associated_ips(self, ip_address: str, count: int = 1):
        if self.associated_ips is None:
            self.associated_ips = {}
        self.associated_ips[ip_address] = self.associated_ips.get(ip_address, 0) + count

    def update_avg_login_frequency(self, day: str, frequency: float):
        if self.avg_login_frequency is None:
            self.avg_login_frequency = {}
        self.avg_login_frequency[day] = frequency

    def update_avg_session_duration(self, day: str, duration: float):
        if self.avg_session_duration is None:
            self.avg_session_duration = {}
        self.avg_session_duration[day] = duration

    def update_geolocation(self, country: str, city: str, latitude: float, longitude: float):
        self.geolocation_country = country
        self.geolocation_city = city
        self.geolocation_latitude = latitude
        self.geolocation_longitude = longitude

    def update_browser_info(self, browser_info: str):
        self.browser_info = browser_info

    def update_os_info(self, os_name: str, os_version: str):
        self.os_name = os_name
        self.os_version = os_version

    def update_device_info(self, device_type: str, device_manufacturer: str, device_model: str):
        self.device_type = device_type
        self.device_manufacturer = device_manufacturer
        self.device_model = device_model

    def update_user_preferences(self, preference_key: str, preference_value: str):
        if self.user_preferences is None:
            self.user_preferences = {}
        self.user_preferences[preference_key] = preference_value

    def update_user_agent(self, user_agent: str):
        self.user_agent = user_agent

    def update_device_id(self, device_id: str):
        self.device_id = device_id

    def update_screen_resolution(self, resolution: str):
        self.screen_resolution = resolution

    def update_two_factor_enabled(self, enabled: bool):
        self.two_factor_enabled = enabled

    def update_transaction_history(self, transaction_id: str, amount: float):
        if self.transaction_history is None:
            self.transaction_history = {}
        self.transaction_history[transaction_id] = amount

    def update_vpn_usage(self, vpn_usage: bool):
        self.vpn_usage = vpn_usage

    def update_behavioral_biometrics(self, biometrics: dict[str, float]):
        if self.behavioral_biometrics is None:
            self.behavioral_biometrics = {}
        self.behavioral_biometrics.update(biometrics)

    def __str__(self):
        return (f"Username history: {', '.join(self.username_history)}; "
                f"Email address history: {', '.join(self.email_address_history)}; "
                f"MAC address: {self.mac_address}; "
                f"Associated IPs: {self.associated_ips}; "
                f"Avg login frequency: {self.avg_login_frequency}; "
                f"Avg session duration: {self.avg_session_duration}; "
                f"Geolocation: {self.geolocation_country}, {self.geolocation_city}, "
                f"Lat: {self.geolocation_latitude}, "
                f"Lon: {self.geolocation_longitude}; "
                f"Browser info: {self.browser_info}; "
                f"OS: {self.os_name} {self.os_version}; "
                f"Device info: {self.device_type} by {self.device_manufacturer}, Model: {self.device_model}; "
                f"User preferences: {self.user_preferences}; "
                f"User agent: {self.user_agent}; "
                f"Device ID: {self.device_id}; "
                f"Screen resolution: {self.screen_resolution}; "
                f"Two-factor enabled: {self.two_factor_enabled}; "
                f"Transaction history: {self.transaction_history}; "
                f"VPN usage: {self.vpn_usage}; "
                f"Behavioral biometrics: {self.behavioral_biometrics}")

