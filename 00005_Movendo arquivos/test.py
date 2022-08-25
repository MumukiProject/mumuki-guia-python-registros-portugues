
  def test_mover_archivo_le_cambia_la_ruta_a_un_archivo_al_pasar_una_ruta_nueva(self):
    archivo = {"percurso":"/usr/miarchivo.doc", "criacao":"15/02/2019"}
    mover_arquivo(archivo, "/home/miarchivo.doc")
    self.assertEqual(archivo["percurso"], "/home/miarchivo.doc")

  def test_mover_archivo_le_mantiene_la_ruta_a_un_archivo_si_se_pasa_la_misma(self):
    archivo = {"percurso":"/usr/miarchivo.doc", "criacao":"15/02/2019"}
    mover_arquivo(archivo, "/usr/miarchivo.doc")
    self.assertEqual(archivo["percurso"], "/usr/miarchivo.doc")

  def test_mover_archivo_no_modifica_la_fecha_de_creacion_del_archivo(self):
    archivo = {"percurso":"/usr/miarchivo.doc", "criacao":"15/02/2019"}
    mover_arquivo(archivo, "/home/miarchivo.doc")
    self.assertEqual(archivo["criacao"], "15/02/2019")