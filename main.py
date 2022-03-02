from User import User
from CuentaBancaria import CuentaBancaria

john = User("John")
mary = User("Mary")
Fabian =User("Fabian")
Cristian = User ("Cristian")
Roberto = User("Roberto")

Fabian.cuenta.hacer_deposito(5000)
# Fabian.cuenta.hacer_deposito(1000)
# Fabian.cuenta.hacer_retiro(500)
# Fabian.cuenta.mostrar_balance_usuario()


# Roberto.cuenta.hacer_deposito(500)
# Roberto.cuenta.hacer_deposito(1000)
# Roberto.cuenta.hacer_retiro(200)
# Roberto.cuenta.hacer_retiro(400)
# Roberto.cuenta.mostrar_balance_usuario()

# Cristian.cuenta.hacer_deposito(2000)
# Cristian.cuenta.hacer_retiro (100)
# Cristian.cuenta.hacer_retiro (100)
# Cristian.cuenta.hacer_retiro (100)
# Cristian.cuenta.mostrar_balance_usuario()

print("Saldo Cristian pre transaccion: ", Cristian.cuenta.balance)
Fabian.cuenta.transfer_dinero(Cristian, 2000)
# Fabian.cuenta.mostrar_balance_usuario()
# Cristian.cuenta.mostrar_balance_usuario()

print("Saldo Cristian post transaccion: ", Cristian.cuenta.balance)




# john.cuenta.hacer_deposito(1500)
# print(john.cuenta.balance)
# # john.hacer_retiro(100)

# mary.hacer_deposito(100).hacer_deposito(200)

# john.transfer_dinero(mary, 100)

# john.mostrar_balance_usuario()

# print(john.pesos)
# print(mary.pesos)

# cuenta = CuentaBancaria(8, 100)
# cuenta_2 = CuentaBancaria(10, 1000)

# cynthia = User("Cynthia")

# CuentaBancaria.imprimir_cuentas()
