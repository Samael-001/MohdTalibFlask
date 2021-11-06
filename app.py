from flask import Flask
from flask import render_template
import json
import os 
import io
from flask import request

app = Flask(__name__)


@app.route("/")
def home():
    #return "<p>Hello, World!</p>"
     return render_template('home.html', name=app)

def get_static_file(path):
    site_root = os.path.realpath(os.path.dirname(__file__))
    return os.path.join(site_root, path)


def get_static_json(path):
    return json.load(open(get_static_file(path)))

@app.route("/reading")
def reading():
    #return "<p>Hello, World!</p>"
    data = get_static_json("static/files/reading.json")
    return render_template('reading.html', data=data)

def order_projects_by_weight(projects):
    try:
        return int(projects['weight'])
    except KeyError:
        return 0

@app.route("/projects")
def projects():
    #return "<p>Hello, World!</p>"
    data = get_static_json("static/projects/projects.json")['projects']
    data.sort(key=order_projects_by_weight, reverse=True)

    tag = request.args.get('tags')
    if tag is not None:
        data = [project for project in data if tag.lower() in [project_tag.lower() for project_tag in project['tags']]]

    return render_template('projects.html', projects=data, tag=tag)

@app.route('/projects/<title>')
def project(title):
    projects = get_static_json("static/projects/projects.json")['projects']
    experiences = get_static_json("static/experiences/experiences.json")['experiences']

    in_project = next((p for p in projects if p['link'] == title), None)
    in_exp = next((p for p in experiences if p['link'] == title), None)

    if in_project is None and in_exp is None:
        return render_template('404.html'), 404
    # fixme: choose the experience one for now, cuz I've done some shite hardcoding here.
    elif in_project is not None and in_exp is not None:
        selected = in_exp
    elif in_project is not None:
        selected = in_project
    else:
        selected = in_exp

    # load html if the json file doesn't contain a description
    if 'description' not in selected:
        path = "experiences" if in_exp is not None else "projects"
        selected['description'] = io.open(get_static_file(
            'static/%s/%s/%s.html' % (path, selected['link'], selected['link'])), "r", encoding="utf-8").read()
    return render_template('project.html', project=selected)


# @app.route('/podcasts/<filename>')
# def podcast(filename):
#     if filename.endswith('.mp3'):
#         return send_file(get_static_file(f'static/podcasts/{filename}'))
#     return abort(404)


# @app.route('/podcasts/index.xml')
# def podcast_rss():
#     return Response(podcast_feed_generator().rss_str(), mimetype='application/rss+xml')



if __name__ == "__main__":
    app.run( debug=True)