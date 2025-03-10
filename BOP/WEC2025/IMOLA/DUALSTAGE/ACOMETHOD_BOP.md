| Manufacturer | Car        | Weight | Power   | PINC    | E/Stint | FDS     |
|:-|:-|:-|:-|:-|:-|:-|
| Alpine       | A424       | 1057kg | 517.0kw |    -    | 913MJ   |    -    |
| Aston Martin | Valkyrie   | 1042kg | 505.0kw | 0.40%   | 900MJ   |    -    |
| BMW          | M-Hybrid   | 1051kg | 509.0kw | 1.00%   | 907MJ   |    -    |
| Cadillac     | V-Series.R | 1044kg | 507.0kw | 1.00%   | 903MJ   |    -    |
| Ferrari      | 499P       | 1073kg | 505.0kw | 1.00%   | 905MJ   | 190kph  |
| Peugeot      | 9X8Evo     | 1060kg | 507.0kw |    -    | 903MJ   | 190kph  |
| Porsche      | 963        | 1057kg | 513.0kw | 1.00%   | 910MJ   |    -    |
| Toyota       | GR010      | 1090kg | 509.0kw | 1.00%   | 915MJ   | 190kph  |

![PACECHART](./IMG/ACOMETHOD.png)
![STRAIGHTLINEPERFORMANCECHART](./IMG/ACOMETHOD_sp.png)
![TYREPERFORMANCECHART](./IMG/ACOMETHOD_tw.png)

### BoP Accuracy: 86.90%; Overall BoP Grade: B1
| Manufacturer | Car        | Type  | RP      | QP      | Weight | Power¹  | Threshhold | PINC    | Power²   | E/Stint | AVG Vmax  | FDS     | RDLC | L/Stint | BOP-Grade | Model Accuracy | Model Points | Match%  | SimDiff |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|
| Alpine       | A424       | LMDH  | 1:34.58 | 1:30.52 | 1057kg | 517.0kw | 210.0kph   |    -    | 517.00kw |  913MJ  | 298.38kph |    -    | 1.02 | 37      | -B2       | 99.37%         | 2056         | 84.80%  | +0.05   |
| Aston Martin | Valkyrie   | LMHNH | 1:35.31 | 1:30.95 | 1042kg | 505.0kw | 210.0kph   | 0.40%   | 507.00kw |  900MJ  | 288.21kph |    -    | 1.05 | 37      | +E1       | 100.00%        | 247          | 58.96%  | #       |
| BMW          | M-Hybrid   | LMDH  | 1:34.86 | 1:30.41 | 1051kg | 509.0kw | 210.0kph   | 1.00%   | 514.10kw |  907MJ  | 300.67kph |    -    | 1.03 | 37      | ~A1       | 99.20%         | 3081         | 100.00% | -0.15   |
| Cadillac     | V-Series.R | LMDH  | 1:34.69 | 1:30.38 | 1044kg | 507.0kw | 210.0kph   | 1.00%   | 512.10kw |  903MJ  | 302.59kph |    -    | 1.03 | 37      | -A2       | 99.22%         | 5358         | 90.35%  | +0.25   |
| Ferrari      | 499P       | LMHHU | 1:34.90 | 1:30.37 | 1073kg | 505.0kw | 210.0kph   | 1.00%   | 510.10kw |  905MJ  | 299.98kph | 190kph  | 1.03 | 37      | ~A1       | 99.93%         | 6954         | 100.00% | -0.10   |
| Peugeot      | 9X8Evo     | LMHHU | 1:35.20 | 1:31.06 | 1060kg | 507.0kw | 210.0kph   |    -    | 507.00kw |  903MJ  | 310.50kph | 190kph  | 1.00 | 37      | +B2       | 100.00%        | 1458         | 81.09%  | +0.34   |
| Porsche      | 963        | LMDH  | 1:34.54 | 1:30.18 | 1057kg | 513.0kw | 210.0kph   | 1.00%   | 518.10kw |  910MJ  | 300.40kph |    -    | 1.02 | 37      | -B2       | 99.87%         | 14199        | 82.07%  | -0.02   |
| Toyota       | GR010      | LMHHU | 1:35.16 | 1:30.42 | 1090kg | 509.0kw | 210.0kph   | 1.00%   | 514.10kw |  915MJ  | 296.19kph | 190kph  | 1.02 | 37      | ~A1       | 99.92%         | 5012         | 97.97%  | -0.16   |

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
| N/Nmax    | A424    | VALKYRIE   | M-HYBRID   | V-SERIES.R | 499P       | 9X8EVO  | 963        | GR010      |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|
|  0.550    |  255    |  250.01    |  253.04    |  252.03    |  251.02    |  250    |  255.06    |  253.04    |
|  0.575    |  278    |  273.01    |  276.05    |  275.04    |  274.03    |  273    |  278.07    |  276.05    |
|  0.600    |  298    |  293.01    |  297.05    |  296.04    |  295.03    |  293    |  299.08    |  297.05    |
|  0.625    |  320    |  314.01    |  318.06    |  317.04    |  316.03    |  314    |  321.08    |  318.06    |
|  0.650    |  341    |  335.01    |  339.06    |  338.05    |  337.03    |  335    |  342.09    |  339.06    |
|  0.675    |  363    |  356.01    |  361.06    |  359.05    |  358.04    |  356    |  364.09    |  361.06    |
|  0.700    |  385    |  377.01    |  383.07    |  381.05    |  380.04    |  377    |  386.10    |  383.07    |
|  0.725    |  407    |  399.02    |  404.07    |  403.06    |  401.04    |  399    |  407.10    |  404.07    |
|  0.750    |  427    |  419.02    |  425.07    |  423.06    |  422.04    |  419    |  428.11    |  425.07    |
|  0.775    |  446    |  438.02    |  444.08    |  442.06    |  441.04    |  438    |  447.11    |  444.08    |
|  0.800    |  464    |  455.02    |  462.08    |  460.06    |  458.04    |  455    |  465.12    |  462.08    |
|  0.825    |  479    |  470.02    |  477.08    |  475.06    |  473.05    |  470    |  480.12    |  477.08    |
|  0.850    |  491    |  482.02    |  488.09    |  486.07    |  485.05    |  482    |  492.12    |  488.09    |
|  0.875    |  502    |  492.02    |  499.09    |  497.07    |  495.05    |  492    |  503.13    |  499.09    |
|  0.900    |  509    |  499.02    |  506.09    |  504.07    |  502.05    |  499    |  510.13    |  506.09    |
|  0.925    |  514    |  504.02    |  511.09    |  509.07    |  507.05    |  504    |  515.13    |  511.09    |
| **0.950** | **517** | **507.02** | **514.09** | **512.07** | **510.05** | **507** | **518.13** | **514.09** |
|  0.975    |  515    |  505.02    |  512.09    |  510.07    |  508.05    |  505    |  516.13    |  512.09    |
|  1.000    |  511    |  502.02    |  508.09    |  506.07    |  505.05    |  502    |  512.13    |  508.09    |
|  1.025    |  441    |  433.02    |  439.08    |  437.06    |  436.04    |  433    |  442.11    |  439.08    |
