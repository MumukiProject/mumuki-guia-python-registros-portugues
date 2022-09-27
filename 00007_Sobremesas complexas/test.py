
  def setUp(self):
    self.pudim_caseiro = { "ingredientes": ["ovos", "leite", "açúcar", "baunilha"], "tempo_de_cozimento": 50 }
    self.cheesecake = { "ingredientes": ["cream cheese", "framboesas"], "tempo_de_cozimento": 80 }
    self.lemon_pie = { "ingredientes": ["suco de limão", "amido de milho", "leite", "ovos"], "tempo_de_cozimento": 65 }
    
  def test_o_pudim_caseiro_é_mais_difícil_de_cozinhar_do_que_o_cheesecake(self):
    self.assertEqual(mais_dificil_de_cozinhar(self.pudim_caseiro, self.cheesecake), self.pudim_caseiro)
  
  def test_o_lemon_pie_é_mais_difícil_de_cozinhar_do_que_o_cheesecake(self):
    self.assertEqual(mais_dificil_de_cozinhar(self.cheesecake, self.lemon_pie), self.lemon_pie)
  
  def test_se_duas_sobremesas_são_igualmente_difíceis_de_cozinhar_retorne_qualquer_uma_das_duas(self):
    mas_dificil = mais_dificil_de_cozinhar(self.pudim_caseiro, self.lemon_pie)
    self.assertTrue(mas_dificil == self.pudim_caseiro or mas_dificil == self.lemon_pie)