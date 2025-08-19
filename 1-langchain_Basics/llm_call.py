import langchain
from flask import template_rendered,Flask,render_template
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage,SystemMessage

# os.environ["GROQ_API_KEY"]=os.getenv('GROQ_API_KEY')
load_dotenv()

model=init_chat_model("groq:deepseek-r1-distill-llama-70b")
messages=[
    SystemMessage("You are helpful AI assistant,give me final output only no extra content "),
    HumanMessage("What are the use and benefits of Langchain")
]
response=model.invoke(messages)
print(response.content)

app = Flask(__name__)

# Define a route for the home page ('/')
@app.route('/')
def index():
    """
    This is the view function for the home page.
    It renders the index.html template.
    """
    # You can pass variables from Python to your HTML file
    page_title = "Welcome to Flask!"
    user_message = "This is a basic Flask template."
    
    return render_template('index.html', title=page_title, message=user_message,ai_message=response.content)

# Define another example route
@app.route('/about')
def about():
    """
    View function for the about page.
    """
    return "<h1>This is the About Page!</h1><p>You can create multiple routes.</p>"


# This block ensures the server only runs when the script is executed directly
if __name__ == '__main__':
    # app.run() starts the development server
    # debug=True enables auto-reloading and an interactive debugger
    app.run(debug=True)
