from flask import Flask, render_template, request, redirect, url_for,render_template_string

app = Flask(__name__)

products = [
    {"name": "Ürün 1", "price": 10.0, "quantity": 100, "image": "static/images/urun1.jpg"},
    {"name": "Ürün 2", "price": 20.0, "quantity": 50, "image": "static/images/urun2.jpg"},
    {"name": "Ürün 3", "price": 15.0, "quantity": 75, "image": "static/images/urun3.jpg"},
    {"name": "Ürün 4", "price": 30.0, "quantity": 60, "image": "static/images/urun4.jpg"},
    {"name": "Ürün 5", "price": 25.0, "quantity": 80, "image": "static/images/urun5.jpg"},
    {"name": "Ürün 6", "price": 35.0, "quantity": 40, "image": "static/images/urun6.jpg"},
    {"name": "Ürün 7", "price": 40.0, "quantity": 30, "image": "static/images/urun7.jpg"},
    {"name": "Ürün 8", "price": 50.0, "quantity": 20, "image": "static/images/urun8.jpg"}
]

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

@app.route('/urunler', methods=['GET', 'POST'])
def urunler():
    if request.method == 'POST':
        selected_products = {}
        for key, value in request.form.get.items():
            if key.startswith('quantity_') and value != '0':
                product_name = key[len('quantity_'):]
                selected_products[product_name] = value
        return redirect(url_for('siparis', selected_products=selected_products))
    return render_template('Ürünler.html')

@app.route('/siparis', methods=['GET', 'POST'])
def siparis():
    if request.method == 'POST':
        
        return "Siparişinizi alındı"
    
    return render_template('siparis.html', products=products)

    
    selected_products = request.args.get('selected_products', {})
    if isinstance(selected_products, str):
        import json
        selected_products = json.loads(selected_products)
    return render_template('siparis.html', selected_products=selected_products)
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