from flask import Flask, request

from caesar import rotate_string

import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
         <!DOCTYPE html>

            <html>
                <head>
                    <style>
                        form {{
                            background: #fcfcfc;
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
                            <label type="number" name="rotation_number">Rotate by:</label>
                            <input type="text" name="rot" value="0">
                            <p class="error"></p>
                        </div>
                        <textarea type="text" name="message_text">{0}</textarea>
                        <br>
                        <input type="submit">
                   </form>
                </body>
            </html>
        
         """

@app.route("/")



def index(): 
        
    
         
    return form.format(" ")

@app.route("/", methods=['POST'])
def encrypt():
    text = request.form.get("message_text")
    num = int(request.form.get("rot"))
    encrypt_text = rotate_string(text, num)
    content =  encrypt_text 

    return form.format(content)


app.run()