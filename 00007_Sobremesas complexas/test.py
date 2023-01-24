
  def test_o_pudim_caseiro_é_mais_difícil_de_cozinhar_do_que_o_cheesecake(self):
    self.assertEqual(mais_dificil_de_cozinhar(pudim_caseiro, cheesecake), pudim_caseiro, "mais_dificil_de_cozinhar(pudim_caseiro, cheesecake) deve retornar pudim_caseiro")

  def test_o_pudim_caseiro_é_mais_difícil_de_cozinhar_do_que_o_cheesecake_com_argumentos_trocados(self):
    self.assertEqual(mais_dificil_de_cozinhar(cheesecake, pudim_caseiro), pudim_caseiro, "mais_dificil_de_cozinhar(cheesecake, pudim_caseiro) deve retornar pudim_caseiro")

  def test_o_lemon_pie_é_mais_difícil_de_cozinhar_do_que_o_cheesecake(self):
    self.assertEqual(mais_dificil_de_cozinhar(cheesecake, lemon_pie), lemon_pie, "mais_dificil_de_cozinhar(cheesecake, lemon_pie) deve retornar lemon_pie")

  def test_o_lemon_pie_é_mais_difícil_de_cozinhar_do_que_o_cheesecake_com_argumentos_trocados(self):
    self.assertEqual(mais_dificil_de_cozinhar(lemon_pie, cheesecake), lemon_pie, "mais_dificil_de_cozinhar(lemon_pie, cheesecake) deve retornar lemon_pie")

  def test_o_pudim_caseiro_é_mais_difícil_de_cozinhar_do_que_o_cheesecake_extra_doce(self):
    self.assertEqual(mais_dificil_de_cozinhar(pudim_caseiro, cheesecake_extra_doce), pudim_caseiro, "mais_dificil_de_cozinhar(pudim_caseiro, cheesecake_extra_doce) deve retornar pudim_caseiro (porque tem mais um ingrediente)")

  def test_o_pudim_caseiro_é_mais_difícil_de_cozinhar_do_que_o_cheesecake_extra_doce_com_argumentos_trocados(self):
    self.assertEqual(mais_dificil_de_cozinhar(cheesecake_extra_doce, pudim_caseiro), pudim_caseiro, "mais_dificil_de_cozinhar(cheesecake_extra_doce, pudim_caseiro) deve retornar pudim_caseiro (porque tem mais um ingrediente)")

  def test_o_cheesecake_extra_doce_é_mais_difícil_de_cozinhar_do_que_o_cheesecake(self):
    self.assertEqual(mais_dificil_de_cozinhar(cheesecake, cheesecake_extra_doce), cheesecake_extra_doce, "mais_dificil_de_cozinhar(cheesecake, cheesecake_extra_doce) deve retornar cheesecake_extra_doce (porque tem mais um ingrediente)")

  def test_o_cheesecake_extra_doce_é_mais_difícil_de_cozinhar_do_que_o_cheesecake_com_argumentos_trocados(self):
    self.assertEqual(mais_dificil_de_cozinhar(cheesecake_extra_doce, cheesecake), cheesecake_extra_doce, "mais_dificil_de_cozinhar(cheesecake_extra_doce, cheesecake) deve retornar cheesecake_extra_doce (porque tem mais um ingrediente)")

  def test_se_duas_sobremesas_são_igualmente_difíceis_de_cozinhar_retorne_qualquer_uma_das_duas(self):
    mas_dificil = mais_dificil_de_cozinhar(pudim_caseiro, lemon_pie)
    self.assertTrue(mas_dificil == pudim_caseiro or mas_dificil == lemon_pie)
