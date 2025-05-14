import json


class Config:
    def __init__(self, config_file: str = "config.json"):
        self.load_config(config_file)

    def load_config(self, config_file: str):
        try:
            with open(config_file, "r") as f:
                config = json.load(f)

            # Anthropic Settings
            self.anthropic_api_key = config.get("anthropic_api_key", "")


        except FileNotFoundError:
            print(f"Config file {config_file} not found. Using default values.")
            self.set_defaults()

    def set_defaults(self):
        # Set default values if config file is not found
        self.anthropic_api_key = ""