"""Dessert classes."""


class Cupcake:
    """A cupcake."""

    cache = {}

    def __repr__(self):
      """Human-readable printout for debugging."""

      return f'<Cupcake name="{self.name}" qty={self.qty}>'

    def __init__(self, name, flavor, price):
        self.name=name
        self.flavor=flavor
        self.price=price
        
        # sets initial qty to 0
        self.qty=0
        # saves cupcake name to cache so can check if available
        self.cache[name] = self

    
    def add_stock(self,amount):
      # Add the amount to self.qty
      # When called the method will add the amount placed in the amount area to self.qty
      # += is shorthand for when the field appears on both sides of the equation
        self.qty+=amount
    
    def sell(self, amount):
      # Sell the given amount of cupcakes and update self.qty.
      # If there are 0 cupcakes available, print 'Sorry, these cupcakes are sold out' 
      # Make sure self.qty never goes below 0
      if self.qty==0:
        print('Sorry, these cupcakes are sold out')
        return

      elif self.qty<amount:
        self.qty = 0
        # print(self.qty,'is all we have. What number would you like?')
        return

        # -= is shorthand for where the field appears on both sides of the equation
      self.qty-=amount

    @staticmethod
    def scale_recipe(ingredients, amount):
     # Scale the list of ingredients by the given amount of cupcakes.
     # ingredients is a list of tuples with (ingredient_name, ingredient_qty). For example: [('flour', 1), ('eggs', 3)]
     # Return a list of tuples with the quantity for each ingredient multiplied by amount.
     # In terminal Cupcake.scale_recipe([('flour', 1), ('eggs', 3)], 2)
        return [(ingredient, qty * amount)
            for ingredient,qty in ingredients]
     
    @classmethod
    def get(cls, name):
     # Return a cupcake from cls.cache. If name doesn’t exist, print "Sorry, that cupcake doesn't exist"
        if name not in cls.cache:
            print("Sorry, that cupcake doesn't exist")
            return

        # name required
        return cls.cache[name]
    
class Brownies(Cupcake):
    
      cache = {}
      
      flavor="chocolate"

      def __init__(self, name, price, qty):
          super().__init__(name, price, qty)  
          # qty added

      def add_stock(self,amount):
          return super().add_stock()

      def sell(self, amount):
          return super().sell()

      @staticmethod
      def scale_recipe(ingredients, amount):
          return super().scale_recipe()
      
      @classmethod
      def get(cls, name):
          return super().get()
      # test cases    
      if __name__ == '__main__':
          import doctest

          result = doctest.testfile('doctests.py',
                                report=False,
                                optionflags=(
                                    doctest.REPORT_ONLY_FIRST_FAILURE
                                ))
          doctest.master.summarize(1)
          if result.failed == 0:
              print('ALL TESTS PASSED')

