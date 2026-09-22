from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

destinations = [
    {"id": 1, "name": "Goa", "location": "India", "price": 4999, "days": "3 Days / 2 Nights",
     "image": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=900&q=80"},
    {"id": 2, "name": "Manali", "location": "Himachal Pradesh, India", "price": 6999, "days": "4 Days / 3 Nights",
     "image": "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=900&q=80"},
    {"id": 3, "name": "Dubai", "location": "UAE", "price": 24999, "days": "5 Days / 4 Nights",
     "image": "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?auto=format&fit=crop&w=900&q=80"},
    {"id": 4, "name": "Bali", "location": "Indonesia", "price": 29999, "days": "6 Days / 5 Nights",
     "image": "https://images.unsplash.com/photo-1537996194471-e657df975ab4?auto=format&fit=crop&w=900&q=80"}
]

@app.route("/")
def home():
    return render_template("index.html", destinations=destinations)

@app.route("/api/destinations")
def api_destinations():
    return jsonify(destinations)

@app.route("/book", methods=["POST"])
def book():
    data = request.form
    name = data.get("name", "").strip()
    email = data.get("email", "").strip()
    destination = data.get("destination", "").strip()
    travel_date = data.get("travel_date", "").strip()
    travelers = data.get("travelers", "1").strip()

    if not name or not email or not destination or not travel_date:
        return jsonify({"success": False, "message": "Please fill all required fields."}), 400

    booking_id = "TRV" + str(abs(hash(
        f"{name}{email}{destination}{travel_date}{travelers}"
    )))[:8]

    return jsonify({
        "success": True,
        "booking_id": booking_id,
        "message": f"Booking request received for {destination}."
    })

@app.route("/health")
def health():
    return jsonify({"status": "UP", "application": "Travel Booking App"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
