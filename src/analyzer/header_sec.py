import requests
import urllib3
import os
from datetime import datetime
from src.utils.logger import get_logger


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

log = get_logger("Analyzer")

def check_security_headers(url):
    """Analisa cabeçalhos e retorna um resumo dos resultados"""
    try:
        log.info(f"Escaneando: {url}")
        response = requests.get(url, timeout=10, verify=False)
        headers = response.headers
        
        target_headers = {
            "Content-Security-Policy": "XSS Protection",
            "Strict-Transport-Security": "HSTS",
            "X-Frame-Options": "Clickjacking Protection",
            "X-Content-Type-Options": "MIME Sniffing"
        }
        
        report_lines = [f"Relatorio para: {url}", f"Data: {datetime.now()}", "-"*40]
        
        for h, desc in target_headers.items():
            status = "[V] PRESENTE" if h in headers else "[X] AUSENTE"
            report_lines.append(f"{status} | {h}")
            
        return "\n".join(report_lines)
                
    except Exception as e:
        return f"Erro ao acessar {url}: {e}"

def save_report(domain, content):
    """Salva o resultado na pasta data/"""
   
    clean_name = domain.replace("https://", "").replace("http://", "").replace("/", "")
    filepath = f"data/report_{clean_name}.txt"
    
    with open(filepath, "w") as f:
        f.write(content)
    log.info(f"Relatorio salvo: {filepath}")

if __name__ == "__main__":
    
    targets = [
        "https://www.google.com",
        "https://www.github.com",
        "https://www.microsoft.com"
    ]
    
    print("\n--- INICIANDO SCAN EM MASSA ---")
    for site in targets:
        result = check_security_headers(site)
        print(result + "\n")
        save_report(site, result)
    print("--- SCAN FINALIZADO ---")