import openai

import userIO.userQuery

openai.api_key = open("chat_gpt_interface/chatGPTKEY", 'r').read().strip('\n')


def starterRequest():
    # openai.api_key = open("chatGPTKEY", 'r').read().strip('\n')
    userPreference = userIO.userQuery.takeUserPreference()
    ##foods = getFoodDictionary.toString
    foods = "Pizza (Calores:300,Sodium 10%), Cheeseburger(Calores:500,Sodium 15%), tomato soup(Calores:200,Sodium 20%), french fries(Calores:300,Sodium 18%), salad(Calores:200,Sodium 0%), greek yogurt(Calores:300,Sodium 0%)"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a nutritionist that is making a meal plan."},
            {"role": "user",
             "content": "I have the folowing preferences for a meal: " + userPreference + ". Please make a singular dinner meal with the folowing food items" + foods + ". You must respond with the names of the food along with the total nutrion value which will be given."}
        ]
    )
    print(response['choices'][0]['message']['content'])


def modifyMenu():
    # openai.api_key = open("chatGPTKEY", 'r').read().strip('\n')
    userPreference = userIO.userQuery.additionalPreference()
    if (userPreference == -1):
        return -1
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a nutritionist that is making a meal plan."},
            {"role": "user",
             "content": "Please modify your previous sugested meal with these additional preferences: " + userPreference+". You must respond with the names of the food along with the total nutrion value which will be given."}
        ]
    )
    print(response['choices'][0]['message']['content'])
    return 0