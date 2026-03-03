import logging
import logging.config

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers' : False,
    'formatters' : {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
        'detailed': {
            'format': '%(asctime)s [%(levelname)s] %(module)s.%(funcName)s:%(lineno)s: %(message)s'
        }
    },
    'handlers': {
        'default':{
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter':'detailed',
            'filename': 'error.log',
            'mode': 'a'
        }
    },
    'loggers': {
        '': {
            'handlers': ['default', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        }
    }

}

def setup_logging():
    logging.config.dictConfig(LOGGING_CONFIG)