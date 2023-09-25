## [Titanic - Machine Learning from Disaster](https://www.kaggle.com/code/alexisbcook/titanic-tutorial/notebook)

O foco deste projeto é exercitar técnicas, habilidades de ETL usando Python.
Ultilizei o site [Kaggle](https://www.kaggle.com/kangle123), plataforma onde é possível adotar problemas e soluciona-los, dentre eles temos problemas reais, educativos e muito mais. Vale a pena conferir.

---

#### Problemática

Com acesso a três arquivos em formato CSV, o foco é analisar ambos e juntar informações para responder a pergunta final, simples.
Criar um DataFrame com duas colunas, uma contendo o id de passageiros presente no arquivo test.csv e outra coluna chamada sobreviventes, essas informações estão presentes no arquivo train.csv.
A coluna de sobreviventes tem uma regra, se o passageiro sobreviveu então o valor é 1 senão, 0.

---

#### Solução
Analises realizadas:
Quantos passageiros havia no navio ?
![TotalPassageiros](https://github.com/suellencosta7/Kangle/blob/main/TitanicChallenger/images/PassageirosTotal.png)

Quantos passageiros tinha no arquivo test.csv?
![Passageiros_train.csv](https://github.com/suellencosta7/Kangle/blob/main/TitanicChallenger/images/passageirosTest.csv.png)

Dos passageiros presentes em Train.csv, quais sobreviveram? 0 para não e 1 para sim.
Todos os 418 passageiros presente em train.csv não sobreviveram.
Para chegar nesta conclusão, segui a seguinte lógica:
 
![looping](https://github.com/suellencosta7/Kangle/blob/main/TitanicChallenger/images/condicaoTrueFalse.png)


Durante as analises, ultilizei o [Looker Studeo - Google](https://lookerstudio.google.com/u/0/navigation/reporting) para analisar os dados em dashboord, não foi criado com intuito em alcançar a perfieção 
de dashs, organizado para apresentação e outros fins. APENAS PARA TESTE

![Dash](https://github.com/suellencosta7/Kangle/blob/main/TitanicChallenger/images/dash.png)



### Conclusão 

É um problema simples que peguei para solidificar a base de ETL, o simples bem feito vale mais que um datalake inteiro feito pela metade. 
Não é executar grades ou pequenas coisas, mas sim solucionar o problem de forma simples e completa.
É o famoso começar e ir até o final sem se perder.
