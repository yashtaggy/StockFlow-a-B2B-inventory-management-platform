from flask import Flask, jsonify
from datetime import datetime, timedelta
from models import db, Product, Inventory, Warehouse, Supplier, SupplierProduct, ProductThreshold, Sale

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
db.init_app(app)

@app.route('/api/companies/<int:company_id>/alerts/low-stock', methods=['GET'])
def low_stock_alerts(company_id):
    alerts = []
    warehouses = Warehouse.query.filter_by(company_id=company_id).all()
    warehouse_ids = [w.id for w in warehouses]

    recent_sales = db.session.query(Sale.product_id).filter(
        Sale.sale_date >= datetime.utcnow() - timedelta(days=30)
    ).distinct()

    query = db.session.query(
        Inventory,
        Product,
        Warehouse,
        ProductThreshold,
        Supplier
    ).join(Product).join(Warehouse).join(ProductThreshold).join(SupplierProduct).join(Supplier).filter(
        Inventory.warehouse_id.in_(warehouse_ids),
        Inventory.quantity < ProductThreshold.threshold,
        Product.id.in_(recent_sales)
    )

    for inv, prod, wh, threshold, supplier in query:
        days_until_stockout = int(inv.quantity / (threshold.daily_avg_sales or 1))
        alerts.append({
            "product_id": prod.id,
            "product_name": prod.name,
            "sku": prod.sku,
            "warehouse_id": wh.id,
            "warehouse_name": wh.name,
            "current_stock": inv.quantity,
            "threshold": threshold.threshold,
            "days_until_stockout": days_until_stockout,
            "supplier": {
                "id": supplier.id,
                "name": supplier.name,
                "contact_email": supplier.contact_email
            }
        })

    return jsonify({
        "alerts": alerts,
        "total_alerts": len(alerts)
    })
