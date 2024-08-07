| Manufacturer     | Car        | Weight | Power   | PINC    | E/Stint | FDS     |
|:-|:-|:-|:-|:-|:-|:-|
| Alpine           | A424       | 1057kg | 517.0kw |    -    | 912MJ   |    -    |
| BMW              | M-Hybrid   | 1049kg | 509.0kw |    -    | 903MJ   |    -    |
| Cadillac         | V-Series.R | 1044kg | 507.0kw |    -    | 898MJ   |    -    |
| Ferrari          | 499P       | 1073kg | 505.0kw |    -    | 897MJ   | 190kph  |
| Isotta Fraschini | Tipo6C     | 1063kg | 517.0kw |    -    | 915MJ   | 190kph  |
| Lamborghini      | SC63       | 1042kg | 520.0kw |    -    | 909MJ   |    -    |
| Peugeot          | 9X8Evo     | 1060kg | 507.0kw |    -    | 897MJ   | 190kph  |
| Porsche          | 963        | 1057kg | 513.0kw |    -    | 909MJ   |    -    |
| Toyota           | GR010      | 1090kg | 509.0kw |    -    | 909MJ   | 190kph  |

![PACECHART](./IMG/ACOMETHOD.png)
![STRAIGHTLINEPERFORMANCECHART](./IMG/ACOMETHOD_sp.png)
![TYREPERFORMANCECHART](./IMG/ACOMETHOD_tw.png)

### BoP Accuracy: 74.92%; Overall BoP Grade: C2
| Manufacturer     | Car        | Type  | RP      | QP      | Weight | Power¹  | Threshhold | PINC    | Power²   | E/Stint | AVG Vmax  | FDS     | RDLC | L/Stint | BOP-Grade | Model Accuracy | Model Points | Match%  | SimDiff |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|
| Alpine           | A424       | LMDH  | 1:51.58 | 1:46.80 | 1057kg | 517.0kw | 210.0kph   |    -    | 517.00kw |  912MJ  | 290.58kph |    -    | 1.00 | 34      | +B2       | 100.00%        | 946          | 82.57%  | #       |
| BMW              | M-Hybrid   | LMDH  | 1:51.82 | 1:46.71 | 1049kg | 509.0kw | 210.0kph   |    -    | 509.00kw |  903MJ  | 287.62kph |    -    | 1.01 | 34      | +B1       | 100.00%        | 1998         | 87.07%  | #       |
| Cadillac         | V-Series.R | LMDH  | 1:51.42 | 1:46.64 | 1044kg | 507.0kw | 210.0kph   |    -    | 507.00kw |  898MJ  | 285.47kph |    -    | 1.02 | 34      | +B1       | 98.11%         | 3991         | 87.63%  | +1.19   |
| Ferrari          | 499P       | LMHHU | 1:50.28 | 1:45.43 | 1073kg | 505.0kw | 210.0kph   |    -    | 505.00kw |  897MJ  | 287.63kph | 190kph  | 1.02 | 34      | -E1       | 98.72%         | 4180         | 55.50%  | +1.92   |
| Isotta Fraschini | Tipo6C     | LMHHU | 1:51.82 | 1:48.45 | 1063kg | 517.0kw | 210.0kph   |    -    | 517.00kw |  915MJ  | 287.36kph | 190kph  | 1.04 | 34      | +Ω1       | 97.73%         | 129          | 49.50%  | #       |
| Lamborghini      | SC63       | LMDH  | 1:51.81 | 1:47.49 | 1042kg | 520.0kw | 210.0kph   |    -    | 520.00kw |  909MJ  | 289.19kph |    -    | 1.04 | 34      | +C1       | 100.00%        | 784          | 75.15%  | #       |
| Peugeot          | 9X8Evo     | LMHHU | 1:50.74 | 1:46.25 | 1060kg | 507.0kw | 210.0kph   |    -    | 507.00kw |  897MJ  | 287.94kph | 190kph  | 1.00 | 34      | -C1       | 100.00%        | 636          | 77.52%  | #       |
| Porsche          | 963        | LMDH  | 1:51.41 | 1:46.18 | 1057kg | 513.0kw | 210.0kph   |    -    | 513.00kw |  909MJ  | 288.49kph |    -    | 1.00 | 34      | ~A1       | 99.91%         | 11713        | 100.00% | +0.67   |
| Toyota           | GR010      | LMHHU | 1:50.36 | 1:45.34 | 1090kg | 509.0kw | 210.0kph   |    -    | 509.00kw |  909MJ  | 286.44kph | 190kph  | 1.00 | 34      | -E1       | 99.90%         | 3123         | 59.29%  | +1.58   |

## Power below Threshhold
| N/Nmax    | A424    | M-HYBRID | V-SERIES.R | 499P    | TIPO6C  | SC63    | 9X8EVO  | 963     | GR010   |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|
|  0.550    |  255    |  251     |  250       |  249    |  255    |  256    |  250    |  253    |  251    |
|  0.575    |  278    |  274     |  273       |  272    |  278    |  279    |  273    |  276    |  274    |
|  0.600    |  298    |  294     |  293       |  292    |  298    |  300    |  293    |  296    |  294    |
|  0.625    |  320    |  315     |  314       |  312    |  320    |  322    |  314    |  317    |  315    |
|  0.650    |  341    |  336     |  335       |  333    |  341    |  343    |  335    |  338    |  336    |
|  0.675    |  363    |  357     |  356       |  355    |  363    |  365    |  356    |  360    |  357    |
|  0.700    |  385    |  379     |  377       |  376    |  385    |  387    |  377    |  382    |  379    |
|  0.725    |  407    |  400     |  399       |  397    |  407    |  409    |  399    |  403    |  400    |
|  0.750    |  427    |  421     |  419       |  417    |  427    |  430    |  419    |  424    |  421    |
|  0.775    |  446    |  440     |  438       |  436    |  446    |  449    |  438    |  443    |  440    |
|  0.800    |  464    |  457     |  455       |  454    |  464    |  467    |  455    |  461    |  457    |
|  0.825    |  479    |  472     |  470       |  469    |  479    |  482    |  470    |  476    |  472    |
|  0.850    |  491    |  484     |  482       |  480    |  491    |  494    |  482    |  487    |  484    |
|  0.875    |  502    |  494     |  492       |  490    |  502    |  505    |  492    |  498    |  494    |
|  0.900    |  509    |  501     |  499       |  497    |  509    |  512    |  499    |  505    |  501    |
|  0.925    |  514    |  506     |  504       |  502    |  514    |  517    |  504    |  510    |  506    |
| **0.950** | **517** | **509**  | **507**    | **505** | **517** | **520** | **507** | **513** | **509** |
|  0.975    |  515    |  507     |  505       |  503    |  515    |  518    |  505    |  511    |  507    |
|  1.000    |  511    |  504     |  502       |  500    |  511    |  514    |  502    |  507    |  504    |
|  1.025    |  441    |  435     |  433       |  431    |  441    |  444    |  433    |  438    |  435    |

## Power above Threshhold
| N/Nmax    | A424    | M-HYBRID | V-SERIES.R | 499P    | TIPO6C  | SC63    | 9X8EVO  | 963     | GR010   |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|
|  0.550    |  255    |  251     |  250       |  249    |  255    |  256    |  250    |  253    |  251    |
|  0.575    |  278    |  274     |  273       |  272    |  278    |  279    |  273    |  276    |  274    |
|  0.600    |  298    |  294     |  293       |  292    |  298    |  300    |  293    |  296    |  294    |
|  0.625    |  320    |  315     |  314       |  312    |  320    |  322    |  314    |  317    |  315    |
|  0.650    |  341    |  336     |  335       |  333    |  341    |  343    |  335    |  338    |  336    |
|  0.675    |  363    |  357     |  356       |  355    |  363    |  365    |  356    |  360    |  357    |
|  0.700    |  385    |  379     |  377       |  376    |  385    |  387    |  377    |  382    |  379    |
|  0.725    |  407    |  400     |  399       |  397    |  407    |  409    |  399    |  403    |  400    |
|  0.750    |  427    |  421     |  419       |  417    |  427    |  430    |  419    |  424    |  421    |
|  0.775    |  446    |  440     |  438       |  436    |  446    |  449    |  438    |  443    |  440    |
|  0.800    |  464    |  457     |  455       |  454    |  464    |  467    |  455    |  461    |  457    |
|  0.825    |  479    |  472     |  470       |  469    |  479    |  482    |  470    |  476    |  472    |
|  0.850    |  491    |  484     |  482       |  480    |  491    |  494    |  482    |  487    |  484    |
|  0.875    |  502    |  494     |  492       |  490    |  502    |  505    |  492    |  498    |  494    |
|  0.900    |  509    |  501     |  499       |  497    |  509    |  512    |  499    |  505    |  501    |
|  0.925    |  514    |  506     |  504       |  502    |  514    |  517    |  504    |  510    |  506    |
| **0.950** | **517** | **509**  | **507**    | **505** | **517** | **520** | **507** | **513** | **509** |
|  0.975    |  515    |  507     |  505       |  503    |  515    |  518    |  505    |  511    |  507    |
|  1.000    |  511    |  504     |  502       |  500    |  511    |  514    |  502    |  507    |  504    |
|  1.025    |  441    |  435     |  433       |  431    |  441    |  444    |  433    |  438    |  435    |
