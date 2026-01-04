from flask import Flask, Request, render_template, redirect, request, send_file, flash
from flask_wtf import CSRFProtect
import PIL.Image, PIL.ExifTags
import io
import xml.etree.ElementTree as ET

app = Flask(__name__)
app.secret_key = 'supersecretkey'
csrf = CSRFProtect()

@app.route('/main')
@app.route('/')
def main():
    return render_template('main.html')


@app.route('/delete-meta', methods=['POST', "GET"])
def analyse():
    if request.method == 'POST':
        uploaded_file = request.files.get('image')
        if uploaded_file:
            filename = uploaded_file.filename.lower() 
            if filename.endswith(('.jpg', '.jpeg', '.png')):
                img = PIL.Image.open(uploaded_file)
                clean_img = PIL.Image.new(img.mode, img.size)
                clean_img.putdata(list(img.getdata()))
                if clean_img.mode == "RGBA":
                    clean_img = clean_img.convert("RGB")
                img_io = io.BytesIO()
                clean_img.save(img_io, format='JPEG')
                img_io.seek(0)
                return send_file(
                    img_io,
                    mimetype='image/png',
                    as_attachment=True,
                    download_name='clean.jpg'
                )
            else:
                flash('this file type is not supported!')
                return redirect('/delete-meta')
        else:
            flash('No file uploaded!')
            return redirect('/delete-meta')
    else:
        return render_template('clear meta.html')
    
@app.route('/scan-svg', methods=['POST', 'GET'])
def svg():
    if request.method == 'POST':
        uploaded_file = request.files.get('image')
        if uploaded_file:
            filename = uploaded_file.filename.lower()
            if filename.endswith(('.svg')):
                try:
                    tree = ET.parse(uploaded_file)
                    root = tree.getroot()
                    found_issue = False
                    for elem in root.iter():
                        if "script" in elem.tag.lower():
                            flash('This file is dangerous: Script tag detected!')
                            found_issue = True
                            break
                    if not found_issue:
                        flash('SVG file analyzed - No immediate threats found via backend check.')
                except Exception as e:
                    flash(f"Error parsing SVG: {str(e)}")
                
                return redirect('/scan-svg')
            else:
                flash('this file is not svg!')
        else:
            flash('no file uploaded')
    else:
        return render_template('svg scan.html')
    
@app.route('/compress', methods=['POST', 'GET'])
def compress():
    if request.method == 'POST':
        uploaded_file = request.files.get('image')
        quality = request.form.get('quality')
        if uploaded_file:
            img = PIL.Image.open(uploaded_file)
            img_io = io.BytesIO()
            if img.format == 'JPEG':
                if img.mode == 'RGBA':
                    img = img.convert('RGB')
                img.save(
                    img_io,
                    format='JPEG',
                    quality=int(quality),
                    optimize=True
                )
                mimetype = 'image/jpeg'
                filename = 'compressed.jpg'
            elif img.format == 'PNG':
                img.save(
                    img_io,
                    format='PNG',
                    optimize=True,
                    compress_level=9
                )
                mimetype = 'image/png'
                filename = 'compressed.png'
            else:
                flash("Unsupported image format")
            img_io.seek(0)
            return send_file(
                img_io,
                mimetype=mimetype,
                as_attachment=True,
                download_name=filename
            )
        else:
            flash('this file type is not suppoted!')
    else:
        return render_template('compress.html')

if __name__ == '__main__':
    app.run(debug=True)