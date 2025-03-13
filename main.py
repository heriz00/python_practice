class Table:
  color = "Brown"
  
  def __init__(self, name):
    self.name = name
    self.info = "Nice Table!"

my_table = Table("My Table")
info_table = Table(my_table.info)

print(my_table.name)
print(info_table.info)

