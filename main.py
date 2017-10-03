from flask import Flask, request

from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")

def index(): 
        
    encrypt_form = """
         <!DOCTYPE html>

            <html>
                <head>
                    <style>
                        form {{
                            background: #ffffff;
                            padding: 20px;
                            margin: 0 auto;
                            width: 540px;
                            font: 16px sans-serif;
                            border-radius: 10px;
                        }}

                        textarea {{
                            margin: 10px 0;
                            width: 540px;
                            height: 120px;
                        }}
                        
                    </style>
                </head>
                <body>
                  <form action="/" method="post">
                        <div>
                            <label for="rot">Rotate by:</label>
                            <input type="text" name="rot" value="0">
                            <p class="error"></p>
                        </div>
                        <textarea type="text" name="text">{0}</textarea>
                        <br>
                        <input type="submit">
                   </form>
                </body>
            </html>
        
         """
         
    return form.format(" ")

@app.route("/", methods=['POST'])
def encrypt(rotate_string):
    text = rotate_string(text)
    
    content = "<h1>" + text + "</h1>"

    return form.format(content)

app.run()