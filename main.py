import logging
import logging.config

from utils.logging_configuration import logs_configuration

from testmodule import sumtest, levelstest


def main():
    log.info("Starting program")

    sumnum = sumtest(5656, 7879878)

    levelstest(sumnum)

    levelstest("My string")


if __name__ == "__main__":

    logging.config.dictConfig(logs_configuration)

    log = logging.getLogger(__name__)

    main()
