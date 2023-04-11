from flask import Flask,render_template,request
from text_summarizer import textsummarizer
app = Flask(__name__,template_folder='templates')

# print (app)

@app.route('/')
def text_summarizer():
    return render_template('TextSummarizer .html')

@app.route('/analyze', methods=['GET','POST'])
def summarizer():
    if request.method == 'POST':
        rawtext= request.form['inputtext']
        summary, original_text=textsummarizer(rawtext)
    return render_template('Summarizer.html', summary = summary, original_text = original_text)

if __name__ == '__main__':
    app.run(debug=True)




