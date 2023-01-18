No momento estávamos criando e consultando dicionários. Não seria interessante poder... modificá-los? :smirk:

A sintaxe para modificar os campos do dicionário é muito semelhante ao que fazemos para alterar os valores das variáveis. Por exemplo, para alterar a temperatura de um planeta:


```python
ム saturno["temperatura_media"] = -140
```
Agora imagine que temos um dicionário para representar um arquivo, do qual conhecemos seu caminho (onde está armazenado) e a data da criação. Se quisermos mudar o percurso, podemos fazer o seguinte...

```python
ム leia_me
{ "percurso": "C:\leia_me.txt", "criacao": "23/09/2004" }

ム mover_arquivo(leia_me, "C:\documentos\leia_me.txt") }
```

Em seguida o dicionário `leia_me` terá modificada seu percurso:

```python
ム leia_me
{ "percurso": "C:\documentos\leia_me.txt", "criacao": "23/09/2004" }
```

> É a sua vez! Defina o procedimento `mover_arquivo`, que utilize um dicionário e um novo caminho e modifique o arquivo com o novo percurso.

