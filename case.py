class MinhaClasse:
    def __enter__(self):
        print("Acessei!!")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Sai!!")


with MinhaClasse() as mc:
    print("Estou dentro!!")