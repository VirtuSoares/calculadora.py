---

### Ficha 2: `calculadora.py`

```python
"""
Módulo Calculadora
Oferece funções para operações matemáticas básicas com tratamento de erros.
"""


def somar(a: float, b: float) -> float:
    """Retorna a soma de dois números."""
    return a + b


def subtrair(a: float, b: float) -> float:
    """Retorna a diferença entre dois números."""
    return a - b


def multiplicar(a: float, b: float) -> float:
    """Retorna o produto de dois números."""
    return a * b


def dividir(a: float, b: float) -> float | None:
    """
    Realiza a divisão entre dois números.

    Retorna None e exibe uma mensagem caso ocorra divisão por zero.
    """
    if b == 0:
        print("[Erro Calculadora]: Divisão por zero não é permitida.")
        return None
    return a / b


if __name__ == "__main__":
    print("--- Teste do Módulo Calculadora ---")
    print(f"Soma (10 + 5): {somar(10, 5)}")



  
  """
Módulo Utilidades
Reúne funções auxiliares para manipulação de listas, validações,
descontos, relatórios e conversões de temperatura.
"""


def converter_temperatura(valor: float, origem: str = "C", destino: str = "F") -> float | None:
    """
    Converte temperaturas entre Celsius (C), Fahrenheit (F) e Kelvin (K).
    """
    origem = origem.upper()
    destino = destino.upper()

    if origem == destino:
        return valor

    # Converter origem para Celsius primeiro
    if origem == "C":
        celsius = valor
    elif origem == "F":
        celsius = (valor - 32) * 5 / 9
    elif origem == "K":
        celsius = valor - 273.15
    else:
        print("[Erro]: Unidade de origem inválida.")
        return None

    # Converter Celsius para o destino
    if destino == "C":
        return celsius
    elif destino == "F":
        return (celsius * 9 / 5) + 32
    elif destino == "K":
        return celsius + 273.15
    else:
        print("[Erro]: Unidade de destino inválida.")
        return None


def validar_senha(senha: str) -> bool:
    """
    Valida se uma senha atende aos requisitos mínimos de segurança:
    - Pelo menos 8 caracteres
    - Pelo menos um número
    - Pelo menos uma letra maiúscula
    """
    if len(senha) < 8:
        return False
    tem_numero = any(c.isdigit() for c in senha)
    tem_maiuscula = any(c.isupper() for c in senha)

    return tem_numero and tem_maiuscula


def caixa_registradora(*precos: float, desconto_percentual: float = 0.0) -> float:
    """
    Recebe um número arbitrário de preços (*args) e calcula o total com desconto opcional.
    """
    total = sum(precos)
    if desconto_percentual > 0:
        total -= total * (desconto_percentual / 100)
    return max(total, 0.0)


def ficha_aluno(nome: str, **dados) -> dict:
    """
    Cria um dicionário com a ficha do aluno recebendo informações dinâmicas (**kwargs).
    """
    ficha = {"nome": nome}
    ficha.update(dados)
    return ficha


def adicionar_item_seguro(lista_original: list, item) -> list:
    """
    Adiciona um item a uma lista utilizando cópia defensiva,
    garantindo que a lista original não seja modificada.
    """
    nova_lista = lista_original.copy()
    nova_lista.append(item)
    return nova_lista


def fatorial(n: int) -> int:
    """
    Calcula o fatorial de um número inteiro de forma recursiva.
    """
    if n < 0:
        raise ValueError("Fatorial não é definido para números negativos.")
    if n in (0, 1):
        return 1
    return n * fatorial(n - 1)


def relatorio(titulo: str, *linhas: str, **config) -> str:
    """
    Gera um relatório formatado recebendo o título, linhas dinâmicas (*args)
    e configurações visuais (**kwargs).
    """
    largura = config.get("largura", 50)
    caractere = config.get("caractere_divisao", "=")

    cabecalho = titulo.center(largura)
    divisoria = caractere * largura

    corpo = "\n".join(f"- {linha}" for linha in linhas)

    return f"{divisoria}\n{cabecalho}\n{divisoria}\n{corpo}\n{divisoria}"


if __name__ == "__main__":
    print("--- Teste do Módulo Utilidades ---")
    print(f"Validação de senha 'Senha123': {validar_senha('Senha123')}")
    print(f"Fatorial de 5: {fatorial(5)}")



  """
Script Principal
Importa os módulos criados e executa demonstrações de todas as funcionalidades.
"""

import calculadora
import utilidades as util
import estatistica as est


def executar_demonstracao():
    print("==================================================")
    print("    DEMONSTRAÇÃO DO ENTREGÁVEL - SPRINT 3        ")
    print("==================================================\n")

    # 1. Demonstração do módulo Calculadora
    print("1. [Calculadora]")
    print(f"   Somar (15 + 25): {calculadora.somar(15, 25)}")
    print(f"   Subtrair (100 - 45): {calculadora.subtrair(100, 45)}")
    print(f"   Multiplicar (6 * 7): {calculadora.multiplicar(6, 7)}")
    print(f"   Dividir (50 / 2): {calculadora.dividir(50, 2)}")
    print(f"   Dividir por Zero (50 / 0): {calculadora.dividir(50, 0)}")
    print("-" * 50)

    # 2. Conversão de Temperatura
    print("\n2. [Conversor de Temperatura]")
    temp_c = 25.0
    temp_f = util.converter_temperatura(temp_c, origem="C", destino="F")
    print(f"   {temp_c}°C é equivalente a {temp_f:.1f}°F")
    print("-" * 50)

    # 3. Validação de Senha
    print("\n3. [Validador de Senha]")
    senhas = ["12345", "senhafraca", "SenhaSegura123"]
    for s in senhas:
        status = "VÁLIDA" if util.validar_senha(s) else "INVÁLIDA"
        print(f"   Senha '{s}': {status}")
    print("-" * 50)

    # 4. Caixa Registradora (*args)
    print("\n4. [Caixa Registradora - *args]")
    total_compras = util.caixa_registradora(29.90, 49.90, 15.00, 105.20, desconto_percentual=10)
    print(f"   Total das compras com 10% de desconto: R$ {total_compras:.2f}")
    print("-" * 50)

    # 5. Ficha do Aluno (**kwargs)
    print("\n5. [Ficha do Aluno - **kwargs]")
    aluno = util.ficha_aluno("Victor Soares", curso="ADS", periodo="1º Semestre", status="Ativo")
    print("   Dados cadastrados:")
    for chave, valor in aluno.items():
        print(f"     - {chave.capitalize()}: {valor}")
    print("-" * 50)

    # 6. Lista Segura (Cópia Defensiva)
    print("\n6. [Lista Segura - Cópia Defensiva]")
    lista_base = ["Python", "JavaScript", "SQL"]
    nova_lista = util.adicionar_item_seguro(lista_base, "Docker")

    print(f"   Lista Original (Intacta): {lista_base}")
    print(f"   Nova Lista (Modificada): {nova_lista}")
    print("-" * 50)

    # 7. Função Recursiva (Fatorial)
    print("\n7. [Fatorial Recursivo]")
    numero_fat = 6
    print(f"   O fatorial de {numero_fat}! é: {util.fatorial(numero_fat)}")
    print("-" * 50)

    # 8. Módulo Estatística (com alias est)
    print("\n8. [Estatística - Alias 'est']")
    notas = [7.5, 8.0, 9.5, 6.0, 8.0, 10.0]
    print(f"   Notas avaliadas: {notas}")
    print(f"   Média: {est.media(notas):.2f}")
    print(f"   Mediana: {est.mediana(notas):.2f}")
    print(f"   Moda: {est.moda(notas)}")
    print("-" * 50)

    # 9. Gerador de Relatório (*args e **kwargs)
    print("\n9. [Relatório Personalizado]")
    documento = util.relatorio(
        "RESUMO DA SPRINT 3",
        "Módulo Calculadora criado e testado",
        "Módulo Utilidades com funções variadas",
        "Tratamento defensivo de listas concluído",
        largura=45,
        caractere_divisao="*"
    )
    print(documento)


if __name__ == "__main__":
    executar_demonstracao()
    print(f"Divisão por zero (10 / 0): {dividir(10, 0)}")
