# call_gemma.py

import google.generativeai as genai

# --- Configuration ---
# IMPORTANT: Replace "YOUR_API_KEY" with the API key you obtained from Google AI Studio.
# It's more secure to set this as an environment variable rather than hardcoding.
# For example, you could set it in your terminal before running the script:
# export GOOGLE_API_KEY="YOUR_API_KEY"
# And then use: api_key = os.getenv("GOOGLE_API_KEY")
# For this example, we'll show direct assignment for simplicity, but be cautious.

API_KEY = "removed for safety"  # <--- REPLACE WITH YOUR ACTUAL API KEY

# Configure the generative AI client with your API key
try:
    genai.configure(api_key=API_KEY)
except Exception as e:
    print(f"Error configuring API key: {e}")
    print("Please ensure you have replaced 'YOUR_API_KEY' with a valid key.")
    exit()

# --- Model Selection ---
# Specify the Gemma 3 27B model.
# Model names can change or vary. Check Google AI Studio for the latest available model identifiers.
# "models/gemma-3-27b-it" is a likely identifier for the instruction-tuned 27B variant.
# Other variants might exist (e.g., base pre-trained).
MODEL_NAME = "models/gemma-3-27b-it"  # Or other Gemma 3 27B variant available via API

# --- Generation Configuration (Optional) ---
# You can customize generation parameters like temperature, top_p, top_k, max_output_tokens
generation_config = {
    "temperature": 0.7,  # Controls randomness. Lower is more deterministic.
    "top_p": 0.95,  # Nucleus sampling.
    "top_k": 40,  # Top-k sampling.
    "max_output_tokens": 1024,  # Maximum number of tokens to generate.
}

# --- Safety Settings (Optional) ---
# Configure safety settings to block harmful content.
# You can adjust the threshold for different categories.
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
]

# --- Initialize the Model ---
try:
    model = genai.GenerativeModel(
        model_name=MODEL_NAME,
        generation_config=generation_config,
        safety_settings=safety_settings,
    )
    print(f"Successfully initialized model: {MODEL_NAME}")
except Exception as e:
    print(f"Error initializing model '{MODEL_NAME}': {e}")
    print("Ensure the model name is correct and available with your API key.")
    exit()


# --- Make an API Call ---
def generate_text(prompt_text):
    """
    Sends a prompt to the Gemma model and returns the generated text.
    """
    print(f"\nSending prompt: '{prompt_text}'")
    try:
        # For text-only models like Gemma (when not using multimodal features)
        response = model.generate_content(prompt_text)

        # Print the full response object for debugging if needed
        # print("Full API Response:", response)

        if response.parts:
            return response.text
        elif response.prompt_feedback and response.prompt_feedback.block_reason:
            return f"Content generation blocked. Reason: {response.prompt_feedback.block_reason_message}"
        else:
            # This part might need adjustment based on the exact response structure
            # if no parts and no block reason, but candidates exist.
            if response.candidates and response.candidates[0].content.parts:
                return response.candidates[0].content.parts[0].text
            return "No content generated or unexpected response structure."

    except Exception as e:
        return f"An error occurred during content generation: {e}"


# --- Example Usage ---
if __name__ == "__main__":
    # Ensure API_KEY is set
    if API_KEY == "YOUR_API_KEY":
        print(
            "ERROR: Please replace 'YOUR_API_KEY' in the script with your actual Google AI API key."
        )
    else:
        # Example prompts
        prompt1 = "Explain the concept of general relativity in simple terms."
        prompt2 = "Write a short story about a friendly robot exploring a new planet."
        prompt3 = "What are some interesting facts about the human brain?"

        # Generate and print responses
        response1 = generate_text(prompt1)
        print(f"\nResponse for prompt 1:\n{response1}")

        response2 = generate_text(prompt2)
        print(f"\nResponse for prompt 2:\n{response2}")

        response3 = generate_text(prompt3)
        print(f"\nResponse for prompt 3:\n{response3}")
