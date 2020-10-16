from common.database import Database
import sqlite3
#print(Database.find_by_name_and_job('mike', 'user'))
Database.create_table('goods')
Database.insert_value('goods', {'goodname':'beef', 'image':'beef.jpg', 'price':'250'})
Database.insert_value('goods', {'goodname':'chicken', 'image':'chicken.jpg', 'price':'250'})
Database.insert_value('goods', {'goodname':'chicken cheese', 'image':'chicken_cheese.jpg', 'price':'250'})
print((Database.get_all_data('goods')))
