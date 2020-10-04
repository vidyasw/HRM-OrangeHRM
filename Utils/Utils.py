#Constants
from OrangeHRM_Common.OrangeHRM_InputManagement import Excel_utility

path = "E:/Vidyashri/PythonSeleniumProjects/HRM-OrangeHRM/OrangeHRM_Common/OrangeHRM_InputManagement" \
       "/OrangeHRM_input_Sheet.xlsx"
src_file = "E:\\Vidyashri\\PythonSeleniumProjects\\HRM-OrangeHRM\\PageObjects\\OrangeHRM_AdminPages\\Job" \
           "\\All_JobSpecification.txt"
dest_file = "E:\\Vidyashri\\PythonSeleniumProjects\\HRM-OrangeHRM\\PageObjects\\OrangeHRM_AdminPages\\Job\\" \
            "Job_Specification.txt"
sheet_Inputs = "Inputs"
url = Excel_utility.getvalue(path,sheet_Inputs,"application_url")
valid_username = Excel_utility.getvalue(path,sheet_Inputs,"valid_userName")
valid_password = Excel_utility.getvalue(path,sheet_Inputs,"valid_password")
msg_username_empty = Excel_utility.getvalue(path,sheet_Inputs,"msg_username_empty")
msg_password_empty = Excel_utility.getvalue(path,sheet_Inputs,"msg_password_empty")
msg_Invalid_credentials = Excel_utility.getvalue(path,sheet_Inputs,"msg_Invalid_credentials")
invalid_username = Excel_utility.getvalue(path,sheet_Inputs,"invalid_userName")
invalid_password = Excel_utility.getvalue(path,sheet_Inputs,"invalid_password")
heading_ForgotYourPassword = Excel_utility.getvalue(path,sheet_Inputs,"heading_ForgotYourPassword")
sheet_Job_Titles = "Job_Titles"
job_title_cto = Excel_utility.getvalue(path, sheet_Job_Titles, "job_Title_CTO")
job_spec_cto = Excel_utility.getvalue(path,sheet_Job_Titles, "job_Spec_CTO")
job_description_cto = Excel_utility.getvalue(path, sheet_Job_Titles, "job_Description_CTO")
job_notes_cto = Excel_utility.getvalue(path,sheet_Job_Titles, "job_notes_CTO")
sheet_Pay_Grade = "Pay_Grade"
pay_grade_level = Excel_utility.getvalue(path,sheet_Pay_Grade,"pay_Grade_Name_CG40")
pay_currency = Excel_utility.getvalue(path,sheet_Pay_Grade,"pay_Currancy_CG40")
min_salary = Excel_utility.getvalue(path,sheet_Pay_Grade,"min_Salary_CG40")
max_salary = Excel_utility.getvalue(path,sheet_Pay_Grade,"max_Salary_CG40")
edit_pay_grade_name = Excel_utility.getvalue(path,sheet_Pay_Grade,"edit_pay_Grade_Name_CG-40")
sheet_Emp_status = "Emp_status"
emp_status_name = Excel_utility.getvalue(path,sheet_Emp_status,"emp_status_intern")
emp_status_name_to_edit = Excel_utility.getvalue(path,sheet_Emp_status,"emp_status_intern_edited")
sheet_Job_Category = "Job_Category"
job_category_it_professional = Excel_utility.getvalue(path,sheet_Job_Category,"job_category_ITProfessional")
job_category_it_professional_edit = Excel_utility.getvalue(path,sheet_Job_Category,"job_category_ITProfessional_edit")
sheet_Work_Shift = "Work_Shift"
shift_name = Excel_utility.getvalue(path,sheet_Work_Shift,"shift_name_AfterNoon-Normal")
shift_hrs_frm = Excel_utility.getvalue(path,sheet_Work_Shift,"shift_hrsFrm_AfterNoon-Normal")
shift_hrs_to = Excel_utility.getvalue(path,sheet_Work_Shift,"shift_hrsTo_AfterNoon-Normal")
shift_name_to_edit = Excel_utility.getvalue(path,sheet_Work_Shift,"edit_shift_name_AfterNoon-Normal")