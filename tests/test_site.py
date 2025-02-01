import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Paragraph, Spacer

def to_upper_camel_case(text):
    return ' '.join([word.capitalize() for word in text.split()])

# Function to capture a screenshot and annotate it with error information
def capture_screenshot(driver, test_name, error_message=None, expected_value=None):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_name = f"{test_name}_{timestamp}.png"
    screenshot_path = os.path.join(os.getcwd(), "screenshots", screenshot_name)

    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    driver.save_screenshot(screenshot_path)

    if error_message and expected_value:
        img = Image.open(screenshot_path)
        draw = ImageDraw.Draw(img)
        font = ImageFont.load_default()
        annotation = f"Error: {error_message}\nExpected: {expected_value}"
        text_position = (10, 10)
        draw.text(text_position, annotation, font=font, fill="red")
        img.save(screenshot_path)
        
    return screenshot_path

def create_pdf(project_name, client_name, profession, status, test_steps, failed_count, test_number=1, screenshot_path=None):
    current_time = datetime.now().strftime("%d/%m/%Y %I:%M:%S %p")
    file_name = f"test_{test_number}.pdf"
    while os.path.exists(file_name):
        test_number += 1
        file_name = f"test_{test_number}.pdf"

    margin_left = 20
    margin_top = 780
    line_height = 12
    y_position = margin_top
    width, height = A4
    
    c = canvas.Canvas(file_name, pagesize=A4)
    c.setFont("Helvetica", 12)

    # Left column
    c.drawString(margin_left, y_position, f"Project Name: {project_name}")
    y_position -= line_height
    c.drawString(margin_left, y_position, f"Date: {current_time}")
    y_position -= line_height
    c.drawString(margin_left, y_position, f"Testing Type: Automatic")
    y_position -= line_height
    c.drawString(margin_left, y_position, f"Tested By: Jagganraj")
    
    # Right column
    y_position = margin_top
    c.setFont("Helvetica", 12)
    c.drawString(width / 2 + margin_left, y_position, f"Client Name: {client_name}")
    y_position -= line_height
    c.drawString(width / 2 + margin_left, y_position, f"Profession: {profession}")
    y_position -= line_height * 2

    c.setLineWidth(0.5)
    c.line(margin_left, y_position, width - margin_left, y_position)
    y_position -= 25  # Line space

    c.setFont("Helvetica", 12)
    c.drawString(margin_left, y_position, "Test Cases:")
    y_position -= line_height

    for i, (test_case, result, expected, suggestion) in enumerate(test_steps):
        color = colors.green if result == "Passed" else colors.red
        c.setFillColor(color)
        c.drawString(margin_left, y_position, f"{i+1}. Test case: {test_case} - {result}")
        y_position -= line_height
        if result == "Failed":
            c.setFillColor(colors.black)
            c.drawString(margin_left, y_position, f"Expected: {expected}")
            y_position -= line_height
            c.drawString(margin_left, y_position, f"Suggestion: {suggestion}")
            y_position -= line_height * 2
        else:
            y_position -= line_height * 2 
    c.setLineWidth(0.5)
    c.line(margin_left, y_position, width - margin_left, y_position)
    y_position -= 15  # Line space

    c.setFont("Helvetica", 10)
    c.setFillColor(colors.black)
    footer_text = f"This is the automated testing for the website {project_name} made by Jagganraj on {current_time}."
    c.drawString(margin_left, y_position - 320, footer_text)

    c.showPage()

    if screenshot_path:
        c.drawString(margin_left, y_position, "Screenshot of failure:")
        y_position -= 15
        c.drawImage(screenshot_path, margin_left, y_position, width=400, height=300)

    c.save()

driver = webdriver.Chrome()
test_number = 1
test_steps = []
failed_count = 0

project_name = to_upper_camel_case(input("Enter the project name: "))  
client_name = to_upper_camel_case(input("Enter the client name: "))  
profession = to_upper_camel_case(input("Enter your profession: "))  
def log_error(test_case, expected, error_message, test_steps, suggestion):
    print(f"\n--- Test Case: {test_case} ---")
    print(f"Expected: {expected}")
    print(f"Error: {error_message}")
    print(f"Suggested Update: {suggestion}")

    test_steps.append((test_case, "Failed", expected, suggestion))

try:
    driver.get("file:///E:/Selenium_testing/first_practice_test/index.html") 
    time.sleep(2)  
    test_steps.append(("Opening Website", "Passed", "", ""))
except Exception as e:
    log_error("Opening Website", "Website should open successfully", f"Failed to open the webpage. Error: {str(e)}", test_steps, "Ensure the path is correct and the webpage is accessible.")
    failed_count += 1

# Verify title
try:
    expected_title = "Simple Website"
    assert expected_title in driver.title
    print(f"Title Verified: '{expected_title}' found.")
    test_steps.append(("Verifying Title", "Passed", expected_title, ""))
except AssertionError:
    suggestion = f"Ensure that the <title> tag in your HTML contains '{expected_title}'."
    log_error("Verifying Title", expected_title, f"Title does not match. Expected '{expected_title}', but got '{driver.title}'", test_steps, suggestion)
    failed_count += 1

# Find the button and click it
try:
    button = driver.find_element(By.ID, "clickMe")
    button.click()
    print("Button Clicked: Action performed successfully.")
    test_steps.append(("Finding and Clicking Button", "Passed", "", ""))
except Exception as e:
    suggestion = "Ensure the button with id 'clickMe' exists and is clickable."
    log_error("Finding and Clicking Button", "Button should be clickable", f"Failed to locate or click the button. Error: {str(e)}", test_steps, suggestion)
    failed_count += 1
time.sleep(2)

# Verify the message appears
try:
    expected_message = "Button clicked!"
    message = driver.find_element(By.ID, "message").text
    assert message == expected_message
    print(f"Message Verified: '{expected_message}' displayed correctly.")
    test_steps.append(("Verifying Message", "Passed", expected_message, ""))
except AssertionError:
    suggestion = f"Ensure that the message element with id 'message' is updated to '{expected_message}' after the button is clicked."
    log_error("Verifying Message", expected_message, f"Error: Expected message to be '{expected_message}', but got '{message}'", test_steps, suggestion)
    failed_count += 1

status = "Failed" if failed_count > 0 else "Passed"

screenshot_path = None
if failed_count > 0:
    screenshot_path = capture_screenshot(driver, "Test_Failure")

create_pdf(project_name, client_name, profession, status, test_steps, failed_count, test_number, screenshot_path)
print("\n--- Test Completed ---")
print("Test Completed!")
driver.quit()