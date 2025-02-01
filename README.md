# Automated Web Testing with Selenium & PDF Report Generation 🧪📊

Welcome to the world of automated testing with Selenium and beautifully generated PDF reports! 🚀

This project is designed to make your web testing process as smooth as possible by automating the tests for your HTML, CSS, and JavaScript websites. After running the tests, the project generates a PDF report that includes detailed test results with **green** for passed tests and **red** for failed ones. **Bonus**: You even get helpful suggestions for fixing those failed tests! 😎

---

## Table of Contents 📚

- [Why This Project?](#why-this-project)
- [Features](#features)
- [How to Run the Tests](#how-to-run-the-tests)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

---

# Why This Project?

Running automated tests is **awesome**, but tracking and reporting those tests in a **well-organized** and **fun** format makes the whole process much more enjoyable! 📈

Imagine running tests and getting a PDF that looks like a **professional** report and gives you clear **feedback** about what went wrong — and even better, it suggests how to fix it! If you're building a website, testing it, and want to present results to your team, this tool is the **perfect assistant**. 🙌

---

# Features

- **Automated Testing:** Automatically runs tests on your HTML, CSS, and JavaScript websites using **Selenium WebDriver**.
- **PDF Report Generation:** After running the tests, a neat **PDF report** is generated with:
  - Date and time of the test 📅
  - Status of each test (Passed or Failed) ✅❌
  - Suggestions for failed tests 💡
- **Screenshot on Failure:** If a test case fails, a screenshot is captured and added to the PDF for better clarity and troubleshooting 🖼️.
- **Customization:** You can add your own details such as **Project Name**, **Client Name**, and **Profession** in the report (e.g., "Tested by Jagganraj" 😉).
- **Smart Test Case Results:** The results are presented in **color-coded format** (Green for Passed, Red for Failed).
- **Date and Time Formatting:** Test reports are timestamped using the **DD/MM/YYYY HH:MM:SS AM/PM** format.
- **Unique PDF Naming:** Each test run generates a new PDF with a unique name (`test_1.pdf`, `test_2.pdf`, etc.).

---

# How to Run the Tests

1. **Clone the repository:**
   ```bash
   git clone https://github.com/JAGGANRAJ27/selenium.git
   cd selenium
   ```

2. **Install dependencies:**
   You’ll need to have **Python 3.x** and **Selenium** installed on your machine. You can install the required dependencies using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the test:**
   Run the test script, and the testing process will start. You’ll be prompted to enter details such as:
   - Project Name 💻
   - Client Name 👩‍💼
   - Profession 🧑‍🔧

   Then, sit back and relax as the test runs and the PDF report is generated!

   ```bash
   python test_site.py
   ```

4. **Find the PDF report**: After the tests finish running, you’ll find a PDF report in the same directory as the script, named like `test_1.pdf`, `test_2.pdf`, etc.

5. **Screenshot on Failure**: If a test fails, a screenshot will be captured and included in the PDF report to show exactly what went wrong.

---

## Customization

You can easily customize the script to suit your own project needs:

- **Add More Test Cases:** Feel free to add more tests to check other parts of your site. Just follow the existing format, and you’re good to go!
- **Modify the Report Styling:** If you have specific requirements for how the PDF report should look, you can tweak the `reportlab` code to adjust fonts, colors, and layout.

### Screenshot Integration

With the added **screenshot feature**, if any test case fails, a screenshot will be taken and added to a **new page** in the generated PDF report. This makes troubleshooting easier by providing a visual cue along with the error message and suggestions.

---

## Contributing

Got a suggestion or a fix? Open a pull request and help us make this project even better!

1. Fork the repository
2. Create your branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a pull request

---

## Credits

- **Selenium WebDriver:** For automating the browser and running our tests. 🖥️
- **ReportLab:** For creating the PDF report (because we need those pretty PDFs!). 📄
- **Jagganraj:** The mastermind behind this awesome testing tool. 😎

---

## Fun Fact 🎉

The first automated tests were written by **Harlan Mills** in the 1960s! Now, we’re taking it a step further by generating detailed PDF reports so you can impress your colleagues or clients. **Automate the boring stuff, and add some fun to the process!** 🎈

---

Now, you can generate detailed test reports with **screenshot support**! Enjoy your automated web testing! 🎉
