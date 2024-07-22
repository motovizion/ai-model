
import ollama

def chat_with_ai():
    # Initialize the conversation history
    messages = [{'role': 'user', 'content': 'My engine started knocking?'}]

    while True:
        # Stream the AI response
        stream = ollama.chat(
            model='asm',
            messages=messages,
            stream=True,
        )

        # Collect the AI response
        response = ""
        for chunk in stream:
            response += chunk['message']['content']
            print(chunk['message']['content'], end='', flush=True)
        
        print()  # Add a newline for better readability
        
        # Append AI response to the conversation history
        messages.append({'role': 'assistant', 'content': response})
        
        # Get user input
        user_input = input("You: ")
        
        # Check if the user wants to exit the chat
        if user_input.lower() in ['exit', 'quit']:
            print("Ending chat.")
            break
        
        # Append user input to the conversation history
        messages.append({'role': 'user', 'content': user_input})

if __name__ == "__main__":
    chat_with_ai()
