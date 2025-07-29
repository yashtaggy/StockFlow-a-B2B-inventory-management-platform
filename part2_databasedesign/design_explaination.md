## Database Design Justifications

- **SKU uniqueness**: Enforced at DB level for integrity.
- **Normalization**: Product and inventory separated for multi-warehouse setup.
- **Bundle support**: Self-referencing many-to-many structure for products.
- **Supplier relation**: Separate mapping table to support many-to-many.
- **Inventory history**: Enables audit trail of changes.
- **Constraints**: Foreign keys used to prevent orphan records.
- **Indexing**: Implicit on PKs; indexing `sku`, `product_id` on joins is recommended.
