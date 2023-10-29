from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

if __name__ == "__main__":

    llm = Ollama(model="llama2",
                 callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]))

    print("🦙 Welcome to the Llama chatbot! 🦙")

    prompt = input("\nQ: ")

    while prompt != "/bye":
        output = llm(prompt)
        print(output)
        prompt = input("\nQ: ")
