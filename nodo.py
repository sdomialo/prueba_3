class Nodo:
    """
    A class representing a node.
    """
    def __init__(self, valor):
        """
        Initialize a new instance of the Nodo class.
        
        Args:
            valor: The value of the node.
        """
        self.valor = valor
        self.siguiente = None

    def obtener_valor(self):
        """
        Get the value of the node.
        
        Returns:
            The value of the node.
        """
        return self.valor

    def obtener_siguiente(self):
        """
        Get the next node.
        
        Returns:
            The next node.
        """
        return self.siguiente

    def establecer_siguiente(self, siguiente):
        """
        Set the next node.
        
        Args:
            siguiente: The next node.
        """
        self.siguiente = siguiente
        
        