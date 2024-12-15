from dataclasses import dataclass
from datetime import datetime
from marketplace.app.user.user import User

@dataclass
class ReferenceAccount:
    user: User
    account_number: str
    bank_name: str
    iban: str | None
    deposits: dict | None 
    withdrawals: dict | None 
    account_status: str | None 
    last_accessed: str | None 
    encryption_key: str | None 
    
    def link_account(self):
        """ Simulate linking the reference account to the platform """
        print(f"Reference account for {self.user.user_profile.username} linked successfully to the platform.")
    
    def unlink_account(self):
        """ Simulate unlinking the reference account from the platform """
        print(f"Reference account for {self.user.user_profile.username} unlinked successfully from the platform.")
    
    def deposit(self, amount: float, currency: str = "USD"):
        """ Simulate depositing funds into the reference account """
        deposit = {"amount": amount, "currency": currency}
        self.deposits[len(self.deposits)] = deposit
        print(f"Deposited {amount} {currency} to reference account.")
    
    def withdraw(self, amount: float, currency: str = "USD"):
        """ Simulate withdrawing funds from the reference account """
        withdrawal = {"amount": amount, "currency": currency}
        self.withdrawals[len(self.withdrawals)] = withdrawal
        print(f"Withdrew {amount} {currency} from reference account.")
    
    def get_balance(self) -> float:
        """ Calculate the total balance in the reference account from deposits and withdrawals """
        total_deposit = sum(d["amount"] for d in self.deposits.values())
        total_withdrawal = sum(w["amount"] for w in self.withdrawals.values())
        balance = total_deposit - total_withdrawal
        return balance

    def account_info(self):
        """ Display basic account information """
        info = f"Account Holder: {self.user.user_profile.username}\n" \
               f"Bank: {self.bank_name}\n" \
               f"Account Number: {self.account_number}\n" \
               f"IBAN: {self.iban if self.iban else 'Not provided'}\n" \
               f"Account Status: {self.account_status}\n" \
               f"Failed Attempts: {self.failed_attempts}\n" \
               f"Last Accessed: {self.last_accessed if self.last_accessed else 'Never'}"
        print(info)

    def update_last_accessed(self):
        """ Update the last accessed timestamp """
        self.last_accessed = datetime.now()
    
    def lock_account(self):
        """ Lock the account after multiple failed attempts """
        if self.failed_attempts >= 3:
            self.account_status = "locked"
            print(f"Account for {self.user.name} is now locked due to multiple failed attempts.")
        else:
            print("Account is secure and not locked.")
    
    def reset_failed_attempts(self):
        """ Reset failed access attempts after successful login or manual reset """
        self.failed_attempts = 0
        print(f"Failed attempts for {self.user.name} have been reset.")