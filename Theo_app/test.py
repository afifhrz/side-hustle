from sqlalchemy import create_engine

engine = create_engine("sqlite:///testdb.db")
db = engine.connect()

maxIdStudent = db.execute("""SELECT MAX(ID) AS ID FROM master_student""")

print(list(maxIdStudent)[0][0])