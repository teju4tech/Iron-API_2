from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/IntoCm/<int:n>')
def inches_to_cms(n):
    I = print(f"Length in Centi_Meter:{n*2.45}")
    result = {
        "In to cm" : f"{n*2.5}",
        "Ip" : "127.23.123.82",
        "SYS" : "Linux",
        "Network" : "CLI-Light",
        "config": "Yes",
        "Mark" : "IIXI",
        "secMOT" : "BIOS LIMITER DETECTED",
        "Indus" : "Stark Industry Key Identifier"
    }

    return jsonify(result)
    return jsonify(I)

if __name__ == '__main__':
    app.run(debug=True)