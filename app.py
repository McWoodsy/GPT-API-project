from flask import Flask, render_template, request
from openai import OpenAI
import json

#   API key
client = OpenAI(api_key="")

app = Flask(__name__,
            template_folder = 'templates',
            )

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/palette", methods=["POST"])
def prompt_to_palette():
    #   Completion call
    query = request.form.get("query")
    color_array = get_colors(query)
    return json.loads(color_array)

#################

#   Completion call that returns a serialized JSON array
def get_colors(text):
    response = client.chat.completions.create(model="gpt-3.5-turbo-0125",
    messages=[
    {"role": "system", "content": """
    You are a colour palette generating assistant that responds to text prompts for colour palettes and provides only their hex
    in a json array . You will provide 5 colours unless the user requests more. YOU WILL PROVIDE NO OUTPUT EXCEPT THE JSON ARRAY.
    if the user provides no input or nonsensical, mispelled input, provide rainbow colors.
    """},
    {"role": "user", "content": " convert the following prompt into a json array of colors, with no newlines, just a pure json array: " + text},
    ],
    max_tokens = 200)
    return response.choices[0].message.content

if __name__ == "__main__":
    app.run(debug=True)