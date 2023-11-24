from flask import Flask, render_template_string, abort, send_from_directory

app = Flask(__name__, static_folder="../static")

# Initialize cache dictionary
cache = {}

def get_content(file_path, tab_name):
    if tab_name not in cache:
        with open(file_path, 'r') as file:
            cache[tab_name] = file.read()
    return cache[tab_name]

@app.route('/')
def index():
    content = get_content('Figures/ideaVisualization.html', 'ideas')
    return render_template_string(open('Templates/base_template.html').read(), content=content, active_tab='ideas')

@app.route('/<tab_name>')
def show_tab(tab_name):
    active_tab = tab_name
    content_path = {
        'ideas': 'Figures/ideaVisualization.html',
        'strengths': 'Figures/strengthVisualization.html',
        'fears': 'Figures/fearVisualization.html',
        'report': 'Templates/read_me.html',
        'video': 'Templates/video_embed.html'
    }.get(tab_name, 'Figures/ideaVisualization.html')
    content = get_content(content_path, tab_name)
    return render_template_string(open('Templates/base_template.html').read(), content=content, active_tab=active_tab)

@app.route('/report')
def report():
    return render_template_string(open('Templates/base_template.html').read(), content=open('Templates/read_me.html').read(), active_tab='report', is_report=True)

@app.route('/video')
def video():
    return render_template_string(open('Templates/base_template.html').read(), content=open('Templates/video_embed.html').read(), active_tab='video', is_report=True)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.static_folder, "favicon.ico", mimetype='image/vnd.microsoft.icon')

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(app.static_folder, filename)

# No need to run the app here since gunicorn will be used instead

