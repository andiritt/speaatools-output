| Manufacturer     | Car        | Weight | Power   | PINC    | E/Stint | FDS     |
|:-|:-|:-|:-|:-|:-|:-|
| Alpine           | A424       | 1047kg | 520.0kw |    -    | 913MJ   |    -    |
| BMW              | M-Hybrid   | 1041kg | 512.0kw |    -    | 905MJ   |    -    |
| Cadillac         | V-Series.R | 1034kg | 510.0kw |    -    | 898MJ   |    -    |
| Ferrari          | 499P       | 1063kg | 508.0kw |    -    | 895MJ   | 190kph  |
| Isotta Fraschini | Tipo6C     | 1059kg | 520.0kw |    -    | 917MJ   | 190kph  |
| Lamborghini      | SC63       | 1042kg | 519.0kw |    -    | 908MJ   |    -    |
| Peugeot          | 9X8Evo     | 1050kg | 510.0kw |    -    | 899MJ   | 190kph  |
| Porsche          | 963        | 1047kg | 516.0kw |    -    | 902MJ   |    -    |
| Toyota           | GR010      | 1080kg | 512.0kw |    -    | 905MJ   | 190kph  |

![PACECHART](./IMG/CUSTOM.png)
![STRAIGHTLINEPERFORMANCECHART](./IMG/CUSTOM_sp.png)
![TYREPERFORMANCECHART](./IMG/CUSTOM_tw.png)

### BoP Accuracy: 73.47%; Overall BoP Grade: C2
| Manufacturer     | Car        | Type  | RP      | QP      | Weight | Power¹  | Threshhold | PINC    | Power²   | E/Stint | AVG Vmax  | FDS     | RDLC | L/Stint | BOP-Grade | Model Accuracy | Model Points | Match% | SimDiff |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|
| Alpine           | A424       | LMDH  | 1:25.81 | 1:23.41 | 1047kg | 520.0kw | 210.0kph   |    -    | 520.00kw |  913MJ  | 313.07kph |    -    | 1.01 | 43      | -C2       | 100.00%        | 946          | 73.60% | #       |
| BMW              | M-Hybrid   | LMDH  | 1:26.07 | 1:23.40 | 1041kg | 512.0kw | 210.0kph   |    -    | 512.00kw |  905MJ  | 309.69kph |    -    | 1.02 | 43      | -B2       | 100.00%        | 1998         | 80.38% | #       |
| Cadillac         | V-Series.R | LMDH  | 1:25.63 | 1:23.23 | 1034kg | 510.0kw | 210.0kph   |    -    | 510.00kw |  898MJ  | 307.60kph |    -    | 1.03 | 43      | -D1       | 98.11%         | 3991         | 65.75% | #       |
| Ferrari          | 499P       | LMHHU | 1:26.30 | 1:23.74 | 1063kg | 508.0kw | 210.0kph   |    -    | 508.00kw |  895MJ  | 309.89kph | 190kph  | 1.03 | 43      | ~A1       | 98.72%         | 4180         | 96.23% | #       |
| Isotta Fraschini | Tipo6C     | LMHHU | 1:27.31 | 1:25.97 | 1059kg | 520.0kw | 210.0kph   |    -    | 520.00kw |  917MJ  | 308.96kph | 190kph  | 1.05 | 43      | +Ω1       | 97.73%         | 129          | 9.97%  | #       |
| Lamborghini      | SC63       | LMDH  | 1:26.22 | 1:24.16 | 1042kg | 519.0kw | 210.0kph   |    -    | 519.00kw |  908MJ  | 309.63kph |    -    | 1.04 | 43      | ~A1       | 100.00%        | 784          | 95.66% | #       |
| Peugeot          | 9X8Evo     | LMHHU | 1:26.40 | 1:24.15 | 1050kg | 510.0kw | 210.0kph   |    -    | 510.00kw |  899MJ  | 310.24kph | 190kph  | 1.01 | 43      | +B1       | 100.00%        | 636          | 88.78% | #       |
| Porsche          | 963        | LMDH  | 1:25.75 | 1:22.99 | 1047kg | 516.0kw | 210.0kph   |    -    | 516.00kw |  902MJ  | 310.83kph |    -    | 1.02 | 43      | -C2       | 99.91%         | 11713        | 72.14% | #       |
| Toyota           | GR010      | LMHHU | 1:26.59 | 1:23.87 | 1080kg | 512.0kw | 210.0kph   |    -    | 512.00kw |  905MJ  | 308.59kph | 190kph  | 1.01 | 43      | +C1       | 99.90%         | 3123         | 78.69% | #       |

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
