from dataclasses import dataclass

@dataclass
class InitiateLinkRequestParams:
    merchant_id: int
    submerchant_id: int