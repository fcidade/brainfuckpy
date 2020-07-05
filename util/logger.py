from logging.config import dictConfig

def setup_logs():
    logging_config = { 
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': { 
            'standard': { 
                'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
            },
        },
        'handlers': { 
            'default': { 
                'level': 'DEBUG',
                'formatter': 'standard',
                'class': 'logging.StreamHandler',
                'stream': 'ext://sys.stdout',  # Default is stderr
            },
        },
        'loggers': { 
            '': {  # root logger
                'handlers': ['default'],
                'level': 'DEBUG',
                'propagate': False
            },
        } 
    }
    dictConfig(logging_config)