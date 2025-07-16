# Weekly allowance
allowance = 2000
print(f"Starting allowance: N{allowance}")

# 1. Spent N400 on books
allowance -= 400
print(f"After buying books: N{allowance}")

# 2. Found N100 under the bed
allowance += 100
print(f"After finding N100: N{allowance}")

# 3. Bought snacks worth N250
allowance -= 250
print(f"After buying snacks: N{allowance}")

# 4. Gave 25% of current allowance to younger sibling
allowance -= (25/100) * (allowance) 
print(f"After giving 25% to sibling: N{allowance:.2f}")

# 5. Used one-third of what’s left to buy data
allowance -= (1/3) * (allowance)
print(f"After buying data: N{allowance:.2f}")

# 6. Split remaining equally between savings and tithing
allowance //= 2

# 7. Remove all complete N100 notes using modulus assignment
allowance %= 100
print(f"Final remaining after removing all N100 notes: N{allowance:.1f}")

