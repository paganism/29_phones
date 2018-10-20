# from phone_processing import app
import logging.handlers
import os


LOG_MAX_BYTES = 10240
LOG_BACKUP_COUNT = 1

handler = logging.handlers.RotatingFileHandler(
    'phone_processing_info.log', maxBytes=LOG_MAX_BYTES, backupCount=LOG_BACKUP_COUNT)
handler.setLevel(logging.INFO)
formatter = logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s '
            '[in %(pathname)s:%(lineno)d]')
handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.INFO)
