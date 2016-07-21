from os import environ
from app import app
app.run(host="0.0.0.0", port=environ.get("PORT", 5000))
