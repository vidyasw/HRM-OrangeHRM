import linecache
import os
from OrangeHRM_Common.OrangeHRM_ReportUtilities.LogGenerator import logger_obj


class Text_utilities():
    def __init__(self):
        pass

    @staticmethod
    def create_specifications(src_file_name,des_file_name,spec_for_role):
        print(src_file_name)
        print(des_file_name)
        if not os.path.exists(src_file_name) and not os.path.exists(des_file_name):
             logger_obj.debug("Some parameters are missing plz check!!")
        started = False
        collected_lines = []
        ''' get the staring line and ending line'''
        with open(src_file_name, "r") as srcFile:
            lines = []
            for i, line in enumerate(srcFile, 1):
                if spec_for_role in line:
                    started = True
                    # print("started at line", i)  # counts from zero !
                    lines.append(i)
                    continue
                if started and line == '\n':
                    # print("found an end of line", i)
                    lines.append(i)
                    break
            # print("Starting line and ending line no", lines)

            '''Read the lines between starting and ending line'''
            for l in range(lines[0], lines[len(lines) - 1]):
                # print(l)
                linecache.getline(src_file_name, l)
                # process line
                collected_lines.append(linecache.getline(src_file_name, l))
            # print(collected_lines)
            srcFile.close()

            '''Write the lines in destination file'''
            F = open(des_file_name, "w")
            F.writelines(collected_lines)
            F.close()