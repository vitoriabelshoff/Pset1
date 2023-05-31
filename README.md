<div align="center">
  
  # Linguagens de Programação
  ## PSet 1
  
</div>
  
Por: Vitória Pizzol Belshoff </br>
Professor: Abrantes Araújo Silva Filho </br>

## Questão 1
> Vamos começar com uma imagem4×1 que é definida com os seguintes parâmetros: </br>
• altura: 1 </br>
• largura: 4 </br>
• pixels: [29, 89, 136, 200] </br>
Se você passar essa imagem pelo filtro de inversão, qual seria o
output esperado? Justifique sua resposta.</br>
### Resposta: 

## Questão 2
> faça a depuração e, quando terminar, seu código deve conseguir
passar em todos os testes do grupo de teste TestInvertida (incluindo especificamente o que você acabou de criar). Execute seu filtro de inversão na imagem
test_images/bluegill.png, salve o resultado como uma imagem PNG e
salve a imagem em seu repositório GitHub.
### Resposta: 

![image](https://github.com/vitoriabelshoff/Pset1/assets/103432976/208f7b26-b835-4c88-a951-8ef84d3803f3)

## Questão 3
> Qual será o valor do pixel na imagem de saída no local indicado pelo destaque
vermelho? Observe que neste ponto ainda não arredondamos ou recortamos o valor, informe exatamente como você calculou. 
### Resposta: 
A correlação pode ser calculada somando as multiplicações dos pixels do kernel com a imagem. Assim teremos:

(80 * 0,00) + (53 * (-0,07)) + (99 * 0) + (129 * (-0,45)) + (127 * 1,2) + (148 * (-0,25)) + (175 * 0) + (174 * (-0,12)) + (193 * 0)

= 0 + (-3.71) + (0) + (-58.05) + (152.4) + (-37) + 0 + (-20.88) + 0

= 32.76

## Questão 4
> : quando você tiver implementado seu código, tente executá-lo em
test_images/pigbird.png com o seguinte kernel 9 × 9: </br>
0 0 0 0 0 0 0 0 0 </br>
0 0 0 0 0 0 0 0 0 </br>
1 0 0 0 0 0 0 0 0 </br>
0 0 0 0 0 0 0 0 0 </br>
0 0 0 0 0 0 0 0 0 </br>
0 0 0 0 0 0 0 0 0 </br>
0 0 0 0 0 0 0 0 0 </br>
0 0 0 0 0 0 0 0 0 </br>
0 0 0 0 0 0 0 0 0 </br>

### Resposta: 
![image](https://github.com/vitoriabelshoff/Pset1/assets/103432976/601d3788-bee6-406f-a266-97d3855efd8b)

## Questão 5
> se quisermos usar uma versão desfocada B que foi feita com um
kernel de desfoque de caixa de 3 × 3, que kernel k poderíamos usar para calcular
toda a imagem nítida com uma única correlação? Justifique sua resposta mostrando
os cálculos.
### Resposta: 
Seria possível usando a correlação de S x,y = round( 2 * Ix,y - Bx,y ). </br>
Para chegar na resposta é preciso usar na fórmula o dobro da imagem pra aplicar a nitidez, dessa forma:
2 * Ix,y : </br>
[ 0 0 0 </br>
0 2 0 </br>
0 0 0 ] </br>
Mas como ja temos os valores de kernel 3 x 3, que seria: </br>
[ 1/9, 1/9, 1/9 </br>
1/9, 1/9, 1/9 </br>
1/9, 1/9, 1/9 ] </br>
É só fazer a subtração de 2Ix,y com Bx,y, então chegamos no resultado: </br>
[ -1/9, -1/9, -1/9 </br>
-1/9, -17/9, -1/9 </br>
-1/9, -1/9, -1/9 ]. </br>
Teste das imagens: </br>
![image](https://github.com/vitoriabelshoff/Pset1/assets/103432976/927d7284-67f5-4771-a1b2-48106c9d24b0)
![image](https://github.com/vitoriabelshoff/Pset1/assets/103432976/8b60200f-1ec0-44cd-83f0-98432520dab1)

## Questão 6
> explique o que cada um dos kernels acima, por si só, está fazendo.
Tente executar mostrar nos resultados dessas correlações intermediárias para ter
uma noção do que está acontecendo aqui.
### Resposta: 
Os kernels mostrados no pdf são responsaveis por derivar a imagem com as bordas destacadas, porem um fazendo pelo eixo x e outro fazenso pelo eixo y.]
Kernel do eixo X: </br>
![image](https://github.com/vitoriabelshoff/Pset1/assets/103432976/319ddbad-0cf8-4bac-9948-4de45f17eed1) </br>
Kernel do eixo Y: </br>
![image](https://github.com/vitoriabelshoff/Pset1/assets/103432976/57260872-592e-4157-8ed6-6a12ac5eca8d)

![image](https://github.com/vitoriabelshoff/Pset1/assets/103432976/e72f1ce3-a934-4f93-8662-f40993c5ac01)





