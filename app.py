import subprocess

from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# In-memory database
items = []


@app.route('/')
def index():
    return render_template('index.html', items=items)


@app.route('/add', methods=['POST'])
def add_item():
    item = request.form.get('item')
    if item:
        items.append(item)
    return redirect(url_for('index'))


@app.route('/delete/<int:index>')
def delete_item(index):
    if index < len(items):
        items.pop(index)
    return redirect(url_for('index'))


@app.route('/update/<int:index>', methods=['POST'])
def update_item(index):
    if index < len(items):
        items[index] = request.form.get('new_item')
    return redirect(url_for('index'))


@app.route('/testing', methods=['POST'])
def testing():
    try:
        payload = request.json
        ref = payload.get('ref', '')

        if ref == 'refs/heads/testing':
            subprocess.run(['script_testing.sh'])

            return "Webhook received, OK for testing branch"
        else:
            return "Webhook received but KO"

    except Exception as e:
        return f"Error webhook " + str(e) + "."


@app.route('/deploy')
def deploy():
    subprocess.run(['script_deploy.sh'])
    return "Script 'script_deploy.sh' OK"


if __name__ == '__main__':
    app.run(debug=True)
