import time
import random

class Sensore:
    def __init__(self, id_sensore, tipo):
        self.id = id_sensore
        self.tipo = tipo
        self.valore_attuale = 0

    def genera_dato(self):
        # Simula un valore di temperatura o umidità
        if self.tipo == "Temperatura":
            self.valore_attuale = round(random.uniform(18.0, 25.0), 2)
        elif self.tipo == "Umidità":
            self.valore_attuale = round(random.uniform(40.0, 60.0), 2)
        else:
            self.valore_attuale = random.randint(0, 100) 

class Dashboard:
    def __init__(self, sensori):
        self.sensori = sensori
        self.log_dati = {s.id: [] for s in sensori} # Dizionario per storico dati
        self.max_storico = 5 # Dati  in memoria per ogni sensore

    def aggiorna_e_mostra(self):
        print("\n" * 50) # Pulisce il terminale
        print("--- Monitoraggio Dati Live (Python Terminal Dashboard) ---")
        print(f"Aggiornato il: {time.strftime('%H:%M:%S')}\n")

        for sensore in self.sensori:
            sensore.genera_dato()
            self.log_dati[sensore.id].append(sensore.valore_attuale)
            # Limita lo storico
            if len(self.log_dati[sensore.id]) > self.max_storico:
                self.log_dati[sensore.id].pop(0) # Rimuove il dato più vecchio

            # Visualizzazione della barra di "progresso" o stato
            if sensore.tipo == "Temperatura":
                simbolo = "🌡️" if sensore.valore_attuale > 22 else "❄️"
                bar_status = "█" * int(sensore.valore_attuale - 15)
                print(f"{sensore.tipo} [{sensore.id}]: {simbolo} {sensore.valore_attuale}°C |{bar_status}{' '*(10-len(bar_status))}|")
            elif sensore.tipo == "Umidità":
                simbolo = "💧" if sensore.valore_attuale > 50 else "☀️"
                bar_status = "█" * int(sensore.valore_attuale / 10)
                print(f"{sensore.tipo} [{sensore.id}]: {simbolo} {sensore.valore_attuale}%  |{bar_status}{' '*(10-len(bar_status))}|")
            
            # Mostra storico
            storico_str = " -> ".join([str(v) for v in self.log_dati[sensore.id]])
            print(f"  Storico: [{storico_str}]\n")


# Creazione e Avvio della Dashboard
sensore_temp = Sensore("T-001", "Temperatura")
sensore_umid = Sensore("H-002", "Umidità")
sensore_pressione = Sensore("P-003", "Pressione") 

dashboard = Dashboard([sensore_temp, sensore_umid, sensore_pressione])

print("Avvio del monitoraggio. Premi CTRL+C per interrompere.")
try:
    while True:
        dashboard.aggiorna_e_mostra()
        time.sleep(2) # Aggiorna ogni 2 secondi
except KeyboardInterrupt:
    print("\nMonitoraggio interrotto. Arrivederci!")