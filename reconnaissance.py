import nmap
import threading

def run_nmap_scan(target):
    nm = nmap.PortScanner()
    nm.scan(target, '22-443')
    return nm.all_hosts()

def start_recon(target):
    threads = []
    results = []

    def run_thread(target, results):
        results.append(run_nmap_scan(target))

    for i in range(5):  # Start 5 threads for faster scanning
        t = threading.Thread(target=run_thread, args=(target, results))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return results
