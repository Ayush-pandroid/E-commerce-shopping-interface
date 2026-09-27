"""
Product Store - a simple Tkinter desktop app.

This version only uses ideas from an introductory Python course:
variables, if/else, for/while loops, functions, lists, tuples and
dictionaries. There are no classes, no threading, no image
downloading, and no file saving - everything is kept simple and
lives only while the program is running.

Run:  python product_store_simple.py
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# ---------------------------------------------------------------------
# DATA
# ---------------------------------------------------------------------
# Each category holds a list of tuples: (name, price, stock)
CATALOG = {
    "Electronics": [
        ("Wireless Headphones", 79.99, 15), ("Mechanical Keyboard", 119.99, 10),
        ("Ergonomic Mouse", 45.50, 20), ("4K Ultra Monitor", 299.99, 8),
        ("Bluetooth Speaker", 35.00, 30)],
    "Footwear": [
        ("Running Shoes", 59.99, 25), ("Leather Loafers", 89.99, 12),
        ("Hiking Boots", 110.00, 10), ("Casual Sneakers", 49.50, 18),
        ("Flip Flops", 15.00, 50)],
    "Apparel": [
        ("Cotton T-Shirt", 19.99, 40), ("Denim Jeans", 49.99, 22),
        ("Hooded Sweatshirt", 39.99, 15), ("Formal Blazer", 129.99, 7),
        ("Winter Jacket", 99.50, 11)],
    "Home & Kitchen": [
        ("Air Fryer", 89.99, 14), ("Coffee Maker", 65.00, 18),
        ("Stainless Steel Cookware", 149.99, 9), ("Blender Smoothiemaker", 39.99, 25),
        ("Electric Kettle", 24.99, 35)],
    "Fitness & Sports": [
        ("Yoga Mat", 22.50, 30), ("Dumbbell Set 10lbs", 45.00, 16),
        ("Resistance Bands", 14.99, 40), ("Basketball", 29.99, 20),
        ("Smart Fitness Band", 49.99, 22)],
    "Books & Stationery": [
        ("Python Programming Guide", 34.99, 25), ("Hardcover Notebook", 12.99, 50),
        ("Fountain Pen Set", 25.00, 15), ("Desk Organizer", 18.50, 20),
        ("Sci-Fi Novel", 14.99, 30)],
    "Beauty & Personal Care": [
        ("Hydrating Face Cream", 28.00, 24), ("Electric Toothbrush", 42.99, 19),
        ("Sulfate-Free Shampoo", 16.50, 35), ("Sunscreen SPF 50", 19.00, 40),
        ("Beard Grooming Kit", 32.50, 12)],
    "Toys & Games": [
        ("Building Blocks Set", 39.99, 18), ("Board Game - Strategy", 29.99, 14),
        ("Remote Control Car", 49.50, 10), ("Jigsaw Puzzle 1000pcs", 18.00, 22),
        ("Plush Teddy Bear", 15.99, 28)],
    "Automotive Accessories": [
        ("Car Phone Mount", 12.99, 45), ("Portable Air Compressor", 39.99, 15),
        ("Car Vacuum Cleaner", 29.99, 20), ("Dash Cam 1080p", 69.99, 8),
        ("Microfiber Cleaning Cloths", 9.99, 60)],
    "Travel & Luggage": [
        ("Travel Backpack 40L", 64.99, 16), ("Hard Shell Suitcase", 119.99, 7),
        ("Neck Pillow Memory Foam", 19.99, 35), ("Packing Cubes Set", 22.50, 25),
        ("Universal Travel Adapter", 17.99, 30)],
}

# One background colour per category, used behind the emoji "picture"
CATEGORY_COLORS = {
    "Electronics": "#4f86c6", "Footwear": "#c67b4f", "Apparel": "#8e6bbf",
    "Home & Kitchen": "#4fa88b", "Fitness & Sports": "#d0a03c",
    "Books & Stationery": "#6b7fbf", "Beauty & Personal Care": "#d0728f",
    "Toys & Games": "#e0793c", "Automotive Accessories": "#6f7b85",
    "Travel & Luggage": "#3f9ab0",
}

# One emoji "picture" per product name (keeps things simple - no real images)
ITEM_EMOJI = {
    "Wireless Headphones": "🎧", "Mechanical Keyboard": "⌨️", "Ergonomic Mouse": "🖱️",
    "4K Ultra Monitor": "🖥️", "Bluetooth Speaker": "🔊", "Running Shoes": "👟",
    "Leather Loafers": "👞", "Hiking Boots": "🥾", "Casual Sneakers": "👟",
    "Flip Flops": "🩴", "Cotton T-Shirt": "👕", "Denim Jeans": "👖",
    "Hooded Sweatshirt": "🧥", "Formal Blazer": "🤵", "Winter Jacket": "🧥",
    "Air Fryer": "🍟", "Coffee Maker": "☕", "Stainless Steel Cookware": "🍳",
    "Blender Smoothiemaker": "🥤", "Electric Kettle": "🫖", "Yoga Mat": "🧘",
    "Dumbbell Set 10lbs": "🏋️", "Resistance Bands": "💪", "Basketball": "🏀",
    "Smart Fitness Band": "⌚", "Python Programming Guide": "📘",
    "Hardcover Notebook": "📓", "Fountain Pen Set": "🖋️", "Desk Organizer": "🗂️",
    "Sci-Fi Novel": "🚀", "Hydrating Face Cream": "🧴", "Electric Toothbrush": "🪥",
    "Sulfate-Free Shampoo": "🧴", "Sunscreen SPF 50": "☀️", "Beard Grooming Kit": "🧔",
    "Building Blocks Set": "🧱", "Board Game - Strategy": "🎲",
    "Remote Control Car": "🚗", "Jigsaw Puzzle 1000pcs": "🧩", "Plush Teddy Bear": "🧸",
    "Car Phone Mount": "📱", "Portable Air Compressor": "💨", "Car Vacuum Cleaner": "🧹",
    "Dash Cam 1080p": "📹", "Microfiber Cleaning Cloths": "🧽",
    "Travel Backpack 40L": "🎒", "Hard Shell Suitcase": "🧳",
    "Neck Pillow Memory Foam": "😴", "Packing Cubes Set": "📦",
    "Universal Travel Adapter": "🔌",
}

LOW_STOCK = 10        # stock at or below this shows a low-stock warning
CARD_WIDTH = 220       # width in pixels of one product card
COLUMNS = 4            # fixed number of cards per row

# Build the "products" dictionary once, using simple loops.
# Key = product id (101, 102, 103, ...), value = a dictionary of details.
products = {}
next_id = 101
for category in CATALOG:
    item_list = CATALOG[category]
    for name, price, stock in item_list:
        products[next_id] = {
            "name": name,
            "category": category,
            "price": price,
            "stock": stock,
            "emoji": ITEM_EMOJI[name],
        }
        next_id = next_id + 1

max_price = 0
for pid in products:
    if products[pid]["price"] > max_price:
        max_price = products[pid]["price"]

# cart: product id -> quantity chosen
cart = {}

# order_history: a list of dictionaries, one per completed order.
# (kept only in memory - it resets each time the program is run)
order_history = []

# Windows that may or may not be open right now
cart_window = None
cart_tree = None
cart_total_label = None


# ---------------------------------------------------------------------
# HELPER FUNCTIONS (cart / stock logic)
# ---------------------------------------------------------------------
def available_stock(pid):
    """How many units of a product are still free to add to the cart."""
    in_cart = 0
    if pid in cart:
        in_cart = cart[pid]
    return products[pid]["stock"] - in_cart


def filtered_product_ids():
    """Return the list of product ids that match the search box,
    the chosen category and the price slider."""
    query = search_var.get().strip().lower()
    category = category_var.get()
    price_limit = price_var.get()

    result = []
    for pid in products:
        item = products[pid]
        name_match = query in item["name"].lower()
        category_text_match = query in item["category"].lower()
        matches_search = name_match or category_text_match

        if category == "All":
            matches_category = True
        else:
            matches_category = item["category"] == category

        matches_price = item["price"] <= price_limit

        if matches_search and matches_category and matches_price:
            result.append(pid)
    return result


# ---------------------------------------------------------------------
# BUILDING THE PRODUCT GRID
# ---------------------------------------------------------------------
def make_add_to_cart_handler(pid):
    """Build a small function that adds ONE specific product (pid) to the
    cart. Each 'Add to Cart' button gets its own handler this way, so we
    do not need a lambda to remember which product the button belongs to."""
    def handler():
        add_to_cart(pid)
    return handler


def build_card(parent, pid, row, col):
    """Create one product card and place it in the grid."""
    item = products[pid]
    color = CATEGORY_COLORS[item["category"]]

    card = tk.Frame(parent, bd=1, relief="solid", padx=8, pady=8, width=CARD_WIDTH)
    card.grid(row=row, column=col, padx=8, pady=8, sticky="n")

    picture = tk.Label(card, text=item["emoji"], bg=color, fg="white",
                        font=("Segoe UI Emoji", 32), width=9, height=4)
    picture.pack()

    tk.Label(card, text=item["name"], font=("Segoe UI", 11, "bold"),
             wraplength=CARD_WIDTH - 20).pack(anchor="w", pady=(6, 0))
    tk.Label(card, text="Category: " + item["category"] + "  |  ID #" + str(pid)
              ).pack(anchor="w")
    tk.Label(card, text="Price: $" + format(item["price"], ".2f"),
             fg="#1a8f3c", font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=2)

    left = available_stock(pid)
    if left <= 0:
        stock_text = "Out of stock"
    elif left <= LOW_STOCK:
        stock_text = "Only " + str(left) + " left!"
    else:
        stock_text = "In stock: " + str(left)
    tk.Label(card, text=stock_text).pack(anchor="w")

    # make_add_to_cart_handler(pid) below builds a small function that
    # remembers THIS card's own product id, so each button adds the
    # right product (instead of every button using the same id).
    add_button = tk.Button(card, text="Add to Cart", command=make_add_to_cart_handler(pid))
    if left <= 0:
        add_button.config(state="disabled")
    add_button.pack(anchor="w", pady=(6, 0))


def refresh_grid():
    """Clear the product grid and rebuild it from scratch. Simple, and
    always shows the correct stock numbers and filtered results."""
    for widget in grid_frame.winfo_children():
        widget.destroy()

    visible_ids = filtered_product_ids()
    count_label.config(text="Showing Results (" + str(len(visible_ids)) + ")")

    if len(visible_ids) == 0:
        tk.Label(grid_frame, text="No products match your search or filter criteria.",
                 padx=20, pady=20).grid(row=0, column=0)
        return

    row = 0
    col = 0
    for pid in visible_ids:
        build_card(grid_frame, pid, row, col)
        col = col + 1
        if col == COLUMNS:
            col = 0
            row = row + 1

    canvas.yview_moveto(0)


def reset_filters():
    search_var.set("")
    category_var.set("All")
    price_var.set(max_price)
    refresh_grid()


# ---------------------------------------------------------------------
# CART ACTIONS
# ---------------------------------------------------------------------
def update_cart_button_text():
    total_items = 0
    for pid in cart:
        total_items = total_items + cart[pid]
    cart_button.config(text="Cart (" + str(total_items) + ")")


def add_to_cart(pid):
    if available_stock(pid) <= 0:
        return
    if pid in cart:
        cart[pid] = cart[pid] + 1
    else:
        cart[pid] = 1
    update_cart_button_text()
    refresh_grid()
    refresh_cart_window()


def remove_from_cart(pid):
    if pid in cart:
        cart[pid] = cart[pid] - 1
        if cart[pid] <= 0:
            del cart[pid]
    update_cart_button_text()
    refresh_grid()
    refresh_cart_window()


def clear_cart():
    cart.clear()
    update_cart_button_text()
    refresh_grid()
    refresh_cart_window()


def remove_selected_from_cart():
    selection = cart_tree.selection()
    if len(selection) > 0:
        pid = int(selection[0])
        remove_from_cart(pid)


def refresh_cart_window():
    """Redraw the cart window's table and total, if that window is open."""
    if cart_window is None or not cart_window.winfo_exists():
        return

    for row_id in cart_tree.get_children():
        cart_tree.delete(row_id)

    total = 0.0
    for pid in cart:
        qty = cart[pid]
        item = products[pid]
        subtotal = item["price"] * qty
        total = total + subtotal
        cart_tree.insert("", "end", iid=str(pid),
                          values=(item["name"], "$" + format(item["price"], ".2f"),
                                  qty, "$" + format(subtotal, ".2f")))

    cart_total_label.config(text="Total: $" + format(total, ".2f"))


def open_cart():
    global cart_window, cart_tree, cart_total_label

    if cart_window is not None and cart_window.winfo_exists():
        cart_window.lift()
        return

    cart_window = tk.Toplevel(root)
    cart_window.title("Your Cart")
    cart_window.geometry("560x380")

    columns = ("name", "price", "qty", "subtotal")
    cart_tree = ttk.Treeview(cart_window, columns=columns, show="headings")
    cart_tree.heading("name", text="Product")
    cart_tree.heading("price", text="Price")
    cart_tree.heading("qty", text="Qty")
    cart_tree.heading("subtotal", text="Subtotal")
    cart_tree.column("name", width=230)
    cart_tree.column("price", width=80, anchor="e")
    cart_tree.column("qty", width=50, anchor="e")
    cart_tree.column("subtotal", width=90, anchor="e")
    cart_tree.pack(fill="both", expand=True, padx=10, pady=10)

    cart_total_label = tk.Label(cart_window, font=("Segoe UI", 12, "bold"))
    cart_total_label.pack(anchor="e", padx=10)

    button_row = tk.Frame(cart_window, padx=10, pady=10)
    button_row.pack(fill="x")
    tk.Button(button_row, text="Remove 1", command=remove_selected_from_cart).pack(side="left")
    tk.Button(button_row, text="Clear", command=clear_cart).pack(side="left", padx=6)
    tk.Button(button_row, text="Checkout", command=checkout).pack(side="right")

    refresh_cart_window()


def checkout():
    if len(cart) == 0:
        return

    total = 0.0
    for pid in cart:
        total = total + products[pid]["price"] * cart[pid]

    confirmed = messagebox.askyesno("Checkout", "Place order for $" + format(total, ".2f") + "?",
                                     parent=cart_window)
    if not confirmed:
        return

    # Build the list of items for this order
    order_items = []
    for pid in cart:
        qty = cart[pid]
        item = products[pid]
        order_items.append({
            "name": item["name"],
            "price": item["price"],
            "quantity": qty,
            "subtotal": round(item["price"] * qty, 2),
        })

    order_history.append({
        "date": datetime.now().strftime("%d-%m-%Y %I:%M %p"),
        "items": order_items,
        "total": round(total, 2),
    })

    # Reduce stock for each item that was bought
    for pid in cart:
        products[pid]["stock"] = products[pid]["stock"] - cart[pid]

    cart.clear()
    update_cart_button_text()
    refresh_grid()
    refresh_cart_window()
    messagebox.showinfo("Order placed", "Thank you! Total charged: $" + format(total, ".2f"),
                         parent=cart_window)


# ---------------------------------------------------------------------
# ORDER HISTORY WINDOW
# ---------------------------------------------------------------------
def open_order_history():
    win = tk.Toplevel(root)
    win.title("Previous Orders")
    win.geometry("650x480")

    tk.Label(win, text="Previous Orders", font=("Segoe UI", 16, "bold")
              ).pack(anchor="w", padx=12, pady=(12, 4))

    if len(order_history) == 0:
        tk.Label(win, text="No previous orders yet.", padx=20, pady=20).pack()
        return

    columns = ("date", "items", "total")
    tree = ttk.Treeview(win, columns=columns, show="headings")
    tree.heading("date", text="Order Date")
    tree.heading("items", text="Items")
    tree.heading("total", text="Order Total")
    tree.column("date", width=170)
    tree.column("items", width=290)
    tree.column("total", width=110, anchor="e")
    tree.pack(fill="both", expand=True, padx=10, pady=10)

    grand_total = 0.0
    # show most recent order first
    index = len(order_history) - 1
    while index >= 0:
        order = order_history[index]
        item_text = ""
        for order_item in order["items"]:
            item_text = item_text + order_item["name"] + " x" + str(order_item["quantity"]) + ", "
        item_text = item_text.rstrip(", ")

        grand_total = grand_total + order["total"]
        tree.insert("", "end", values=(order["date"], item_text,
                                        "$" + format(order["total"], ".2f")))
        index = index - 1

    tk.Label(win, text="Total Spent on Previous Orders: $" + format(grand_total, ".2f"),
             font=("Segoe UI", 12, "bold")).pack(anchor="e", padx=12, pady=(0, 12))


# ---------------------------------------------------------------------
# SCROLLING SUPPORT FOR THE PRODUCT GRID
# ---------------------------------------------------------------------
def on_grid_frame_resize(event):
    canvas.configure(scrollregion=canvas.bbox("all"))


def on_mouse_wheel(event):
    if event.delta > 0:
        canvas.yview_scroll(-2, "units")
    else:
        canvas.yview_scroll(2, "units")


def on_scroll_up(event):
    canvas.yview_scroll(-2, "units")


def on_scroll_down(event):
    canvas.yview_scroll(2, "units")


def on_search_key_release(event):
    refresh_grid()


def on_category_selected(event):
    refresh_grid()


# ---------------------------------------------------------------------
# BUILD THE MAIN WINDOW
# ---------------------------------------------------------------------
root = tk.Tk()
root.title("Product Store")
root.geometry("1150x720")
root.minsize(700, 500)

search_var = tk.StringVar()
category_var = tk.StringVar(value="All")
price_var = tk.DoubleVar(value=max_price)

# ---- header ----
header = tk.Frame(root, padx=14, pady=10)
header.pack(fill="x")
tk.Label(header, text="🛍️ Modern Product Catalog", font=("Segoe UI", 18, "bold")).pack(side="left")
history_button = tk.Button(header, text="📜 Previous Orders", command=open_order_history)
history_button.pack(side="right", padx=(0, 6))
cart_button = tk.Button(header, text="🛒 Cart (0)", command=open_cart)
cart_button.pack(side="right")

tk.Label(root, text="Browse, filter, and search across 50 products in 10 categories.",
         padx=14).pack(anchor="w")
ttk.Separator(root).pack(fill="x", pady=8)

# ---- body: sidebar + product grid ----
body = tk.Frame(root)
body.pack(fill="both", expand=True)

sidebar = tk.Frame(body, padx=14, pady=14)
sidebar.pack(side="left", fill="y")

tk.Label(sidebar, text="🔍 Search & Filters", font=("Segoe UI", 12, "bold")
          ).pack(anchor="w", pady=(0, 10))

tk.Label(sidebar, text="Search products").pack(anchor="w")
search_entry = tk.Entry(sidebar, textvariable=search_var, width=26)
search_entry.pack(anchor="w", pady=(2, 12))
search_entry.bind("<KeyRelease>", on_search_key_release)

tk.Label(sidebar, text="Category").pack(anchor="w")
category_names = ["All"]
for name in sorted(CATALOG):
    category_names.append(name)
category_box = ttk.Combobox(sidebar, textvariable=category_var, values=category_names,
                             state="readonly", width=24)
category_box.pack(anchor="w", pady=(2, 12))
category_box.bind("<<ComboboxSelected>>", on_category_selected)

price_label = tk.Label(sidebar, text="Max Price: $" + format(max_price, ".2f"))
price_label.pack(anchor="w")


def on_price_change(value):
    price_label.config(text="Max Price: $" + format(price_var.get(), ".2f"))
    refresh_grid()


price_scale = ttk.Scale(sidebar, from_=0, to=max_price, variable=price_var,
                         command=on_price_change, length=190)
price_scale.pack(anchor="w", pady=2)

tk.Button(sidebar, text="Reset filters", command=reset_filters).pack(anchor="w", pady=16)

ttk.Separator(body, orient="vertical").pack(side="left", fill="y")

main_area = tk.Frame(body)
main_area.pack(side="left", fill="both", expand=True)

count_label = tk.Label(main_area, font=("Segoe UI", 13, "bold"), padx=14, pady=8)
count_label.pack(anchor="w")

canvas_wrap = tk.Frame(main_area)
canvas_wrap.pack(fill="both", expand=True)

canvas = tk.Canvas(canvas_wrap, highlightthickness=0)
scrollbar = ttk.Scrollbar(canvas_wrap, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

grid_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=grid_frame, anchor="nw")
grid_frame.bind("<Configure>", on_grid_frame_resize)

# mouse wheel scrolling (Windows/macOS uses <MouseWheel>, Linux uses Button-4/5)
root.bind_all("<MouseWheel>", on_mouse_wheel)
root.bind_all("<Button-4>", on_scroll_up)
root.bind_all("<Button-5>", on_scroll_down)

# draw the product cards for the first time
refresh_grid()

root.mainloop()
