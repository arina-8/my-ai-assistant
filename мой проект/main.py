import os 
from dotenv import load_dotenv
from gigachat import GigaChat
from prompts import SYSTEM_PROMPT
load_dotenv()
from gigachat.models import ChatCompletionRequest, ChatMessage
key = os.getenv("GIGACHAT_CREDENTIAL")
scope = os.getenv("GIGACHAT_SCOPE")
question = input("Какую книгу вы ищете?").strip()
request = ChatCompletionRequest(
    messages =[
        ChatMessage(
            role= "system",
            content=SYSTEM_PROMPT,
        ),
        ChatMessage(
            role= "user",
            content=question,
        )
    ]

)
print("Отправляем запрос....")
with GigaChat(
    credentials=key,
    scope=scope,
    model="GigaChat-2",
    ca_bundle_file="certs/russian_trusted_root_ca_pem.crt",
    timeout=60,
) as client:
    response = client.chat.create(request)
answer = response.messages[0].content[0].text
print("ответ:")
print(answer)