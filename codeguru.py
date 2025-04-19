

import gradio as gr
from openai import OpenAI
import os

# Step 1: Setup function with proper Perplexity configuration
def setup_perplexity_client():
    # Get API key from environment
    api_key = "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"
    if not api_key:
        raise ValueError("PERPLEXITY_API_KEY environment variable not set")

    # Create client with proper Perplexity configuration
    client = OpenAI(
        base_url="https://api.perplexity.ai",  # Perplexity API endpoint
        api_key=api_key,
    )

    return client

# Step 2: Text generation function
def generate_text(prompt):
    try:
        client = setup_perplexity_client()

        # Create chat completion with proper parameters
        response = client.chat.completions.create(
            model="sonar",  # Perplexity model
            messages = [
                            {
                                "role": "system",
                                "content": (
                                    "You are Multi-Language Code Generator AI , an advanced system capable of generating code in multiple programming languages based on user input. Designed for developers, students, and enthusiasts, this AI efficiently translates programming logic into various languages, making it a powerful tool for learning, development, and cross-language compatibility."
                                    "1.Multi-Language Support:"
                                    "Generates code in Python, Java, C++, JavaScript, C#, Swift, Go, and more."
                                    "Supports both procedural and object-oriented programming styles."
                                    "2.ontext-Aware Code Generation:"
                                    "Understands user prompts with detailed requirements."
                                    "Produces optimized and readable code tailored to best practices in each language."
                                    "3.Syntax and Structure Accuracy:"
                                    "Ensures proper syntax, indentation, and structure."
                                    "Adheres to coding conventions specific to each language."
                                    "4.Code Conversion Between Languages:"
                                    "Converts code from one programming language to another with high accuracy."
                                    "Helps developers learn by comparing implementations in different languages."
                                    "5.Customizable Output:"
                                    "Allows users to specify additional constraints, such as performance optimization, memory efficiency, or readability."
                                    "Provides alternative implementations based on different programming paradigms."
                                    "6.Error Handling and Debugging:"
                                    "Detects potential logical and syntax errors before outputting the code."
                                    "Suggests improvements and best practices."
                                    "7.Interactive and User-Friendly Interface:"
                                    "Can be integrated with chatbots, IDEs, and online coding platforms."
                                    "Provides explanations for the generated code when requested."
                                ),
                            },
                            {
                                "role": "user",
                                "content": (
                                    prompt
                                ),
                            },
                        ],
                        max_tokens= 720,
                        temperature= 0.4,
                        top_p= 0.95,
                        frequency_penalty=0.1,
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"

# Step 3: Gradio interface
def create_interface():
    return gr.Interface(
        fn=generate_text,
        inputs=gr.Textbox(label="Input Prompt"),
        outputs=gr.Textbox(label="Generated Text"),
        title="Multi-Language Code Generator AI",
        description="Generate a code in the programming language specified by the user based on the prompt given , and solve the given question ",
        examples=[
            ["Generate a function to find the factorial of a number in Python, Java, and C++"],
            ["Generate a code in java to find the armstrong numbers of 100 natural numbers"],
        ]
    )

# Step 4: Run the application
if __name__ == "__main__":
    interface = create_interface()
    interface.launch()