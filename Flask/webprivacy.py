from flask import Flask, render_template_string, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

HTML_TEMPLATE = """
<!doctype html>
<html lang="en">
  <head>
    <title>🔐 Privacy Score Analyzer</title>
    <style>
      body { font-family: Arial, sans-serif; background-color: #f2f2f2; padding: 30px; }
      .container { max-width: 700px; margin: auto; background-color: white; padding: 25px; border-radius: 10px; box-shadow: 0px 0px 10px rgba(0,0,0,0.1); }
      h1 { color: #333; }
      .score { font-size: 1.5em; color: #007bff; margin-top: 20px; }
      .issues { color: red; }
      .success { color: green; }
      input[type="text"] { width: 100%; padding: 10px; margin-top: 10px; margin-bottom: 15px; border-radius: 5px; border: 1px solid #ccc; }
      input[type="submit"] { padding: 10px 20px; background-color: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; }
      input[type="submit"]:hover { background-color: #0056b3; }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>🔐 Privacy Score Analyzer</h1>
      <form method="post">
        <label for="url">Enter a website:</label>
        <input type="text" name="url" placeholder="e.g. nytimes.com" required>
        <input type="submit" value="Analyze">
      </form>
      {% if score is not none %}
        <div class="score">🔎 Privacy Score: {{ score }}/100</div>
        {% if issues %}
          <div class="issues">
            <h3>⚠️ Issues Found:</h3>
            <ul>
              {% for issue in issues %}
                <li>{{ issue }}</li>
              {% endfor %}
            </ul>
          </div>
        {% else %}
          <div class="success">✅ Excellent! No major privacy issues found.</div>
        {% endif %}
      {% endif %}
      {% if error %}
        <div class="issues"><strong>Error:</strong> {{ error }}</div>
      {% endif %}
    </div>
  </body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def analyze():
    score = None
    issues = []
    error = None

    if request.method == 'POST':
        url_input = request.form.get('url', '').strip()
        if not url_input:
            error = "Please enter a valid URL."
        else:
            try:
                # Add http:// if missing
                if not url_input.startswith("http"):
                    url_input = "http://" + url_input

                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                }
                response = requests.get(url_input, headers=headers, timeout=8)
                html = response.text
                soup = BeautifulSoup(html, "html.parser")

                score = 100
                final_url = response.url

                # Check HTTPS
                if not final_url.startswith("https"):
                    score -= 20
                    issues.append("❌ Website does not use HTTPS.")

                # Check trackers
                tracker_keywords = ["google-analytics", "doubleclick", "facebook.net"]
                trackers_found = []
                for script in soup.find_all("script"):
                    for keyword in tracker_keywords:
                        if keyword in str(script).lower():
                            trackers_found.append(keyword)
                if trackers_found:
                    score -= 20
                    issues.append(f"❌ Trackers found: {', '.join(set(trackers_found))}")

                # Check Content-Security-Policy
                meta_csp = soup.find("meta", attrs={"http-equiv": "Content-Security-Policy"})
                if not meta_csp:
                    score -= 10
                    issues.append("❌ Missing Content-Security-Policy tag.")

            except requests.exceptions.RequestException as e:
                error = f"Network error: {e}"
            except Exception as e:
                error = f"Unexpected error: {e}"

    return render_template_string(HTML_TEMPLATE, score=score, issues=issues, error=error)

if __name__ == '__main__':
    app.run(debug=True)