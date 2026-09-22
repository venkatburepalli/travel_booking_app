# TravelGo - Python Travel Booking App

## Folder structure

travel_booking_app/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js

## Run locally

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open http://localhost:5000

Health check:
http://localhost:5000/health

There is intentionally NO Dockerfile. Create it yourself for Docker practice.
