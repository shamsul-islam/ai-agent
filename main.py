import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Load environment variables from .env file
load_dotenv()

# Get the Google API key from the environment
google_api_key = os.getenv("GOOGLE_API_KEY")

# Check if the API key is available
if not google_api_key:
    print("Error: GOOGLE_API_KEY not found. Please create a .env file and add your key.")
else:
    # Initialize the Google Generative AI model
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=google_api_key)

    # Create a prompt template
    prompt = PromptTemplate(
        input_variables=["topic", "language"],
        template="Write a professional LinkedIn post of 2-4 paragraphs about {topic} in {language}."
    )

    # Create an LLM chain
    chain = LLMChain(llm=llm, prompt=prompt)

    # Get user input
    topic = input("Enter the topic for the LinkedIn post: ")
    language = input("Enter the language for the post (e.g., English, Bengali, Spanish): ")

    # Run the chain and get the result
    result = chain.invoke({'topic': topic, 'language': language})

    # Print the result
    print("\nGenerated LinkedIn Post:\n")
    print(result)
