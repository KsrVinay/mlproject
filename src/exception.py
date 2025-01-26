import sys

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
        # Generate a detailed error message
        detailed_message = error_message_detail(error, error_detail)
        
        # Initialize the base class with the detailed message
        super().__init__(detailed_message)
        
        # Store the detailed message for future reference
        self.error_message = detailed_message

    def __str__(self):
        '''
        Returns the detailed error message when the exception is printed.
        '''
        return self.error_message
