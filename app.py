from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template with CSS for styling
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>URL Encoder/Decoder</title>
<style>
    body {
        font-family: Arial, sans-serif;
        background: linear-gradient(to right, #74ebd5, #acb6e5);
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100vh;
        margin: 0;
    }
    .container {
        background: white;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    form {
        display: flex;
        flex-direction: column;
    }
    input[type="text"], button {
        margin-bottom: 10px;
        padding: 10px;
        border-radius: 4px;
        border: 1px solid #ddd;
    }
    button {
        background-color: #4CAF50;
        color: white;
        cursor: pointer;
    }
    button:hover {
        background-color: #45a049;
    }
</style>
</head>
<body>
<div class="container">
    <h2>URL Encoder/Decoder</h2>
    <form action="" method="post">
        <input type="text" name="url" placeholder="Enter URL here..." required>
        <button type="submit" name="action" value="encode">Encode</button>
        <button type="submit" name="action" value="decode">Decode</button>
    </form>
        {% if result %}
            <div class="result">{{ result }}
                <button onclick="copyToClipboard('{{ result }}')">Copy to clipboard</button>
            </div>
        {% endif %}
</div>
    <script>
        function copyToClipboard(text) {
            navigator.clipboard.writeText(text).then(function() {
                log("Copied to clipboard");
            }, function(err) {
                log('Error in copying text: ', err);
            });
        }
    </script>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        url = request.form['url']
        action = request.form.get('action')
        
        if action == 'encode':
            result = url.replace('.', '[.]')
        elif action == 'decode':
            result = url.replace('[.]', '.')
            
    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == '__main__':
    app.run(debug=True)
