# converter.py
from estructuras.lineales.stack import Stack 

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

    def _execute_operation(self, op: str, val1: float, val2: float) -> float:
        """Método auxiliar para ejecutar operaciones aritméticas sin usar eval()."""
        if op == '+': return val1 + val2
        if op == '-': return val1 - val2
        if op == '*': return val1 * val2
        if op == '/': return val1 / val2
        if op == '$': return val1 ** val2  # Potencia en Python
        return 0.0

    def infix_to_postfix(self, infix_expr: str) -> str:
        """Convierte una expresión infija válida a posfija usando la clase Stack."""
        operator_stack = Stack()
        postfix_result = []
        
        infix_expr = infix_expr.replace(" ", "")

        for char in infix_expr:
            if char.isalnum():
                postfix_result.append(char)
            elif char == '(':
                operator_stack.push(char)
            elif char == ')':
                while not operator_stack.is_empty() and operator_stack.top() != '(':
                    postfix_result.append(operator_stack.pop())
                operator_stack.pop() 
            elif self._is_operator(char):
                while (not operator_stack.is_empty() and 
                       operator_stack.top() != '(' and 
                       self.precedence.get(operator_stack.top(), 0) >= self.precedence[char]):
                    postfix_result.append(operator_stack.pop())
                operator_stack.push(char)

        while not operator_stack.is_empty():
            postfix_result.append(operator_stack.pop())

        return "".join(postfix_result)

    # =========================================================================
    # NUEVO MÉTODO COMPLEMENTARIO: EVALUACIÓN POSFIJA
    # =========================================================================
    def evaluate_postfix(self, postfix_expr: str) -> float:
        """
        Evalúa una expresión posfija con operandos de un solo dígito 
        utilizando la estructura de datos Stack heredada.
        """
        evaluation_stack = Stack()
        # Quitamos espacios por seguridad
        postfix_expr = postfix_expr.replace(" ", "")

        for char in postfix_expr:
            # Si es dígito, lo casteamos a entero/flotante y va a la pila
            if char.isdigit():
                evaluation_stack.push(float(char))
            
            # Si es operador, extraemos los dos últimos y operamos
            elif self._is_operator(char):
                operand_2 = evaluation_stack.pop()
                operand_1 = evaluation_stack.pop()
                
                # Validación en caso de expresiones posfijas mal formadas
                if operand_1 is None or operand_2 is None:
                    raise ValueError("Expresión posfija inválida (Faltan operandos).")
                
                resultado_parcial = self._execute_operation(char, operand_1, operand_2)
                evaluation_stack.push(resultado_parcial)

        # El resultado final queda en el Top de la pila
        resultado_final = evaluation_stack.pop()
        
        if not evaluation_stack.is_empty():
            raise ValueError("Expresión posfija inválida (Sobran operandos).")
            
        return resultado_final