from dataclasses import dataclass


@dataclass
class Passport:
    def __init__(self):
        pass

    byr: int  # Birth year
    iyr: int  # Issue Year
    eyr: int  # Expiration year
    hgt: str  # Height
    hcl: str  # Hair Color
    ecl: str  # Eye Color
    pid: str  # Passport ID
    cid: str  # Country ID
