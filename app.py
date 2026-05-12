import os
import sys

def run_vault():
    # Buscando o segredo da variável de ambiente (Injeção dinâmica)
    # Isso evita salvar senhas no código!
    secret_key = os.getenv('CHAVE_MESTRA_DO_COFRE')

    if not secret_key:
        print("❌ ERRO: Cofre trancado. Chave mestra não encontrada!")
        sys.exit(1)

    print("🔓 Cofre acessado com sucesso!")
    # Simulando o Log Masking: nunca imprimimos a chave real nos logs!
    print(f"Processando dados com a chave: {secret_key[:2]}********")

if __name__ == "__main__":
    run_vault()
