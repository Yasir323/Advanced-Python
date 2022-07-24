# Sample code from the documentation of the asyncpg
# PostgreSQL driver.

import asyncpg

connection = await asyncpg.connect('postgresql://postgres@localhost/test')
tr = connection.transaction()

await tr.start()
try:
    await connection.execute("INSERT INTO mytable VALUES (1, 2, 3)")
except:
    await tr.rollback()
    raise
else:
    await tr.commit()

# This can be replaced by
async with connection.transaction():
    await connection.execute("INSERT INTO mytable VALUES (1, 2, 3)")
