"""
webscraping from DigiGlobe

"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import datetime
import time

############################################
#   UPDATE THE LINK TO YOUR DRIVER HERE    #
############################################
driver = webdriver.Chrome('C:/Users/zwi/Downloads/chromedriver.exe')



# browse to page
driver.get('https://discover.digitalglobe.com/')
driver.maximize_window()

# click "Area of Interest"
WebDriverWait(driver,60).until(EC.presence_of_element_located((By.CLASS_NAME, 'jss58')))
driver.find_elements_by_class_name('jss58')[3].click()
# click "Coordinate entry"
button_coord = driver.find_elements_by_id('btn_coordinate_entry')
button_coord[0].click()
# enter coordinates and distances 
input_lat = driver.find_elements_by_id('id_textfield_latitude')
input_lat[0].send_keys('1.319109')
input_long = driver.find_elements_by_id('id_textfield_longitude')
input_long[0].send_keys('103.864071')
input_width = driver.find_elements_by_id('id_textfield_width')
input_width[0].send_keys('65')
input_height = driver.find_elements_by_id('id_textfield_height')
input_height[0].send_keys('45')
# click "Draw"
button_draw = driver.find_elements_by_id('id_action_coordinates_entry_proceed')
button_draw[0].click()

# click "Filters" after a delay
time.sleep(20)
button_filter = driver.find_elements_by_id('id_btn_filters')
button_filter[0].click()

# set start date to be 2 weeks prior (end date in DigiGlobe defaults to current)
current_date = datetime.datetime.now().date()
difference = datetime.timedelta(14)
previous_date = current_date - difference
date_split = str(previous_date).split("-")
date_input = date_split[1]+"/"+date_split[2]+"/"+date_split[0]

#time.sleep(2)
input_startdate = driver.find_elements_by_id('calendar_start_date_tf')
input_startdate[0].send_keys(Keys.CONTROL,'a')
input_startdate[0].send_keys(Keys.BACKSPACE)
input_startdate[0].send_keys(str(date_input))

# click "Refresh results"
button_refresh = driver.find_elements_by_id('id_btn_refresh_results')
button_refresh[0].click()
time.sleep(5)

# open results in separate window
button_results = driver.find_element_by_id('close_results_window')
button_results.click()
time.sleep(2)

# switch to new window
handles = driver.window_handles
driver.switch_to.window(handles[1])

# on new window, click view
views = driver.find_elements_by_link_text('view')
for item in views:
    item.click()
    
    
# switch to image tab
driver.switch_to.active_element
#driver.switch_to.window(handles[0])
#driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)

# download sat image
#img = driver.find_element_by_xpath('//img[1]')
#img = driver.find_element_by_css_selector('img')
#img = driver.find_elements_by_xpath("//a//img")
#img = driver.find_elements_by_tag_name('img')
#img = driver.find_element_by_tag_name('body')

#src = img[0].get_attribute('src')
#urllib.urlretrieve(src,'img1.jpeg')



#time.sleep(5)
#WebDriverWait(driver,60).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input.typeahead_input')))
#driver.find_element_by_css_selector('input.typeahead_input').send_keys('Uttarakhand')
#WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="SUBMIT_HOTELS"]')))
#driver.find_elements(By.XPATH, '//*[@id="SUBMIT_HOTELS"]')[0].click()
#time.sleep(5)
