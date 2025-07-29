CREATE TABLE companies (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE warehouses (
    id SERIAL PRIMARY KEY,
    company_id INT REFERENCES companies(id),
    name VARCHAR(255) NOT NULL
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    sku VARCHAR(100) UNIQUE NOT NULL,
    price DECIMAL(10, 2)
);

CREATE TABLE inventory (
    id SERIAL PRIMARY KEY,
    product_id INT REFERENCES products(id),
    warehouse_id INT REFERENCES warehouses(id),
    quantity INT DEFAULT 0,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE suppliers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    contact_email VARCHAR(255)
);

CREATE TABLE supplier_products (
    supplier_id INT REFERENCES suppliers(id),
    product_id INT REFERENCES products(id),
    PRIMARY KEY (supplier_id, product_id)
);

CREATE TABLE inventory_history (
    id SERIAL PRIMARY KEY,
    product_id INT,
    warehouse_id INT,
    quantity_change INT,
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE product_bundles (
    bundle_id INT REFERENCES products(id),
    component_product_id INT REFERENCES products(id),
    quantity INT,
    PRIMARY KEY (bundle_id, component_product_id)
);
