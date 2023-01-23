Você se lembra quando vimos que uma lista pode ser composta de outras listas? Com os dicionários, se aplica a mesma ideia! :hushed: Se tivermos alguma estrutura de dados complexa, pode acontecer que não seja suficiente representá-la apenas por meio de strings, números, booleanos e listas, mas precisaremos de _outro_ dicionário dentro.

Você não pode viver de sobremesas! Bom, talvez sim, mas vamos continuar com uma alimentação saudável :stuck_out_tongue_winking_eye:. Usando um dicionário, queremos modelar um menu completo que é composto por: um prato principal :curry:, os vegetais da salada que acompanham o prato principal :tomato:, e uma sobremesa :custard: como já vínhamos trabalhando, ou seja, continua sendo um dicionário.

O exemplo a seguir mostra um menu com berinjelas à milanesa como prato principal, uma salada de batata, cenoura e ervilhas como acompanhamento e um cheesecake de sobremesa. Como o dicionário é um pouco longo, e para torná-lo mais legível, vamos escrevê-lo da seguinte forma:


``` python
menu_do_dia = {
  "prato_principal": "berinjelas à milanesa",
  "salada": ["batata", "cenoura", "ervilhas"],
  "sobremesa": { "ingredientes": ["cream cheese", "framboesas"], "tempo_de_cozimento": 80 }
}
```

> Conheça os `ingredientes` da `sobremesa` do `menu_infantil`. É um dicionário dentro de um dicionário, então vamos ter que acessar primeiro o campo `dessert` e depois o campo `ingredientes`. Se você não consegue descobrir como, você pode olhar na dica. :mag:
