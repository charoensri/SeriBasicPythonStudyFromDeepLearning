from ollama import Client
client = Client(host='http://localhost:11434')  # default

def get_llm_response(prompt):
    """This function takes as input a prompt, which must be a string enclosed in quotation marks,
    and passes it to OpenAI's xxx model. The function then saves the response of the model as
    a string.
    """

    try:
        if not isinstance(prompt, str):
            raise ValueError("Input must be a string enclosed in quotes.")
        
#       client = Client(host='http://localhost:11434')  # default
        # or for remote: Client(host='http://192.168.1.100:11434'
        response = client.chat(
            model='gpt-oss:20b',
            messages=[
                    {
                    "role": "system",
                    "content": "You are a helpful but terse AI assistant who gets straight to the point.",
                    },
                    {'role': 'user', 'content': 'Please introduce yourself briefly.'},
                    #{'role': 'user', 'content': list_of_tasks[0]},
                    {'role': 'user', 'content':  prompt},
                    ],
                    stream=False,
        )
       #print(response['message']['content'])
       #return response
        return (response['message']['content'])
    except TypeError as e:
        print("Error:", str(e))


def print_llm_response(prompt):
    """This function takes as input a prompt, which must be a string enclosed in quotation marks,
    and passes it to OpenAI's GPT3.5 model. The function then prints the response of the model.
    """
    llm_response = get_llm_response(prompt)
    print(llm_response)