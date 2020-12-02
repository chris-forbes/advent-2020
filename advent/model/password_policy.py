from dataclasses import dataclass


@dataclass
class PasswordPolicy:
	minimum: int
	maximum: int
	character :str
	