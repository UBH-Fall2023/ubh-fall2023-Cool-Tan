import chat_gpt_interface.chatGPT
chat_gpt_interface.chatGPT.starterRequest()

secondResponse = chat_gpt_interface.chatGPT.modifyMenu()

while secondResponse != -1:
    secondResponse = chat_gpt_interface.chatGPT.modifyMenu()

print('shutting down')
