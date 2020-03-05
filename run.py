from flask import Flask

app = Flask(__name__)

import Capa_Aplicacion.VentaServices as ventas
import Capa_Aplicacion.FacturaServices as facturas
import Capa_Aplicacion.ProductoServices as productos

app.register_blueprint(ventas.blueprint)
app.register_blueprint(facturas.blueprint)
app.register_blueprint(productos.blueprint)

if __name__ == '__main__':
    app.run(debug=True)
