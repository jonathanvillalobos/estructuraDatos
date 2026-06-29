# converter.py
from estructuras.lineales.stack import Stack  # Cambia 'tu_archivo_de_pila' por el nombre real de tu archivo (.py)

class ExpressionConverter:
    def __init__(self):
        # Definimos la precedencia matemática de los operadores
        self.precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '$': 3  # Potencia
        }

    def _is_operator(self, char: str) -> bool:
        """Método auxiliar interno para identificar operadores."""
        return char in self.precedence

    def infix_to_postfix(self, infix_expr: str) -> str:
        """Convierte una expresión infija válida a posfija usando la clase Stack de clase."""
        operator_stack = Stack()
        postfix_result = []
        
        # Quitamos espacios en blanco para procesar limpiamente caracter por caracter
        infix_expr = infix_expr.replace(" ", "")

        for char in infix_expr:
            # Caso 1: Es un operando (Letra o Número) -> Va directo al resultado
            if char.isalnum():
                postfix_result.append(char)
                
            # Caso 2: Paréntesis de apertura -> Se guarda en la pila como frontera
            elif char == '(':
                operator_stack.push(char)
                
            # Caso 3: Paréntesis de cierre -> Desapilar hasta encontrar el '('
            elif char == ')':
                while not operator_stack.is_empty() and operator_stack.top() != '(':
                    postfix_result.append(operator_stack.pop())
                operator_stack.pop()  # Sacamos el '(' sobrante de la pila y lo descartamos
                
            # Caso 4: Es un operador (+, -, *, /, $)
            elif self._is_operator(char):
                # Mientras la pila no esté vacía, no sea un '(' y el operador en el 'top' 
                # tenga mayor o igual prioridad que el operador actual, se desapila.
                while (not operator_stack.is_empty() and 
                       operator_stack.top() != '(' and 
                       self.precedence.get(operator_stack.top(), 0) >= self.precedence[char]):
                    postfix_result.append(operator_stack.pop())
                
                # Al terminar la condición, el operador actual se guarda en la pila
                operator_stack.push(char)

        # Caso final: Vaciar todo lo que haya quedado rezagado en la pila al terminar la expresión
        while not operator_stack.is_empty():
            postfix_result.append(operator_stack.pop())

        return "".join(postfix_result)