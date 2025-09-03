# Importa as bibliotecas necessárias
from machine import Pin, PWM
import time

# --- Configuração dos Pinos ---
BUZZER_PIN = 10
LED_PIN_1 = 13
LED_PIN_2 = 12

# --- Dicionário de Notas Musicais ---
NOTES = {
    's': 0,
    'A3': 220, 'B3': 247, 'C4': 262, 'D4': 294, 'E4': 330,
    'F4': 349, 'G4': 392, 'A4': 440,
}

# --- A Melodia de "Noite Feliz" ---
# Formato: ('nota', duração_relativa)
tempo = 0.3  # Tempo mais lento, ideal para esta canção

melody = [
    # "Noite feliz, noite feliz"
    ('G4', 3), ('A4', 1.5), ('G4', 1.5), ('E4', 3),
    ('G4', 3), ('A4', 1.5), ('G4', 1.5), ('E4', 3),
    # "Oh, Senhor, Deus de amor"
    ('D4', 4), ('D4', 2), ('B3', 4),
    ('C4', 4), ('C4', 2), ('B3', 4),
    # "Pobrezinho, nasceu em Belém"
    ('A4', 3), ('A4', 1.5), ('C4', 1.5), ('B3', 1.5), ('A4', 1.5),
    ('G4', 1.5), ('A4', 1.5), ('G4', 3), ('E4', 3),
    # "Eis na lapa, Jesus nosso bem"
    ('A4', 3), ('A4', 1.5), ('C4', 1.5), ('B3', 1.5), ('A4', 1.5),
    ('G4', 1.5), ('A4', 1.5), ('G4', 3), ('E4', 3),
    # "Dorme em paz, ó Jesus"
    ('D4', 4), ('D4', 2), ('F4', 3), ('D4', 1.5), ('B3', 3),
    ('C4', 6)
]

# Função para tocar uma única nota e piscar LEDs
def play_tone(pwm, frequency, duration_multiplier):
    duration = duration_multiplier * tempo
    
    # Acende os LEDs no início da nota
    led.on()
    ledazul.off()
    
    if frequency > 0:
        pwm.freq(frequency)
        pwm.duty_u16(20000)  # Ajustei o volume um pouco, pode mudar se quiser
    
    time.sleep(duration)
    pwm.duty_u16(0)  # Para o som
    
    # Inverte os LEDs na pausa entre as notas
    led.off()
    ledazul.on()
    time.sleep(0.05)
    ledazul.off()

# --- Programa Principal ---
if __name__ == '__main__':
    # Inicializa o pino do buzzer usando PWM
    buzzer = PWM(Pin(BUZZER_PIN))
    
    # Inicializa os LEDs
    led = Pin(LED_PIN_1, Pin.OUT)
    ledazul = Pin(LED_PIN_2, Pin.OUT)

    print("Tocando Noite Feliz...")

    try:
        # Loop para tocar cada nota da melodia
        for note, duration_multiplier in melody:
            frequency = NOTES.get(note, 0)
            play_tone(buzzer, frequency, duration_multiplier)

        print("Feliz Natal!")

    finally:
        # Garante que tudo será desligado no final
        buzzer.deinit()
        led.off()
        ledazul.off()