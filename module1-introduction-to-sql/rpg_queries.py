import sqlite3


con = sqlite3.connect('rpg_db.sqlite3')

cur = con.cursor()
print('CONNECTION', cur)

qry = 'SELECT COUNT(*) FROM armory_item;'
cur.execute(qry)
result = cur.execute(qry).fetchall()
print(result)

# 1. How Many Total Character Are There?
qry1 = 'SELECT COUNT(*) FROM  charactercreator_character;'
ans1 = cur.execute(qry1).fetchone()
print(f'How Many Total Characters Are There? {ans1}')


# 2. How Many Of Each Specfic Subclass?
total_characters = cur.execute(qry).fetchone()
print('Total Characters:', total_characters[0])

qry2 = 'SELECT COUNT(DISTINCT character_ptr_id) FROM charactercreator_mage'
mage_characters = cur.execute(qry2).fetchone()
print('Total Mages:', mage_characters[0])

qry3 = 'SELECT COUNT(DISTINCT character_ptr_id) FROM charactercreator_thief'
thief_characters = cur.execute(qry3).fetchone()
print('Total Thiefs:', thief_characters[0])

qry4 = 'SELECT COUNT(DISTINCT character_ptr_id) FROM charactercreator_cleric'
cleric_characters = cur.execute(qry4).fetchone()
print('Total Clerics:', cleric_characters[0])

qry5 = 'SELECT COUNT(DISTINCT character_ptr_id) FROM charactercreator_fighter'
fighter_characters = cur.execute(qry5).fetchone()
print('Total Fighters:', fighter_characters[0])

# 3. How Many Total Items?
qry6 = 'SELECT COUNT(DISTINCT item_id) FROM armory_item'
total_items = cur.execute(qry6).fetchone()
print('Total Items:', total_items[0])

# 4. How Many Of The Items Are Weapons?
qry7 = '''
SELECT COUNT(item_ptr_id) FROM armory_item 
LEFT JOIN armory_weapon ON armory_item.item_id = armory_weapon.item_ptr_id
WHERE item_id = item_ptr_id
'''
total_weapons = cur.execute(qry7).fetchone()
print('Total Weapons:', total_weapons[0])

# 5. How Many Are Not?
qry8 = '''
SELECT COUNT(DISTINCT item_id)
FROM armory_item
LEFT JOIN armory_weapon ON armory_item.item_id = armory_weapon.item_ptr_id
WHERE item_id < 138
'''
total_non_weapon_items = cur.execute(qry8).fetchone()
print('Total Non-Weapons:', total_non_weapon_items[0])

qry9 = '''
SELECT character_id, COUNT(item_id) AS n_items
FROM charactercreator_character_inventory AS inventory
GROUP BY inventory.character_id
LIMIT 20
'''
character_items = cur.execute(qry9).fetchall
print(character_items)