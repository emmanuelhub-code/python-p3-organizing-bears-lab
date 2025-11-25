# 1. Select all female bears (name + age)
select_all_female_bears_return_name_and_age = """
SELECT name, age
FROM bears
WHERE sex = 'F';
"""

# 2. Select all bears names and ages ordered by age descending
select_all_bears_names_and_ages_ordered_by_age_desc = """
SELECT name, age
FROM bears
ORDER BY age DESC;
"""

# 3. Select the oldest bear and return name and age
select_oldest_bear_and_returns_name_and_age = """
SELECT name, age
FROM bears
ORDER BY age DESC
LIMIT 1;
"""

# 4. Select the youngest bear and return name and age
select_youngest_bear_and_returns_name_and_age = """
SELECT name, age
FROM bears
ORDER BY age ASC
LIMIT 1;
"""

# 5. Select the bear with calm temperament
select_bear_with_calm_temperament = """
SELECT *
FROM bears
WHERE temperament = 'calm';
"""

# 6. Select all bears names only, ordered alphabetically
select_all_bears_names_and_orders_in_alphabetical_order = """
SELECT name
FROM bears
ORDER BY name ASC;
"""

# 7. Select all bears that are alive (all columns)
select_all_bears_that_are_alive = """
SELECT *
FROM bears
WHERE alive = 1;
"""

# 8. Select all bears names and ages that are alive, youngest to oldest
select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
SELECT name, age
FROM bears
WHERE alive = 1
ORDER BY age ASC;
"""
