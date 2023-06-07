#-------------------#
# Product Functions #
#-------------------#

products = []

def add_products(cod, desc, stock, value):
    # Adds a dict inside a list. 
    # The dict contains the new product info.
    item = {
        'code': cod,
        'desc': desc,
        'stock': stock,
        'value': value
    }

    products.append(item)

def product_query(cod):
    
    for item in products:
        if item['code'] == cod:
            return item
    return False

def modify_product(cod, desc, stock, value):
        for item in products:
            if item['code'] == cod:
                 item['desc'] = desc
                 item['stock'] = stock
                 item['value'] = value
                 return True
        return False


def list_products():
    for item in products:
        print(f'Cod: {item["code"]}\nName: {item["desc"]}')
        print(f'Stock: {item["stock"]}\nValue: {item["value"]}')
        print("-"*30)

#-------------------------#
# Shopping Cart Functions #
#-------------------------#

cart = []

def add_to_cart(cod, amount):
    
    item = product_query(cod)

    if item == False:
        print('Product not found')
        return False
     
    if amount > item['stock']:
        print('Not enough stock')
        return False
     
    for article in cart:
        if article['code'] == cod:
            article['stock'] += amount
            return True
    # Agrego item al carrito
    aux = {
        "code": cod,
        "desc"  : item["desc"],
        "stock" : amount,
        "value" : item["value"]
    }
    
    cart.append(aux)

def remove_from_cart(cod, amount):
    for item in cart:
        if item['cod'] == cod:
            if amount > item['stock']:
                print('Not enough items on cart to remove')
                return False
            item['stock'] -= amount

            if item['stock'] == 0:
                cart.remove(item)
            return True
    print('Product not found in cart')
    return False

def list_cart_items():
    total_cost = 0

    for item in cart:
        print(f'Cod: {item["code"]}\nName: {item["desc"]}')
        print(f'Stock: {item["stock"]}\nValue: {item["value"]}')
        cost = item['stock'] * item['value']
        total_cost += cost
        print(f'Item cost: ${cost}')
        print("-"*30)
    
    print(f'Total cost: ${total_cost}')
    print("="*30)



#-----------------------------#
# Adding products and testing #
#-----------------------------#

add_products(1, 'Mouse', 100, 3500)
add_products(2, 'Keyboard', 50, 3800)
add_products(3, 'Webcam', 75, 4000)
add_products(4, 'Mic', 25, 2200)

print('\n===============\n')

list_products()

print('\n===============\n')

add_to_cart(1, 3)
add_to_cart(3, 1)
add_to_cart(3, 1)
add_to_cart(2, 1)

list_cart_items()

# print('\n===============\n')

# a = product_query(3)
# if a == False:
#     print('Product not found')
# else:
#     print(a)

# print('\n===============\n')

# b = modify_product(3, 'Webcam', 66, 4700)
# if b:
#     print("Product info updated")
# else:
#     print('Product not found')

# a = product_query(3)
# if a == False:
#     print('Product not found')
# else:
#     print(a)

# print('\n===============\n')

# list_products()

print("\033[H\033[J")     # Clean screen ascii code

class Product:
    #constructor or initializer:
    def __init__(self, item_id, description, amount, price):
        self.code = item_id
        self.item = description
        self.stock = amount
        self.cost = price

    def __str__(self):
        message = f"Item code: {self.code}\n"
        message += f"Item description: {self.item}\n"
        message += f"Item amount: {self.stock} units\n"
        message += f"Item price: ${self.cost}\n"
        return message
    
    def __del__(self):
        print(f"{self.item} ha sido eliminado")

    def modificar(self, description, amount, price):
        self.item = description
        self.stock = amount