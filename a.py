from selenium import webdriver
import pytest
@pytest.mark.parametrize("username,password,message",
                        [ ("Admin","admin123","Success"),
                         ("admin123", "Admin", "Invalid credentials"),
                         ("", "admin123", "Username cannot be empty"),
                         ("admin", "", "Password cannot be empty"),
                         ("", "", "Username cannot be empty")]
                         )
def test_orange_hrm_login_functionality(username, password, message):
      print('Step 1 : Launch Chrome Browser ')
      chromeBrowser =webdriver.Chrome(executable_path= '../driver/chromedriver')
      print('Step2 : Enter Url in Address bar ')
      chromeBrowser.get('https://opensource-demo.orangehrmlive.com/')

      print('Step3 : Enter Username ')
      userinput = chromeBrowser.find_element_by_id('txtUsername')  # search txtUsename -id wala -- element on browser
      userinput.clear()
      userinput.send_keys(username)

      print('Step4 : Enter Password ')
      passinput = chromeBrowser.find_element_by_id('txtPassword')
      passinput.clear()  # input -- remove existing text --reset --> karo-- password input
      passinput.send_keys(password)  # enter--> password---

      print('Step5 : Click On Login : ')
      loginbtn = chromeBrowser.find_element_by_id('btnLogin')
      loginbtn.click()

      welcome = None
      errormessage = None

      try:
          welcome = chromeBrowser.find_element_by_id('welcome')  # successful login
      except:
            pass

      try:
          errormessage = chromeBrowser.find_element_by_id('spanMessage')  # login success ful nh ho rah
      except:
           pass

      if message == 'Success':
         assert welcome.text == 'Welcome kumar'  # welcome shud be present
         assert errormessage == None  # error message nh hona chahiye
      else:
         assert welcome == None  # Absent
         assert message == errormessage.text  # match hona chahiye..

      chromeBrowser.close()  #
# return chromeBrowser

if __name__ == '__main__':
     pass
    #driver = launch_chrome_browser()
    #print(driver)