import socket
from src.utils.logger import get_logger

log = get_logger("Scanner")

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((ip, port))
            if result == 0:
                log.info(f"Porta {port} ABERTA em {ip}")
            return result == 0
    except Exception as e:
        log.error(f"Erro ao escanear {ip}:{port} -> {e}")

if __name__ == "__main__":
    target = "127.0.0.1"
    ports = [21, 22, 80, 443, 3306]
    
    log.info(f"Iniciando scan em {target}...")
    for p in ports:
        scan_port(target, p)