import speech_recognition as sr

r = sr.Recognizer()


def prompt_helper():
    input_prompt = ""
    input_type = input("\nPress enter to type, or say something to speak: ")
    if input_type == "":
        input_prompt = input("(Text) Q? ")
    else:
        print("(Speech) Q? ")
        with sr.Microphone() as source:
            audio = r.listen(source)
            print("Done!")
            print("Sphinx thinks you said ::: " + r.recognize_sphinx(audio))
        input_prompt = r.recognize_sphinx(audio)
    return input_prompt


def help_output():
    print("=====================================")
    print("Here are some commands you can use:")
    print("/bye - Exit the program")
    print("/help - Display this help message")
    print("=====================================")
    print("Here are some keywords you can use in your prompts:")
    print("write - Write down the output into a .txt file")
    print("email - Write down the output into a .txt file in docs/emails")
    print("prepare - Write down the output into a .txt file in docs/prep")
    print("research - Write down the output into a .txt file in docs/research")
    print("=====================================\n")


def greeting():
    ascii_art = """
     ______ __  __  ______  ______  __  __  ______ __  __   ________       __      __      ______  __    __  ______  
    /\  ___/\_\_\_\/\  ___\/\  ___\/\ \/\ \/\__  _/\ \/\ \ / /\  ___\     /\ \    /\ \    /\  __ \/\ "-./  \/\  __ \\
    \ \  __\/_/\_\/\ \  __\\\\ \ \___\ \ \_\ \/_/\ \\\\ \ \ \ \\'/\ \  __\     \ \ \___\ \ \___\ \  __ \ \ \-./\ \ \  __ \ 
     \ \_____/\_\/\_\ \_____\ \_____\ \_____\ \ \_\\\\ \_\ \__| \ \_____\    \ \_____\ \_____\ \_\ \_\ \_\ \ \_\ \_\ \_\\
      \/_____\/_/\/_/\/_____/\/_____/\/_____/  \/_/ \/_/\/_/   \/_____/     \/_____/\/_____/\/_/\/_/\/_/  \/_/\/_/\/_/
    """
    # Write the word "LLAMA" in ASCII art
    print(ascii_art)
    print("Welcome to Executive Llama!")
    print("I am running on the 13B Llama2 model 🦙")
    print("Everything is performed locally, so no data is sent to the cloud.")
    print("If you ever need help, just type /help.")
    print("You can also type /bye to exit.")
