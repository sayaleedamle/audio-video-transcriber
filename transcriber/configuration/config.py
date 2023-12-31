from pathlib import Path
from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI


load_dotenv()


class Config:
    model_name = os.getenv("OPENAI_MODEL")
    llm_cache = os.getenv("LLM_CACHE") == "True"
    llm = ChatOpenAI(
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        model=model_name,
        temperature=0,
        request_timeout=os.getenv("REQUEST_TIMEOUT"),
        cache=llm_cache,
        streaming=True,
    )
    verbose_llm = os.getenv("VERBOSE_LLM") == "True"

    ui_timeout = os.getenv("REQUEST_TIMEOUT")

    project_root = Path(os.getenv("PROJECT_ROOT"))
    transcribed_text = Path(os.getenv("TEXT_PATH_DISC"))
    if not transcribed_text.exists():
        transcribed_text.mkdir(exist_ok=True, parents=True)
    audio_file_path = Path(os.getenv("AUDIO_FILE"))
    if not audio_file_path.exists():
        audio_file_path.mkdir(exist_ok=True, parents=True)


cfg = Config()


if __name__ == "__main__":
    print("llm: ", cfg.llm)
    print("project root: ", cfg.project_root / "toml_support")
