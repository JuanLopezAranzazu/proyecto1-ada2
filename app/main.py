import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from terminal_inteligente import brute_force_ti, dp_ti, greedy_ti
from subasta_publica import brute_force_sp, dp_sp, greedy_sp
import timeit

class App:
  def __init__(self, root):
    self.root = root
    self.root.title("TERMINAL INTELIGENTE / SUBASTA PÚBLICA")
    self.create_widgets()

  def create_widgets(self):
    # Crear el marco para la columna de formulario
    self.frame_form = ttk.Frame(self.root, padding="10")
    self.frame_form.grid(row=0, column=0, sticky="nsew")

    # Combobox para seleccionar el problema
    ttk.Label(self.frame_form, text="Seleccionar problema:").grid(row=0, column=0, columnspan=2)
    self.combo_problems = ttk.Combobox(self.frame_form, values=["Terminal Inteligente", "Subasta Pública"])
    self.combo_problems.grid(row=1, column=0, columnspan=2)
    self.combo_problems.set("Terminal Inteligente")  # Valor por defecto

    # Botón para cargar el archivo
    self.btn_load = ttk.Button(self.frame_form, text="Cargar archivo", command=self.load_file)
    self.btn_load.grid(row=2, column=0, columnspan=2)

    # Combobox para seleccionar el algoritmo
    ttk.Label(self.frame_form, text="Seleccionar algoritmo:").grid(row=3, column=0, columnspan=2)
    self.combo_algorithms = ttk.Combobox(self.frame_form, values=["Fuerza Bruta", "Programación Voraz", "Programación Dinámica"])
    self.combo_algorithms.grid(row=4, column=0, columnspan=2)
    self.combo_algorithms.set("Fuerza Bruta")  # Valor por defecto

    # Botón para ejecutar el algoritmo
    self.btn_run = ttk.Button(self.frame_form, text="Ejecutar", command=self.run_algorithm)
    self.btn_run.grid(row=5, column=0, columnspan=2)

    # Crear el marco para la columna de resultados
    self.frame_results = ttk.Frame(self.root, padding="10")
    self.frame_results.grid(row=0, column=1, sticky="nsew")

    # Área de resultados
    self.text_results = tk.Text(self.frame_results, width=40, height=20)
    self.text_results.grid(row=0, column=0)

    # Ajustar el peso de las columnas
    self.root.grid_columnconfigure(0, weight=1)  # Columna del formulario
    self.root.grid_columnconfigure(1, weight=2)  # Columna de resultados

    self.algorithms_ti={
      "Fuerza Bruta": brute_force_ti.brute_force,
      "Programación Dinámica": dp_ti.dynamic_programming,
      "Programación Voraz": greedy_ti.greedy,
    }

    self.algorithms_sp={
      "Fuerza Bruta": brute_force_sp.brute_force,
      "Programación Dinámica": dp_sp.dynamic_programming,
      "Programación Voraz": greedy_sp.greedy,
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
      
      start_time = timeit.default_timer()
      result=self.algorithms_ti[algorithm](stringA, stringB, operations_dict)
      elapsed_time = timeit.default_timer() - start_time
      print(result)
      print(f"Tiempo de ejecución: {elapsed_time:.10f} segundos")

    elif problem == "Subasta Pública":
      # Validar que los datos estén cargados
      if not 'A' in globals() or not 'B' in globals() or not 'n' in globals() or not 'offers' in globals():
        self.text_results.delete(1.0, tk.END)
        self.text_results.insert(tk.END, "Error: Cargar archivo primero\n")
        return
      
      start_time = timeit.default_timer()
      result=self.algorithms_sp[algorithm](A, B, offers)
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