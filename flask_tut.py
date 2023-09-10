from flask import Flask, render_template, request, url_for, flash, redirect
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

# ...

def visit(title,club,tag):
    print(title,club,tag)
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    URL = "https://cfi.iitm.ac.in/blog?search="+title
    driver.get(URL)
    time.sleep(1)
    elem=driver.find_elements(By.TAG_NAME,'a')[2]
    print(elem)
    elem.click()
    time.sleep(3)
    return driver

app = Flask(__name__)
app.config['SECRET_KEY'] = 'df0331cefc6c2b9a5d0208a726a5d1c0fd37324feb625506'

app = Flask(__name__)

messages = [{'title': 'Message One','club':'what club?!','tag':'what tag!'}]

@app.route('/', methods=('GET', 'POST'))
def index():
    return redirect("/create/")


@app.route('/create/', methods=('GET', 'POST'))
def create():
    tags=[]
    if request.method == 'POST':
        print(request.form)
        title = request.form['title']
        tag=request.form['tag']
        if not title:
            title=""
        if request.form.get('AI'):
            tags.append("AI")
        if request.form.get('webo'):
            tags.append("webops")
        
        dri=visit(title,tags,tag)

        
        messages.append({'title': title})
        return redirect(url_for('index'))

    return render_template('create.html')