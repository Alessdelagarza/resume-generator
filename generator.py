from config import Config
import anthropic


config = Config()

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key=config.anthropic_api_key,
)

message = client.messages.create(
    model="claude-3-7-sonnet-20250219",
    max_tokens=20000,
    temperature=1,
    system="professional",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "you are a professional recruiter in the tech sector. Your job is to look at current job postings and build a resume from provided experience that best fits the role description. "
                }
            ]
        }
    ]
)
print(message.content)





