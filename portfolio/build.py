import json
import os
import jinja2
import shutil

def build():
    os.makedirs('dist', exist_ok=True)
    with open('content.json', 'r') as info:
        data = json.load(info)
    with open('templates/index.html', 'r') as items:
        content = items.read()

    template = jinja2.Template(content)
    renderHTML = template.render(
        name=data['name']
    )

    with open('dist/index.html' , 'w') as f:
        f.write(renderHTML)
    
    shutil.copy('static/style.css', 'dist/style.css')

if __name__ == '__main__':
    build()
