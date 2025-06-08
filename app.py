from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

# Simple motivational messages list
motivations = [
    "Today is a gift, walk in it with confidence.",
    "Your mind is powerful. Speak victory today.",
    "You are stronger than your struggle.",
    "This ride might be short, but your purpose is long.",
    "You are blessed to be a blessing."
]

# Web page design
html = """
<!doctype html>
<title>Michael's Uber AI Greeting</title>
<h1>Enter Customer Name</h1>
<form method="POST">
  <input name="customer" placeholder="Customer Name" required>
  <button type="submit">Generate Greeting</button>
</form>

{% if greeting %}
  <h2>{{ greeting }}</h2>
{% endif %}
"""

@app.route('/', methods=["GET", "POST"])
def home():
    greeting = None
    if request.method == "POST":
        name = request.form.get("customer")
        message = random.choice(motivations)
        greeting = f"Good morning {name}. {message}"
    return render_template_string(html, greeting=greeting)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

