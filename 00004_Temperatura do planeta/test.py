
  def test_temperatura_do_planeta_funciona_para_Mercúrio(self):
    self.assertEqual(temperatura_do_planeta(mercurio), "Mercúrio tem uma temperatura média de 67 graus")

  def test_temperatura_do_planeta_funciona_para_Saturno(self):
    self.assertEqual(temperatura_do_planeta(saturno), "Saturno tem uma temperatura média de -139 graus")

  def test_temperatura_do_planeta_funciona_para_Vênus(self):
    self.assertEqual(temperatura_do_planeta(venus), "Vênus tem uma temperatura média de 462 graus")

  def test_temperatura_do_planeta_funciona_para_Marte(self):
    self.assertEqual(temperatura_do_planeta(marte), "Marte tem uma temperatura média de -63 graus")

  def test_temperatura_do_planeta_funciona_para_qualquer_planeta(self):
    self.assertEqual(temperatura_do_planeta({"nome":"cualquier planeta", "temperatura_media":999}), "cualquier planeta tem uma temperatura média de 999 graus")