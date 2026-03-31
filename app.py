import streamlit as st
from flask import Flask, request, send_file
import requests
import io

app = Flask(__name__)

API_KEY = "YOUR_CLIPDROP_API_KEY"

@app.route("/remove", methods=["POST"])
def remove_object():
    image = request.files["image"]
    mask = request.files["mask"]

    response = requests.post(
        "https://clipdrop-api.co/cleanup/v1",
        files={
            "image_file": image,
            "mask_file": mask
        },
        headers={"x-api-key": API_KEY}
    )

    return send_file(
        io.BytesIO(response.content),
        mimetype="image/png"
    )

if __name__ == "__main__":
    app.run(port=8501)