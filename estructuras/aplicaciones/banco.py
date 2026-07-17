# controlador_banco.py
from datetime import datetime
# Importación limpia y directa gracias a que estás en la raíz
from estructuras.lineales.queue import Queue

class ControladorBanco:
    def __init__(self):
        self.contador_turnos = 0
        self.banco_cerrado = False
        self.cola_espera = Queue()
        self.historial_tiempos = []  
        self.total_atendidos = 0

    def registrar_nuevo_turno(self):
        if self.banco_cerrado:
            return None
            
        self.contador_turnos += 1
        hora_creacion = datetime.now()
        
        datos_cliente = {
            "numero": self.contador_turnos,
            "hora_llegada": hora_creacion
        }
        self.cola_espera.enqueue(datos_cliente)
        return self.contador_turnos

    def procesar_atencion(self):
        if self.cola_espera.isEmpty():
            return None
            
        datos_cliente = self.cola_espera.dequeue()
        numero_turno = datos_cliente["numero"]
        hora_llegada = datos_cliente["hora_llegada"]
        hora_atencion = datetime.now()
        
        # CORRECCIÓN CRÍTICA: Obtenemos los segundos netos y los redondeamos
        duracion = hora_atencion - hora_llegada
        segundos_transcurridos = round(duracion.total_seconds())
        
        # Evita que por un delay de milisegundos de la CPU dé números negativos o raros
        if segundos_transcurridos < 0:
            segundos_transcurridos = 0
        
        self.historial_tiempos.append(segundos_transcurridos)
        self.total_atendidos += 1
        
        # Formateo limpio: Minutos y Segundos exactos
        minutos = segundos_transcurridos // 60
        segundos = segundos_transcurridos % 60
        tiempo_formateado = f"{minutos}m {segundos}s"
        
        hora_atencion_str = hora_atencion.strftime("%H:%M:%S")
        
        return {
            "numero": numero_turno,
            "tiempo_transcurrido": tiempo_formateado,
            "hora_atencion": hora_atencion_str
        }

    def intentar_cierre(self):
        self.banco_cerrado = True
        return self.cola_espera.size

    def obtener_metricas_finales(self):
        if self.total_atendidos > 0:
            promedio_segundos = sum(self.historial_tiempos) / self.total_atendidos
            promedio_formateado = f"{int(promedio_segundos // 60)}m {int(promedio_segundos % 60)}s"
        else:
            promedio_formateado = "0m 0s"
            
        return {
            "total_atendidos": str(self.total_atendidos),
            "tiempo_promedio": promedio_formateado
        }