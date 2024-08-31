from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace # type: ignore
from langchain_core.prompts import PromptTemplate # type: ignore
from langchain_core.prompts import PromptTemplate # type: ignore
from langchain.chains import SimpleSequentialChain, LLMChain # type: ignore
from dotenv import load_dotenv # type: ignore
import os

# Load environment variables
load_dotenv()

# Initialize the HuggingFace endpoint
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    huggingfacehub_api_token=os.getenv("HUGGINGFACE_ACCESS_TOKEN"),
)

# # first way to create a prompt template
# langchainPrompt = PromptTemplate.from_template("Recipe of {cake} cake")
# prompt_output = langchainPrompt.format(cake = "chocolate")
# print(prompt_output)



# 2nd way to create a prompt template
# langchainPromptFinal = PromptTemplate(template = "Recipe of {type} cake", inputVariable=["type"])   
# output = langchainPromptFinal.format(type = "chocolate")
# print(output) 


# third way to create a prompt template
# prompt = ChatHuggingFace = "system: this chat is about to understanding langchain, user: what is the chat model of langchain?"
# result = llm.invoke(prompt)
# print(result)




# Chaning in langchain starts here
prompt1 = PromptTemplate(template = "Suggest me a muslim baby name for: {text}", input_variables = ["text"])
prompt2 = PromptTemplate(template = "And write a poem for this name: {text}", input_variables = ["text"])

chain1 = LLMChain(llm=llm, prompt=prompt1)
chain2 = LLMChain(llm=llm, prompt=prompt2)

chain = SimpleSequentialChain(chains = [chain1, chain2])
result = chain.invoke("boy")
print(result)


