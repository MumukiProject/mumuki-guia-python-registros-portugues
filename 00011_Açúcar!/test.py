
  def test_adoçar_menu_adicionar_açúcar_à_sobremesa_se_não_tiver(self):
    menu = {"prato_principal": "bife de lomo", "salada": ["papa", "zanahoria", "arvejas"], "sobremesa": { "ingredientes": ["queso crema", "frambuesas"], "tiempo_de_coccion": 80 }}
    adocar_menu(menu)
    
    self.assertEqual(len(menu["sobremesa"]["ingredientes"]), 3)
    self.assertTrue(menu["sobremesa"]["ingredientes"][-1] == "açúcar" or menu["sobremesa"]["ingredientes"][-1] == "açucar")

  def test_adoçar_menu_adicionar_açúcar_à_sobremesa_mesmo_se_tiver(self):
    menu = {"prato_principal": "milanesas", "salada": ["lechuga", "cebolla"], "sobremesa": { "ingredientes": ["dulce de leche", "vainillas", "azucar"], "tiempo_de_coccion": 60 }}
    adocar_menu(menu)
    
    self.assertEqual(len(menu["sobremesa"]["ingredientes"]), 4)
    self.assertTrue(menu["sobremesa"]["ingredientes"][-1] == "açúcar" or menu["sobremesa"]["ingredientes"][-1] == "açucar")