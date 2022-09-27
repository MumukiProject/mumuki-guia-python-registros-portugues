
  def test_um_arquivo_de_2012_não_é_do_milênio_passado(self):
    archivo = {"percurso":"", "criacao":"01/01/2012"}
    self.assertFalse(e_do_milenio_passado(archivo))
  
  def test_um_arquivo_de_2000_não_é_do_milênio_passado(self):
    archivo = {"percurso":"", "criacao":"01/01/2000"}
    self.assertFalse(e_do_milenio_passado(archivo))
  
  def test_um_arquivo_de_1999_é_do_milênio_passado(self):
    archivo = {"percurso":"", "criacao":"23/09/1994"}
    self.assertTrue(e_do_milenio_passado(archivo))
  
  def test_um_arquivo_de_1994_é_do_milênio_passado(self):
    archivo = {"percurso":"", "criacao":"23/09/1994"}
    self.assertTrue(e_do_milenio_passado(archivo))