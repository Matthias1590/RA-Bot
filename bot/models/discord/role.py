from dataclasses import dataclass
import discord


@dataclass
class Role:
    # The role id
    id: int

    def __eq__(self, other: object) -> bool:
        if isinstance(other, (Role, discord.Role)):
            return self.id == other.id
        else:
            raise TypeError(
                f"Cannot compare {type(self).__name__} to {type(other).__name__}"
            )
