Introduction to rag app: there are three file here 
1: HuggingFace.py: in this file we kept our model hugging face H4 
2: main.py: In this file out model is Google Gemini model
3: gemni.py: In this file we created the Rag-app which will take data from Data.txt file. In Data.txt file we have data about human diseases. Our model will take data from this file and 
and tell us about diseases, causes and treatments or medicine. In this file there is a code of Rag-base-application<!-- how to get started with langchain -->

- create dev container
- install poetry
- install langchain
- install langchain-core
- install model like (gemni model, Openai, hugging face)
        poetry add langchain-core
        poetry add langchain-community
        poetry add langchain-openai / langchain-google-genai

- create main.py file
        get api key


  To run this project you have to run the following command in your terminal
  poetry run python <file_name_you_want_to_run>.py

