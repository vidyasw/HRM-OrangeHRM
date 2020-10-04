from pathlib import Path  # To join PATH.
import os  # To get the Current Working Directory.
from sys import exit
from OrangeHRM_Common.OrangeHRM_ReportUtilities.LogGenerator import logger_obj #ReportsUtilities.LogGenerator import logger_obj  # To Log the Tool Execution Process.
# from OrangeHRM_Common.OrangeHRM_ExceptionHandling import CommonFileName  # To get a common name for Log, HTML and PDF report files.


# To execute a list of steps before exiting the program.
def call_exception_utility(exit_code):
    try:
        if exit_code == 1:
            # To generate IBE Sanity Summary File.
            absolute_path_summary_file = Path(os.getcwd()) / "ActivitySummary.txt"
            with open(absolute_path_summary_file, 'w') as SummaryFile:
                # 1 --> PASS and 0 --> FAIL
                SummaryFile.write("0")

        # input("Press Enter to continue...")

        if exit_code != 0:
            exit(1)

    except Exception as e:
        logger_obj.exception("File Name : {current_py_file_name} ".format(current_py_file_name=os.path.basename(__file__)), exc_info=False)
        logger_obj.exception("Error : ", exc_info=False)
        logger_obj.exception("Type --> " + type(e).__name__, exc_info=False)
        logger_obj.exception("Details --> " + str(e), exc_info=False)
        exit(1)
