from flask import Flask, request, render_template
import PyPDF2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    pdf_file = request.files['pdf_file']
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    text = ""
    for page in range(pdf_reader.numPages):
        text += pdf_reader.getPage(page).extractText()
    # Save the extracted text to a database or file
    return "PDF file uploaded and text extracted"

@app.route('/search', methods=['GET'])
def search():
    keyword = request.args.get('keyword')
    # Search the extracted text for the keyword
    results = []
    # Add the search results to the results list
    return render_template('search.html', results=results)


