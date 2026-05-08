#  Cyber Security Lab - Header Analyzer

Este projeto é um laboratório de automação para análise de cabeçalhos de segurança HTTP. Ele foi desenvolvido para identificar rapidamente a ausência de proteções críticas como CSP, HSTS e X-Frame-Options em múltiplos alvos simultaneamente.

##  Funcionalidades
- **Scan em Massa:** Analisa múltiplos domínios em uma única execução.
- **Relatórios Automáticos:** Gera arquivos individuais de texto em `data/` com os resultados.
- **Logging Profissional:** Sistema de logs para rastreio de erros de conexão e execução.

##  Estrutura
- `src/analyzer/`: Lógica de extração e análise de headers.
- `src/utils/`: Sistema de logs centralizado.
- `data/`: (Local) Armazenamento dos relatórios gerados.

##  Instalação e Uso
1. Clone o repositório.
2. Crie e ative seu ambiente virtual: `python -m venv .venv`.
3. Instale as dependências: `pip install -r requirements.txt`.
4. Execute o scanner:
   ```bash
   python -m src.analyzer.header_sec
