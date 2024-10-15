import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
    filename='basic_logger.log',
    filemode='w'
)

logging.debug("Debug message")
logging.info("Informative message")
logging.error("Error message")

LogWithLevelName = logging.getLogger('myLoggerSample')
level = logging.INFO
LogWithLevelName.setLevel(level)
LogWithLevelName.info('This is a log message.')
