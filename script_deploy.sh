#!/bin/bash
git clone https://github.com/mrykse/MLP_webhook_ngrock.git
git pull origin main
pip install -r requirements.txt
python app.py
