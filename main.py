from command import OrderCommand, Chef

def client_code(command):
    command.execute()

# Creamos objetos de comando para preparar una pizza y una hamburguesa
pizza_command = OrderCommand(Chef(), "Pizza")
hamburguesa_command = OrderCommand(Chef(), "Hamburguesa")

# Usamos los comandos para preparar comida
client_code(pizza_command)
client_code(hamburguesa_command)
