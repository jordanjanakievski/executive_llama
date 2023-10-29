if __name__ == "__main__":
    import os

    os.system("ollama run llama2:13b")

    prompt = input("Prompt: ")

    while prompt != "/exit":
        os.system(prompt)
        prompt = input("Prompt: ")

    print("Goodbye!")
