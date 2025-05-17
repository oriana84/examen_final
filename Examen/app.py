from flask import Flask, render_template, request

app = Flask(__name__)

# Usuarios registrados
usuarios = {
    'juan': {'password': 'admin', 'rol': 'Administrador'},
    'pepe': {'password': 'user', 'rol': 'Usuario'}
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])
        precio_unitario = 9000
        total_sin_descuento = cantidad * precio_unitario

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0.0

        monto_descuento = total_sin_descuento * descuento
        total_con_descuento = total_sin_descuento - monto_descuento

        resultado = {
            'nombre': nombre,
            'total_sin_descuento': total_sin_descuento,
            'monto_descuento': monto_descuento,
            'total_con_descuento': total_con_descuento
        }

    return render_template('ejercicio1.html', resultado=resultado)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        if usuario in usuarios and usuarios[usuario]['password'] == contrasena:
            rol = usuarios[usuario]['rol']
            mensaje = f"Bienvenido {rol.lower()} {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
