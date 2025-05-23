| Manufacturer | Car        | Weight | Power   | PINC    | E/Stint | FDS     |
|:-|:-|:-|:-|:-|:-|:-|
| Toyota       | GR010      | 1099kg | 512.0kw | 1.00%   | 914MJ   | 190kph  |
| Ferrari      | 499P       | 1083kg | 508.0kw | 1.00%   | 910MJ   | 190kph  |
| Cadillac     | V-Series.R | 1054kg | 510.0kw | 1.00%   | 902MJ   |    -    |
| Porsche      | 963        | 1067kg | 516.0kw |    -    | 914MJ   |    -    |
| BMW          | M-Hybrid   | 1061kg | 512.0kw | 1.00%   | 911MJ   |    -    |
| Alpine       | A424       | 1067kg | 520.0kw |    -    | 924MJ   |    -    |
| Aston Martin | Valkyrie   | 1042kg | 506.0kw | 0.40%   | 901MJ   |    -    |
| Peugeot      | 9X8Evo     | 1060kg | 510.0kw | -1.00%  | 914MJ   | 190kph  |

![PACECHART](./IMG/ACOMETHOD.png)
![STRAIGHTLINEPERFORMANCECHART](./IMG/ACOMETHOD_sp.png)
![TYREPERFORMANCECHART](./IMG/ACOMETHOD_tw.png)

### BoP Accuracy: 90.06%; Overall BoP Grade: A2
| Manufacturer | Car        | Type  | RP      | QP      | Weight | Power¹  | Threshhold | PINC    | Power²   | E/Stint | AVG Vmax  | FDS     | RDLC | L/Stint | BOP-Grade | Model Accuracy | Model Points | Match%  | SimDiff |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|
| Alpine       | A424       | LMDH  | 1:42.47 | 1:38.89 | 1067kg | 520.0kw | 210.0kph   |    -    | 520.00kw |  924MJ  | 304.03kph |    -    | 1.01 | 33      | -B2       | 96.10%         | 2390         | 83.29%  | -0.16   |
| Aston Martin | Valkyrie   | LMHNH | 1:43.07 | 1:38.97 | 1042kg | 506.0kw | 210.0kph   | 0.40%   | 508.00kw |  901MJ  | 303.28kph |    -    | 1.03 | 33      | +C2       | 100.00%        | 466          | 72.83%  | -0.00   |
| BMW          | M-Hybrid   | LMDH  | 1:42.78 | 1:38.93 | 1061kg | 512.0kw | 210.0kph   | 1.00%   | 517.10kw |  911MJ  | 305.45kph |    -    | 1.02 | 33      | ~A1       | 100.00%        | 3339         | 95.51%  | -0.18   |
| Cadillac     | V-Series.R | LMDH  | 1:42.82 | 1:39.09 | 1054kg | 510.0kw | 210.0kph   | 1.00%   | 515.10kw |  902MJ  | 307.50kph |    -    | 1.02 | 33      | ~A1       | 99.56%         | 5841         | 99.97%  | +0.27   |
| Ferrari      | 499P       | LMHHU | 1:42.86 | 1:38.95 | 1083kg | 508.0kw | 210.0kph   | 1.00%   | 513.10kw |  910MJ  | 304.88kph | 190kph  | 1.02 | 33      | ~A1       | 99.57%         | 7417         | 100.00% | +0.05   |
| Peugeot      | 9X8Evo     | LMHHU | 1:43.08 | 1:39.39 | 1060kg | 510.0kw | 210.0kph   | -1.00%  | 504.90kw |  914MJ  | 313.04kph | 190kph  | 1.00 | 33      | +C1       | 100.00%        | 1891         | 79.70%  | +0.37   |
| Porsche      | 963        | LMDH  | 1:42.79 | 1:38.81 | 1067kg | 516.0kw | 210.0kph   |    -    | 516.00kw |  914MJ  | 305.01kph |    -    | 1.01 | 33      | ~A1       | 98.39%         | 16118        | 99.59%  | -0.35   |
| Toyota       | GR010      | LMHHU | 1:43.08 | 1:39.26 | 1099kg | 512.0kw | 210.0kph   | 1.00%   | 517.10kw |  914MJ  | 303.10kph | 190kph  | 1.01 | 33      | +B1       | 99.90%         | 5196         | 89.57%  | +0.01   |

## Power below Threshhold
| N/Nmax    | A424    | VALKYRIE | M-HYBRID | V-SERIES.R | 499P    | 9X8EVO  | 963     | GR010   |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|
|  0.550    |  256    |  249     |  252     |  251       |  250    |  251    |  254    |  252    |
|  0.575    |  279    |  272     |  275     |  274       |  273    |  274    |  277    |  275    |
|  0.600    |  300    |  292     |  296     |  295       |  293    |  295    |  298    |  296    |
|  0.625    |  322    |  313     |  317     |  316       |  314    |  316    |  319    |  317    |
|  0.650    |  343    |  334     |  338     |  337       |  335    |  337    |  340    |  338    |
|  0.675    |  365    |  355     |  359     |  358       |  357    |  358    |  362    |  359    |
|  0.700    |  387    |  377     |  381     |  380       |  378    |  380    |  384    |  381    |
|  0.725    |  409    |  398     |  403     |  401       |  399    |  401    |  406    |  403    |
|  0.750    |  430    |  418     |  423     |  422       |  420    |  422    |  427    |  423    |
|  0.775    |  449    |  437     |  442     |  441       |  439    |  441    |  446    |  442    |
|  0.800    |  467    |  454     |  460     |  458       |  456    |  458    |  463    |  460    |
|  0.825    |  482    |  469     |  475     |  473       |  471    |  473    |  478    |  475    |
|  0.850    |  494    |  481     |  486     |  485       |  483    |  485    |  490    |  486    |
|  0.875    |  505    |  491     |  497     |  495       |  493    |  495    |  501    |  497    |
|  0.900    |  512    |  498     |  504     |  502       |  500    |  502    |  508    |  504    |
|  0.925    |  517    |  503     |  509     |  507       |  505    |  507    |  513    |  509    |
| **0.950** | **520** | **506**  | **512**  | **510**    | **508** | **510** | **516** | **512** |
|  0.975    |  518    |  504     |  510     |  508       |  506    |  508    |  514    |  510    |
|  1.000    |  514    |  501     |  506     |  505       |  503    |  505    |  510    |  506    |
|  1.025    |  444    |  432     |  437     |  436       |  434    |  436    |  441    |  437    |

## Power above Threshhold
| N/Nmax    | A424    | VALKYRIE   | M-HYBRID   | V-SERIES.R | 499P       | 9X8EVO     | 963     | GR010      |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|
|  0.550    |  256    |  250.01    |  255.06    |  254.05    |  253.04    |  248.44    |  254    |  255.06    |
|  0.575    |  279    |  273.01    |  278.06    |  277.05    |  276.04    |  271.48    |  277    |  278.06    |
|  0.600    |  300    |  293.01    |  298.07    |  297.06    |  296.05    |  291.52    |  298    |  298.07    |
|  0.625    |  322    |  314.01    |  320.07    |  319.06    |  317.05    |  312.56    |  319    |  320.07    |
|  0.650    |  343    |  335.02    |  341.08    |  340.07    |  338.05    |  333.59    |  340    |  341.08    |
|  0.675    |  365    |  357.02    |  363.08    |  362.07    |  360.06    |  354.63    |  362    |  363.08    |
|  0.700    |  387    |  378.02    |  385.09    |  383.07    |  382.06    |  375.67    |  384    |  385.09    |
|  0.725    |  409    |  399.02    |  407.09    |  405.08    |  403.06    |  396.71    |  406    |  407.09    |
|  0.750    |  430    |  420.02    |  427.10    |  426.08    |  424.07    |  416.74    |  427    |  427.10    |
|  0.775    |  449    |  439.02    |  446.10    |  445.09    |  443.07    |  435.78    |  446    |  446.10    |
|  0.800    |  467    |  456.02    |  464.11    |  463.09    |  461.07    |  453.81    |  463    |  464.11    |
|  0.825    |  482    |  471.02    |  479.11    |  478.09    |  476.07    |  468.84    |  478    |  479.11    |
|  0.850    |  494    |  483.02    |  491.11    |  489.09    |  487.08    |  479.86    |  490    |  491.11    |
|  0.875    |  505    |  493.02    |  502.12    |  500.10    |  498.08    |  489.87    |  501    |  502.12    |
|  0.900    |  512    |  500.02    |  509.12    |  507.10    |  505.08    |  496.89    |  508    |  509.12    |
|  0.925    |  517    |  505.02    |  514.12    |  512.10    |  510.08    |  501.89    |  513    |  514.12    |
| **0.950** | **520** | **508.02** | **517.12** | **515.10** | **513.08** | **504.90** | **516** | **517.12** |
|  0.975    |  518    |  506.02    |  515.12    |  513.10    |  511.08    |  502.90    |  514    |  515.12    |
|  1.000    |  514    |  503.02    |  511.12    |  509.10    |  507.08    |  499.89    |  510    |  511.12    |
|  1.025    |  444    |  434.02    |  441.10    |  440.09    |  438.07    |  430.77    |  441    |  441.10    |
