| Manufacturer     | Car        | Weight | Power   | PINC    | E/Stint | FDS     |
|:-|:-|:-|:-|:-|:-|:-|
| Alpine           | A424       | 1047kg | 520.0kw |    -    | 914MJ   |    -    |
| BMW              | M-Hybrid   | 1041kg | 512.0kw |    -    | 906MJ   |    -    |
| Cadillac         | V-Series.R | 1034kg | 510.0kw |    -    | 901MJ   |    -    |
| Ferrari          | 499P       | 1063kg | 508.0kw |    -    | 894MJ   | 190kph  |
| Isotta Fraschini | Tipo6C     | 1059kg | 520.0kw |    -    | 919MJ   | 190kph  |
| Lamborghini      | SC63       | 1042kg | 519.0kw |    -    | 907MJ   |    -    |
| Peugeot          | 9X8Evo     | 1050kg | 510.0kw |    -    | 898MJ   | 190kph  |
| Porsche          | 963        | 1047kg | 516.0kw |    -    | 909MJ   |    -    |
| Toyota           | GR010      | 1080kg | 512.0kw |    -    | 911MJ   | 190kph  |

![PACECHART](./IMG/CUSTOM.png)
![STRAIGHTLINEPERFORMANCECHART](./IMG/CUSTOM_sp.png)
![TYREPERFORMANCECHART](./IMG/CUSTOM_tw.png)

### BoP Accuracy: 84.88%; Overall BoP Grade: B2
| Manufacturer     | Car        | Type  | RP      | QP      | Weight | Power¹  | Threshhold | PINC    | Power²   | E/Stint | AVG Vmax  | FDS     | RDLC | L/Stint | BOP-Grade | Model Accuracy | Model Points | Match% | SimDiff |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|
| Alpine           | A424       | LMDH  | 3:29.33 | 3:24.04 | 1047kg | 520.0kw | 210.0kph   |    -    | 520.00kw |  914MJ  | 335.21kph |    -    | 1.01 | 12      | -C1       | 100.00%        | 946          | 79.87% | -1.13   |
| BMW              | M-Hybrid   | LMDH  | 3:30.36 | 3:24.42 | 1041kg | 512.0kw | 210.0kph   |    -    | 512.00kw |  906MJ  | 331.59kph |    -    | 1.02 | 12      | ~A1       | 100.00%        | 1998         | 97.34% | -0.71   |
| Cadillac         | V-Series.R | LMDH  | 3:29.53 | 3:24.21 | 1034kg | 510.0kw | 210.0kph   |    -    | 510.00kw |  901MJ  | 329.35kph |    -    | 1.03 | 12      | -B1       | 98.11%         | 3991         | 88.60% | +0.13   |
| Ferrari          | 499P       | LMHHU | 3:29.80 | 3:24.18 | 1063kg | 508.0kw | 210.0kph   |    -    | 508.00kw |  894MJ  | 331.80kph | 190kph  | 1.03 | 12      | ~A1       | 98.72%         | 4180         | 95.11% | +0.22   |
| Isotta Fraschini | Tipo6C     | LMHHU | 3:31.91 | 3:29.25 | 1059kg | 520.0kw | 210.0kph   |    -    | 520.00kw |  919MJ  | 330.80kph | 190kph  | 1.04 | 12      | +Ω1       | 97.73%         | 129          | 31.24% | +0.73   |
| Lamborghini      | SC63       | LMDH  | 3:30.46 | 3:26.02 | 1042kg | 519.0kw | 210.0kph   |    -    | 519.00kw |  907MJ  | 331.53kph |    -    | 1.05 | 12      | +A2       | 100.00%        | 784          | 93.11% | +0.28   |
| Peugeot          | 9X8Evo     | LMHHU | 3:30.22 | 3:25.33 | 1050kg | 510.0kw | 210.0kph   |    -    | 510.00kw |  898MJ  | 332.18kph | 190kph  | 1.01 | 12      | ~A1       | 100.00%        | 636          | 96.58% | +0.21   |
| Porsche          | 963        | LMDH  | 3:29.33 | 3:23.16 | 1047kg | 516.0kw | 210.0kph   |    -    | 516.00kw |  909MJ  | 332.81kph |    -    | 1.01 | 12      | -B2       | 99.91%         | 11713        | 82.31% | +0.09   |
| Toyota           | GR010      | LMHHU | 3:30.01 | 3:24.03 | 1080kg | 512.0kw | 210.0kph   |    -    | 512.00kw |  911MJ  | 330.41kph | 190kph  | 1.01 | 12      | ~A1       | 99.90%         | 3123         | 99.76% | +0.17   |

## Power below Threshhold
| N/Nmax    | A424    | M-HYBRID | V-SERIES.R | 499P    | TIPO6C  | SC63    | 9X8EVO  | 963     | GR010   |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|
|  0.550    |  256    |  252     |  251       |  250    |  256    |  256    |  251    |  254    |  252    |
|  0.575    |  279    |  275     |  274       |  273    |  279    |  279    |  274    |  277    |  275    |
|  0.600    |  300    |  296     |  295       |  293    |  300    |  299    |  295    |  298    |  296    |
|  0.625    |  322    |  317     |  316       |  314    |  322    |  321    |  316    |  319    |  317    |
|  0.650    |  343    |  338     |  337       |  335    |  343    |  342    |  337    |  340    |  338    |
|  0.675    |  365    |  359     |  358       |  357    |  365    |  364    |  358    |  362    |  359    |
|  0.700    |  387    |  381     |  380       |  378    |  387    |  386    |  380    |  384    |  381    |
|  0.725    |  409    |  403     |  401       |  399    |  409    |  408    |  401    |  406    |  403    |
|  0.750    |  430    |  423     |  422       |  420    |  430    |  429    |  422    |  427    |  423    |
|  0.775    |  449    |  442     |  441       |  439    |  449    |  448    |  441    |  446    |  442    |
|  0.800    |  467    |  460     |  458       |  456    |  467    |  466    |  458    |  463    |  460    |
|  0.825    |  482    |  475     |  473       |  471    |  482    |  481    |  473    |  478    |  475    |
|  0.850    |  494    |  486     |  485       |  483    |  494    |  493    |  485    |  490    |  486    |
|  0.875    |  505    |  497     |  495       |  493    |  505    |  504    |  495    |  501    |  497    |
|  0.900    |  512    |  504     |  502       |  500    |  512    |  511    |  502    |  508    |  504    |
|  0.925    |  517    |  509     |  507       |  505    |  517    |  516    |  507    |  513    |  509    |
| **0.950** | **520** | **512**  | **510**    | **508** | **520** | **519** | **510** | **516** | **512** |
|  0.975    |  518    |  510     |  508       |  506    |  518    |  517    |  508    |  514    |  510    |
|  1.000    |  514    |  506     |  505       |  503    |  514    |  513    |  505    |  510    |  506    |
|  1.025    |  444    |  437     |  436       |  434    |  444    |  443    |  436    |  441    |  437    |

## Power above Threshhold
| N/Nmax    | A424    | M-HYBRID | V-SERIES.R | 499P    | TIPO6C  | SC63    | 9X8EVO  | 963     | GR010   |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|
|  0.550    |  256    |  252     |  251       |  250    |  256    |  256    |  251    |  254    |  252    |
|  0.575    |  279    |  275     |  274       |  273    |  279    |  279    |  274    |  277    |  275    |
|  0.600    |  300    |  296     |  295       |  293    |  300    |  299    |  295    |  298    |  296    |
|  0.625    |  322    |  317     |  316       |  314    |  322    |  321    |  316    |  319    |  317    |
|  0.650    |  343    |  338     |  337       |  335    |  343    |  342    |  337    |  340    |  338    |
|  0.675    |  365    |  359     |  358       |  357    |  365    |  364    |  358    |  362    |  359    |
|  0.700    |  387    |  381     |  380       |  378    |  387    |  386    |  380    |  384    |  381    |
|  0.725    |  409    |  403     |  401       |  399    |  409    |  408    |  401    |  406    |  403    |
|  0.750    |  430    |  423     |  422       |  420    |  430    |  429    |  422    |  427    |  423    |
|  0.775    |  449    |  442     |  441       |  439    |  449    |  448    |  441    |  446    |  442    |
|  0.800    |  467    |  460     |  458       |  456    |  467    |  466    |  458    |  463    |  460    |
|  0.825    |  482    |  475     |  473       |  471    |  482    |  481    |  473    |  478    |  475    |
|  0.850    |  494    |  486     |  485       |  483    |  494    |  493    |  485    |  490    |  486    |
|  0.875    |  505    |  497     |  495       |  493    |  505    |  504    |  495    |  501    |  497    |
|  0.900    |  512    |  504     |  502       |  500    |  512    |  511    |  502    |  508    |  504    |
|  0.925    |  517    |  509     |  507       |  505    |  517    |  516    |  507    |  513    |  509    |
| **0.950** | **520** | **512**  | **510**    | **508** | **520** | **519** | **510** | **516** | **512** |
|  0.975    |  518    |  510     |  508       |  506    |  518    |  517    |  508    |  514    |  510    |
|  1.000    |  514    |  506     |  505       |  503    |  514    |  513    |  505    |  510    |  506    |
|  1.025    |  444    |  437     |  436       |  434    |  444    |  443    |  436    |  441    |  437    |
