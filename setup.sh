#!/bin/bash

echo "🔧 Setting up virtual environment..."
python3 -m venv .venv
source .venv/bin/activate

echo "📦 Installing requirements..."
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ Setup complete. Activate with: source .venv/bin/activate"
