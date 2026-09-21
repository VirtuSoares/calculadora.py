# 📌 Entregável de Desenvolvimento em Python – Semana 03 (Desafio Sprint 3)

Este repositório contém a resolução dos desafios da **Semana 03**, focados em **modularização de código, funções, passagem de parâmetros (`*args` e `**kwargs`), escopo, mutabilidade e criação de módulos reeditáveis**.

---

## 🎯 Objetivo da Atividade
* Compreender a divisão de problemas complexos em módulos e funções independentes.
* Utilizar boas práticas de manipulação de parâmetros, como mutabilidade controlada (cópia defensiva) e tratamento de exceções/erros.
* Dominar o uso de `*args` (tuplas de argumentos arbitrários) e `**kwargs` (dicionários de palavras-chave).
* Implementar documentação de código usando **Docstrings** e convenções **PEP 8** (`snake_case`).
* Garantir o isolamento de módulos com o bloco `if __name__ == "__main__":`.

---

## 🛠️ Módulos e Funcionalidades

### 1. `calculadora.py`
Contém funções matemáticas básicas (`somar`, `subtrair`, `multiplicar`) e tratamento explícito para divisão por zero em `dividir`.

### 2. `utilidades.py`
Módulo utilitário contendo:
* **Conversor de Temperatura:** Suporte a Celsius, Fahrenheit e Kelvin.
* **Validador de Senha:** Verificação de critérios de segurança (comprimento, números, letras maiúsculas/minúsculas).
* **Caixa Registradora (`*precos`):** Processamento flexível de múltiplos preços e descontos.
* **Ficha do Aluno (`**dados`):** Gerador de ficha cadastral utilizando dicionários dinâmicos.
* **Lista Segura:** Adição defensiva de elementos sem alterar a lista original.
* **Fatorial Recursivo:** Cálculo matemático via recursão.
* **Gerador de Relatórios (`*linhas`, `**config`):** Formatação customizada de documentos.

### 3. `estatistica.py` *(Módulo Bônus)*
Contém cálculos estatísticos básicos: `media`, `mediana` e `moda`.

### 4. `main.py`
Script principal que importa todos os módulos (utilizando referências diretas e aliases como `import estatistica as est`) e demonstra o funcionamento completo do ecossistema.

---

## 📁 Estrutura do Repositório

```text
.
├── README.md
├── calculadora.py
├── utilidades.py
├── estatistica.py
└── main.py
