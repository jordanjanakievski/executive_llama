from vosk import Model, KaldiRecognizer
import pyaudio
from termcolor import colored, cprint

# Constants
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 8000
RECORD_SECONDS = 5

model = Model("utils/vosk-model-en-us-0.22-lgraph")
rec = KaldiRecognizer(model, 16000)
mic = pyaudio.PyAudio()


def prompt_helper():
    input_prompt = ""
    input_type = input("\nPress enter to type, or say something to speak: ")
    if input_type == "":
        input_prompt = input("(Text) Q? ")
    else:
        print("(Speech) Q? ")
        stream = mic.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
        stream.start_stream()

        # Stop looping when there is no more data in the stream (when the user stops talking)
        while True:
            data = stream.read(CHUNK, exception_on_overflow=False)
            if len(data) == 0:
                break
            if rec.AcceptWaveform(data):
                print("Vocal Prompt")
                text = rec.Result()
                print(f"'{text[14:-3]}'")
                input_prompt = f"{text[14:-3]}"
                break

        stream.close()

    if input_prompt == "":
        input_prompt = input("(Text) Q? ")
    return input_prompt


def help_output():
    help_response = colored("""
    Here are some commands you can use:
    /bye - Exit the program
    /help - Display this help message

    Here are some keywords you can use in your prompts:
    write - Write down the output into a .txt file
    email - Write down the output into a .txt file in docs/emails
    prepare - Write down the output into a .txt file in docs/prep
    research - Write down the output into a .txt file in docs/research
    """, "yellow")
    cprint(help_response)


def greeting():
    ascii_art = colored("""
     ______ __  __  ______  ______  __  __  ______ __  __   ________       __      __      ______  __    __  ______  
    /\  ___/\_\_\_\/\  ___\/\  ___\/\ \/\ \/\__  _/\ \/\ \ / /\  ___\     /\ \    /\ \    /\  __ \/\ "-./  \/\  __ \\
    \ \  __\/_/\_\/\ \  __\\\\ \ \___\ \ \_\ \/_/\ \\\\ \ \ \ \\'/\ \  __\     \ \ \___\ \ \___\ \  __ \ \ \-./\ \ \  __ \ 
     \ \_____/\_\/\_\ \_____\ \_____\ \_____\ \ \_\\\\ \_\ \__| \ \_____\    \ \_____\ \_____\ \_\ \_\ \_\ \ \_\ \_\ \_\\
      \/_____\/_/\/_/\/_____/\/_____/\/_____/  \/_/ \/_/\/_/   \/_____/     \/_____/\/_____/\/_/\/_/\/_/  \/_/\/_/\/_/
    """, "blue")
    # Write the word "LLAMA" in ASCII art
    cprint(ascii_art)
    print("Welcome to Executive Llama!")
    print("I am running on the 13B Llama2 model 🦙")
    print("Everything is performed locally, so no data is sent to the cloud.")
    print("If you ever need help, just type /help.")
    print("You can also type /bye to exit.")
