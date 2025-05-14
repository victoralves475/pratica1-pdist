import hprose
import threading

class DicionarioDistribuido:
    def __init__(self):
        self.dicionario = {}
        self.lock = threading.Lock()

    def update(self, chave: str, valor: int) -> bool:
        with self.lock:
            existe = chave in self.dicionario
            self.dicionario[chave] = valor
            print(f"update('{chave}', {valor}) -> {'nova entrada' if not existe else 'entrada atualizada'}")
            return not existe  # retorna True se não existia antes

    def remove(self, chave: str) -> bool:
        with self.lock:
            if chave in self.dicionario:
                del self.dicionario[chave]
                print(f"remove('{chave}') -> removido com sucesso")
                return True
            else:
                print(f"remove('{chave}') -> não existe")
                return False

    def get(self, chave: str) -> int:
        with self.lock:
            valor = self.dicionario.get(chave, -1)
            print(f"get('{chave}') -> {valor}")
            return valor

if __name__ == "__main__":
    service = hprose.HttpServer(port=8181)
    service.addInstanceMethods(DicionarioDistribuido())
    print("Servidor iniciado na porta 8181")
    service.start()
