import logging
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Setting up logging
logging.basicConfig(level=logging.INFO)

# Flask configurations
app.config.from_mapping(
    HOST='0.0.0.0',
    PORT=8081,
)

@app.route('/', methods=['GET', 'POST'])
def home():
    """
    Home route to render the main page and handle the conversion form submission.
    """
    jira_output = ''
    if request.method == 'POST':
        input_text = request.form.get('input_text', '').strip()
        if input_text:
            jira_output = convert_to_jira_table(input_text)
        else:
            logging.warning("Empty input received for conversion.")
    
    return render_template('index.html', jira_output=jira_output)

def convert_to_jira_table(input_text):
    """
    Convert the provided text into Jira table markdown.
    
    Args:
    - input_text (str): Text to be converted into Jira table format.

    Returns:
    - str: Jira formatted table.
    """
    lines = input_text.split("\n")
    
    if not lines:
        return ""

    headers = lines[:6]
    data = lines[6:]
    
    jira_headers = "|| " + " || ".join(headers) + " ||"
    jira_data = []
    
    for i in range(0, len(data), 6):
        row = data[i:i+6]
        jira_row = "| " + " | ".join(row) + " |"
        jira_data.append(jira_row)
    
    return jira_headers + "\n" + "\n".join(jira_data)

@app.errorhandler(404)
def page_not_found(e):
    logging.error(f"404 error: {e}")
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    logging.error(f"500 error: {e}")
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(host=app.config.get('HOST'), port=app.config.get('PORT'))
