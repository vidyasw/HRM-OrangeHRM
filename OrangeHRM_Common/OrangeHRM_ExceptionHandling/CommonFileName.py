from datetime import datetime
import os

try:
    common_file_name = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
except Exception as e:
    print("File Name : {current_py_file_name} ".format(current_py_file_name=os.path.basename(__file__)))
    print("Error : ")
    print("Type --> " + type(e).__name__)
    print("Details --> ", e)
    exit(1)
