# Overview
The UB HACKING C3 MEAL PLANNER is an application designed to create a personalized meal plan based on the daily menu at C3 and your food preferences. This README.md provides instructions on how to set up and run the application.

# Installation
To run this project, follow these steps:

# 1. Install Required Libraries
Before running the project, make sure to install the necessary Python libraries by using the provided pip file which can be found under WebScrape/Pipfile:

    pip install selenium
    pip install webdriver-manager
    pip install panda

The Pipfile file contains the required versions of the libraries, including:

    selenium
    webdriver-manager
    pandas

# 2. Obtain an OpenAI API Key
To use the OpenAI GPT-3 model, you need to create an OpenAI account and generate an API Key. We do not include our API Key in the project for security reasons.

# 3. Set Up Your API Key
Create a text file in the chat_gpt_interface folder and paste your OpenAI API Key into that file.

# Running the Application
Now that you've installed the necessary libraries and set up your API Key, you can run the application. Follow these steps:

Navigate to the ubh-fall2023-Cool-Tan folder in your terminal.

Run the main.py file:

    python main.py

You will be prompted to choose your preferred style of food.

The application will open a Chrome browser, scrape the Net Nutrition website, and provide you with a meal based on your preferences.

After receiving the output, you will be given the option to make changes. Type your desired modifications, or type "NO" to end the session.

# Additional Information

The WebScrape directory contains the necessary files and dependencies for web scraping.
We recommend creating a virtual environment for this project to manage dependencies more effectively.
With these changes, your README file is more organized, easy to follow, and visually appealing. This will help users set up and run your project with confidence.
