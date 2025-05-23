| Manufacturer | Car        | Weight | Power   | PINC    | E/Stint | FDS     |
|:-|:-|:-|:-|:-|:-|:-|
| Toyota       | GR010      | 1076kg | 520.0kw |    -    | 915MJ   | 190kph  |
| Ferrari      | 499P       | 1074kg | 520.0kw |    -    | 916MJ   | 190kph  |
| Cadillac     | V-Series.R | 1046kg | 515.0kw | 0.90%   | 909MJ   |    -    |
| Porsche      | 963        | 1049kg | 510.0kw | 1.90%   | 910MJ   |    -    |
| BMW          | M-Hybrid   | 1049kg | 513.0kw | 1.30%   | 913MJ   |    -    |
| Alpine       | A424       | 1052kg | 510.0kw | 1.90%   | 914MJ   |    -    |
| Aston Martin | Valkyrie   | 1031kg | 510.0kw | 1.90%   | 907MJ   |    -    |
| Peugeot      | 9X8Evo     | 1030kg | 510.0kw |    -    | 905MJ   | 190kph  |

![PACECHART](./IMG/AUTO.png)
![STRAIGHTLINEPERFORMANCECHART](./IMG/AUTO_sp.png)
![TYREPERFORMANCECHART](./IMG/AUTO_tw.png)

### BoP Accuracy: 94.58%; Overall BoP Grade: A2
| Manufacturer | Car        | Type  | RP      | QP      | Weight | Power¹  | Threshhold | PINC    | Power²   | E/Stint | AVG Vmax  | FDS     | RDLC | L/Stint | BOP-Grade | Model Accuracy | Model Points | Match%  | SimDiff |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|
| Alpine       | A424       | LMDH  | 1:54.98 | 1:50.51 | 1052kg | 510.0kw | 210.0kph   | 1.90%   | 519.70kw |  914MJ  | 291.17kph |    -    | 1.02 | 34      | ~A1       | 96.10%         | 2390         | 96.92%  | +0.10   |
| Aston Martin | Valkyrie   | LMHNH | 1:54.97 | 1:49.98 | 1031kg | 510.0kw | 210.0kph   | 1.90%   | 519.70kw |  907MJ  | 292.65kph |    -    | 1.05 | 34      | +C2       | 100.00%        | 466          | 73.44%  | #       |
| BMW          | M-Hybrid   | LMDH  | 1:54.99 | 1:50.23 | 1049kg | 513.0kw | 210.0kph   | 1.30%   | 519.70kw |  913MJ  | 293.25kph |    -    | 1.02 | 34      | ~A1       | 100.00%        | 3339         | 100.00% | -0.06   |
| Cadillac     | V-Series.R | LMDH  | 1:54.98 | 1:50.38 | 1046kg | 515.0kw | 210.0kph   | 0.90%   | 519.60kw |  909MJ  | 295.33kph |    -    | 1.02 | 34      | ~A1       | 99.56%         | 5841         | 98.78%  | -0.19   |
| Ferrari      | 499P       | LMHHU | 1:54.97 | 1:50.16 | 1074kg | 520.0kw | 210.0kph   |    -    | 520.00kw |  916MJ  | 293.60kph | 190kph  | 1.03 | 34      | ~A1       | 99.57%         | 7417         | 100.00% | +0.52   |
| Peugeot      | 9X8Evo     | LMHHU | 1:54.98 | 1:50.44 | 1030kg | 510.0kw | 210.0kph   |    -    | 510.00kw |  905MJ  | 302.72kph | 190kph  | 1.03 | 34      | +B1       | 100.00%        | 1891         | 87.48%  | -0.17   |
| Porsche      | 963        | LMDH  | 1:54.98 | 1:50.09 | 1049kg | 510.0kw | 210.0kph   | 1.90%   | 519.70kw |  910MJ  | 293.23kph |    -    | 1.02 | 34      | ~A1       | 98.39%         | 16118        | 100.00% | +0.21   |
| Toyota       | GR010      | LMHHU | 1:54.97 | 1:50.28 | 1076kg | 520.0kw | 210.0kph   |    -    | 520.00kw |  915MJ  | 292.42kph | 190kph  | 1.03 | 34      | ~A1       | 99.90%         | 5196         | 100.00% | +0.48   |

## Power below Threshhold
| N/Nmax    | A424    | VALKYRIE | M-HYBRID | V-SERIES.R | 499P    | 9X8EVO  | 963     | GR010   |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|
|  0.550    |  251    |  251     |  253     |  254       |  256    |  251    |  251    |  256    |
|  0.575    |  274    |  274     |  276     |  277       |  279    |  274    |  274    |  279    |
|  0.600    |  295    |  295     |  296     |  297       |  300    |  295    |  295    |  300    |
|  0.625    |  316    |  316     |  317     |  319       |  322    |  316    |  316    |  322    |
|  0.650    |  337    |  337     |  338     |  340       |  343    |  337    |  337    |  343    |
|  0.675    |  358    |  358     |  360     |  362       |  365    |  358    |  358    |  365    |
|  0.700    |  380    |  380     |  382     |  383       |  387    |  380    |  380    |  387    |
|  0.725    |  401    |  401     |  403     |  405       |  409    |  401    |  401    |  409    |
|  0.750    |  422    |  422     |  424     |  426       |  430    |  422    |  422    |  430    |
|  0.775    |  441    |  441     |  443     |  445       |  449    |  441    |  441    |  449    |
|  0.800    |  458    |  458     |  461     |  463       |  467    |  458    |  458    |  467    |
|  0.825    |  473    |  473     |  476     |  478       |  482    |  473    |  473    |  482    |
|  0.850    |  485    |  485     |  487     |  489       |  494    |  485    |  485    |  494    |
|  0.875    |  495    |  495     |  498     |  500       |  505    |  495    |  495    |  505    |
|  0.900    |  502    |  502     |  505     |  507       |  512    |  502    |  502    |  512    |
|  0.925    |  507    |  507     |  510     |  512       |  517    |  507    |  507    |  517    |
| **0.950** | **510** | **510**  | **513**  | **515**    | **520** | **510** | **510** | **520** |
|  0.975    |  508    |  508     |  511     |  513       |  518    |  508    |  508    |  518    |
|  1.000    |  505    |  505     |  507     |  509       |  514    |  505    |  505    |  514    |
|  1.025    |  436    |  436     |  438     |  440       |  444    |  436    |  436    |  444    |

## Power above Threshhold
| N/Nmax    | A424       | VALKYRIE   | M-HYBRID   | V-SERIES.R | 499P    | 9X8EVO  | 963        | GR010   |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|
|  0.550    |  256.34    |  256.34    |  256.33    |  256.31    |  256    |  251    |  256.34    |  256    |
|  0.575    |  279.37    |  279.37    |  279.36    |  279.34    |  279    |  274    |  279.37    |  279    |
|  0.600    |  299.40    |  299.40    |  299.39    |  299.37    |  300    |  295    |  299.40    |  300    |
|  0.625    |  321.43    |  321.43    |  321.41    |  321.39    |  322    |  316    |  321.43    |  322    |
|  0.650    |  342.45    |  342.45    |  342.44    |  342.42    |  343    |  337    |  342.45    |  343    |
|  0.675    |  364.48    |  364.48    |  364.47    |  364.45    |  365    |  358    |  364.48    |  365    |
|  0.700    |  386.51    |  386.51    |  386.50    |  386.47    |  387    |  380    |  386.51    |  387    |
|  0.725    |  408.54    |  408.54    |  408.53    |  408.50    |  409    |  401    |  408.54    |  409    |
|  0.750    |  429.57    |  429.57    |  429.55    |  429.52    |  430    |  422    |  429.57    |  430    |
|  0.775    |  448.60    |  448.60    |  448.58    |  448.55    |  449    |  441    |  448.60    |  449    |
|  0.800    |  466.62    |  466.62    |  466.60    |  466.57    |  467    |  458    |  466.62    |  467    |
|  0.825    |  481.64    |  481.64    |  481.62    |  481.59    |  482    |  473    |  481.64    |  482    |
|  0.850    |  493.66    |  493.66    |  493.64    |  493.60    |  494    |  485    |  493.66    |  494    |
|  0.875    |  504.67    |  504.67    |  504.65    |  504.62    |  505    |  495    |  504.67    |  505    |
|  0.900    |  511.68    |  511.68    |  511.66    |  511.63    |  512    |  502    |  511.68    |  512    |
|  0.925    |  516.69    |  516.69    |  516.67    |  516.63    |  517    |  507    |  516.69    |  517    |
| **0.950** | **519.69** | **519.69** | **519.67** | **519.64** | **520** | **510** | **519.69** | **520** |
|  0.975    |  517.69    |  517.69    |  517.67    |  517.63    |  518    |  508    |  517.69    |  518    |
|  1.000    |  513.68    |  513.68    |  513.66    |  513.63    |  514    |  505    |  513.68    |  514    |
|  1.025    |  443.59    |  443.59    |  443.57    |  443.54    |  444    |  436    |  443.59    |  444    |
