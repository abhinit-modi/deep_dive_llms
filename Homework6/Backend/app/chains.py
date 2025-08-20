import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.runnables import RunnablePassthrough
from transformers import AutoTokenizer
import schemas
from prompts import (
    raw_prompt,
    format_context,
)
# from data_indexing import DataIndexer

load_dotenv()

# data_indexer = DataIndexer()

MODEL_ID = "meta-llama/Meta-Llama-3-8B-Instruct"

llm = HuggingFaceEndpoint(
    model=MODEL_ID,
    huggingfacehub_api_token=os.environ['HF_TOKEN'],
    max_new_tokens=512,
    stop_sequences=["<|endoftext|>", "[EOS]"],
    streaming=True,
)

chat_model = ChatHuggingFace(llm=llm)

simple_chain = (raw_prompt | chat_model).with_types(input_type=schemas.UserQuestion)

# # TODO: create formatted_chain by piping raw_prompt_formatted and the LLM endpoint.
# formatted_chain = None

# # TODO: use history_prompt_formatted and HistoryInput to create the history_chain
# history_chain = None

# # TODO: Let's construct the standalone_chain by piping standalone_prompt_formatted with the LLM
# standalone_chain = None

# input_1 = RunnablePassthrough.assign(new_question=standalone_chain)
# input_2 = {
#     'context': lambda x: format_context(data_indexer.search(x['new_question'])),
#     'standalone_question': lambda x: x['new_question']
# }
# input_to_rag_chain = input_1 | input_2

# # TODO: use input_to_rag_chain, rag_prompt_formatted, 
# # HistoryInput and the LLM to build the rag_chain.
# rag_chain = None

# # TODO:  Implement the filtered_rag_chain. It should be the 
# # same as the rag_chain but with hybrid_search = True.
# filtered_rag_chain = None






