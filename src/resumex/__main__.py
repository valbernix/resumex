import os
import logging
import logging.config

from resumex.config import Paths


def main():
    set_up_logging()


def set_up_logging():
    os.makedirs(Paths.LOGS, exist_ok=True)
    logging.config.fileConfig(
        Paths.CONFIG.joinpath("logging.conf"),
        defaults={"fname": str(Paths.LOGS.joinpath("resumex.log"))},
    )


if __name__ == "__main__":
    main()
