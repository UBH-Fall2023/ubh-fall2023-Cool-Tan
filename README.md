# UB HACKING C3 MEAL PLANNER
- This application will make a meal for you based on the daily menu at C3 and the preferences you give.
- The WebScrape directory contains 2 files, a pip file containing the versions of certain libraries needed. These libraries should be installed as you clone the repository but if it isn't, open a terminal instance, cd to the project directory, and type in the following prompts:
-   pip install selenium
-   pip install webdriver-manager
-   pip install panda
- To run this project, you will need to create your own OpenAI API key. We haven't attached ours to this project since that would be a security risk; however, all you need to do to run this project is create an OpenAI account and generate an API Key.
- Once you have the API key, you will need to create a text file in the chat_gpt_interface folder and paste your API Key into that text file
- Run main.py (Be sure to run main.py in the ubh-fall2023-Cool-Tan folder and not the main.py file in WebScrape), provide in a prompt. The first prompt would be your preferred style of food
- Watch the program open a Chrome instance, scrape through the Net Nutrition website, and provide you with the meal you desire
- Once an output is produced, you will receive a prompt that asks whether you want to make any changes. If you do, type in what you want, otherwise type NO to end the session

