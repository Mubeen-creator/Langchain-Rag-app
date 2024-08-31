from langchain_google_genai import GoogleGenerativeAI # type: ignore
from langchain.prompts import PromptTemplate # type: ignore
from dotenv import load_dotenv # type: ignore
import os

# importing messages to save date
from langchain.schema import AIMessage, HumanMessage, SystemMessage # type: ignore



load_dotenv()

llm = GoogleGenerativeAI(
    google_api_key = os.getenv("GEMINI_API_KEY"),
    model="gemini-1.5-flash",
)

# Define the prompt template

# prompt = PromptTemplate(
#     template="create a story on two friends who are going to market to buy some fruits. Characters name are:  {characters}, your response should start with the character name and then add colon e,g Mubeen: Hey Arsalan, how are you?" ,
#     input_variables=["characters"]  ,
# )

# chain = prompt | llm

# response = chain.invoke({"characters": "Mubeen, Arsalan"})
# print(response)





# messages in langchain: ---- they are used to ask questions and receive answers again and again like chat model we ask the question and then get the answer. We can ask the questions again and again and again. and it will store the previous answers in memory. like chatbot or chatGPT.


# prompt = PromptTemplate(
#     template="Create the story {context} your response should be characters based you should start the response with character name and then add colon e,g ABC: context.",
#     input_variables=["context"]  ,
# )

# chain = prompt | llm


# while True:
#     human_message = input("Enter your story context: ")
#     ai_message = chain.invoke({"context": human_message})
#     print(ai_message)




# messaegs in langchain:
conversation = [
    SystemMessage(content = "You are a helpful assistant."),
    HumanMessage(content = "Can you help me with my homework."),
    AIMessage(content = "Of course! what subject do you need help with?"),
    HumanMessage(content = "I am struggling wite math."),
    AIMessage("I can help with that. What is specific math problem.")

]

conversation.append(HumanMessage(content = "I think the problem is about finding the sum of two numbers"))

for message in conversation:
    if isinstance(message, HumanMessage):
        print(f"User: {message.content}")
    elif isinstance(message, AIMessage):
        print(f"AI: {message.content}")
    elif isinstance(message, SystemMessage):
        print(f"System: {message.content}")
