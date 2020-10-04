import logging  # To Log the Tool Execution Process.
from pathlib import Path  # To join PATH.
import os  # To get the Current Working Directory.
from OrangeHRM_Common.OrangeHRM_ExceptionHandling import CommonFileName  # To get a common name for Log, HTML and PDF report files.


def generate_log(log_folder_name):
    try:
        print("\nLog Information : ")
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        log_folder_absolute_path = \
            Path("E:/Vidyashri/PythonSeleniumProjects/HRM-OrangeHRM/Execution_Reports") / log_folder_name
        print("Log Folder Absolute Path : ", log_folder_absolute_path)
        if not os.path.exists(log_folder_absolute_path):
            os.mkdir(log_folder_absolute_path)
        log_file_name = CommonFileName.common_file_name + "Log.txt"
        print("Log file Name : ", log_file_name)
        log_file_absolute_path = Path(log_folder_absolute_path) / log_file_name
        print("Log file Absolute Path : ", log_file_absolute_path)

        print("Writing Column Names to Log File")
        with open(log_file_absolute_path, "w") as LOG_FILE:
            LOG_FILE.write("DATE TIME,FILE NAME,FUNCTION NAME,LINE NUMBER,LOG LEVEL NAME,"
                           "NAME,LOG MESSAGE\n\n")
        print("Expected Parameters wrote to Log File successfully!\n")

        formatter = logging.Formatter("%(asctime)s,%(filename)s,%(funcName)s,%(lineno)d,%(levelname)s,%(name)s,%(message)s", datefmt="%d-%m-%Y %H-%M-%S")
        file_logger = logging.FileHandler(filename=log_file_absolute_path)
        file_logger.setFormatter(formatter)
        logger.addHandler(file_logger)
        #console_logger = logging.StreamHandler()
        #logger.addHandler(console_logger)
        return logger

    except Exception as e:
        print("File Name : {current_py_file_name} ".format(current_py_file_name=os.path.basename(__file__)))
        print("Error : ")
        print("Type --> " + type(e).__name__)
        print("Details --> ", e)
        exit(1)


logger_obj = generate_log(log_folder_name="ExecutionLogs")
