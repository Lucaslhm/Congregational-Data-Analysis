import argparse
from flask import Flask, render_template_string

# Set up the argument parser
parser = argparse.ArgumentParser(description='Serve Congregational Visualizations.')
parser.add_argument('base', help='Base HTML to be used to display the site')
parser.add_argument('ideas', help='HTML file containing the Congregational Ideas visualization.')
parser.add_argument('strengths', help='HTML file containing the Congregational Strengths visualization.')
parser.add_argument('fears', help='HTML file containing the Congregational Fears visualization.')

# Parse the arguments
args = parser.parse_args()

app = Flask(__name__)

# Initialize cache dictionary
cache = {}

def get_content(file_path, tab_name):
    # If the content is not in the cache, read from the file and store it in the cache
    if tab_name not in cache:
        with open(file_path, 'r') as file:
            cache[tab_name] = file.read()
    return cache[tab_name]

@app.route('/')
def index():
    # Default to show the Ideas visualization
    content = get_content(args.ideas, 'ideas')
    return render_template_string(open(args.base).read(), content=content, active_tab='ideas')

@app.route('/<tab_name>')
def show_tab(tab_name):
    content = ""
    if tab_name == 'ideas':
        content = get_content(args.ideas, 'ideas')
    elif tab_name == 'strengths':
        content = get_content(args.strengths, 'strengths')
    elif tab_name == 'fears':
        content = get_content(args.fears, 'fears')
    return render_template_string(open(args.base).read(), content=content, active_tab=tab_name)

if __name__ == '__main__':
    app.run(debug=True)
