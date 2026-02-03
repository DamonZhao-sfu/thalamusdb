# Also changes ground truth score thresholds.
USE_BART = False
# Automatically set to True when running GUI.
GUI = False

# vLLM LLaVA Vision Model Configuration
# Set USE_VLLM to True to use vLLM-deployed LLaVA model instead of GPT-4-Turbo
USE_VLLM = False
VLLM_BASE_URL = "http://localhost:8000/v1"  # vLLM server endpoint
VLLM_MODEL_NAME = "llava-hf/llava-v1.6-mistral-7b-hf"  # Model name as deployed
VLLM_API_KEY = "EMPTY"  # vLLM typically doesn't require an API key