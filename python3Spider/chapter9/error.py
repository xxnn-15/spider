class PoolEmeptyError(Exception):
    def __str__(self) -> str:
        return "proxy pool is empty."
