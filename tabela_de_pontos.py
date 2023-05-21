class TabelaDePontos:
      def __init__(self):
        self.multiplicador = 2
        self.pontos_t1 = 0
        self.pontos_t2 = 0
      
      def pontuar(self, id_time):
          if id_time == 1:
              self.pontos_t1 += self.multiplicador 
          elif id_time == 2:
              self.pontos_t2 += self.multiplicador 
          return

      def aumentar_multiplicador(self):
          self.multiplicador += 2
          return
      
      def is_termino(self):
          if self.pontos_t1 >= 12:
            return 1
          if self.pontos_t2 >= 12:
            return 2
          return 0
          
      def limpar_estado_de_jogo(self):
          self.multiplicador = 2
        