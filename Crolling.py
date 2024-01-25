from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

driver = webdriver.Chrome()
driver.get('https://www.google.com/search?q= INPUTYOUR_KEY_WORDS ')
driver.implicitly_wait(2)

clicks = 10  # Set the number of questions you want to click

for i in range(clicks):
    # Fetch the list of questions again to get updated elements
    paa_questions = driver.find_elements(By.CLASS_NAME, "related-question-pair")

    if i < len(paa_questions):
        print('Clicking question #', i + 1)
        try:
            # Click the question
            paa_questions[i].click()
            time.sleep(random.uniform(2, 5))  # Wait for the content randomly

            # Fetch the list of questions again to get the updated question text
            updated_questions = driver.find_elements(By.CLASS_NAME, "CSkcDe")
            if i < len(updated_questions):
                question_text = updated_questions[i].text
                print("Question:", question_text)
            else:
                print("No updated question found for index", i)

        except Exception as e:
            print("Error clicking a question or extracting text:", e)
    else:
        print("No more questions available at index", i)

driver.quit()
