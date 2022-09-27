
  def test_cristo_redentor_se_chama_Cristo_Redentor(self):
    self.assertEqual(cristo_redentor["nome"].lower(), "cristo redentor")

  def test_cristo_redentor_é_do_Rio_de_Janeiro(self):
    self.assertEqual(cristo_redentor["localizacao"], "Rio de Janeiro, Brasil")

  def test_cristo_redentor_tem_seu_ano_de_construção(self):
    self.assertEqual(cristo_redentor["ano_da_construcao"], 1922)

  def test_elevador_lacerda_se_chama_Elevador_Lacerda(self):
    self.assertEqual(elevador_lacerda["nome"].lower(), "elevador lacerda")

  def test_elevador_lacerda_é_de_Salvador_Brasil(self):
    self.assertEqual(elevador_lacerda["localizacao"], "Salvador, Brasil")

  def test_elevador_lacerda_tem_seu_ano_de_construção(self):
    self.assertEqual(elevador_lacerda["ano_da_construcao"], 1873)