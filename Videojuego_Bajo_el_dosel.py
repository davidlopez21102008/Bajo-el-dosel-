import random

# ==========================================
# 1. HERRAMIENTAS Y LAMBDAS
# ==========================================
# Lambda para formatear títulos e impresiones
formatear_titulo = lambda texto: f"\n========================================\n {texto.upper()}\n========================================"

# ==========================================
# 2. CLASES DE JUGADOR Y HERRAMIENTAS
# ==========================================
class Jugador:
    def __init__(self, nombre="Mateo"):
        self.__nombre = nombre
        self.__dificultad = "Normal"
        self.__herramientas = []
        self.salud = 100

    # Encapsulamiento con Getters y Setters
    def get_nombre(self):
        return self.__nombre
    def set_dificultad(self, dificultad):
        self.__dificultad = dificultad
    def get_dificultad(self):
        return self.__dificultad
    def agregar_herramienta(self, item):
        self.__herramientas.append(item)
        print(f" -> Añadido al inventario: {item}")
    def mostrar_inventario(self):
        print(f"\nInventario de {self.__nombre}: {', '.join(self.__herramientas) if self.__herramientas else 'Vacío'}")

# ==========================================
# 3. CLASES BASE Y HERENCIA (NIVELES)
# ==========================================
class NivelBase:
    def __init__(self, titulo, objetivo):
        self.titulo = titulo
        self.objetivo = objetivo
    def mostrar_encabezado(self):
        print(formatear_titulo(self.titulo))
        print(f"OBJETIVO: {self.objetivo}\n")
    def ejecutar(self, jugador):
        raise NotImplementedError("Este método debe ser implementado por la subclase")

# Polimorfismo: Nivel de Combate/Táctico
class NivelDuelo(NivelBase):
    def __init__(self, titulo, objetivo, herramientas_nivel):
        super().__init__(titulo, objetivo)
        self.herramientas_nivel = herramientas_nivel
    def ejecutar(self, jugador):
        self.mostrar_encabezado()
        for item in self.herramientas_nivel:
            jugador.agregar_herramienta(item)
   
        print("\nMECÁNICAS: Colocación de trampas de bambú | Uso de armas | Coordinación")
        print("1. Colocar trampas de bambú y emboscar")
        print("2. Fuego directo de bajo calibre")
        
        while True:
            try:
                opcion = int(input("Selecciona tu acción (1 o 2): "))
                if opcion in [1, 2]:
                    break
                print("Por favor, ingresa 1 o 2.")
            except ValueError:
                print("Entrada inválida. Debe ser un número.")

        if opcion == 1:
            print("\n¡Éxito! Las trampas desorganizan la patrulla y consiguen las provisiones junto a Ernesto y Tino.")
        else:
            print("\nLogran replegar al enemigo mediante coordinación, aunque con más riesgo. Provisiones aseguradas.")
        return True

# Polimorfismo: Nivel de Infiltración / Sigilo
class NivelInfiltracion(NivelBase):
    def __init__(self, titulo, objetivo, herramientas_nivel):
        super().__init__(titulo, objetivo)
        self.herramientas_nivel = herramientas_nivel

    def ejecutar(self, jugador):
        self.mostrar_encabezado()
        for item in self.herramientas_nivel:
            jugador.agregar_herramienta(item)

        print("\nMECÁNICAS: Sigilo urbano/rural | Distracción | Dilema de Santiago")
        print("Te infiltras para contactar al informante y extraer medicinas para Ixmucané.")
        print("De pronto, te encuentras frente a Santiago...")
        print("1. Evitar a Santiago mediante distracción (Sin violencia)")
        print("2. Encarar directamente a tu antiguo amigo")

        while True:
            try:
                opcion = int(input("Selecciona tu acción (1 o 2): "))
                if opcion in [1, 2]:
                    break
                print("Por favor, selecciona 1 o 2.")
            except ValueError:
                print("Entrada inválida. Ingresa un número válido.")

        if opcion == 1:
            print("\nLogras distraer la atención y obtienes las medicinas con éxito y sin levantar sospechas.")
        else:
            print("\nConversas brevemente con Santiago; aunque la tensión es alta, logras cumplir el objetivo.")
        return True

# ==========================================
# 4. SISTEMA DE MENÚS Y FLUJO PRINCIPAL
# ==========================================
class JuegoBajoElDosel:
    def __init__(self):
        self.jugador = Jugador()

    def iniciar(self):
        while True:
            print(formatear_titulo("BAJO EL DOSEL - Menú Principal"))
            print("1. Continuar")
            print("2. Nueva Partida")
            print("3. Opciones")
            print("4. Créditos")
            print("5. Salir")

            try:
                opcion = int(input("\nSelecciona una opción: "))
                if opcion == 1:
                    print("\nNo hay partidas guardadas previamente.")
                elif opcion == 2:
                    self.flujo_nueva_partida()
                elif opcion == 3:
                    self.menu_opciones()
                elif opcion == 4:
                    self.mostrar_creditos()
                elif opcion == 5:
                    print("\n¡Gracias por jugar Bajo el Dosel!")
                    break
                else:
                    print("Opción no válida. Intenta de nuevo.")
            except ValueError:
                print("Error: Ingresa un número entero válido.")

    def menu_opciones(self):
        print(formatear_titulo("Opciones"))
        print("Configuración de audio y pantalla predeterminada en Consola.")
        input("Presiona Enter para regresar...")

    def mostrar_creditos(self):
        print(formatear_titulo("Créditos"))
        print("Videojuego Educativo 'Bajo el Dosel'")
        print("Desarrollado para consola usando Python Puro.")
        input("Presiona Enter para regresar...")

    def flujo_nueva_partida(self):
        print(formatear_titulo("Nueva Partida: Inicio de Proceso"))
        
        # Selección de Dificultad
        print("Selecciona Dificultad:")
        print("1. Fácil (Novato)")
        print("2. Normal (Equilibrado)")
        print("3. Difícil (Desafío)")
        
        while True:
            try:
                dif = int(input("Opción: "))
                if dif == 1:
                    self.jugador.set_dificultad("Fácil")
                    break
                elif dif == 2:
                    self.jugador.set_dificultad("Normal")
                    break
                elif dif == 3:
                    self.jugador.set_dificultad("Difícil")
                    break
                print("Opción inválida.")
            except ValueError:
                print("Error: Debes ingresar un número (1, 2 o 3).")

        # Tutorial Inicial
        while True:
            tut = input("\n¿Revisar Tutorial Inicial? (SI/NO): ").strip().upper()
            if tut in ["SI", "NO"]:
                if tut == "SI":
                    print("\n[TUTORIAL] Mecánicas básicas: Movimiento, Sigilo y Uso de Herramientas aprendidas.")
                break
            print("Responde con 'SI' o 'NO'.")

        # Historia Intro
        print(formatear_titulo("HISTORIA"))
        print("Mateo se une a la columna guerrillera liderada por el Comandante Ernesto...")
        input("Presiona Enter para continuar al Nivel 2...")

        # Nivel 2
        nivel2 = NivelDuelo(
            "Nivel 2: Frente Clandestino (Emboscada en la Ruta)",
            "Conseguir provisiones con Ernesto y Tino.",
            ["Machete", "Cueras y mecapales"]
        )
        nivel2.ejecutar(self.jugador)

        # Nivel 3
        nivel3 = NivelInfiltracion(
            "Nivel 3: Voces en el Pueblo (Infiltración)",
            "Extraer medicinas para Ixmucané y contactar informante.",
            ["Cuchillo de caza táctico", "Botiquín de campo (Hierbas + Yodo)", "Jícara/Tecomate"]
        )
        nivel3.ejecutar(self.jugador)

        # Transición Final
        print(formatear_titulo("HISTORIA: Ofensiva de Tierra Quemada"))
        print("Enfrentamiento decisivo con las fuerzas de Ríos Montt y el Capitán Valenzuela.")
        
        # Decisiones Finales (¿Dónde poner la lealtad?)
        self.nivel_final()

    def nivel_final(self):
        print(formatear_titulo("¿DÓNDE PONER LA LEALTAD?"))
        print("1. OPCIÓN A: CUBRIR LA RETIRADA")
        print("   Objetivo: Ganar tiempo para civiles hacia la frontera.")
        print("   Acción: Duelo táctico final contra el Capitán Valenzuela.")
        print("2. OPCIÓN B: EL RETORNO A LA TIERRA")
        print("   Objetivo: Romper cerco de las PAC.")
        print("   Acción: Encarar destino con Santiago y desaparecer.")

        while True:
            try:
                eleccion = int(input("\nElige el destino final (1 o 2): "))
                if eleccion == 1:
                    print(formatear_titulo("NIVEL FINAL: Cenizas y Memoria (OPCIÓN A)"))
                    print("\n>>> FINAL A: Salvar civiles, sacrificio potencial, preservación de memoria histórica.")
                    break
                elif eleccion == 2:
                    print(formatear_titulo("NIVEL FINAL: Cenizas y Memoria (OPCIÓN B)"))
                    print("\n>>> FINAL B: Clandestinidad civil, proteger raíces de la comunidad.")
                    break
                print("Por favor selecciona 1 o 2.")
            except ValueError:
                print("Entrada no válida.")
        
        self.jugador.mostrar_inventario()
        print("\n=== FIN DE LA PARTIDA ===")
        input("Presiona Enter para regresar al Menú Principal...")

# ==========================================
# 5. PUNTO DE ENTRADA
# ==========================================
if __name__ == "__main__":
    juego = JuegoBajoElDosel()
    juego.iniciar()