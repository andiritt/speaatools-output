| Manufacturer | Car        | Weight | Power   | PINC    | E/Stint | FDS     |
|:-|:-|:-|:-|:-|:-|:-|
| Alpine       | A424       | 1057kg | 517.0kw |    -    | 916MJ   |    -    |
| Aston Martin | Valkyrie   | 1042kg | 505.0kw | 0.40%   | 900MJ   |    -    |
| BMW          | M-Hybrid   | 1051kg | 509.0kw |    -    | 906MJ   |    -    |
| Cadillac     | V-Series.R | 1044kg | 507.0kw |    -    | 901MJ   |    -    |
| Ferrari      | 499P       | 1073kg | 505.0kw |    -    | 904MJ   | 190kph  |
| Peugeot      | 9X8Evo     | 1060kg | 507.0kw |    -    | 907MJ   | 190kph  |
| Porsche      | 963        | 1057kg | 513.0kw |    -    | 910MJ   |    -    |
| Toyota       | GR010      | 1090kg | 509.0kw |    -    | 911MJ   | 190kph  |

![PACECHART](./IMG/ACOMETHOD.png)
![STRAIGHTLINEPERFORMANCECHART](./IMG/ACOMETHOD_sp.png)
![TYREPERFORMANCECHART](./IMG/ACOMETHOD_tw.png)

### BoP Accuracy: 74.49%; Overall BoP Grade: C2
| Manufacturer | Car        | Type  | RP      | QP      | Weight | Power¹  | Threshhold | PINC    | Power²   | E/Stint | AVG Vmax  | FDS     | RDLC | L/Stint | BOP-Grade | Model Accuracy | Model Points | Match% | SimDiff |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|
| Alpine       | A424       | LMDH  | 1:26.57 | 1:23.20 | 1057kg | 517.0kw | 210.0kph   |    -    | 517.00kw |  916MJ  | 269.34kph |    -    | 1.02 | 43      | -D1       | 99.37%         | 2056         | 69.63% | +0.25   |
| Aston Martin | Valkyrie   | LMHNH | 1:27.96 | 1:24.28 | 1042kg | 505.0kw | 210.0kph   | 0.40%   | 507.00kw |  900MJ  | 260.16kph |    -    | 1.05 | 43      | +Ω1       | 100.00%        | 247          | 30.84% | #       |
| BMW          | M-Hybrid   | LMDH  | 1:27.36 | 1:23.60 | 1051kg | 509.0kw | 210.0kph   |    -    | 509.00kw |  906MJ  | 270.69kph |    -    | 1.02 | 43      | +B1       | 99.20%         | 3081         | 86.71% | +0.26   |
| Cadillac     | V-Series.R | LMDH  | 1:27.44 | 1:23.79 | 1044kg | 507.0kw | 210.0kph   |    -    | 507.00kw |  901MJ  | 272.43kph |    -    | 1.02 | 43      | +C2       | 99.22%         | 5358         | 73.86% | +0.27   |
| Ferrari      | 499P       | LMHHU | 1:26.92 | 1:23.12 | 1073kg | 505.0kw | 210.0kph   |    -    | 505.00kw |  904MJ  | 270.07kph | 190kph  | 1.03 | 43      | -A2       | 99.93%         | 6954         | 90.49% | +0.26   |
| Peugeot      | 9X8Evo     | LMHHU | 1:27.25 | 1:23.80 | 1060kg | 507.0kw | 210.0kph   |    -    | 507.00kw |  907MJ  | 280.29kph | 190kph  | 0.99 | 43      | +B1       | 100.00%        | 1458         | 89.07% | +0.37   |
| Porsche      | 963        | LMDH  | 1:26.79 | 1:23.13 | 1057kg | 513.0kw | 210.0kph   |    -    | 513.00kw |  910MJ  | 270.45kph |    -    | 1.01 | 43      | -B2       | 99.87%         | 14199        | 82.80% | -0.05   |
| Toyota       | GR010      | LMHHU | 1:26.62 | 1:22.68 | 1090kg | 509.0kw | 210.0kph   |    -    | 509.00kw |  911MJ  | 266.67kph | 190kph  | 1.02 | 43      | -C2       | 99.92%         | 5012         | 72.54% | +0.26   |

## Power below Threshhold
| N/Nmax    | A424    | VALKYRIE | M-HYBRID | V-SERIES.R | 499P    | 9X8EVO  | 963     | GR010   |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|
|  0.550    |  255    |  249     |  251     |  250       |  249    |  250    |  253    |  251    |
|  0.575    |  278    |  272     |  274     |  273       |  272    |  273    |  276    |  274    |
|  0.600    |  298    |  292     |  294     |  293       |  292    |  293    |  296    |  294    |
|  0.625    |  320    |  312     |  315     |  314       |  312    |  314    |  317    |  315    |
|  0.650    |  341    |  333     |  336     |  335       |  333    |  335    |  338    |  336    |
|  0.675    |  363    |  355     |  357     |  356       |  355    |  356    |  360    |  357    |
|  0.700    |  385    |  376     |  379     |  377       |  376    |  377    |  382    |  379    |
|  0.725    |  407    |  397     |  400     |  399       |  397    |  399    |  403    |  400    |
|  0.750    |  427    |  417     |  421     |  419       |  417    |  419    |  424    |  421    |
|  0.775    |  446    |  436     |  440     |  438       |  436    |  438    |  443    |  440    |
|  0.800    |  464    |  454     |  457     |  455       |  454    |  455    |  461    |  457    |
|  0.825    |  479    |  469     |  472     |  470       |  469    |  470    |  476    |  472    |
|  0.850    |  491    |  480     |  484     |  482       |  480    |  482    |  487    |  484    |
|  0.875    |  502    |  490     |  494     |  492       |  490    |  492    |  498    |  494    |
|  0.900    |  509    |  497     |  501     |  499       |  497    |  499    |  505    |  501    |
|  0.925    |  514    |  502     |  506     |  504       |  502    |  504    |  510    |  506    |
| **0.950** | **517** | **505**  | **509**  | **507**    | **505** | **507** | **513** | **509** |
|  0.975    |  515    |  503     |  507     |  505       |  503    |  505    |  511    |  507    |
|  1.000    |  511    |  500     |  504     |  502       |  500    |  502    |  507    |  504    |
|  1.025    |  441    |  431     |  435     |  433       |  431    |  433    |  438    |  435    |

## Power above Threshhold
| N/Nmax    | A424    | VALKYRIE   | M-HYBRID | V-SERIES.R | 499P    | 9X8EVO  | 963     | GR010   |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|
|  0.550    |  255    |  250.01    |  251     |  250       |  249    |  250    |  253    |  251    |
|  0.575    |  278    |  273.01    |  274     |  273       |  272    |  273    |  276    |  274    |
|  0.600    |  298    |  293.01    |  294     |  293       |  292    |  293    |  296    |  294    |
|  0.625    |  320    |  314.01    |  315     |  314       |  312    |  314    |  317    |  315    |
|  0.650    |  341    |  335.01    |  336     |  335       |  333    |  335    |  338    |  336    |
|  0.675    |  363    |  356.01    |  357     |  356       |  355    |  356    |  360    |  357    |
|  0.700    |  385    |  377.01    |  379     |  377       |  376    |  377    |  382    |  379    |
|  0.725    |  407    |  399.02    |  400     |  399       |  397    |  399    |  403    |  400    |
|  0.750    |  427    |  419.02    |  421     |  419       |  417    |  419    |  424    |  421    |
|  0.775    |  446    |  438.02    |  440     |  438       |  436    |  438    |  443    |  440    |
|  0.800    |  464    |  455.02    |  457     |  455       |  454    |  455    |  461    |  457    |
|  0.825    |  479    |  470.02    |  472     |  470       |  469    |  470    |  476    |  472    |
|  0.850    |  491    |  482.02    |  484     |  482       |  480    |  482    |  487    |  484    |
|  0.875    |  502    |  492.02    |  494     |  492       |  490    |  492    |  498    |  494    |
|  0.900    |  509    |  499.02    |  501     |  499       |  497    |  499    |  505    |  501    |
|  0.925    |  514    |  504.02    |  506     |  504       |  502    |  504    |  510    |  506    |
| **0.950** | **517** | **507.02** | **509**  | **507**    | **505** | **507** | **513** | **509** |
|  0.975    |  515    |  505.02    |  507     |  505       |  503    |  505    |  511    |  507    |
|  1.000    |  511    |  502.02    |  504     |  502       |  500    |  502    |  507    |  504    |
|  1.025    |  441    |  433.02    |  435     |  433       |  431    |  433    |  438    |  435    |
