import os


def get_data_path(path: str) -> os.PathLike:
    return os.path.join(os.path.dirname(__file__), "data", path)  # type: ignore
