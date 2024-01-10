# Automation testing - Basic calculator
Automated testing of a basic calculator in Python and Selenium

# What have I learned in this project?

# 1- How to take values from a read textbox
 I have learned how to select and copy text from a reading text box:
    txt_text_result = txt_answer.get_attribute("value")

  and how to pass it to print:
    print("The result of " + var_operation + " is: " + txt_text_result)

# 2- The importance of indexing the FOR well
At the beginning, when the script only performed one operation, I didn't realise that the FOR indexing was incorrect. Until I created the data.json file and saw that only the last operation was performed, I didn't realise the error.
