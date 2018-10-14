import os
import logging 

class Logger(object):
    """
    Class to setup and utilize basic logging

    Args:
        self
        name: The name of the class utilizing logging
    """
    def __init__(self, name):
        name = name.replace('.log','')
        logger = logging.getLogger('log_namespace.%s' % name)
        logger.setLevel(logging.DEBUG)
        if not logger.handlers:
            if not os.path.isdir('log'):
                os.mkdir('log')
            file_name = os.path.join('log', '%s.log' % name)   
            handler = logging.FileHandler(file_name)
            formatter = logging.Formatter('%(asctime)s %(levelname)s:%(name)s %(message)s')
            handler.setFormatter(formatter)
            handler.setLevel(logging.DEBUG)
            logger.addHandler(handler)
        self._logger = logger

    """
    Method to return an instance of the logger

    Args:
        self
    """
    def get(self):
        return self._logger