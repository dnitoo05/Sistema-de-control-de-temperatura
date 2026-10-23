#Nito Oropeza Diego Fernando
#Ordoñez Calderón Angel

#Arquitecturas Embebidas Automotrices
#Practica 2

#Importamos librerias a utilizar
from machine import Pin, ADC
from time import sleep, sleep_ms 

#Configuramos pin del motor
motor = Pin(15,Pin.OUT)

#Configuramos pin del sensor
adc = ADC(Pin(36))
adc.atten(ADC.ATTN_11DB)

#Temperatura de encendido del ventilador
temperatura = 30.0

print("Monitor de tempreratura")

while True:
    muestras = 10
    lectura_acumulada = 0
    
    for _ in range(muestras):
        lectura_acumulada =+ adc.read()
        sleep_ms(10)
        
    lectura_promedio = lectura_acumulada / muestras
    
    v_sensor = lectura_promedio *(3.3/4095.0)
    
    temp = v_sensor * 100
    
    print(f"Temperatura: {temp:.1f} °C")
    
    if temp >= temperatura:
        motor.on()
    else:
        motor.off()
        
    sleep(1)

