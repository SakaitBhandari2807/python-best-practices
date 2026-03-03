import logging

logger = logging.getLogger(__name__)


def process(a, b):
    logger.info('Processing started..')
    try:
        r = a/b
    except ZeroDivisionError:
        logger.error('Division by zero', exc_info=True)