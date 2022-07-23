import item from Item

class Phone(Item):
  def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
    #call to super function to have acess to all attributes/methods from parent Class
    super().__init__(
      name, price, quantity
    )
    # run validations to the received arguments
    assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equal to zero!"

    # Assign to self objects
    self.broken_phones = broken_phones

phone1 = Phone("iPhone 13", 700, 10)
