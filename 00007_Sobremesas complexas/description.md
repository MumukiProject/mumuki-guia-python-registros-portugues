Alguns exercícios atrás, falamos sobre a diferença entre listas e dicionários. Mas isso não significa que não podemos usar as duas estruturas ao mesmo tempo! :wink:

Por exemplo, uma lista pode ser o campo de um dicionário. Veja estes dicionários de sobremesas, dos quais sabemos quantos minutos de cozimento são necessários e seus ingredientes:


```python
pudim_caseiro = { "ingredientes": ["ovos", "leite", "açúcar", "baunilha"], "tempo_de_cozimento": 50 }
cheesecake = { "ingredientes": ["cream cheese", "framboesas"], "tempo_de_cozimento": 80 }
lemon_pie = { "ingredientes": ["suco de limão", "amido de milho", "leite", "ovos"], "tempo_de_cozimento": 65 }
# ... etc ...
```


> Defina a função `mais_dificil_de_cozinhar`, que utilize dois dicionários de sobremesas como argumento e retorne aquele com mais ingredientes dos dois:

> ``` python
ム mais_dificil_de_cozinhar(pudim_caseiro, cheesecake)
{ "ingredientes": ["ovos", "leite", "açúcar", "baunilha"], "tempo_de_cozimento": 50 }
```

