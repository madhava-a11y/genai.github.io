

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
                                    "You are the Review Master, an expert at analyzing review_type reviews with 15+ years of experience in customer satisfaction analysis."

                                    "REVIEW TO ANALYZE:"
                                    "review_text"

                                    "As the Review Master, please provide a comprehensive analysis including:"

                                    "1. OVERVIEW: A brief summary of the review sentiment (positive, negative, or mixed)"
                                    "2. KEY POINTS:"
                                    " - Positive aspects highlighted in the review"
                                    " - Negative aspects or concerns mentioned"
                                    "  - Neutral observations"
                                    "3. IMPROVEMENT SUGGESTIONS: Actionable recommendations based on the feedback"
                                    "4. SENTIMENT SCORE: Rate the overall sentiment on a scale of 1-10"
                                    "5. AUTHENTICITY ASSESSMENT: Does this review appear genuine or potentially biased?"

                                    "Your analysis should be balanced, insightful, and provide specific references to details mentioned in the review."
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
                        temperature= 0.4,
                        top_p= 0.9,
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
        title="Perplexity AI Review Master: AI Review Analysis",
        description="Paste a customer review, and AI will analyze its sentiment, key points, and authenticity.",
        examples=[
            ["The product quality is great, but the shipping took too long."],
            ["Terrible experience! The support team never responded."],
        ]
    )

# Step 4: Run the application
if __name__ == "__main__":
    interface = create_interface()
    interface.launch()