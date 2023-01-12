<h3>Links</h3>

link do repositorio <br>
https://gitlab.com/fse_fga/trabalhos-2022_2/trabalho-2-2022-2
<hr>


<h3>To Do List</h3>

- Arquivo main em python
<hr>


<h3>Codigo main</h3>

```
main
{
  //  INICIALIZAÇÃO
  init.gpio(23,24) output
  init i2c /devi2c-1 abrir o barramento para comunicar
  init uart /dev/serial/0 - definir a palavra e a velocidade etc etc

  // LOOP LEITURA
  ler_comandos() //uart-modbus
}
```
