
  def test_cristo_redentor_se_chama_Cristo_Redentor(self):
    self.assertEqual(cristo_redentor["nome"].lower(), "Cristo Redentor")

  def test_cristo_redentor_é_do_Rio_de_Janeiro(self):
    self.assertEqual(cristo_redentor["localizacao"], "Rio de Janeiro, Brasil")

  def test_cristo_redentor_tiene_su_anio_de_construccion(self):
    self.assertEqual(cristo_redentor["ano_da_construcao"], 1922)

  def test_elevador_lacerda_se_chama_Elevador_Lacerda(self):
    self.assertEqual(elevador_lacerda["nome"].lower(), "Elevador Lacerda")

  def test_elevador_lacerda_é_do_Rosario_Argentina(self):
    self.assertEqual(elevador_lacerda["localizacao"], "Salvador, Brasil")

  def test_elevador_lacerda_tiene_su_anio_de_construccion(self):
    self.assertEqual(elevador_lacerda["ano_da_construcao"], 1873)