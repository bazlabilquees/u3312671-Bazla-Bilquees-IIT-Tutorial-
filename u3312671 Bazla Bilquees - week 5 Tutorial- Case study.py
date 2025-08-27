movies = {
    "Dune": 12.5,
    "Barbie": 11.0,
    "Oppenheimer": 13.0,
    "Spirited Away": 10.0
}

purchases = []  # list of (title, qty, price_each)

def apply_group_discount(qty, price_each):
    if qty >= 4:
        return price_each * 0.9  # 10% off
    return price_each

def apply_member_discount(total, is_member):
    if is_member:
        return total * 0.95  # 5% off
    return total

# 🛒 Part A — Input loop
while True:
    title = input("Enter movie title (or 'done' to finish): ")
    if title == "done":
        break
    if title not in movies:
        print("Available movies:", ", ".join(movies.keys()))
        continue
    try:
        qty = int(input(f"Enter quantity of tickets for '{title}': "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    price_each = apply_group_discount(qty, movies[title])
    purchases.append((title, qty, price_each))

# 🧾 Part B — Receipt
print("\n--- Receipt ---")
grand_total = 0
for title, qty, price_each in purchases:
    line_total = qty * price_each
    grand_total += line_total
    print(f"{title}: {qty} x ${price_each:.2f} = ${line_total:.2f}")

# Member discount
is_mmovies = {
    "Dune": 12.5,
    "Barbie": 11.0,
    "Oppenheimer": 13.0,
    "Spirited Away": 10.0
}

purchases = []  # list of (title, qty, price_each)

def apply_group_discount(qty, price_each):
    if qty >= 4:
        return price_each * 0.9  # 10% off
    return price_each

def apply_member_discount(total, is_member):
    if is_member:
        return total * 0.95  # 5% off
    return total

# 🛒 Part A — Input loop
while True:
    title = input("Enter movie title (or 'done' to finish): ")
    if title == "done":
        break
    if title not in movies:
        print("Available movies:", ", ".join(movies.keys()))
        continue
    try:
        qty = int(input(f"Enter quantity of tickets for '{title}': "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    price_each = apply_group_discount(qty, movies[title])
    purchases.append((title, qty, price_each))

# 🧾 Part B — Receipt
print("\n--- Receipt ---")
grand_total = 0
for title, qty, price_each in purchases:
    line_total = qty * price_each
    grand_total += line_total
    print(f"{title}: {qty} x ${price_each:.2f} = ${line_total:.2f}")

# Member discount
is_member = input("Do you have a member code? (yes/no): ").lower() == "yes"
grand_total = apply_member_discount(grand_total, is_member)
print(f"Grand Total: ${grand_total:.2f}")

# 📊 Part C — Sales Summary
tickets_by_movie = {}
revenue_by_movie = {}

for title, qty, price_each in purchases:
    tickets_by_movie[title] = tickets_by_movie.get(title, 0) + qty
    revenue_by_movie[title] = revenue_by_movie.get(title, 0) + qty * price_each

print("\n--- Sales Summary ---")
for title in movies:
    tickets = tickets_by_movie.get(title, 0)
    revenue = revenue_by_movie.get(title, 0.0)
    print(f"{title}: {tickets} tickets sold, ${revenue:.2f} revenue")

# 📈 Part E — Analytics
# Top-selling movie
top_title = None
top_qty = -1
for title, qty in tickets_by_movie.items():
    if qty > top_qty:
        top_title, top_qty = title, qty
print(f"\nTop Seller: {top_title} ({top_qty} tickets)")

# Sort by revenue
sorted_by_rev = sorted(revenue_by_movie.items(), key=lambda kv: kv[1], reverse=True)
print("\nMovies sorted by revenue:")
for title, rev in sorted_by_rev:
    print(f"{title}: ${rev:.2f}")

# Average tickets per purchase
total_tickets = sum(qty for _, qty, _ in purchases)
average_tickets = total_tickets / len(purchases) if purchases else 0
print(f"\nAverage tickets per purchase: {average_tickets:.2f}")
ember = input("Do you have a member code? (yes/no): ").lower() == "yes"
grand_total = apply_member_discount(grand_total, is_member)
print(f"Grand Total: ${grand_total:.2f}")

# 📊 Part C — Sales Summary
tickets_by_movie = {}
revenue_by_movie = {}

for title, qty, price_each in purchases:
    tickets_by_movie[title] = tickets_by_movie.get(title, 0) + qty
    revenue_by_movie[title] = revenue_by_movie.get(title, 0) + qty * price_each

print("\n--- Sales Summary ---")
for title in movies:
    tickets = tickets_by_movie.get(title, 0)
    revenue = revenue_by_movie.get(title, 0.0)
    print(f"{title}: {tickets} tickets sold, ${revenue:.2f} revenue")

# 📈 Part E — Analytics
# Top-selling movie
top_title = None
top_qty = -1
for title, qty in tickets_by_movie.items():
    if qty > top_qty:
        top_title, top_qty = title, qty
print(f"\nTop Seller: {top_title} ({top_qty} tickets)")

# Sort by revenue
sorted_by_rev = sorted(revenue_by_movie.items(), key=lambda kv: kv[1], reverse=True)
print("\nMovies sorted by revenue:")
for title, rev in sorted_by_rev:
    print(f"{title}: ${rev:.2f}")

# Average tickets per purchase
total_tickets = sum(qty for _, qty, _ in purchases)
average_tickets = total_tickets / len(purchases) if purchases else 0
print(f"\nAverage tickets per purchase: {average_tickets:.2f}")
