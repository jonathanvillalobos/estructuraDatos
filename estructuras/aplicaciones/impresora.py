# controlador_fifo.py

# Importación de tu estructura de datos Queue
# (Ajusta la ruta de importación si tu archivo queue.py está en otra carpeta)
from estructuras.lineales.queue import Queue  

# ==========================================
# 1. MODELO DE DATOS
# ==========================================

class TrabajoImpresion:
    """Representa cada documento encolado."""
    def __init__(self, usuario: str, documento: str, paginas: int):
        self.usuario = usuario
        self.documento = documento
        self.paginas = paginas

    def __str__(self):
        return f"[{self.usuario}] {self.documento} ({self.paginas} págs.)"


# ==========================================
# 2. CONTROLADOR DE OPERACIONES FIFO
# ==========================================

class ControladorFIFO:
    """
    Controlador que aísla la lógica de la interfaz. 
    Maneja la cola de impresión y valida las restricciones del sistema.
    """
    def __init__(self):
        # Se inicializa tu clase Queue importada
        self._cola_impresion = Queue()

    def agregar_trabajo(self, usuario: str, documento: str, paginas: int) -> tuple[bool, str]:
        """
        Intenta encolar un nuevo trabajo de impresión.
        Retorna una tupla (éxito, mensaje_de_error_o_confirmacion).
        """
        # Validación mínima: Campos vacíos
        if not usuario.strip() or not documento.strip():
            return False, "Error: No se aceptan campos vacíos."

        # Validación mínima: Páginas menores que 1
        if paginas < 1:
            return False, "Error: El número de páginas debe ser mayor o igual a 1."

        # Encolar elemento
        nuevo_trabajo = TrabajoImpresion(usuario.strip(), documento.strip(), paginas)
        self._cola_impresion.enqueue(nuevo_trabajo)
        return True, f"Trabajo '{documento}' agregado con éxito."

    def procesar_siguiente(self) -> tuple[TrabajoImpresion, str] | tuple[None, str]:
        """
        Retira y retorna el elemento al frente (FIFO).
        Retorna una tupla (TrabajoImpresion, mensaje) o (None, mensaje de cola vacía).
        """
        if self._cola_impresion.isEmpty():
            return None, "La cola de impresión está vacía."

        trabajo_atendido = self._cola_impresion.dequeue()
        return trabajo_atendido, f"Se ha impreso exitosamente: {trabajo_atendido.documento}"

    def obtener_pendientes(self) -> list:
        """Retorna todos los trabajos actualmente encolados en su orden correspondiente."""
        return self._cola_impresion.to_list()

    def obtener_siguiente_en_espera(self) -> TrabajoImpresion | None:
        """Consulta el elemento al frente de la cola sin retirarlo."""
        return self._cola_impresion.firstQueue()

    def obtener_total_pendientes(self) -> int:
        """Retorna la cantidad actual de trabajos en la cola."""
        return self._cola_impresion.size