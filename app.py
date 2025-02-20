from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for homepage
@app.route('/')
def home():
    name = request.args.get('name')  # Get the name from query parameter
    if name:
        welcome_message = f"Welcome, {name}!"
    else:
        welcome_message = "Welcome to our website!"
    return render_template('index.html', welcome_message=welcome_message)

# Route for contact form
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return redirect(url_for('thank_you', name=name, email=email))  # Redirect to thank you page with data
    return render_template('contact.html')

# Route for thank you page
@app.route('/thank_you')
def thank_you():
    name = request.args.get('name')
    email = request.args.get('email')
    return render_template('thank_you.html', name=name, email=email)

if __name__ == '__main__':
    app.run(debug=True)
