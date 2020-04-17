import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='ex1.log',
    filemode='w',
    format='%(asctime)s -- %(levelname)s:%(levelno)s  --  %(message)s'
)

test_message = 'hello'

logging.debug(f'debug message : {test_message}')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')
