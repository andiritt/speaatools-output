| Manufacturer     | Car        | Weight | Power   | PINC    | E/Stint | FDS     |
|:-|:-|:-|:-|:-|:-|:-|
| Alpine           | A424       | 1045kg | 513.0kw |    -    | 913MJ   |    -    |
| BMW              | M-Hybrid   | 1038kg | 510.0kw |    -    | 907MJ   |    -    |
| Cadillac         | V-Series.R | 1030kg | 516.0kw |    -    | 909MJ   |    -    |
| Ferrari          | 499P       | 1053kg | 508.0kw |    -    | 902MJ   | 190kph  |
| Isotta Fraschini | Tipo6C     | 1059kg | 520.0kw |    -    | 917MJ   | 190kph  |
| Lamborghini      | SC63       | 1035kg | 514.0kw |    -    | 908MJ   |    -    |
| Peugeot          | 9X8Evo     | 1065kg | 508.0kw |    -    | 910MJ   | 190kph  |
| Porsche          | 963        | 1037kg | 507.0kw |    -    | 904MJ   |    -    |
| Toyota           | GR010      | 1064kg | 515.0kw |    -    | 917MJ   | 190kph  |

![PACECHART](./IMG/OFFICIAL.png)
![STRAIGHTLINEPERFORMANCECHART](./IMG/OFFICIAL_sp.png)
![TYREPERFORMANCECHART](./IMG/OFFICIAL_tw.png)

### BoP Accuracy: 72.32%; Overall BoP Grade: C2
| Manufacturer     | Car        | Type  | RP      | QP      | Weight | Power¹  | Threshhold | PINC    | Power²   | E/Stint | AVG Vmax  | FDS     | RDLC | L/Stint | BOP-Grade | Model Accuracy | Model Points | Match%  | SimDiff |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|
| Alpine           | A424       | LMDH  | 2:07.12 | 2:02.58 | 1045kg | 513.0kw | 210.0kph   |    -    | 513.00kw |  913MJ  | 311.25kph |    -    | 1.01 | 25      | ~A1       | 99.49%         | 1360         | 96.19%  | -0.38   |
| BMW              | M-Hybrid   | LMDH  | 2:07.09 | 2:01.48 | 1038kg | 510.0kw | 210.0kph   |    -    | 510.00kw |  907MJ  | 310.05kph |    -    | 1.02 | 25      | ~A1       | 98.62%         | 2363         | 100.00% | -0.25   |
| Cadillac         | V-Series.R | LMDH  | 2:06.03 | 2:00.93 | 1030kg | 516.0kw | 210.0kph   |    -    | 516.00kw |  909MJ  | 307.54kph |    -    | 1.03 | 25      | -D2       | 98.50%         | 4201         | 63.68%  | +0.69   |
| Ferrari          | 499P       | LMHHU | 2:06.24 | 2:00.94 | 1053kg | 508.0kw | 210.0kph   |    -    | 508.00kw |  902MJ  | 310.06kph | 190kph  | 1.04 | 25      | -D1       | 100.00%        | 4441         | 69.03%  | +0.22   |
| Isotta Fraschini | Tipo6C     | LMHHU | 2:08.36 | 2:04.90 | 1059kg | 520.0kw | 210.0kph   |    -    | 520.00kw |  917MJ  | 306.16kph | 190kph  | 1.05 | 25      | +Ω1       | 98.48%         | 130          | 20.54%  | -0.28   |
| Lamborghini      | SC63       | LMDH  | 2:07.47 | 2:03.03 | 1035kg | 514.0kw | 210.0kph   |    -    | 514.00kw |  908MJ  | 306.51kph |    -    | 1.06 | 25      | +B2       | 100.00%        | 784          | 82.22%  | -0.24   |
| Peugeot          | 9X8Evo     | LMHHU | 2:07.49 | 2:02.56 | 1065kg | 508.0kw | 210.0kph   |    -    | 508.00kw |  910MJ  | 308.43kph | 190kph  | 0.99 | 25      | +D1       | 100.00%        | 808          | 66.87%  | -0.04   |
| Porsche          | 963        | LMDH  | 2:06.78 | 2:01.17 | 1037kg | 507.0kw | 210.0kph   |    -    | 507.00kw |  904MJ  | 308.38kph |    -    | 1.02 | 25      | -A2       | 99.87%         | 12613        | 93.24%  | -0.56   |
| Toyota           | GR010      | LMHHU | 2:05.95 | 2:00.45 | 1064kg | 515.0kw | 210.0kph   |    -    | 515.00kw |  917MJ  | 307.86kph | 190kph  | 1.03 | 25      | -E1       | 99.73%         | 2956         | 59.08%  | +0.85   |

## Power below Threshhold
| N/Nmax    | A424    | M-HYBRID | V-SERIES.R | 499P    | TIPO6C  | SC63    | 9X8EVO  | 963     | GR010   |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|
|  0.550    |  253    |  251     |  254       |  250    |  256    |  253    |  250    |  250    |  254    |
|  0.575    |  276    |  274     |  277       |  273    |  279    |  276    |  273    |  273    |  277    |
|  0.600    |  296    |  295     |  298       |  293    |  300    |  297    |  293    |  293    |  297    |
|  0.625    |  317    |  316     |  319       |  314    |  322    |  318    |  314    |  314    |  319    |
|  0.650    |  338    |  337     |  340       |  335    |  343    |  339    |  335    |  335    |  340    |
|  0.675    |  360    |  358     |  362       |  357    |  365    |  361    |  357    |  356    |  362    |
|  0.700    |  382    |  380     |  384       |  378    |  387    |  383    |  378    |  377    |  383    |
|  0.725    |  403    |  401     |  406       |  399    |  409    |  404    |  399    |  399    |  405    |
|  0.750    |  424    |  422     |  427       |  420    |  430    |  425    |  420    |  419    |  426    |
|  0.775    |  443    |  441     |  446       |  439    |  449    |  444    |  439    |  438    |  445    |
|  0.800    |  461    |  458     |  463       |  456    |  467    |  462    |  456    |  455    |  463    |
|  0.825    |  476    |  473     |  478       |  471    |  482    |  477    |  471    |  470    |  478    |
|  0.850    |  487    |  485     |  490       |  483    |  494    |  488    |  483    |  482    |  489    |
|  0.875    |  498    |  495     |  501       |  493    |  505    |  499    |  493    |  492    |  500    |
|  0.900    |  505    |  502     |  508       |  500    |  512    |  506    |  500    |  499    |  507    |
|  0.925    |  510    |  507     |  513       |  505    |  517    |  511    |  505    |  504    |  512    |
| **0.950** | **513** | **510**  | **516**    | **508** | **520** | **514** | **508** | **507** | **515** |
|  0.975    |  511    |  508     |  514       |  506    |  518    |  512    |  506    |  505    |  513    |
|  1.000    |  507    |  505     |  510       |  503    |  514    |  508    |  503    |  502    |  509    |
|  1.025    |  438    |  436     |  441       |  434    |  444    |  439    |  434    |  433    |  440    |

## Power above Threshhold
| N/Nmax    | A424    | M-HYBRID | V-SERIES.R | 499P    | TIPO6C  | SC63    | 9X8EVO  | 963     | GR010   |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|
|  0.550    |  253    |  251     |  254       |  250    |  256    |  253    |  250    |  250    |  254    |
|  0.575    |  276    |  274     |  277       |  273    |  279    |  276    |  273    |  273    |  277    |
|  0.600    |  296    |  295     |  298       |  293    |  300    |  297    |  293    |  293    |  297    |
|  0.625    |  317    |  316     |  319       |  314    |  322    |  318    |  314    |  314    |  319    |
|  0.650    |  338    |  337     |  340       |  335    |  343    |  339    |  335    |  335    |  340    |
|  0.675    |  360    |  358     |  362       |  357    |  365    |  361    |  357    |  356    |  362    |
|  0.700    |  382    |  380     |  384       |  378    |  387    |  383    |  378    |  377    |  383    |
|  0.725    |  403    |  401     |  406       |  399    |  409    |  404    |  399    |  399    |  405    |
|  0.750    |  424    |  422     |  427       |  420    |  430    |  425    |  420    |  419    |  426    |
|  0.775    |  443    |  441     |  446       |  439    |  449    |  444    |  439    |  438    |  445    |
|  0.800    |  461    |  458     |  463       |  456    |  467    |  462    |  456    |  455    |  463    |
|  0.825    |  476    |  473     |  478       |  471    |  482    |  477    |  471    |  470    |  478    |
|  0.850    |  487    |  485     |  490       |  483    |  494    |  488    |  483    |  482    |  489    |
|  0.875    |  498    |  495     |  501       |  493    |  505    |  499    |  493    |  492    |  500    |
|  0.900    |  505    |  502     |  508       |  500    |  512    |  506    |  500    |  499    |  507    |
|  0.925    |  510    |  507     |  513       |  505    |  517    |  511    |  505    |  504    |  512    |
| **0.950** | **513** | **510**  | **516**    | **508** | **520** | **514** | **508** | **507** | **515** |
|  0.975    |  511    |  508     |  514       |  506    |  518    |  512    |  506    |  505    |  513    |
|  1.000    |  507    |  505     |  510       |  503    |  514    |  508    |  503    |  502    |  509    |
|  1.025    |  438    |  436     |  441       |  434    |  444    |  439    |  434    |  433    |  440    |
