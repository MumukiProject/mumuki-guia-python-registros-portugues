
  def test_un_postre_de_una_hora_y_media_no_es_rapido(self):
    postres_rapidos = [ { "ingredientes": ["galletitas", "dulceDeLeche", "crema"], "tempo_de_cozimento": 20 }, { "ingredientes": ["huevos", "leche", "azúcar", "vainilla"], "tempo_de_cozimento": 50 } ]
    postre_de_leche = {"ingredientes":["leche"], "tempo_de_cozimento":90}
    adicionar_a_sobremesas_rapidas(postres_rapidos, postre_de_leche)
    self.assertEqual(len(postres_rapidos), 2)
  
  def test_un_postre_de_media_hora_es_rapido(self):
    postres_rapidos = [ { "ingredientes": ["galletitas", "dulceDeLeche", "crema"], "tempo_de_cozimento": 20 }, { "ingredientes": ["huevos", "leche", "azúcar", "vainilla"], "tempo_de_cozimento": 50 } ]
    postre_de_leche = {"ingredientes":["leche"], "tempo_de_cozimento":30}
    adicionar_a_sobremesas_rapidas(postres_rapidos, postre_de_leche)
    self.assertEqual(len(postres_rapidos), 3)
    self.assertEqual(postres_rapidos[-1], postre_de_leche)

  def test_un_postre_de_una_hora_es_rapido(self):
    postres_rapidos = [ { "ingredientes": ["galletitas", "dulceDeLeche", "crema"], "tempo_de_cozimento": 20 }, { "ingredientes": ["huevos", "leche", "azúcar", "vainilla"], "tempo_de_cozimento": 50 } ]
    postre_de_leche = {"ingredientes":["leche"], "tempo_de_cozimento": 60}
    adicionar_a_sobremesas_rapidas(postres_rapidos, postre_de_leche)
    self.assertEqual(len(postres_rapidos), 3)
    self.assertEqual(postres_rapidos[-1], postre_de_leche)