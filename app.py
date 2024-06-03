from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('İndex.html')

@app.route('/hakkimizda')
def hakkimizda():
    return render_template('Hakkımızda.html')

@app.route('/hizmetler')
def hizmetler():
    return render_template('Hizmetler.html')

@app.route('/iletisim', methods=["GET", "POST"])
def iletisim():
    if request.method == "POST":
        email = request.form['email']
        message = request.form['message']
        return f"Email: {email}, Message: {message}"
    return render_template('iletişim.html')

@app.route('/urunler', methods=["GET", "POST"])
def urunler():
    if request.method == "POST":
        selected_products = request.form.getlist('products')
        quantities = {product: request.form[f'quantity_{product}'] for product in selected_products}
        return render_template('siparis.html', selected_products=quantities)
    return render_template('Ürünler.html')

@app.route('/siparis', methods=["POST"])
def siparis():
    name = request.form.get('name')
    email = request.form.get('email')
    address = request.form.get('address')
    credit_card = request.form.get('credit-card')
    cvv = request.form.get('cvv')
    expiry = request.form.get('expiry')

    # Sipariş bilgilerini burada işleyebilirsiniz, veritabanına kaydedebilirsiniz vb.
    print(f"Ad Soyad: {name}")
    print(f"Email: {email}")
    print(f"Adres: {address}")
    print(f"Kredi Kartı: {credit_card}")
    print(f"CVV: {cvv}")
    print(f"Son Kullanma Tarihi: {expiry}")
    
    return "Siparişiniz alındı"

@app.route("/muayene")
def muayene():
    return render_template("muayene.html")

@app.route("/rontgen")
def rontgen():
    return render_template("romtgen.html")

@app.route("/asi")
def asiuygulamalari():
    return render_template("asiuygulamalari.html")

@app.route("/mikrop")
def mikrop():
    return render_template("mikrocip.html")

@app.route("/lab")
def lab():
    return render_template("laboratuvar.html")


if __name__ == '__main__':
    app.run(debug=True)
