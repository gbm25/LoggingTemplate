from config import root_dir, app_name
import colorlog
from logging.handlers import SMTPHandler

logs_configuration = {
    'version': 1,
    'disable_existing_loggers': False,
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['debug_console_handler', 'info_timedrotating_file_handler', 'error_file_handler']
        }
    },
    'handlers': {
        'debug_console_handler': {
            'level': 'DEBUG',
            'formatter': 'colored',
            'class': 'colorlog.StreamHandler',
            'stream': 'ext://sys.stdout',
        },
        'info_timedrotating_file_handler': {
            'level': 'INFO',
            'formatter': 'info',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': f'{root_dir}/logs/{app_name}.log',
            'when': 'D',
            'interval': 1,
            'backupCount': 5,
            "encoding": "utf-8"
        },
        'error_file_handler': {
            'level': 'WARNING',
            'formatter': 'error',
            'class': 'logging.FileHandler',
            'filename': f'{root_dir}/logs/error.log',
            'mode': 'a',
            "encoding": "utf-8"
        },
        'mail_handler': {  # Not tested/implemented
            'level': 'ERROR',
            'formatter': 'error',
            'class': 'logging.handlers.SMTPHandler',
            'mailhost': ("smtp.yourdomain.com", 587),
            'fromaddr': "from@yourdomain.com",
            'toaddrs': "to@yourdomain.com",
            'subject': f"Error on {app_name}",
            'credentials': ("from@yourdomain.com", "password"),
            'secure': ()
        }
    },
    'formatters': {
        'info': {
            'format': '%(asctime)s-%(levelname)s-%(name)s::%(module)s(%(lineno)s) - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'error': {
            'format': '%(asctime)s-%(levelname)s-%(name)s-PID:%(process)d::%(module)s(%(lineno)s) - %(funcName)s - %('
                      'message)s',

        },
        'colored': {
            '()': 'colorlog.ColoredFormatter',
            'format': '%(log_color)s%(asctime)s-[%(levelname)s]-%(name)s-%(process)d::%(module)s(%(lineno)s) - %('
                      'message)s ',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    }
}
