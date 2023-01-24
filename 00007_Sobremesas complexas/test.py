
  def test_o_pudim_caseiro_é_mais_difícil_de_cozinhar_do_que_o_cheesecake(self):
    self.assertEqual(mais_dificil_de_cozinhar(pudim_caseiro, cheesecake), pudim_caseiro, "mais_dificil_de_cozinhar(pudim_caseiro, cheesecake) deve retornar pudim_caseiro")

  def test_o_pudim_caseiro_é_mais_difícil_de_cozinhar_do_que_o_cheesecake_com_argumentos_trocados(self):
    self.assertEqual(mais_dificil_de_cozinhar(cheesecake, pudim_caseiro), pudim_caseiro, "mais_dificil_de_cozinhar(cheesecake, pudim_caseiro) deve retornar pudim_caseiro")

  def test_o_lemon_pie_é_mais_difícil_de_cozinhar_do_que_o_cheesecake(self):
    self.assertEqual(mais_dificil_de_cozinhar(cheesecake, lemon_pie), lemon_pie, "mais_dificil_de_cozinhar(cheesecake, lemon_pie) deve retornar lemon_pie")

  def test_o_lemon_pie_é_mais_difícil_de_cozinhar_do_que_o_cheesecake_com_argumentos_trocados(self):
    self.assertEqual(mais_dificil_de_cozinhar(lemon_pie, cheesecake), lemon_pie, "mais_dificil_de_cozinhar(lemon_pie, cheesecake) deve retornar lemon_pie")

  def test_se_duas_sobremesas_são_igualmente_difíceis_de_cozinhar_retorne_qualquer_uma_das_duas(self):
    mas_dificil = mais_dificil_de_cozinhar(pudim_caseiro, lemon_pie)
    self.assertTrue(mas_dificil == pudim_caseiro or mas_dificil == lemon_pie)
