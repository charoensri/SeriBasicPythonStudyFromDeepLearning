from ollama import Client
import ipywidgets as widgets
from IPython.display import display, HTML   
import io
import os
import base64
import pandas as pd

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
                    #"content": "You are a helpful but terse AI assistant who gets straight to the point.",
                    "content": "You are a helpful but funny AI assistant who never gets straight to the point.",
                    },
                    {'role': 'user', 'content': 'Please introduce yourself in a paragraph with a humorous tone.'},
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

def upload_txt_file():
    """
    Uploads a text file and saves it to the specified directory.
    
    Args:
        directory (str): The directory where the uploaded file will be saved. 
        Defaults to the current working directory.
    """
    # Create the file upload widget
    upload_widget = widgets.FileUpload(
        accept='.txt',  # Accept text files only
        multiple=False  # Do not allow multiple uploads
    )
    # Impose file size limit
    output = widgets.Output()
    
    # Function to handle file upload
    def handle_upload(change):
        with output:
            output.clear_output()
            # Read the file content
            content = upload_widget.value[0]['content']
            name = upload_widget.value[0]['name']
            size_in_kb = len(content) / 1024
            
            if size_in_kb > 3:
                print(f"Your file is too large, please upload a file that doesn't exceed 3KB.")
                return
		    
            # Save the file to the specified directory
            with open(name, 'wb') as f:
                f.write(content)
            # Confirm the file has been saved
            print(f"The {name} file has been uploaded.")

    # Attach the file upload event to the handler function
    upload_widget.observe(handle_upload, names='value')

    display(upload_widget, output)

def list_files_in_directory(directory='.'):
    """
    Lists all non-hidden files in the specified directory.
    
    Args:
        directory (str): The directory to list files from. Defaults to the current working directory.
    """
    try:
        files = [f for f in os.listdir(directory) if (not f.startswith('.') and not f.startswith('_'))]
        for file in files:
            print(file)
    except Exception as e:
        print(f"An error occurred: {e}")


def read_journal(journal_file):
    f = open(journal_file, "r")
    journal = f.read() 
    f.close()
    return journal

def create_download_link(file_path, description):
    with open(file_path, 'rb') as file:
        file_data = file.read()
        encoded_data = base64.b64encode(file_data).decode()
        href = f'<a href="data:text/html;base64,{encoded_data}" download="{file_path}">{description}</a>'
        return HTML(href)
def download_file():
    """
    Creates a widget to download a file from the working directory.
    """
    # Text input to specify the file name
    file_name_input = widgets.Text(
        value='',
        placeholder='Enter file name',
        description='File:',
        disabled=False
    )
    
    # Button to initiate the download
    download_button = widgets.Button(
        description='Download',
        disabled=False,
        button_style='', # 'success', 'info', 'warning', 'danger' or ''
        tooltip='Download the specified file',
        icon='download' # (FontAwesome names without the `fa-` prefix)
    )
    
    # Output widget to display the download link
    output = widgets.Output()

    def on_button_click(b):
        with output:
            output.clear_output()
            file_name = file_name_input.value
            if (not file_name.startswith('.') and not file_name.startswith('_')):
                try:
                    download_link = create_download_link(file_name, 'Click here to download your file')
                    display(download_link)
                except Exception as e:
                    print(f"Error: {e}")
            else:
                print("Please enter a valid file name.")
    
    # Attach the button click event to the handler
    download_button.on_click(on_button_click)
    
    # Display the widgets
    display(widgets.HBox([file_name_input, download_button]), output)       

def display_table(data):
    df = pd.DataFrame(data)

    # Display the DataFrame as an HTML table
    display(HTML(df.to_html(index=False))) 

def read_journal(journal_file):
    f = open(journal_file, "r")
    journal = f.read() 
    f.close()

    # Return the journal content
    return journal

def print_journal(file):
    f = open(file, "r")
    journal = f.read()
    f.close()
    #print(journal)    
    return journal

def fahrenheit_to_celsius(fahrenheit):
    # Calculation for getting the temperature in celsius
    celsius = (fahrenheit - 32) * 5 / 9
    # Print the results
    #print(f"{fahrenheit}°F is equivalent to {celsius:.2f}°C")
    return celsius

def read_csv(file):
    f = open(file, "r")
    
    csv_reader = csv.DictReader(f)
    data = []
    for row in csv_reader:
        data.append(row)
    f.close()
    
    return data

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32 
    print(f"{celsius}°C is equivalent to {fahrenheit:.2f}°F")