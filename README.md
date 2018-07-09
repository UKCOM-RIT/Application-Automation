# Application-Automation

This project was developed using Python 3.6.0 IDLE. 
Selenium is the main module used for web scraping and automation. 

All passwords used for testing must be removed before pushing to any publicly available repository.

For questions contact bryan_racic@uky.edu

## Prerequisites
- Python 3.6
- **Browser Specific Webdriver**
  - *(see getting started for more details)*

## Getting started

Selenium requires a driver to interface with your browser of choice. 
This project uses Safari as it provides native support for the WebDriver API, all that's required for this browser is enabling developer options. 

```
- Ensure that the Develop menu is available. It can be turned on by opening Safari preferences (Safari > Preferences in the menu bar), 
going to the Advanced tab, and ensuring that the Show Develop menu in menu bar checkbox is checked.
- Enable Remote Automation in the Develop menu. This is toggled via Develop > Allow Remote Automation in the menu bar.
- Authorize safaridriver to launch the webdriverd service which hosts the local web server. 
To permit this, run /usr/bin/safaridriver once manually and complete the authentication prompt.
```

*more information found [here](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)*

WebDriver is available for other browsers as well, 
more information on setup and installation for these specfic browsers:
- [**Chrome**](https://sites.google.com/a/chromium.org/chromedriver/downloads)
- [**Edge**](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
- [**Firefox**](https://github.com/mozilla/geckodriver/releases)

**_NOTE:_**
It will be necissary to make a small change depending on the browser used. 
>driver = webdriver.Safari()
