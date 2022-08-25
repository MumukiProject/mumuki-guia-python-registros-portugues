
  def test_un_archivo_del_2012_no_es_del_milenio_pasado(self):
    archivo = {"percurso":"", "criacao":"01/01/2012"}
    self.assertFalse(e_do_milenio_passado(archivo))
  
  def test_un_archivo_de_2000_no_es_del_milenio_pasado(self):
    archivo = {"percurso":"", "criacao":"01/01/2000"}
    self.assertFalse(e_do_milenio_passado(archivo))
  
  def test_un_archivo_de_1999_es_del_milenio_pasado(self):
    archivo = {"percurso":"", "criacao":"23/09/1994"}
    self.assertTrue(e_do_milenio_passado(archivo))
  
  def test_un_archivo_de_1994_es_del_milenio_pasado(self):
    archivo = {"percurso":"", "criacao":"23/09/1994"}
    self.assertTrue(e_do_milenio_passado(archivo))