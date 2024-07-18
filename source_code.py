import json;
from selenium import webdriver;
from selenium.webdriver.common.by import By;

f = open('data.json')
degrees_list = json.load(f)

def updateJSON():
  # Serializing json
  json_object = json.dumps(degrees_list, indent=2)
  
  # Writing to sample.json
  with open("data.json", "w") as outfile:
    outfile.write(json_object)


def function():

  driver = webdriver.Chrome();
  driver.get('http://results.cu.edu.eg/DarOlom/login.aspx');

  for id in range(30001, 39999):
    input_field = driver.find_element(By.CSS_SELECTOR, "#ContentPlaceHolder1_UserCode")
    input_field.clear()
    input_field.send_keys(id);
    driver.find_element(By.CSS_SELECTOR, "#ContentPlaceHolder1_LoginButton").click();
    
    try:
      name = driver.find_element(By.CSS_SELECTOR, '#ContentPlaceHolder1_lblName').text
    except:
      continue

    degress = [];

    # Subjects Count
    for x in range(14):
      try:
        degress.append(driver.find_element(By.CSS_SELECTOR, f"#ContentPlaceHolder1_gridTerm1_lblgrade_{x}").text)
      except:
        degress.append('حجب');


    try:
      total_grade = driver.find_element(By.CSS_SELECTOR, f"#ContentPlaceHolder1_lbltotalGrade").text
    except:  
      total_grade = 'حجب'

    # Update Array
    degrees_list.append({
      "name": name,
      "id": id,
      "degrees": degress,
      "total_grade": total_grade
    })

    # Update "data.json" file
    updateJSON()


    driver.back()
    continue


function()


# for id in range(30001, 39999):
#   function(id)

# function(30502)

