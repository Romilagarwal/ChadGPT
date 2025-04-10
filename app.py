def check_and_call(sentence):
    if "javascript" in sentence.lower():
        source = requests.get('https://developer.mozilla.org/en-US/docs/Web/JavaScript').text
        soup = BeautifulSoup(source, 'html.parser')
        data = soup.find('article', class_='main-page-content').text
        return data

    elif "react" in sentence.lower():
        source = requests.get('https://react.dev/reference/react').text
        soup = BeautifulSoup(source, 'html.parser')
        data = soup.find('article', class_='font-normal break-words text-primary dark:text-primary-dark').text
        return data

    elif "node" in sentence.lower():
        source = requests.get('https://nodejs.org/docs/latest/api/documentation.html').text
        soup = BeautifulSoup(source, 'html.parser')
        data = soup.find('div', id='apicontent').text
        return data

    elif "npm" in sentence.lower():
        source = requests.get('https://docs.npmjs.com/about-npm').text
        soup = BeautifulSoup(source, 'html.parser')
        data = soup.find('main', class_='Box-sc-g0xbh4-0 jrNUvm').text
        return data

    elif "express" in sentence.lower():
        source = requests.get('https://expressjs.com/en/starter/installing.html').text
        soup = BeautifulSoup(source, 'html.parser')
        data = soup.find('div', id='page-doc').text
        return data

    elif "mongoose" in sentence.lower():
        source = requests.get('https://mongoosejs.com/docs/guide.html').text
        soup = BeautifulSoup(source, 'html.parser')
        data = soup.find('div', class_='container').text
        return data

    elif "next" in sentence.lower():
        source = requests.get('https://nextjs.org/docs').text
        soup = BeautifulSoup(source, 'html.parser')
        data = soup.find('div', class_='prose prose-vercel max-w-none').text
        return data

    elif "axios" in sentence.lower():
        source = requests.get('https://axios-http.com/docs/intro').text
        soup = BeautifulSoup(source, 'html.parser')
        data = soup.find('div', class_='body').text
        return data

    elif "tailwind" in sentence.lower():
        source = requests.get('https://tailwindcss.com/docs').text
        soup = BeautifulSoup(source, 'html.parser')
        data = soup.find('main', class_='max-w-3xl mx-auto relative z-20 pt-10 xl:max-w-none').text
        return data

    elif "vite" in sentence.lower():
        source = requests.get('https://vitejs.dev/guide/').text
        soup = BeautifulSoup(source, 'html.parser')
        data = soup.find('div', class_='content-container').text
        return data

    else:
        print("Sorry, I didn't understand that. Please try again.")

from flask import Flask, request, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def process_sentence():
    if request.method == 'POST':
        print(request.form['sentence'])
        sentence = request.form.get('sentence')
        if sentence:
            response = check_and_call(sentence)
            return render_template('response.html', response=response)
        else:
            return render_template('index.html', error="Please provide a sentence.")
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run (debug=True)
