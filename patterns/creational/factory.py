from abc import ABC, abstractmethod
class LLM(ABC):
    @abstractmethod
    def initialize_llm(self):
        """Child concrete class will implement it"""

class ChatGPT(LLM):
    def __init__(self, api_key):
        self.api_key = api_key

    def initialize_llm(self):
        print("Initializing Chat GPT")

class Gemini(LLM):
    def __init__(self, key):
        self.key = key

    def initialize_llm(self):
        print("Initializing Gemini")

class Perplexity(LLM):
    def __init__(self, key):
        self.key = key

    def initialize_llm(self):
        print("Initializing Perplexity")

class LlmFactory:
    @staticmethod
    def create(llm_model, key):
        if llm_model == 'chat-gpt':
            return ChatGPT(key)
        elif llm_model == 'Gemini':
            return Gemini(key)
        elif llm_model == 'perplexity':
            return Perplexity(key)
        else:
            print("Not a valid model")
            return None

# client = LlmFactory.create('chat-gpt', 'abhasasha-ancbha_asmdhasdadgxxa')
# client.initialize_llm()
client = LlmFactory.create('Gemini', 'axvdfsretqmid09aja-ajdfha7egbamaaa')
client.initialize_llm()

