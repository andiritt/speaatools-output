| Manufacturer     | Car        | Weight | Power   | PINC    | E/Stint | FDS     |
|:-|:-|:-|:-|:-|:-|:-|
| Alpine           | A424       | 1040kg | 491.0kw |    -    | 888MJ   |    -    |
| BMW              | M-Hybrid   | 1044kg | 493.0kw |    -    | 890MJ   |    -    |
| Cadillac         | V-Series.R | 1050kg | 491.0kw |    -    | 885MJ   |    -    |
| Ferrari          | 499P       | 1069kg | 487.0kw |    -    | 876MJ   | 190kph  |
| Isotta Fraschini | Tipo6C     | 1089kg | 520.0kw |    -    | 922MJ   | 190kph  |
| Lamborghini      | SC63       | 1068kg | 509.0kw |    -    | 901MJ   |    -    |
| Peugeot          | 9X8Evo     | 1030kg | 482.0kw |    -    | 871MJ   | 190kph  |
| Porsche          | 963        | 1042kg | 488.0kw |    -    | 883MJ   |    -    |
| Toyota           | GR010      | 1072kg | 487.0kw |    -    | 888MJ   | 190kph  |

![PACECHART](./IMG/AUTO.png)
![STRAIGHTLINEPERFORMANCECHART](./IMG/AUTO_sp.png)
![TYREPERFORMANCECHART](./IMG/AUTO_tw.png)

### BoP Accuracy: 95.33%; Overall BoP Grade: A1
| Manufacturer     | Car        | Type  | RP      | QP      | Weight | Power¹  | Threshhold | PINC    | Power²   | E/Stint | AVG Vmax  | FDS     | RDLC | L/Stint | BOP-Grade | Model Accuracy | Model Points | Match%  | SimDiff |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|
| Alpine           | A424       | LMDH  | 3:33.78 | 3:28.23 | 1040kg | 491.0kw | 0.0kph     |    -    | 491.00kw |  888MJ  | 329.11kph |    -    | 1.01 | 12      | ~A1       | 100.00%        | 946          | 98.05%  | -1.13   |
| BMW              | M-Hybrid   | LMDH  | 3:33.81 | 3:27.65 | 1044kg | 493.0kw | 0.0kph     |    -    | 493.00kw |  890MJ  | 326.73kph |    -    | 1.01 | 12      | -A2       | 100.00%        | 1998         | 90.89%  | -0.71   |
| Cadillac         | V-Series.R | LMDH  | 3:33.80 | 3:28.24 | 1050kg | 491.0kw | 0.0kph     |    -    | 491.00kw |  885MJ  | 323.05kph |    -    | 1.01 | 12      | ~A1       | 98.11%         | 3991         | 95.56%  | +0.13   |
| Ferrari          | 499P       | LMHHU | 3:33.80 | 3:27.94 | 1069kg | 487.0kw | 0.0kph     |    -    | 487.00kw |  876MJ  | 326.10kph | 190kph  | 1.02 | 12      | ~A1       | 98.72%         | 4180         | 100.00% | +0.22   |
| Isotta Fraschini | Tipo6C     | LMHHU | 3:33.78 | 3:31.07 | 1089kg | 520.0kw | 0.0kph     |    -    | 520.00kw |  922MJ  | 327.47kph | 190kph  | 1.01 | 12      | +C1       | 97.73%         | 129          | 77.72%  | +0.73   |
| Lamborghini      | SC63       | LMDH  | 3:33.81 | 3:29.20 | 1068kg | 509.0kw | 0.0kph     |    -    | 509.00kw |  901MJ  | 326.27kph |    -    | 1.02 | 12      | ~A1       | 100.00%        | 784          | 96.78%  | +0.28   |
| Peugeot          | 9X8Evo     | LMHHU | 3:33.80 | 3:28.72 | 1030kg | 482.0kw | 0.0kph     |    -    | 482.00kw |  871MJ  | 327.73kph | 190kph  | 1.02 | 12      | ~A1       | 100.00%        | 636          | 99.37%  | +0.21   |
| Porsche          | 963        | LMDH  | 3:33.77 | 3:27.32 | 1042kg | 488.0kw | 0.0kph     |    -    | 488.00kw |  883MJ  | 326.71kph |    -    | 1.01 | 12      | ~A1       | 99.91%         | 11713        | 100.00% | +0.09   |
| Toyota           | GR010      | LMHHU | 3:33.83 | 3:27.61 | 1072kg | 487.0kw | 0.0kph     |    -    | 487.00kw |  888MJ  | 325.35kph | 190kph  | 1.01 | 12      | ~A1       | 99.90%         | 3123         | 99.63%  | +0.17   |

## Power below Threshhold
| N/Nmax    | A424    | M-HYBRID | V-SERIES.R | 499P    | TIPO6C  | SC63    | 9X8EVO  | 963     | GR010   |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|
|  0.550    |  242    |  243     |  242       |  240    |  256    |  251    |  237    |  240    |  240    |
|  0.575    |  264    |  265     |  264       |  262    |  279    |  274    |  259    |  262    |  262    |
|  0.600    |  284    |  285     |  284       |  281    |  300    |  294    |  278    |  282    |  281    |
|  0.625    |  304    |  305     |  304       |  301    |  322    |  315    |  298    |  302    |  301    |
|  0.650    |  324    |  325     |  324       |  322    |  343    |  336    |  318    |  322    |  322    |
|  0.675    |  345    |  346     |  345       |  342    |  365    |  357    |  338    |  343    |  342    |
|  0.700    |  366    |  367     |  366       |  363    |  387    |  379    |  359    |  364    |  363    |
|  0.725    |  386    |  388     |  386       |  383    |  409    |  400    |  380    |  384    |  383    |
|  0.750    |  406    |  407     |  406       |  403    |  430    |  421    |  399    |  403    |  403    |
|  0.775    |  424    |  426     |  424       |  421    |  449    |  440    |  417    |  422    |  421    |
|  0.800    |  441    |  443     |  441       |  437    |  467    |  457    |  433    |  438    |  437    |
|  0.825    |  455    |  457     |  455       |  452    |  482    |  472    |  447    |  453    |  452    |
|  0.850    |  466    |  468     |  466       |  463    |  494    |  484    |  458    |  464    |  463    |
|  0.875    |  476    |  478     |  476       |  473    |  505    |  494    |  468    |  474    |  473    |
|  0.900    |  483    |  485     |  483       |  479    |  512    |  501    |  474    |  480    |  479    |
|  0.925    |  488    |  490     |  488       |  484    |  517    |  506    |  479    |  485    |  484    |
| **0.950** | **491** | **493**  | **491**    | **487** | **520** | **509** | **482** | **488** | **487** |
|  0.975    |  489    |  491     |  489       |  485    |  518    |  507    |  480    |  486    |  485    |
|  1.000    |  486    |  488     |  486       |  482    |  514    |  504    |  477    |  483    |  482    |
|  1.025    |  419    |  421     |  419       |  416    |  444    |  435    |  412    |  417    |  416    |

## Power above Threshhold
| N/Nmax    | A424    | M-HYBRID | V-SERIES.R | 499P    | TIPO6C  | SC63    | 9X8EVO  | 963     | GR010   |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|
|  0.550    |  242    |  243     |  242       |  240    |  256    |  251    |  237    |  240    |  240    |
|  0.575    |  264    |  265     |  264       |  262    |  279    |  274    |  259    |  262    |  262    |
|  0.600    |  284    |  285     |  284       |  281    |  300    |  294    |  278    |  282    |  281    |
|  0.625    |  304    |  305     |  304       |  301    |  322    |  315    |  298    |  302    |  301    |
|  0.650    |  324    |  325     |  324       |  322    |  343    |  336    |  318    |  322    |  322    |
|  0.675    |  345    |  346     |  345       |  342    |  365    |  357    |  338    |  343    |  342    |
|  0.700    |  366    |  367     |  366       |  363    |  387    |  379    |  359    |  364    |  363    |
|  0.725    |  386    |  388     |  386       |  383    |  409    |  400    |  380    |  384    |  383    |
|  0.750    |  406    |  407     |  406       |  403    |  430    |  421    |  399    |  403    |  403    |
|  0.775    |  424    |  426     |  424       |  421    |  449    |  440    |  417    |  422    |  421    |
|  0.800    |  441    |  443     |  441       |  437    |  467    |  457    |  433    |  438    |  437    |
|  0.825    |  455    |  457     |  455       |  452    |  482    |  472    |  447    |  453    |  452    |
|  0.850    |  466    |  468     |  466       |  463    |  494    |  484    |  458    |  464    |  463    |
|  0.875    |  476    |  478     |  476       |  473    |  505    |  494    |  468    |  474    |  473    |
|  0.900    |  483    |  485     |  483       |  479    |  512    |  501    |  474    |  480    |  479    |
|  0.925    |  488    |  490     |  488       |  484    |  517    |  506    |  479    |  485    |  484    |
| **0.950** | **491** | **493**  | **491**    | **487** | **520** | **509** | **482** | **488** | **487** |
|  0.975    |  489    |  491     |  489       |  485    |  518    |  507    |  480    |  486    |  485    |
|  1.000    |  486    |  488     |  486       |  482    |  514    |  504    |  477    |  483    |  482    |
|  1.025    |  419    |  421     |  419       |  416    |  444    |  435    |  412    |  417    |  416    |
