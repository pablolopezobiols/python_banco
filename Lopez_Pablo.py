import time
# =========================================
# CONSTANTES
# =========================================


PIN_CORRECTO = "1234"
INTENTOS_MAXIMOS = 3
SALDO_INICIAL = 50000

OPCION_DEPOSITAR = 1
OPCION_EXTRAER = 2
OPCION_SALIR = 3

INTENTOS_CONEXION = 3
PAUSA_CONEXION = 1


# =========================================
# FUNCIONES
# =========================================


def simular_conexion():
    """Muestra los intentos de conexión al servidor."""
    for n in range (1, INTENTOS_CONEXION +1):
        print("Conectando al servidor... Intento: ", n)
        time.sleep(PAUSA_CONEXION)



def validar_acceso(pin_correcto):
    """Pide el PIN y devuelve True si es correcto dentro de los intentos permitidos."""
    
    for n in range(INTENTOS_MAXIMOS, 0, -1):
        
        pin=input("Ingrese el PIN: ")
        time.sleep(1)
        if pin==pin_correcto:
            return True
        
        print(f"Te quedan {n-1} intento/s ")
        time.sleep(1)



def mostrar_menu():
    """Muestra el menú y devuelve una opción válida."""
    print("""MENU:
    1-DEPOSITAR
    2-EXTRAER
    3-SALIR""") 
    opcion=int(input(""))

    if opcion==OPCION_DEPOSITAR or opcion==OPCION_EXTRAER or opcion==OPCION_SALIR:
        return opcion
    
    print("Opcion invalida")



def pedir_monto():
    """Pide un monto mayor a cero y lo devuelve."""
    while True:
        monto=int(input("Ingrese un monto: "))

        if monto>0:
            return monto
            
        
        print("Monto invalido")



def depositar(saldo, monto):
    """Devuelve el saldo luego de depositar."""
    print(f"saldo: {saldo}")
    print(f"monto: {monto}")
    print(f"nuevo saldo: {saldo+monto}")
    return saldo+monto



def extraer(saldo, monto):
    """Intenta extraer dinero. Si no alcanza, mantiene el saldo."""
    if monto<=saldo:
       return saldo-monto
    print("Fondos insuficientes")
    return saldo


# =========================================
# PROGRAMA PRINCIPAL
# =========================================

def main():
    """Ejecuta el cajero automático."""
    simular_conexion()

    if not validar_acceso(PIN_CORRECTO):
        print("Acceso denegado.")
        return

    saldo = SALDO_INICIAL
    print("Acceso concedido.")
    print("Saldo actual:", saldo)
    time.sleep(1)

    while True:
        opcion = mostrar_menu()

        if opcion == OPCION_DEPOSITAR:
            monto = pedir_monto()
            saldo = depositar(saldo, monto)
            print("Depósito realizado.")
            print("Saldo actual:", saldo)

        elif opcion == OPCION_EXTRAER:
            monto = pedir_monto()
            saldo = extraer(saldo, monto)
            print("Saldo actual:", saldo)

        else:
            print("Gracias por usar el cajero.")
            break

main()