import subprocess
import time
import sys

def main():
    start_time = time.time()

    # Obter o nome do arquivo do argumento de linha de comando
    filename = sys.argv[1]

    # Execute o arquivo .py
    subprocess.run(["python3", filename])

    end_time = time.time()

    # Verifique se o tempo de execução excedeu 2 segundos
    if end_time - start_time > 2:
        raise TimeoutError("O tempo de execução do arquivo excedeu 2 segundos.")

if __name__ == "__main__":
    main()