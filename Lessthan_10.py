from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pandas as pd

# Use a context manager to ensure the driver is closed properly
with webdriver.Chrome() as driver:
    driver.get('https://www.google.com/search?q= INPUT_YOUR_KEYWORDS ')
    driver.implicitly_wait(2)

    clicks = 2  # Set the number of questions you want to click
    list_paa = []

    for i in range(clicks):
        # Use explicit wait instead of fixed sleep time
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "related-question-pair")))

        paa_questions = driver.find_elements(By.CLASS_NAME, "related-question-pair")

        if i < len(paa_questions):
            print('Clicking question #', i + 1)
            try:
                # Click the question
                paa_questions[i].click()

                # Wait for the content to load
                wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "CSkcDe")))

                # Fetch the list of questions again to get the updated question text
                updated_questions = driver.find_elements(By.CLASS_NAME, "CSkcDe")
                if i < len(updated_questions):
                    question_text = updated_questions[i].text
                    list_paa.append({'Questions': question_text})
                    print("Question:", question_text)
                else:
                    print("No updated question found for index", i)

            except NoSuchElementException as e:
                print("Element not found:", e)
            except Exception as e:
                print("Error clicking a question or extracting text:", e)
        else:
            print("No more questions available at index", i)

# Convert list of dictionaries to DataFrame
df = pd.DataFrame(list_paa)

# Drop any rows in the DataFrame that contain NaN values
df = df.dropna()

# Ensure query variable is defined and valid for a file name
query = 'RESULT_PAA'  # Make sure to replace this with your actual query variable
csv_filename = f'{query}.csv'

# Save the DataFrame to a CSV file
df.to_csv(csv_filename, index=False)
