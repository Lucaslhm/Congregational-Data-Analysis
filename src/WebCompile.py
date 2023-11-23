import argparse
from flask import Flask, render_template_string, abort, send_from_directory

app = Flask(__name__, static_folder="../static")

# Set up the argument parser
parser = argparse.ArgumentParser(description='Serve Congregational Visualizations.')
parser.add_argument('base', help='Base HTML to be used to display the site')
parser.add_argument('ideas', help='HTML file containing the Congregational Ideas visualization.')
parser.add_argument('strengths', help='HTML file containing the Congregational Strengths visualization.')
parser.add_argument('fears', help='HTML file containing the Congregational Fears visualization.')
parser.add_argument('report', help='HTML file containing the report.')
parser.add_argument('video', help='HTML file containing the embedded youtube video.')

# Parse the arguments
args = parser.parse_args()

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
    # Set the active tab and get the corresponding content
    active_tab = tab_name
    content = get_content(getattr(args, tab_name), tab_name)
    return render_template_string(open(args.base).read(), content=content, active_tab=active_tab)

@app.route('/report')
def report():
    # Serve the report page and set the active tab to 'report'
    # Include a new variable to indicate that it's the report page
    return render_template_string(open(args.base).read(), content=open(args.report).read(), active_tab='report', is_report=True)

@app.route('/video')
def video():
    # Serve the video page and set the active tab to 'video'
    return render_template_string(open(args.base).read(), content=open(args.video).read(), active_tab='video', is_report=True)


@app.route('/favicon.ico')
def favicon():
    # If you have a favicon.ico file in your static directory, use the following line:
    return send_from_directory(app.static_folder, "favicon.ico", mimetype='image/vnd.microsoft.icon')


@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    app.run(debug=True)