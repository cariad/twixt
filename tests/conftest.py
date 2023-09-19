from logging import DEBUG, getLogger

from twixt.logging import logger

logger.setLevel(DEBUG)
getLogger("bendy").setLevel(DEBUG)
