
  def test_mover_arquivo_muda_a_rota_para_um_arquivo_ao_passar_para_uma_rota_nova(self):
    archivo = {"caminho":"/usr/miarchivo.doc", "criacao":"15/02/2019"}
    mover_arquivo(archivo, "/home/miarchivo.doc")
    self.assertEqual(archivo["caminho"], "/home/miarchivo.doc")

  def test_mover_arquivo_mantém_a_rota_em_um_arquivo_se_passa_a_mesma_rota(self):
    archivo = {"caminho":"/usr/miarchivo.doc", "criacao":"15/02/2019"}
    mover_arquivo(archivo, "/usr/miarchivo.doc")
    self.assertEqual(archivo["caminho"], "/usr/miarchivo.doc")

  def test_mover_arquivo_não_modifica_a_data_da_criação_do_arquivo(self):
    archivo = {"caminho":"/usr/miarchivo.doc", "criacao":"15/02/2019"}
    mover_arquivo(archivo, "/home/miarchivo.doc")
    self.assertEqual(archivo["criacao"], "15/02/2019")