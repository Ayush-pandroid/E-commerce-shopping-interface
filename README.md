# 🛍️ Product Store — Desktop Catalog App

A simple desktop shopping catalog app built with **Python** and **Tkinter**. Browse 50 products across 10 categories, filter and search, add items to a cart, check out, and review past orders — all in a single-file, beginner-friendly script.

## Overview

Product Store simulates a small e-commerce storefront as a native desktop GUI. It's built using only introductory Python concepts — variables, loops, conditionals, functions, lists, tuples, and dictionaries — with no external dependencies, no classes, and no persistent storage. All data (cart, orders, stock levels) lives in memory for the duration of the program and resets on restart.

## Features

- 🗂️ **10 product categories** with 50 total products, each with a name, price, stock level, and an emoji "image"
- 🔍 **Live search** by product name or category (updates as you type)
- 🎚️ **Category filter** and **max price slider** to narrow down results
- 🧾 **Product grid** with scrollable cards showing price, stock, and an "Add to Cart" button
- ⚠️ **Low-stock and out-of-stock indicators**, with the Add to Cart button disabled when a product is unavailable
- 🛒 **Shopping cart window** — view items, quantities, and subtotals; remove one unit at a time or clear the whole cart
- ✅ **Checkout flow** with a confirmation dialog that reduces stock and records the order
- 📜 **Order history window** listing all past orders (most recent first) with a running grand total
- 🖱️ Mouse-wheel scrolling support (Windows, macOS, and Linux)

## Technologies / Tools Used

- **Python 3** (standard library only)
- **Tkinter** — GUI framework (including the `ttk` themed widgets and `messagebox`)
- **datetime** — timestamps for order history

No third-party packages or internet access are required.

## Installation & Setup

**Requirements:** Python 3.8+ (Tkinter comes bundled with it — no extra installs needed).

1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/<your-repo>.git
   cd <your-repo>
   ```

2. Run the app:
   ```bash
   python product_store_simple.py
   ```

That's it — a window titled **"Product Store"** will open with the catalog.

> If `tkinter` is missing (mainly on Linux), install it with `sudo apt-get install python3-tk` (Debian/Ubuntu) or `sudo dnf install python3-tkinter` (Fedora).

## How to Use

1. Use the **search box**, **category dropdown**, or **max price slider** in the left sidebar to filter products.
2. Click **Add to Cart** on any product card to add it to your cart.
3. Click **🛒 Cart** in the top-right to open the cart window, where you can:
   - Remove one unit of a selected item
   - Clear the entire cart
   - Checkout (confirms the total and places the order)
4. Click **📜 Previous Orders** to view your order history and total amount spent.
5. Click **Reset filters** in the sidebar to clear search/category/price filters.

## Testing Instructions

This project does not include an automated test suite — it's a small GUI script meant for manual, interactive testing. To verify functionality:

1. **Launch the app** and confirm all 50 products render correctly across 10 categories.
2. **Search test:** Type a partial product or category name (e.g., `"shoe"`) and confirm the grid updates live and the result count is accurate.
3. **Filter test:** Select a category from the dropdown and confirm only matching products appear; drag the price slider and confirm products above that price disappear.
4. **Reset test:** Click **Reset filters** and confirm search text, category, and price slider return to defaults.
5. **Cart test:**
   - Add a product to the cart and confirm the cart button count increases.
   - Open the cart window and confirm the item, price, quantity, and subtotal are correct.
   - Remove one unit and confirm the quantity/subtotal update (and the row disappears at 0).
   - Clear the cart and confirm it empties.
6. **Stock test:** Add enough of the same item to exhaust its stock and confirm the card shows "Out of stock" and disables the **Add to Cart** button.
7. **Checkout test:** Add items, checkout, confirm the dialog, and verify:
   - The cart empties afterward
   - Stock levels decrease by the purchased quantity
   - A confirmation message shows the correct total
8. **Order history test:** Open **Previous Orders** after checking out and confirm the order appears at the top with the correct date, item list, and total, and that the grand total updates correctly across multiple orders.

## Screenshots

_Add screenshots here to showcase the UI, e.g.:_

```markdown
![Main catalog view](screenshots/catalog.png)
![Cart window](screenshots/cart.png)
![Order history](screenshots/order-history.png)
```

## Project Structure

```
.
├── product_store_simple.py   # Main application (single-file)
└── README.md                 # This file
```

## Notes & Limitations

- All data (products, cart, stock, order history) is **in-memory only** and resets when the program closes.
- No image files or network calls are used — product "pictures" are emoji for simplicity.
- Built intentionally with beginner-level Python constructs (no classes, no external libraries) for educational purposes.
