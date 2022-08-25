
  def setUp(self):
    self.pudim_caseiro = { "ingredientes": ["ovos", "leite", "açúcar", "baunilha"], "tempo_de_cozimento": 50 }
    self.cheesecake = { "ingredientes": ["cream cheese", "framboesas"], "tempo_de_cozimento": 80 }
    self.lemon_pie = { "ingredientes": ["suco de limão", "amido de milho", "leite", "ovos"], "cook_time": 65 }
    
  def test_el_flan_casero_es_mas_dificil_de_cocinar_que_el_cheesecake(self):
    self.assertEqual(mais_dificil_de_cozinhar(self.pudim_caseiro, self.cheesecake), self.pudim_caseiro)
  
  def test_el_lemon_pie_es_mas_dificil_de_cocinar_que_el_cheesecake(self):
    self.assertEqual(mais_dificil_de_cozinhar(self.cheesecake, self.lemon_pie), self.lemon_pie)
  
  def test_si_dos_postres_son_igual_de_dificiles_de_cocinar_devuelve_cualquiera_de_los_dos(self):
    mas_dificil = mais_dificil_de_cozinhar(self.pudim_caseiro, self.lemon_pie)
    self.assertTrue(mas_dificil == self.pudim_caseiro or mas_dificil == self.lemon_pie)