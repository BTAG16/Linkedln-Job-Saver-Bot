# LinkedIn Job Saver Bot

This is a Python bot that automates job searching, saving, and following companies on LinkedIn using **Selenium**. The bot logs in to LinkedIn, searches for jobs, saves job postings, and follows the companies listed in the job descriptions.

## Features

- **Login Automation**: Logs into LinkedIn with stored credentials from environment variables.
- **Job Search**: Navigates to the LinkedIn job search page and interacts with the job listings.
- **Save Jobs**: Saves job listings to your LinkedIn account.
- **Follow Companies**: Automatically follows companies associated with the job listings.
- **Error Handling**: Implements safe element finding to avoid errors due to stale elements or missing elements.
- **CAPTCHA Handling**: Waits for user input to solve CAPTCHA when necessary.

## Tech Stack

- **Python 3.x**
- **Selenium**: For automating browser interactions.
- **Chrome WebDriver**: For headless browser automation.
- **dotenv**: For securely loading environment variables.
- **ActionChains**: For simulating mouse movements and clicks.

## Setup

### Prerequisites

1. **Install Python 3.x**: Ensure Python 3.x is installed on your system.
2. **Install Dependencies**: Use pip to install the required libraries:
    ```bash
    pip install selenium python-dotenv
    ```
3. **Download ChromeDriver**: Ensure you have the correct version of [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) installed for your browser version.

4. **Set Up Environment Variables**:
    - Create a `.env` file in the root of your project with the following content:
    ```env
    EMAIL=your_email@example.com
    PASSWORD=your_password
    ```
    Replace `your_email@example.com` and `your_password` with your LinkedIn credentials.

### Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/btag16/linkedin-job-saver-bot.git
   cd linkedin-job-saver-bot
   ```

2. Run the script:
   ```bash
   python linkedin_job_saver_bot.py
   ```

3. The bot will automatically attempt to log in. If LinkedIn asks for CAPTCHA verification, solve the CAPTCHA manually and press Enter to continue.

4. The bot will start searching for job listings, saving job positions, and following the companies listed in the job descriptions.

### Notes

- **Captcha**: If LinkedIn prompts for a CAPTCHA, you need to manually solve it as Selenium cannot bypass CAPTCHA.
- **Element Selection**: The bot uses XPath and CSS selectors to find elements. If LinkedIn changes their website layout or classes, you may need to update the selectors.
- **Browser Automation**: The bot will open a Chrome browser and perform actions. You can modify the script to run in headless mode by adding `chrome_options.add_argument("--headless")` if you prefer not to open the browser window.

## License

This project is licensed under the MIT License.

---

Feel free to contribute, suggest improvements, or ask questions by opening an issue in this repository.
