## Code Review - Issues and Fixes

### Issues Identified:

1. No SKU uniqueness check.
2. `warehouse_id` directly stored in Product (violates normalization).
3. No input validation (could crash if a key is missing).
4. Double commit increases risk of partial save.
5. Price should be stored as Decimal.
6. No error handling or rollback.

### Potential Impact in Production:

- Duplicate SKUs lead to data inconsistency.
- Products wrongly tied to a single warehouse.
- Crashes on invalid input, hurts user experience.
- Inconsistent state if first commit succeeds and second fails.

### Fixes Made:

- Added input validation and error handling.
- Used `flush()` to avoid partial commits.
- Ensured SKU uniqueness check.
- Removed `warehouse_id` from Product.
- Used Decimal for price precision.
- Returned proper status codes and error messages.
