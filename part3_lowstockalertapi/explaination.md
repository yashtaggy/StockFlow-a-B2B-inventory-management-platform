## API Implementation - Approach & Assumptions

- Filtered inventory based on company's warehouses
- Used a 30-day window for recent sales
- Assumed daily average sales are stored per product
- Suppliers linked through a many-to-many table
- Returned projected days left based on current stock / avg sales
- Handled empty sales data using fallback of 1 unit/day
- Used SQLAlchemy for all DB operations
