import sys
from src import tarea_1, tarea_2, tarea_3, tarea_4
from src.utils import grapher

def main():
    if len(sys.argv) < 2:
        print("Indicar la tarea a ejecutar.")
        return

    tarea = sys.argv[1]

    if tarea == "tarea_1":
        tarea_1.resolver_tarea_1()

    elif tarea == "tarea_2":
        if len(sys.argv) < 3:
            print("Proporcionar la frecuencia.")
            return
        frecuencia = sys.argv[2]
        tarea_2.resolver_tarea_2(frecuencia)

    elif tarea == "tarea_3":
        if len(sys.argv) < 5:
            print("Debes proporcionar amplitud, frecuencia y fase.")
            return
        amplitud = sys.argv[2]
        frecuencia = sys.argv[3]
        fase = sys.argv[4]
        tarea_3.resolver_tarea_3(amplitud, frecuencia, fase)

    elif tarea == "tarea_4":
        if len(sys.argv) < 3:
            print("Debes proporcionar el número de bits.")
            return
        num_bits = sys.argv[2]
        tarea_4.resolver_tarea_4(num_bits)

    else:
        print("Tarea no reconocida. Usa: tarea_1, tarea_2, tarea_3 o tarea_4")

if __name__ == "__main__":
    main()
