from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint untuk menerima data lokasi
@app.route('/update_location', methods=['POST'])
def update_location():
    data = request.json
    phone_number = data.get("phone_number")
    latitude = data.get("latitude")
    longitude = data.get("longitude")
    
    # Menampilkan lokasi di konsol atau menyimpan ke database
    print(f"Lokasi untuk {phone_number}: Latitude {latitude}, Longitude {longitude}")
    
    # Menanggapi client dengan status berhasil
    return jsonify({"status": "success", "message": "Lokasi berhasil diperbarui"}), 200

if __name__ == "__main__":
    app.run(debug=True)
