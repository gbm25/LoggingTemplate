import logging

log = logging.getLogger(__name__)


def sumtest(number1: int, number2: int):

    log.info("Everything goes as expected")
    return number1 + number2


def levelstest(something):

    log.debug("Debug output !")
    log.info("Info output !")
    log.warning("Warning output !")
    log.critical("Critical output !")
    log.error("Error output !" )
    try:
        if isinstance(something, str):
            raise TypeError("I don't want a string on my function !")
    except TypeError as error:
        log.exception("Error (exception case) output !")


