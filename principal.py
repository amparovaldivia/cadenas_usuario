from usuario import Usuario

usuario_uno=Usuario("Juan","juan@gmail.com",1000)
usuario_dos=Usuario("Luisa","luisa@gmail.com",20000)
usuario_tres=Usuario("Lila","lila@gmail.com",34000)

usuario_uno.hacer_deposito(50000).hacer_deposito(70000).hacer_deposito(100000).hacer_retiro(20000).mostrar_balance_usuario()

usuario_dos.hacer_deposito(150000).hacer_deposito(81533).hacer_retiro(22000).mostrar_balance_usuario()

usuario_tres.hacer_deposito(500500).hacer_retiro(35000).hacer_retiro(15000).hacer_retiro(120000).mostrar_balance_usuario().transfer_dinero(usuario_dos,15000).mostrar_balance_usuario()


