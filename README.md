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