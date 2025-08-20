from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate
from typing import List
# import models



def format_prompt(prompt) -> PromptTemplate:
    # TODO: format the input prompt by using the model specific instruction template
    # TODO: return a langchain PromptTemplate
    return PromptTemplate.from_template(prompt)

# def format_chat_history(messages: List[models.Message]):
#     # TODO:  implement format_chat_history to format 
#     # the list of Message into a text of chat history.
#     raise NotImplemented

def format_context(docs: List[str]):
    # TODO:  the output of the DataIndexer.search is a list of text, 
    # so we need to concatenate that list into a text that can fit into 
    # the rag_prompt_formatted. Implement format_context that takes a 
    # like of strings and returns the context as one string.
    raise NotImplemented

raw_prompt = "{question}"

# TODO: Create the history_prompt prompt that will capture the question and the conversation history. 
# The history_prompt needs a {chat_history} placeholder and a {question} placeholder.
history_prompt: str = None

# TODO: Create the standalone_prompt prompt that will capture the question and the chat history
# to generate a standalone question. It needs a {chat_history} placeholder and a {question} placeholder,
standalone_prompt: str = None

# TODO: Create the rag_prompt that will capture the context and the standalone question to generate
# a final answer to the question.
rag_prompt: str = None

# TODO: create raw_prompt_formatted by using format_prompt
# raw_prompt_formatted = format_prompt(raw_prompt)
# raw_prompt = PromptTemplate.from_template(raw_prompt)
raw_prompt = ChatPromptTemplate.from_messages([
  HumanMessagePromptTemplate.from_template(raw_prompt),
])

# TODO: use format_prompt to create history_prompt_formatted
history_prompt_formatted: PromptTemplate = None
# TODO: use format_prompt to create standalone_prompt_formatted
standalone_prompt_formatted: PromptTemplate = None
# TODO: use format_prompt to create rag_prompt_formatted
rag_prompt_formatted: PromptTemplate = None





