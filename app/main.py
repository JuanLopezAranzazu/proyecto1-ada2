import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from terminal_inteligente import brute_force_terminal, dynamic_programming_terminal, greedy_terminal, uniform_cost_terminal
from subasta_publica import brute_force_auction, dynamic_programming_auction, greedy_auction
import timeit

class App:
  def __init__(self, root):
    self.root = root
    self.root.title("Proyecto 1 ADA II")
    self.root.geometry("600x400")
    self.create_widgets()

  def create_widgets(self):
    # Crear el marco para la columna de formulario
    self.frame_form = ttk.Frame(self.root, padding="10")
    self.frame_form.grid(row=0, column=0, sticky="nsew")

    # Combobox para seleccionar el problema
    ttk.Label(self.frame_form, text="Seleccionar problema:").grid(row=0, column=0, columnspan=2, sticky="ew")
    self.combo_problems = ttk.Combobox(self.frame_form, values=["Terminal Inteligente", "Subasta Pública"])
    self.combo_problems.grid(row=1, column=0, columnspan=2, sticky="ew")
    self.combo_problems.set("Terminal Inteligente")  # Valor por defecto

    # Botón para cargar el archivo
    self.btn_load = ttk.Button(self.frame_form, text="Cargar archivo", command=self.load_file)
    self.btn_load.grid(row=2, column=0, columnspan=2, pady=10, sticky="ew")

    # Combobox para seleccionar el algoritmo
    ttk.Label(self.frame_form, text="Seleccionar algoritmo:").grid(row=3, column=0, columnspan=2, sticky="ew")
    self.combo_algorithms = ttk.Combobox(self.frame_form, values=["Fuerza Bruta", "Programación Voraz", "Programación Dinámica", "Costo Uniforme"])
    self.combo_algorithms.grid(row=4, column=0, columnspan=2, sticky="ew")
    self.combo_algorithms.set("Fuerza Bruta")  # Valor por defecto

    # Botón para ejecutar el algoritmo
    self.btn_run = ttk.Button(self.frame_form, text="Ejecutar", command=self.run_algorithm)
    self.btn_run.grid(row=5, column=0, columnspan=2, pady=10, sticky="ew")

    # Crear el marco para la columna de resultados
    self.frame_results = ttk.Frame(self.root, padding="10")
    self.frame_results.grid(row=0, column=1, sticky="nsew")

    # Área de resultados
    self.text_results = tk.Text(self.frame_results, wrap="word", width=50, height=20)
    self.text_results.grid(row=0, column=0, sticky="nsew")

    # Configurar el frame_form para expandirse en ambas direcciones
    self.frame_form.grid_columnconfigure(0, weight=1)  # Permitir crecimiento horizontal

    # Configurar el frame_results para expandirse en ambas direcciones
    self.frame_results.grid_rowconfigure(0, weight=1)  # Permitir crecimiento vertical
    self.frame_results.grid_columnconfigure(0, weight=1)  # Permitir crecimiento horizontal

    # Ajustar el peso de las columnas
    self.root.grid_columnconfigure(0, weight=1)  # Columna del formulario
    self.root.grid_columnconfigure(1, weight=2)  # Columna de resultados

    # Ajustar el peso de las filas
    self.root.grid_rowconfigure(0, weight=1)  # Fila principal
    
    # Diccionario de algoritmos para cada problema
    self.terminal={
      "Fuerza Bruta": brute_force_terminal.brute_force,
      "Programación Dinámica": dynamic_programming_terminal.dynamic_programming,
      "Programación Voraz": greedy_terminal.greedy,
      "Costo Uniforme": uniform_cost_terminal.uniform_cost,
    }

    self.auction={
      "Fuerza Bruta": brute_force_auction.brute_force,
      "Programación Dinámica": dynamic_programming_auction.dynamic_programming,
      "Programación Voraz": greedy_auction.greedy,
    }

  def load_file(self):
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
      with open(file_path, 'r') as file:
        lines = file.readlines()
        # Determinar el problema seleccionado
        problem = self.combo_problems.get()
        
        if problem == "Terminal Inteligente":
          # Procesar archivo para Terminal Inteligente
          try:
            global stringA, stringB, operations_dict
            stringA = lines[0].strip()  # Primera línea: A
            stringB = lines[1].strip()  # Segunda línea: B
            advance, delete, replace, insert, kill = map(int, lines[2].strip().split())
            operations_dict = {
              "advance": advance,
              "delete": delete,
              "replace": replace,
              "insert": insert,
              "kill": kill
            }
            # Mostrar datos cargados en el área de resultados
            self.text_results.delete(1.0, tk.END)
            self.text_results.insert(tk.END, f"String A: {stringA}\nString B: {stringB}\nOperations: {operations_dict}\n")
          except Exception as e:
            self.text_results.delete(1.0, tk.END)
            self.text_results.insert(tk.END, f"Error al cargar el archivo: {e}\n")
                
        elif problem == "Subasta Pública":
          # Procesar archivo para Subasta Pública
          try:
            global A, B, n, offers
            A = int(lines[0].strip())  # Primera línea: A
            B = int(lines[1].strip())  # Segunda línea: B
            n = int(lines[2].strip())  # Tercera línea: n
            offers = []
            for i in range(n):
                parts = list(map(int, lines[3 + i].strip().split()))
                offers.append(parts)  # Cada oferta como una lista [pi, mi, Mi]
            
            # Mostrar datos cargados en el área de resultados
            self.text_results.delete(1.0, tk.END)
            self.text_results.insert(tk.END, f"A: {A}\nB: {B}\nn: {n}\nOffers: {offers}\n")
          except Exception as e:
            self.text_results.delete(1.0, tk.END)
            self.text_results.insert(tk.END, f"Error al cargar el archivo: {e}\n")

  def run_algorithm(self):
    algorithm = self.combo_algorithms.get()
    problem = self.combo_problems.get()

    if problem == "Terminal Inteligente":
      # Validar que los datos estén cargados
      if not 'stringA' in globals() or not 'stringB' in globals() or not 'operations_dict' in globals():
        self.text_results.delete(1.0, tk.END)
        self.text_results.insert(tk.END, "Error: Cargar archivo primero\n")
        return
      
      # Validar que el algoritmo esté implementado
      if algorithm not in self.terminal:
        self.text_results.delete(1.0, tk.END)
        self.text_results.insert(tk.END, "Error: Algoritmo no implementado\n")
        return

      start_time = timeit.default_timer()
      result=self.terminal[algorithm](stringA, stringB, operations_dict)
      elapsed_time = timeit.default_timer() - start_time
      print(result)
      print(f"Tiempo de ejecución: {elapsed_time:.10f} segundos")

    elif problem == "Subasta Pública":
      # Validar que los datos estén cargados
      if not 'A' in globals() or not 'B' in globals() or not 'n' in globals() or not 'offers' in globals():
        self.text_results.delete(1.0, tk.END)
        self.text_results.insert(tk.END, "Error: Cargar archivo primero\n")
        return
      
      # Validar que el algoritmo esté implementado
      if algorithm not in self.auction:
        self.text_results.delete(1.0, tk.END)
        self.text_results.insert(tk.END, "Error: Algoritmo no implementado\n")
        return
      
      start_time = timeit.default_timer()
      result=self.auction[algorithm](A, B, offers)
      elapsed_time = timeit.default_timer() - start_time
      print(result)
      print(f"Tiempo de ejecución: {elapsed_time:.10f} segundos")

    # Mostrar resultados en el Text widget
    self.text_results.delete(1.0, tk.END)
    self.text_results.insert(tk.END, result)
    self.text_results.insert(tk.END, f"\nTiempo de ejecución: {elapsed_time:.10f} segundos\n")

if __name__ == "__main__":
  root = tk.Tk()
  app = App(root)
  root.mainloop()
