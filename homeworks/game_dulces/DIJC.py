import tkinter as tk
from tkinter import messagebox
import random
from collections import defaultdict

TIPOS_DULCES = ['A', 'B', 'C']

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.dulces = defaultdict(int)
        self.chupetines = 0
        self.salvado = False

    def recibir_dulces(self):
        for _ in range(2):
            tipo = random.choice(TIPOS_DULCES)
            self.dulces[tipo] += 1

    def canjear_dulces(self):
        if all(self.dulces[tipo] >= 1 for tipo in TIPOS_DULCES):
            for tipo in TIPOS_DULCES:
                self.dulces[tipo] -= 1
            self.chupetines += 1
            self.salvado = True
            extra = random.choice(TIPOS_DULCES)
            self.dulces[extra] += 1
            return f"Canjeado por chupetín + {extra}"
        else:
            return "No tienes los tres tipos."

    def tiene_dulce(self, tipo):
        return self.dulces[tipo] > 0

    def quitar_dulce(self, tipo):
        if self.dulces[tipo] > 0:
            self.dulces[tipo] -= 1
            return True
        return False

    def dar_dulce(self, tipo):
        self.dulces[tipo] += 1

    def mostrar_inventario(self):
        return f"{self.nombre} | Dulces: {dict(self.dulces)}, Chupetines: {self.chupetines}, Salvado: {self.salvado}"


class JuegoDulcesGUI:
    def __init__(self, root, nombres_jugadores):
        self.root = root
        self.jugadores = [Jugador(nombre) for nombre in nombres_jugadores]
        self.jugador_actual = None

        # Iniciar juego
        self.iniciar_juego()

        # Configurar interfaz
        self.root.title("🎮 Juego de Dulces")
        self.crear_widgets()

    def iniciar_juego(self):
        for j in self.jugadores:
            j.recibir_dulces()
            j.salvado = False

    def crear_widgets(self):
        # --- SELECCIÓN DEL JUGADOR ---
        self.lbl_seleccion = tk.Label(self.root, text="Selecciona tu jugador:")
        self.lbl_seleccion.pack(pady=5)

        self.lista_jugadores = tk.Listbox(self.root)
        self.lista_jugadores.pack(pady=5)
        for j in self.jugadores:
            self.lista_jugadores.insert(tk.END, j.nombre)
        self.lista_jugadores.bind("<<ListboxSelect>>", self.seleccionar_jugador)

        # --- INFORMACIÓN DEL JUGADOR ---
        self.lbl_info = tk.Label(self.root, text="", justify=tk.LEFT)
        self.lbl_info.pack(pady=10)

        # --- MENÚ DE ACCIONES (PEDIR O INTERCAMBIAR) ---
        self.frame_menu_acciones = tk.Frame(self.root)
        self.frame_menu_acciones.pack(pady=10)

        self.btn_pedir_menu = tk.Button(self.frame_menu_acciones, text="Pedir dulce", command=self.mostrar_formulario_pedir)
        self.btn_pedir_menu.grid(row=0, column=0, padx=10)

        self.btn_intercambiar_menu = tk.Button(self.frame_menu_acciones, text="Intercambiar dulce", command=self.mostrar_formulario_intercambio)
        self.btn_intercambiar_menu.grid(row=0, column=1, padx=10)

        # --- FORMULARIO DE PEDIR DULCE (oculto al inicio) ---
        self.frame_pedir = tk.Frame(self.root)

        tk.Label(self.frame_pedir, text="Tipo de dulce:").grid(row=0, column=0, padx=5)
        self.entry_tipo_pedido = tk.Entry(self.frame_pedir, width=5)
        self.entry_tipo_pedido.grid(row=0, column=1, padx=5)

        tk.Label(self.frame_pedir, text="Jugador:").grid(row=0, column=2, padx=5)
        self.lista_jugadores_pedido = tk.Listbox(self.frame_pedir, height=3, width=10)
        for j in self.jugadores:
            self.lista_jugadores_pedido.insert(tk.END, j.nombre)
        self.lista_jugadores_pedido.grid(row=0, column=3, padx=5)

        self.btn_pedir = tk.Button(self.frame_pedir, text="Pedir", command=self.pedir_dulce)
        self.btn_pedir.grid(row=0, column=4, padx=5)

        # --- FORMULARIO DE INTERCAMBIO (oculto al inicio) ---
        self.frame_intercambio = tk.Frame(self.root)

        tk.Label(self.frame_intercambio, text="Dulce que das:").grid(row=0, column=0, padx=5)
        self.entry_tipo_tuyo = tk.Entry(self.frame_intercambio, width=5)
        self.entry_tipo_tuyo.grid(row=0, column=1, padx=5)

        tk.Label(self.frame_intercambio, text="por").grid(row=0, column=2, padx=5)

        tk.Label(self.frame_intercambio, text="Dulce que quieres:").grid(row=0, column=3, padx=5)
        self.entry_tipo_otro = tk.Entry(self.frame_intercambio, width=5)
        self.entry_tipo_otro.grid(row=0, column=4, padx=5)

        tk.Label(self.frame_intercambio, text="Con:").grid(row=0, column=5, padx=5)
        self.lista_jugadores_intercambio = tk.Listbox(self.frame_intercambio, height=3, width=10)
        for j in self.jugadores:
            self.lista_jugadores_intercambio.insert(tk.END, j.nombre)
        self.lista_jugadores_intercambio.grid(row=0, column=6, padx=5)

        self.btn_intercambiar = tk.Button(self.frame_intercambio, text="Propón intercambio", command=self.proponer_intercambio)
        self.btn_intercambiar.grid(row=0, column=7, padx=5)

        # --- BOTÓN CANJEAR DULCES (siempre visible) ---
        self.btn_canjear = tk.Button(self.root, text="Canjear dulces", command=self.canjear_dulces)
        self.btn_canjear.pack(pady=10)

    def seleccionar_jugador(self, event=None):
        seleccion = self.lista_jugadores.curselection()
        if seleccion:
            self.jugador_actual = self.jugadores[seleccion[0]]
            self.actualizar_info()

    def actualizar_info(self):
        if self.jugador_actual:
            self.lbl_info.config(text=self.jugador_actual.mostrar_inventario())

    def mostrar_formulario_pedir(self):
        self.ocultar_formularios()
        self.frame_pedir.pack(pady=10)

    def mostrar_formulario_intercambio(self):
        self.ocultar_formularios()
        self.frame_intercambio.pack(pady=10)

    def ocultar_formularios(self):
        self.frame_pedir.pack_forget()
        self.frame_intercambio.pack_forget()

    def canjear_dulces(self):
        if not self.jugador_actual:
            messagebox.showwarning("Advertencia", "Selecciona un jugador primero.")
            return

        # Verificar si tiene los 3 tipos de dulces
        if all(self.jugador_actual.dulces[tipo] >= 1 for tipo in TIPOS_DULCES):
            # Ventana emergente para elegir el tipo de dulce extra
            eleccion = tk.StringVar()

            # Crear ventana emergente personalizada
            dialogo = tk.Toplevel(self.root)
            dialogo.title("Elige un dulce")
            dialogo.geometry("300x120")

            tk.Label(dialogo, text="¿Qué tipo de dulce deseas como recompensa?").pack(pady=5)

            for tipo in TIPOS_DULCES:
                tk.Radiobutton(dialogo, text=tipo, variable=eleccion, value=tipo).pack(anchor='w')

            def confirmar():
                tipo_elegido = eleccion.get()
                if tipo_elegido:
                    # Realizar el canje
                    for tipo in TIPOS_DULCES:
                        self.jugador_actual.dulces[tipo] -= 1
                    self.jugador_actual.chupetines += 1
                    self.jugador_actual.salvado = True
                    self.jugador_actual.dulces[tipo_elegido] += 1
                    dialogo.destroy()
                    messagebox.showinfo("Éxito", f"Canjeado por chupetín + {tipo_elegido}")
                    self.actualizar_info()

            tk.Button(dialogo, text="Aceptar", command=confirmar).pack(pady=5)
        else:
            messagebox.showinfo("No se puede canjear", "Necesitas tener al menos un dulce de cada tipo (A, B y C).")

    def pedir_dulce(self):
        if not self.jugador_actual:
            messagebox.showwarning("Advertencia", "Selecciona un jugador primero.")
            return

        tipo_pedido = self.entry_tipo_pedido.get().upper()
        if tipo_pedido not in TIPOS_DULCES:
            messagebox.showerror("Error", "Tipo de dulce inválido.")
            return

        idx_jugador = self.lista_jugadores_pedido.curselection()
        if not idx_jugador:
            messagebox.showwarning("Advertencia", "Selecciona un jugador al que pedirle.")
            return

        jugador_solicitado = self.jugadores[idx_jugador[0]]

        if jugador_solicitado == self.jugador_actual:
            messagebox.showwarning("Advertencia", "No puedes pedirte dulces a ti mismo.")
            return

        if not jugador_solicitado.tiene_dulce(tipo_pedido):
            messagebox.showinfo("Resultado", f"{jugador_solicitado.nombre} no tiene dulce tipo {tipo_pedido}.")
            return

        respuesta = messagebox.askyesno("Solicitud", f"{jugador_solicitado.nombre}, ¿deseas dar un dulce {tipo_pedido}?")

        if respuesta:
            jugador_solicitado.quitar_dulce(tipo_pedido)
            self.jugador_actual.dar_dulce(tipo_pedido)
            messagebox.showinfo("Éxito", f"Has recibido un dulce {tipo_pedido}.")
            self.actualizar_info()  # Refresca el inventario

    def proponer_intercambio(self):
        if not self.jugador_actual:
            messagebox.showwarning("Advertencia", "Selecciona un jugador primero.")
            return

        tipo_tuyo = self.entry_tipo_tuyo.get().upper()
        tipo_otro = self.entry_tipo_otro.get().upper()
        if tipo_tuyo not in TIPOS_DULCES or tipo_otro not in TIPOS_DULCES:
            messagebox.showerror("Error", "Tipos de dulces inválidos.")
            return

        idx_jugador = self.lista_jugadores_intercambio.curselection()
        if not idx_jugador:
            messagebox.showwarning("Advertencia", "Selecciona un jugador al que intercambiar.")
            return

        jugador_objetivo = self.jugadores[idx_jugador[0]]
        if jugador_objetivo == self.jugador_actual:
            messagebox.showwarning("Advertencia", "No puedes intercambiarte dulces contigo mismo.")
            return

        if not self.jugador_actual.tiene_dulce(tipo_tuyo):
            messagebox.showerror("Error", f"No tienes un dulce de tipo {tipo_tuyo}.")
            return

        respuesta = messagebox.askyesno("Propuesta", f"{jugador_objetivo.nombre}, ¿aceptas intercambiar "
                                                    f"{tipo_tuyo} por {tipo_otro}?")

        if respuesta:
            if jugador_objetivo.tiene_dulce(tipo_otro):
                self.jugador_actual.quitar_dulce(tipo_tuyo)
                jugador_objetivo.quitar_dulce(tipo_otro)
                self.jugador_actual.dar_dulce(tipo_otro)
                jugador_objetivo.dar_dulce(tipo_tuyo)
                messagebox.showinfo("Éxito", "¡Intercambio realizado!")
                self.actualizar_info()  # Refresca el inventario
            else:
                messagebox.showerror("Error", f"{jugador_objetivo.nombre} no tiene dulce de tipo {tipo_otro}.")
        else:
            messagebox.showinfo("Cancelado", "El jugador rechazó el intercambio.")


# Ejecutar aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = JuegoDulcesGUI(root, ["Ana", "Beto", "Carlos","Harrison","Russbel","Brian","Cesia","Roberth","Danny"])
    root.mainloop()