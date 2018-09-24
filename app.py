from flask import Flask, render_template, redirect, url_for, send_from_directory, request
from flask_bootstrap import Bootstrap
from PIL import Image
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
Bootstrap(app)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
images_directory = os.path.join(APP_ROOT, 'images')
thumbnails_directory = os.path.join(APP_ROOT, 'thumbnails')
if not os.path.isdir(images_directory):
    os.mkdir(images_directory)
if not os.path.isdir(thumbnails_directory):
    os.mkdir(thumbnails_directory)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gallery')
def gallery():
    thumbnail_names = os.listdir('./thumbnails')
    return render_template('gallery.html', thumbnail_names=thumbnail_names)

@app.route('/thumbnails/<filename>')
def thumbnails(filename):
    return send_from_directory('thumbnails', filename)

@app.route('/images/<filename>')
def images(filename):
    return send_from_directory('images', filename)

@app.route('/public/<path:filename>')
def static_files(filename):
    return send_from_directory('./public', filename)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        for upload in request.files.getlist('images'):
            filename = upload.filename
            # Sempre é uma boa ideia proteger um nome de arquivo antes de armazená-lo
            filename = secure_filename(filename)
            # Isto é para verificar se os arquivos são suportados
            ext = os.path.splitext(filename)[1][1:].strip().lower()
            if ext in set(['jpg', 'jpeg', 'png']):
                print('File supported moving on...')
            else:
                return render_template('error.html', message='Uploaded files are not supported...')
            destination = '/'.join([images_directory, filename])
            # Salve a imagem original
            upload.save(destination)
            # Salve uma cópia da imagem em miniatura
            image = Image.open(destination)
            image.thumbnail((300, 170))
            image.save('/'.join([thumbnails_directory, filename]))
        return redirect(url_for('gallery'))
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 3000))
