import discord


class User:
    # The id of the user
    id: int

    def __eq__(self, other: object) -> bool:
        if isinstance(other, (User, discord.User, discord.Member)):
            return self.id == other.id
        else:
            raise TypeError(
                f"Cannot compare {type(self).__name__} to {type(other).__name__}"
            )
