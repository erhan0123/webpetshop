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

@app.route('/urunler', methods=['GET', 'POST'])
def urunler():
    if request.method == 'POST':
        selected_products = {}
        for key, value in request.form.items():
            if key.startswith('quantity_') and value != '0':
                product_name = key[len('quantity_'):]
                selected_products[product_name] = value
        return redirect(url_for('siparis', selected_products=selected_products))
    return render_template('Ürünler.html')

@app.route('/siparis', methods=['GET', 'POST'])
def siparis():
    if request.method == 'POST':
        # Process the order form submission
        name = request.form['name']
        email = request.form['email']
        address = request.form['address']
        credit_card = request.form['credit-card']
        cvv = request.form['cvv']
        expiry = request.form['expiry']
        # Here you would typically save the order to a database or send it via email
        return "Siparişiniz alındı! Teşekkür ederiz."
    
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