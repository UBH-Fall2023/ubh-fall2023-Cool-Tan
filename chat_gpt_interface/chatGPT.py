import openai

import userIO.userQuery

openai.api_key = open("chatGPTKEY", 'r').read().strip('\n')


def starterRequest():
    userPreference = userIO.userQuery.takeUserPreference()
    ##foods = getFoodDictionary.toString
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a nutritionist that is making a meal plan."},
            {"role": "user", "content": "I have the folowing preferences for a meal: "+userPreference+". Please make a meal with the folowing food items"+foods}
        ]
    )
    print(response['choices'][0]['message']['content'])

def modifyMenu():
    userPreference = userIO.userQuery.takeUserPreference()
    ##foods = getFoodDictionary.toString
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a nutritionist that is making a meal plan."},
            {"role": "user", "content": "Please modify your previous response with these additional preferences: "+userPreference}
        ]
    )
    print(response['choices'][0]['message']['content'])