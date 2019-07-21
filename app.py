from flask import Flask, request, render_template
import caesar_cipher
from genetic_algorithm import run_genetic_algorithm

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    '''
        render respective templates along with function calls for respective encryption, decryption & cracking for Caesar Cipher.
    '''
    if request.method == 'POST':
        plain_text = request.form['plain_text']
        cipher_text = request.form['cipher_text']
        function = request.form.get('choices')
        key_size = int(request.form.get('key_choices'))
        if str(function) == "Encrypt":
            return render_template('caesar.html', data=[25, plain_text, caesar_cipher.encrypt(plain_text, key_size)])
        if str(function) == "Decrypt":
            return render_template('caesar.html', data=[25, caesar_cipher.decrypt(cipher_text, key_size), cipher_text])
        if str(function) == "Crack":
            return render_template('caesar.html', data=[25, caesar_cipher.crack(cipher_text), cipher_text])
    return render_template("caesar.html", data=[25, "Plain Text", "Cipher Text"])


if __name__ == '__main__':
	app.run()  