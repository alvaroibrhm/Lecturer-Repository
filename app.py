import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Directory where uploaded files will be stored
UPLOAD_FOLDER = 'Directories/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Route for the home page - displays repository structure
@app.route('/')
def index():
    # List all directories in the main folder
    dirs = {}
    base_dir = os.path.join(app.config['UPLOAD_FOLDER'])

    for root, subdirs, files in os.walk(base_dir):
        relative_path = os.path.relpath(root, base_dir)
        dirs[relative_path] = {'subdirs': subdirs, 'files': files}

    return render_template('index.html', dirs=dirs)

# Route for uploading files
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Get the selected directory and the file to upload
        directory = request.form.get('directory')
        file = request.files['file']

        if file and directory:
            # Save the file in the selected directory
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], directory, file.filename))
            return redirect(url_for('index'))

    # If GET request, show upload form
    dirs = next(os.walk(app.config['UPLOAD_FOLDER']))[1]  # List of directories for dropdown
    return render_template('upload.html', dirs=dirs)

if __name__ == '__main__':
    app.run(debug=True)
