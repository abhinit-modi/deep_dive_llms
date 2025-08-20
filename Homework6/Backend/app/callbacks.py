from typing import Dict, Any, List
from langchain_core.callbacks import BaseCallbackHandler
import schemas
import crud


class LogResponseCallback(BaseCallbackHandler):

    def __init__(self, user_request: schemas.UserRequest, db):
        super().__init__()
        self.user_request = user_request
        self.db = db

    def on_llm_end(self, outputs: Dict[str, Any], **kwargs: Any) -> Any:
        """Run when llm ends running."""
        # TODO: The function on_llm_end is going to be called when the LLM stops sending 
        # the response. Use the crud.add_message function to capture that response.
        raise NotImplemented

    def on_llm_start(
        self, serialized: Dict[str, Any], prompts: List[str], **kwargs: Any
    ) -> Any:
        for prompt in prompts:
            print(prompt)