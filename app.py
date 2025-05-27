# from flask import Flask, render_template, request, make_response, redirect
# import subprocess
# import os

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template('index.html')

# @app.route("/robots.txt")
# def robots():
#     return "User-agent: *\nDisallow: /humans.html"

# @app.route("/humans.html")
# def humans_page():
#     human_cookie = request.cookies.get('human')
#     if human_cookie == 'true':
#         return render_template('human_check_passed.html')
#     else:
#         response = make_response(render_template('humans.html'))
#         return response

# @app.route("/arrakis")
# def arrakis_page():
#     return render_template('arrakis.html')

# @app.route("/check_password", methods=['POST'])
# def check_password():
#     password = request.form.get('password')
#     if password == "MasoomBacha":
#         return render_template('krypton.html')
#     else:
#         return "<p>Incorrect password. Try again.</p>"

# @app.route("/space_ping", methods=['POST'])
# def space_ping():
#     command = request.form.get('command')
#     safe_commands = ["ping", "traceroute"] # Example - not robust

#     # Very basic and INSECURE input filtering
#     if any(bad_char in command for bad_char in [";", "&", "|", "$", "`"]):
#         return "<p>That doesn't look very space-like...</p>"

#     try:
#         process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#         stdout, stderr = process.communicate(timeout=5)
#         output = stdout.decode('utf-8') + stderr.decode('utf-8')
#         return f"<pre>{output}</pre>"
#     except subprocess.TimeoutExpired:
#         return "<p>Space ping timed out!</p>"
#     except Exception as e:
#         return f"<p>Error in space: {e}</p>"

# @app.route("/flag.txt")
# def get_flag():
#     # INSECURE in a real CTF - FOR DEMONSTRATION ONLY
#     with open("flag.txt", "r") as f:
#         flag = f.read()
#     return f"<h1>Congratulations! The flag is: {flag}</h1>"

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, request, make_response, redirect
import subprocess
import os

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/robots.txt")
def robots():
    return "User-agent: *\nDisallow: /humans.html"

@app.route("/humans.html")
def humans_page():
    human_cookie = request.cookies.get('human')
    if human_cookie == 'true':
        return render_template('human_check_passed.html')
    else:
        response = make_response(render_template('humans.html'))
        return response

@app.route("/arrakis")
def arrakis_page():
    return render_template('arrakis.html')

@app.route("/check_password", methods=['POST'])
def check_password():
    password = request.form.get('password')
    if password == "MasoomBacha":
        return render_template('krypton.html')
    else:
        return "<p>Incorrect password. Try again.</p>"

# @app.route("/space_ping", methods=['POST'])
# def space_ping():
#     command = request.form.get('command')
#     safe_commands = ["ping", "traceroute", "cat"] # Example - not robust

#     # Very basic and INSECURE input filtering
#     if any(bad_char in command for bad_char in [";", "&", "|", "$", "`"]):
#         return "<p>That doesn't look very space-like...</p>"

#     try:
#         process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#         stdout, stderr = process.communicate(timeout=5)
#         output = stdout.decode('utf-8') + stderr.decode('utf-8')
#         return f"<pre>{output}</pre>"
#     except subprocess.TimeoutExpired:
#         return "<p>Space ping timed out!</p>"
#     except Exception as e:
#         return f"<p>Error in space: {e}</p>"

@app.route("/space_ping", methods=['POST'])
def space_ping():
    command = request.form.get('command')

    # Block dangerous shell metacharacters
    forbidden_chars = [";", "&", "|", "$", "`", ">", "<", "(", ")", "[", "]", "{", "}"]

    if any(char in command for char in forbidden_chars):
        return "<p>🚫 Command blocked by interstellar firewall.</p>"

    # Allow only a strict whitelist of commands
    allowed_commands = ["string ACM_Ctf.txt"]  # or any other unique one you decide

    if command not in allowed_commands:
        return "<p>❌ That command is not allowed in this galaxy.</p>"

    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate(timeout=5)
        output = stdout.decode('utf-8') + stderr.decode('utf-8')
        return f"<pre>{output}</pre>"
    except subprocess.TimeoutExpired:
        return "<p>⏳ Space ping timed out!</p>"
    except Exception as e:
        return f"<p>💥 Error in hyperspace: {e}</p>"


@app.route("/ACM_Ctf.txt")
def get_flag():
    # INSECURE in a real CTF - FOR DEMONSTRATION ONLY
    with open("ACM_Ctf.txt", "r") as f:
        flag = f.read()
    return f"<h1>Congratulations! The flag is: {flag}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
