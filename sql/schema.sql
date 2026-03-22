-- Playground database schema

CREATE TABLE departments (
    id          SERIAL PRIMARY KEY,
    name        VARCHAR(100) NOT NULL UNIQUE,
    budget      NUMERIC(12, 2),
    created_at  TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE employees (
    id            SERIAL PRIMARY KEY,
    first_name    VARCHAR(50)  NOT NULL,
    last_name     VARCHAR(50)  NOT NULL,
    email         VARCHAR(150) NOT NULL UNIQUE,
    department_id INTEGER REFERENCES departments(id) ON DELETE SET NULL,
    role          VARCHAR(50)  NOT NULL DEFAULT 'employee',
    salary        NUMERIC(10, 2),
    hire_date     DATE         NOT NULL,
    active        BOOLEAN      NOT NULL DEFAULT TRUE,
    created_at    TIMESTAMP    NOT NULL DEFAULT NOW(),
    updated_at    TIMESTAMP    NOT NULL DEFAULT NOW()
);

CREATE TABLE products (
    id          SERIAL PRIMARY KEY,
    sku         VARCHAR(50)  NOT NULL UNIQUE,
    name        VARCHAR(200) NOT NULL,
    category    VARCHAR(100),
    unit_price  NUMERIC(10, 2) NOT NULL,
    stock       INTEGER NOT NULL DEFAULT 0,
    created_at  TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE orders (
    id          SERIAL PRIMARY KEY,
    employee_id INTEGER REFERENCES employees(id),
    status      VARCHAR(20) NOT NULL DEFAULT 'pending'
                CHECK (status IN ('pending', 'processing', 'shipped', 'delivered', 'cancelled')),
    total       NUMERIC(12, 2),
    notes       TEXT,
    created_at  TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at  TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE order_items (
    id          SERIAL PRIMARY KEY,
    order_id    INTEGER NOT NULL REFERENCES orders(id) ON DELETE CASCADE,
    product_id  INTEGER NOT NULL REFERENCES products(id),
    quantity    INTEGER NOT NULL CHECK (quantity > 0),
    unit_price  NUMERIC(10, 2) NOT NULL,
    UNIQUE (order_id, product_id)
);

-- Seed data
INSERT INTO departments (name, budget) VALUES
    ('Engineering', 2000000.00),
    ('Marketing',    800000.00),
    ('Sales',        600000.00),
    ('HR',           400000.00);

INSERT INTO products (sku, name, category, unit_price, stock) VALUES
    ('WGT-A', 'Widget A', 'Widgets', 20.00, 5000),
    ('WGT-B', 'Widget B', 'Widgets', 40.00, 3000),
    ('GDG-X', 'Gadget X', 'Gadgets', 50.00, 1500),
    ('GDG-Y', 'Gadget Y', 'Gadgets', 150.00, 800);
