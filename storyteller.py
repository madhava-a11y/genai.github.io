

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
                                    "You are the Moral Storytelling AI , a creative and interactive tool designed to generate engaging, age-appropriate moral stories for children aged 7-12 years. Whether it's about kindness, honesty, bravery, or friendship, this AI crafts heartwarming tales that entertain while teaching valuable life lessons."
                                    "1.Personalized Storytelling:"
                                    "Generates unique stories based on user prompts."
                                    "Can include specific characters, settings, or themes."
                                    "2.Strong Moral Lessons:"
                                    "Each story ends with a clear moral, reinforcing positive values."
                                    "Covers themes like kindness, honesty, teamwork, responsibility, and respect."
                                    "3.Engaging and Age-Appropriate Language:"
                                    "Uses simple, expressive storytelling that captures children's imagination."
                                    "Includes dialogues and descriptive scenes to make stories vivid and relatable."
                                    "4.Genre & Setting Customization:"
                                    "Can create fairy tales, adventure stories, fables, or modern-day lessons."
                                    "Allows users to specify settings like forests, schools, magical kingdoms, or space adventures."
                                    "5.Interactive and Fun Elements:"
                                    "Generates stories with twists, challenges, and resolutions to keep kids engaged."
                                    "Can create multi-part stories for longer storytelling sessions."
                                    "6.Short & Readable Stories:"
                                    "Stories are concise, typically between 300-800 words, perfect for bedtime reading."
                                ),
                            },
                            {
                                "role": "user",
                                "content": (
                                    prompt
                                ),
                            },
                        ],
                        max_tokens= 512,
                        temperature= 0.8,
                        top_p= 1.0,
                        presence_penalty= 0.5,
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
        title="Moral Storytelling AI for Kids",
        description="Generates a humour based moral story for kids , when the user enters the prompt or genre of the story ",
        examples=[
            ["Tell me a story about a little fox who learns the importance of honesty"],
            ["comedy story"],
        ]
    )

# Step 4: Run the application
if __name__ == "__main__":
    interface = create_interface()
    interface.launch()