# Python - Exceptions

This directory covers safe data handling, error prevention, and structural control flow using exception handling concepts (`try`, `except`, `else`, `finally`) without relying on standard built-in functions like `len()`.

## Files Reference
* **0-safe_print_list.py**: Function that safely prints a specific number of elements from a list regardless of its structural size boundaries.
* **1-safe_print_integer.py**: Function that safely prints an integer using string formatting and handles conversion exceptions cleanly.
* **2-safe_print_list_integers.py**: Function that prints only the integers from a mixed-type list up to index x, allowing indexing exceptions to bubble up.
* **3-safe_print_division.py**: Function that divides two integers and handles structural print states within a `finally` block framework.
* **4-list_division.py**: Function that divides elements between two separate lists sequentially with multi-exception handling fallbacks.
* **5-raise_exception.py**: Function that explicitly raises a standard `TypeError` exception.
* **6-raise_exception_msg.py**: Function that explicitly raises a `NameError` containing a custom text message string.
