from importlib.metadata import metadata as MetaProvider
from importlib.resources import files
from platformdirs import user_log_dir
from pathlib import Path

_meta = MetaProvider("resumex")


class PkgInfo:
    AUTHOR = _meta["Author"]
    NAME = _meta["Name"]


class Paths:
    CONFIG = Path(__file__).parent
    LOGS = Path(user_log_dir(PkgInfo.NAME, PkgInfo.AUTHOR))
    TEMPLATES = files("resumex.templates")
