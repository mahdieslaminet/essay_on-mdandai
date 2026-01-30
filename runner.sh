#!/bin/bash

echo "🚀 Starting Full Stack AI Project"

# -------------------------------
# Backend
# -------------------------------
echo "🔧 Starting Backend (FastAPI)..."
cd backend || exit 1

if [ -d "venv" ]; then
  source venv/bin/activate
  echo "✅ Backend venv activated"
else
  echo "❌ backend/venv not found"
  exit 1
fi

uvicorn main:app \
  --host 0.0.0.0 \
  --port 8000 \
  --reload &

BACK_PID=$!
echo "✅ Backend running (PID=$BACK_PID)"

# -------------------------------
# Frontend
# -------------------------------
echo "🌐 Starting Frontend..."
cd ../frontend || exit 1

python3 -m http.server 3000 &

FRONT_PID=$!
echo "✅ Frontend running (PID=$FRONT_PID)"

# -------------------------------
# Wait
# -------------------------------
echo "------------------------------------"
echo "🟢 Backend  → http://localhost:8000"
echo "🟢 Frontend → http://localhost:3000"
echo "Press CTRL+C to stop everything"
echo "------------------------------------"

wait
