class World:
    """
    Representa o conjunto de todos os objetos na simulacao.
    """

    WIDTH = 800
    HEIGHT = 600

    def __init__(self, objects=[], gravity=0):
        self.objects = list(objects)
        self.gravity = gravity

    def draw(self):
        """
        Desenha todos objetos na tela.
        """
        for obj in self.objects:
            obj.draw()

    def update(self, dt):
        """
        Atualiza o estado da simulacao, evoluindo por um intervalo dt.
        """
        for obj in self.objects:
            obj.update(dt)

    def add(self, obj):
        """
        Adiciona objeto ao mundo.
        """
        self.objects.append(obj)
