import sys 
# from src.logger import logging

def error_message_details(error , error_detail : sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename 
    error_message = "Error Occured in  python script [{0}] line no [{1}] and error message is [{2}]".format(
        file_name , exc_tb.tb_lineno ,str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self,error_message , error_detail:sys):
        super().__init__(error_detail)
        self.error_message = error_message_details(error_message,error_detail)
    
    def __str__(self):
        return self.error_message 
    
# if __name__ == '__main__':
#     try :
#         logging.info('Logging Started')
#         a = 1/0 
#     except Exception as e :
#         raise CustomException(e,sys)

    