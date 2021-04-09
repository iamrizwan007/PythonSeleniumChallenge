from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.worldometers.info/world-population/")

#initializing this to compare at later point just for the first time get inside the if condition
#when current population -> 0 not equal to actual pop

actual_pop = "0"
actual_birth_today = "0"
actual_death_today = "0"
actual_pop_growth_today = "0"
actual_birth_this_year = "0"
actual_death_this_year = "0"
actual_pop_growth_this_year = "0"

while True:
 current_pop = driver.find_element_by_xpath("//span[@rel='current_population']").text
 if current_pop != actual_pop:
  actual_pop = current_pop
  print("Current World Population \n",current_pop)
 
 current_birth_today = driver.find_element_by_xpath("//span[@rel='births_today']").text
 if current_birth_today != actual_birth_today:
  actual_birth_today = current_birth_today
  print("Births Today \n",current_birth_today)

 current_death_today = driver.find_element_by_xpath("//span[@rel='dth1s_today']").text
 if current_death_today != actual_death_today:
  actual_death_today = current_death_today
  print("Deaths Today\n",current_death_today)

 current_pop_growth_today = driver.find_element_by_xpath("//span[@rel='absolute_growth']").text
 if current_pop_growth_today != actual_pop_growth_today:
  actual_pop_growth_today = current_pop_growth_today
  print("Population Growth Today \n",current_pop_growth_today)

 current_birth_this_year = driver.find_element_by_xpath("//span[@rel='births_this_year']").text
 if current_birth_this_year != actual_birth_this_year:
  actual_birth_this_year = current_birth_this_year
  print("Births This Year \n",current_birth_this_year)

 current_death_this_year = driver.find_element_by_xpath("//span[@rel='dth1s_this_year']").text
 if current_death_this_year != actual_death_this_year:
  actual_death_this_year = current_death_this_year
  print("Deaths This Year\n",current_death_this_year)

 current_pop_growth_this_year = driver.find_element_by_xpath("//span[@rel='absolute_growth_year']").text
 if current_pop_growth_this_year != actual_pop_growth_this_year:
  actual_pop_growth_this_year = current_pop_growth_this_year
  print("Population Growth This Year \n",current_pop_growth_this_year)
