# %%
import OllamaHelper as ohelper

# %%
#list of tasks in priority order. Multi-line lists are allowed in python!
list_of_tasks = [
    "Compose a brief email to my boss explaining that I will be late for tomorrow's meeting.",
    "Write a birthday poem for Otto, celebrating his 28th birthday.",
    "Write a 300-word review of the movie 'The Arrival'."
]

# %%
prompt = list_of_tasks[0]
print(ohelper.get_llm_response(prompt))
#prompt = list_of_tasks[1]
#print(ohelper.get_llm_response(prompt))
#prompt = list_of_tasks[2]
#print(ohelper.get_llm_response(prompt))

# %%
len(list_of_tasks)

# %% [markdown]
# task = list_of_tasks[0]
# from ollama import Client
# # Connect to custom host
# client = Client(host='http://localhost:11434')  # default
# # or for remote: Client(host='http://192.168.1.100:11434')
# 
# response = client.chat(
#     model='gpt-oss:20b',
#     messages=[{'role': 'user', 'content': 'Hello!'},
#               {'role': 'user', 'content': list_of_tasks[0]},
#               {'role': 'user', 'content': list_of_tasks[1]}
#               ],
# )
# print(response['message']['content'])

# %%



