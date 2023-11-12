import pyttsx3
import os
from datetime import datetime
from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from utils.prompt_utils import prompt_helper, help_output, greeting

if __name__ == "__main__":

    # Set up Llama model
    llm = Ollama(model="llama2:13b",
                 callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]))

    # Set up text-to-speech engine
    engine = pyttsx3.init('nsss')
    engine.setProperty('rate', 170)
    engine.setProperty('volume', 0.8)

    # Check if there is a directory called docs
    # If not, create one

    if not os.path.exists("docs"):
        os.makedirs("docs")
        os.makedirs("docs/emails")
        os.makedirs("docs/prep")
        os.makedirs("docs/research")
        os.makedirs("docs/misc")

    # Start the program
    greeting()
    prompt = prompt_helper()

    while prompt != "/bye":
        if prompt == "/help":
            help_output()
        else:
            output = llm(prompt)
            if "write" in prompt.lower():
                engine.say("I will go write that down")
                engine.runAndWait()
                now = datetime.now()
                formatted_date = now.strftime('%A_%m-%d-%Y_%H:%M')
                if "email" in prompt.lower():
                    # Send the output into a .txt file and save the file in docs/emails
                    with open("docs/emails/" + str(formatted_date) + ".txt", "w") as f:
                        f.write(output)
                    f.close()
                elif "prepare" in prompt.lower():
                    # Send the output into a .txt file and save the file in docs/prep
                    with open("docs/prep/" + str(formatted_date) + ".txt", "w") as f:
                        f.write(output)
                    f.close()
                elif "research" in prompt.lower():
                    # Send the output into a .txt file and save the file in docs/research
                    with open("docs/research/" + str(formatted_date) + ".txt", "w") as f:
                        f.write(output)
                    f.close()
                else:
                    with open("docs/misc/" + str(formatted_date) + ".txt", "w") as f:
                        f.write(output)
            else:
                engine.say(output)
                engine.runAndWait()
        prompt = prompt_helper()
