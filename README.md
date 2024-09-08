# Credential Sprayer Script

This script is designed to automate login attempts for Facebook using Selenium WebDriver and Firefox (Geckodriver). It checks for valid credentials from a list provided in a `creds.txt` file and saves any working credentials to a `workingcreds.txt` file.

## Requirements

1. **Credentials File (`creds.txt`)**: 
   - You need to provide a file named `creds.txt` in the following format:
     ```
     ExampleEmail@gmail.com: ExamplePass123
     ```
   - Each line should contain an email and a password separated by a colon (`:`).

2. **Working Credentials**: 
   - Any credentials that successfully log in will be saved to a `workingcreds.txt` file for later reference.

3. **Geckodriver**: 
   - The script uses Selenium with Firefox, so you need to have [Geckodriver](https://github.com/mozilla/geckodriver/releases/tag/v0.35.0) installed.
   - Make sure to update the path to `geckodriver` in the script where necessary.

## Current Features

- The script currently works **only for Facebook** login attempts.
- The script checks each email and password pair from the `creds.txt` file and verifies whether the login is successful.
- Working credentials are saved to `workingcreds.txt`.
  
## Planned Updates

- Support for other websites in addition to Facebook.
- Improvements in functionality and error handling.
- More robust detection of login results.

## Known Issues

- When working credentials are found, the **language** on the Facebook page may switch (e.g., to a different locale). This can cause the `checkresult` function to provide incorrect results, as it relies on specific English phrases to determine login success or failure.
- Be cautious when using the script with websites in different languages; the results may vary.

## Setup

1. **Install Geckodriver**:
   - Download and install [Geckodriver](https://github.com/mozilla/geckodriver/releases/tag/v0.35.0).
   - Update the path to `geckodriver` in the script:
     ```python
     from selenium.webdriver.firefox.service import Service
     gecko_path = '/path/to/geckodriver'  # Update this to your geckodriver path
     service = Service(executable_path=gecko_path)
     ```

2. **Run the Script**:
   - Make sure `creds.txt` is formatted correctly.
   - Run the script to check the credentials. Working credentials will be stored in `workingcreds.txt`.

## Disclaimer

This script is intended for educational purposes only. Use it at your own risk, the author is in no way responsible for your actions.

