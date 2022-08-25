
  def test_endulzar_menu_le_agrega_azucar_al_postre_si_no_tiene(self):
    menu = {"prato_principal": "bife de lomo", "salada": ["papa", "zanahoria", "arvejas"], "sobremesa": { "ingredientes": ["queso crema", "frambuesas"], "tiempo_de_coccion": 80 }}
    adocar_menu(menu)
    
    self.assertEqual(len(menu["sobremesa"]["ingredientes"]), 3)
    self.assertTrue(menu["sobremesa"]["ingredientes"][-1] == "açúcar" or menu["sobremesa"]["ingredientes"][-1] == "açucar")

  def test_endulzar_menu_le_agrega_azucar_al_postre_aun_si_tiene(self):
    menu = {"prato_principal": "milanesas", "salada": ["lechuga", "cebolla"], "sobremesa": { "ingredientes": ["dulce de leche", "vainillas", "azucar"], "tiempo_de_coccion": 60 }}
    adocar_menu(menu)
    
    self.assertEqual(len(menu["sobremesa"]["ingredientes"]), 4)
    self.assertTrue(menu["sobremesa"]["ingredientes"][-1] == "açúcar" or menu["sobremesa"]["ingredientes"][-1] == "açucar")