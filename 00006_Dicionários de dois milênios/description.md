No exercício anterior modificamos o caminho do dicionário, mas não usamos sua data de criação. Vamos usá-la! Queremos saber se um arquivo é do milênio passado, o que acontece quando o ano é anterior a 2000 :back: :


```python
ム e_do_milenio_passado({ "caminho": "D:\fotonascimento.jpg", "criacao": "14/09/1989" })
True

ム e_do_milenio_passado({ "caminho": "D:\fotocasamento.jpg", "criacao": "25/09/2017" })
False
```

> Defina a função `e_do_milenio_passado`. A função `ano` irá ajudá-lo, ela funciona assim:
>
```python
ム ano("04/11/1993")
1993
```


