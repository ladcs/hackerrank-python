# questões hacker rank e python

<details>
<summary>
<strong>Taum and B'day</strong>
</summary>

Taum planeja celebrar o aniversário do seu amigo, Disksha. Há dois tipos de presentes que o Disksha espera de Taum: um tipo de presente é preto e outro é branco. Para fazer ele feliz, Taum comprou <strong>b</strong> presentes preto e <strong>w</strong> presentes branco.

O custo do presente branco <strong>wc</strong> por unidade.

O custo do presente preto <strong>bc</strong> por unidade.

O custo para converter o presente, de branco para preto e de preto para branco é <strong>z</strong>.

Deve determinar o custo mínimo para comprar os presentes.

<strong>exemplo:</strong>
b = 3

w = 5

bc = 3

wc = 4

z = 1



Ele comprou 3 presentes preto, 5 presentes branco, o presente preto custa 3 e o branco custa 4. assim a saida ficaria 3 * 3 + 4 * 5 = 29

<strong> Descrição da função: </strong>

Entrada

int b: o número de presentes preto.

int w: o número de presentes branco.

int bc: preço dos presentes preto.

int wc: preço dos presentes branco.

int z:  preço para converter a cor do presente.

Retorno

int: custo minimo.

<strong> entrada hacker rank</strong>

primeiro valor => t, número de entradas. 1<= t <= 10

segundo valor => b, w. 0 <= b, w <= 10⁹

terceiro valor => bc, wc, z. <= bc, wc, z <= 10⁹

<strong>entrada e saída</strong>

Entrada:
```bs
STDIN   Function
-----   --------
5       t = 5

10 10   b = 10, w = 10

1 1 1   bc = 1, wc = 1, z = 1

5 9     b = 5, w = 9

2 3 4   bc = 2, wc = 3, z = 4

3 6     b = 3, w = 6

9 1 1   bc = 9, wc = 1, z = 1

7 7     b = 7, w = 7

4 2 1   bc = 4, wc = 2, z = 1

3 3     b = 3, w = 3

1 9 2   bc = 1, wc = 9, z = 2
```

Saída:
```bs
20
37
12
35
12
```

<strong> Explicação: </strong>

caso 1: bc == wc, saída b * bc + w * wc => 10 * 1 + 10 * 1 = 20

caso 2: wc + z > bc, saída b * bc + w * wc => 5 * 2 + 9 * 3 = 37

caso 3: bc > wc + z, saída  (b + w) * wc + b * z => (6 + 3) * 1 + 3 * 1 = 9 + 3 = 12

caso 4: bc > wc + z, saída (b + w) * wc + b * z => (7 + 7) * 2 + 7 * 1 = 14 * 2 + 7 = 35

caso 5: wc > bc + z, saída (b + w) * bc + w * z => (3 + 3) * 1 + 3 * 2 = 6 + 6 = 12

</details>

<details><summary><strong>angry professor</strong></summary>

Um professor de matemática tem uma classe de estudantes. Ele está frustrado com a frequência em suas aulas e decidiu cancelar se não houver o número mínimo de estudantes no horário.

<strong>Exemplo</strong>

n = 5

k = 3

a = [-2, -3, 0, 1, 2]

Eles quer o número mínimo é de 3 alunos presentes, os 3 primeiros chegaram antes ou no horário e os 2 últimos atrasado, assim tem aula retornando 'NO'.


<strong>descrição da função</strong>

a função angryProfessor retorna YES se a aula for cancelada, ou NO caso contrário.

angryProfessor tem os parametros:

int k => número de alunos no horário. 1 <= k <= n
    
int a[n] => array dos horários dos alunos. -100 <= a[i] <= 100, 1 <= n <= 1000

Retornos

string: tanto YES ou NO

Input Format

primeira linha <strong> t</strong>, número de casos.

segunda linha n e k.

terceira linha a[n].


<strong>entrada hacker-rank</strong>

2

4 3

-1 -3 4 2

4 2

0 -1 2 1

<strong>saida da função</strong>

YES

NO

<strong>Explicação</strong>

caso 1: espera 3 alunos no horário (a[i] <= 0), tendo apenas dois, assim a aula é cancelada retornando YES.

4 2

0 -1 2 1

caso 2: espera 2 alunos no horário, tem 2 no horário, assim a aula não é cancelada, retornado NO

</details>

<details><summary><strong>beautful day for a movie</strong></summary>

Lily criou um jogo com números inteiros, nele ela calcula a diferença entre um número e seu reverso. Por exemplo: a diferença entre o número <strong>12</strong> e o <strong>21</strong>, que é 9.

Ela usa esse jogo para tomadas de decisões. Ela vai observar os dias para ver um filme em um intervalo de dias.

Assim, dando um intervalo <strong>[i, i + 1, ..., j]</strong> e o número <strong>k</strong>, deve se determinar a quantidades de bons dias para ir ao cinema, pegando a diferença do dia, mais o seu inverso dividido pelo número <strong>k</strong>

<strong>Exemplo</strong>

n = 5

k = 3

a = [-2, -3, 0, 1, 2]

Eles quer o número mínimo é de 3 alunos presentes, os 3 primeiros chegaram antes ou no horário e os 2 últimos atrasado, assim tem aula retornando 'NO'.


<strong>descrição da função</strong>

a função viralAdvertising retorna um número.

viralAdvertising tem os parametros:

int i, j => criação do intervalo dos dias, i é o começo e j o final do interválo. 1 <= i, j <= 2x10⁶

int k => número para dividir. 1 <= k <= 2X10⁹

Retornos

int

Input Format

i j k

<strong>entrada hacker-rank</strong>

20 23 6

<strong>saida da função</strong>

2

<strong>Explicação</strong>

Intervalo dos dias 20, 21, 22, 23.

dia 20: |20 - 02| / 6 = 18 / 6 = 3, inteiro, dia bonito.

dia 21: |21 - 12| / 6 = 9 / 6 = 1,5, não é inteiro, não é um dia bonito.

dia 22: |22 - 22| / 6 = 0 / 6 = 0, inteiro, dia bonito.

dia 23: |23 - 32| / 6 = 9 / 6 = 1,5, não é inteiro, não é um dia bonito.

Assim dias bonitos temos dia 20 e 22, retorno igual 2!

</details>

<details><summary><strong>Viral Advertising</strong></summary>

A empresa HackerLand adotou uma estratégia de propaganda viral. Quando um produto é lançado, eles lançam a propaganda para exatamente <strong>5</strong> pessoas em uma mídia social.

No primeiro dia metade das <strong>5</strong> pessoas, arredondado para baixo (i.e. floor(5/2)=2), gostaram e enviaram para <strong>3</strong>, ou seja, <strong>6</strong> pessoas, receberam a propagando no segundo dia.

Assim se mantem com o passar dos dias, as pessoas que gostarem da propaganda envia para 3 pessoas, onde a metade delas irão gostar.

<strong>descrição da função</strong>

A função viralAdvertising retorna um número.

viralAdvertising tem os parametros:

int n => número de dias. 1 <=  n <= 50

Retornos

int, quantas pessoas gostaram no período total.

Input Format

n

<strong>entrada hacker-rank</strong>

5


3

<strong>saida da função</strong>

24


9

<strong>Explicação</strong>

<strong> caso 1 </strong>

dia     compartilhado       curtido     acumulado
1           5                   2           2
2           6                   3           5
3           9                   4           9
4           12                  6           15
5           18                  9           24

Assim no quinto dia tem 24 acumulado.


<strong> caso 2 </strong>

No primeiro dia 5 pessoas receberam, 5/2 = 2,5, assim 2 pessoas gostaram e compartilham para 6, no segundo dia das 6 pessoas, 6/2 = 3 curtiram e compartilharam para 9 pessoas, ou seja, 5 pessoas gostaram até então, por fim no terceiro dia das 9 pessoas tem-se que 9/2 = 4,5, ou seja, 4 pessoas gostaram, dando 9 pessoas que gostaram no final.

</details>

<details><summary><strong>Save the Prisoners!</summary></strong>

Uma prisão tem um número de prisioneiros e um número de guloseimas para distribuir a eles. O carcereiro decide a maneira mais justa de dividir as guloseimas é sentar os prisioneiros ao redor de uma mesa circular em cadeiras numeradas sequencialmente. Um número de cadeira será sorteado de um chapéu. Começando com o prisioneiro naquela cadeira, uma guloseima será entregue a cada prisioneiro sequencialmente ao redor da mesa até que todas tenham sido distribuídas.

O carcereiro está fazendo uma pequena brincadeira, porém. A última peça de guloseima parece com todas as outras, mas tem um gosto horrível. Determine o número da cadeira ocupada pelo prisioneiro que receberá essa guloseima.

<strong>descrição da função</strong>

A função saveThePrisoner retorna um número.

saveThePrisoner tem os parametros:

int n => número de prisioneiros. 1 <=  n <= 10⁹

int m => número de doces. 1 <= m <= 1010⁹

int s => número da cadeira no qual começa. 1 <= s <= n

Retornos

int, última cadeira a receber um doce.

Input Format

t     => quantos casos 1 <= t <= 100

n  m  s

<strong>entrada hacker-rank</strong>
2
5 2 1
5 2 2
<strong>saida da função</strong>
2
3

<strong>Explicação</strong>
No primeiro caso há 5 prisioneiro, dois doces e começa pela cadeira 1, assim a segunda cadeira recebe o último doce.

No segundo caso a mesma situação começa na cadeira 2, fazendo que o último doce fique com a cadeira 3.
</details>