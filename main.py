from flask import Flask, send_from_directory

app = Flask(__name__)
# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


def add_no_sniff(response):
    response.headers["X-Content-Type-Options"] = "nosniff"

@app.route("/")
def serve_login_page():
    response = send_from_directory('src', 'about.html')
    add_no_sniff(response)
    return response


@app.route("/index.css")
def serve_index_css():
    response = send_from_directory("public", "index.css")
    add_no_sniff(response)
    return response

@app.route("/education.html")
def serve_education_page():
    response = send_from_directory('src', 'education.html')
    add_no_sniff(response)
    return response

@app.route("/about.html")
def serve_about_page():
    response = send_from_directory('src', 'about.html')
    add_no_sniff(response)
    return response

@app.route("/projects.html")
def serve_project_page():
    response = send_from_directory('src', 'projects.html')
    add_no_sniff(response)
    return response

@app.route("/index.js")
def serve_javascript_page():
    response = send_from_directory('public', 'index.js')
    add_no_sniff(response)
    return response

@app.route("/profile-pic-linkedin.jpg")
def serve_profile_pic():
    response = send_from_directory('public', 'profile-pic-linkedin.jpg')
    add_no_sniff(response)
    return response

if __name__ == "__main__":
    app.run()
