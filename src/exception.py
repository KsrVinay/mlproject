import sys
from src.logger import logging
def error_message_detail(error, error_detail: sys):
    '''
    Extracts detailed error information, including the filename, line number, and error message.
    '''
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = 'Error occurred in python script name [{0}] line number [{1}] error message [{2}]'.format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error, error_detail: sys):
        '''
        Custom exception class to provide detailed error information.
        '''
        detailed_message = error_message_detail(error, error_detail)
        
        super().__init__(detailed_message)
    
        self.error_message = detailed_message

    def __str__(self):
        '''
        Returns the detailed error message when the exception is printed.
        '''
        return self.error_message
