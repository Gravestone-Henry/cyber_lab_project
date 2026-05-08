## CyberLab: Analisador de Postura de Segurança Web
O CyberLab é uma ferramenta de automação voltada para a fase de Reconhecimento (Recon) em auditorias de segurança. Ele foi criado para analisar a "camada de proteção invisível" de sites e aplicações web: os cabeçalhos de resposta HTTP.

## O que é este projeto?
Imagine que um site é uma casa. O código que você vê é a fachada, mas os Cabeçalhos de Segurança são os cadeados, alarmes e cercas elétricas que impedem que invasores usem técnicas comuns para entrar.

Este projeto automatiza a verificação desses "cadeados", gerando relatórios detalhados sobre o que está protegido e o que está vulnerável.

## Funcionalidades Detalhadas
1. Varredura Multi-Alvo (Bulk Scan)
Em vez de testar um site por vez, o script processa uma lista de endereços. Isso é essencial para profissionais que precisam auditar dezenas de servidores de uma empresa rapidamente.

2. Análise de Vulnerabilidades Comuns
O projeto foca em quatro pilares de defesa web:

HSTS (Strict-Transport-Security): Evita que a conexão seja "rebaixada" para HTTP inseguro, prevenindo roubo de senhas em redes Wi-Fi públicas.

CSP (Content-Security-Policy): A defesa mais forte contra XSS (injeção de scripts maliciosos que roubam dados do navegador).

X-Frame-Options: Bloqueia o Clickjacking, técnica onde um site malicioso "esconde" o site real em um quadro invisível para forçar cliques em botões de transferência ou exclusão.

X-Content-Type-Options: Impede que o navegador tente "adivinhar" o tipo de um arquivo, o que evita que uma imagem inofensiva seja executada como um vírus.

3. Sistema de Relatórios e Logs
Logs em tempo real: Mostra o progresso do scan no terminal.

Relatórios Persistentes: Salva cada análise em arquivos .txt na pasta data/, criando um histórico de auditoria.

## Organização do Laboratório
A estrutura de pastas segue o padrão de mercado para projetos profissionais:

src/: O coração do projeto. Contém a lógica de análise (analyzer) e ferramentas de apoio (utils).

data/: Onde ficam os resultados. Esta pasta é ignorada pelo Git para garantir a privacidade dos seus dados de scan.

.venv/: Ambiente virtual que isola o projeto, garantindo que ele não quebre outras ferramentas do seu computador.

requirements.txt: A "receita" do projeto. Contém todas as bibliotecas necessárias para que qualquer outra pessoa consiga rodar o laboratório.

## Como Instalar e Usar
Pré-requisitos
Python 3.x instalado.

Git instalado.

Passo a Passo
Clone o repositório:

Bash
git clone https://github.com/Gravestone-henry/cyber_lab_project.git
cd cyber_lab_project
Prepare o ambiente:

Bash
    python -m venv .venv
    # Ative:
    # Windows: .venv\Scripts\activate
    # Linux/Mac: source .venv/bin/activate
    

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    

4.  **Execute o laboratório:**
    ```bash
    python -m src.analyzer.header_sec
    



##  Aprendizados em Cyber Security
Durante o desenvolvimento deste projeto, foram aplicados conceitos de:
*   **Man-in-the-Middle (MitM):** Lidar com interceptações de rede e certificados SSL.
*   **Hardening Web:** Configuração de servidores para reduzir a superfície de ataque.
*   **Automação de Recon:** Uso de Python para acelerar processos de coleta de informações (OSINT).


---
<p align="center">
  <i><font color="grey">
    "Analisando cabeçalhos porque o tráfego é efêmero, mas uma vulnerabilidade é eterna.<br>
    <b>𝔊𝔯𝔞𝔳𝔢𝔰𝔱𝔬𝔫𝔢 ℌ𝔢𝔫𝔯𝔶</b> — Entre logs, códigos e o abismo do servidor." 
  </font></i>
</p>
