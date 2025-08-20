from langserve import RemoteRunnable
chain = RemoteRunnable("https://abhinit-hw6.hf.space/simple")
# chain = RemoteRunnable("http://localhost:8000/simple")
stream = chain.stream(input={'question':'How are you?'})
for chunk in stream:
    print(chunk, end="", flush=True)