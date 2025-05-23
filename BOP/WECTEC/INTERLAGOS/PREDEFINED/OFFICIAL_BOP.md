| Manufacturer     | Car        | Weight | Power   | PINC    | E/Stint | FDS     |
|:-|:-|:-|:-|:-|:-|:-|
| Alpine           | A424       | 1044kg | 516.0kw | -1.30%  | 910MJ   |    -    |
| BMW              | M-Hybrid   | 1044kg | 512.0kw |    -    | 908MJ   |    -    |
| Cadillac         | V-Series.R | 1039kg | 519.0kw | -1.50%  | 907MJ   |    -    |
| Ferrari          | 499P       | 1060kg | 503.0kw | 1.80%   | 905MJ   | 190kph  |
| Isotta Fraschini | Tipo6C     | 1030kg | 520.0kw |    -    | 914MJ   | 190kph  |
| Lamborghini      | SC63       | 1039kg | 519.0kw | -1.00%  | 905MJ   |    -    |
| Peugeot          | 9X8Evo     | 1051kg | 510.0kw |    -    | 909MJ   | 190kph  |
| Porsche          | 963        | 1051kg | 512.0kw |    -    | 908MJ   |    -    |
| Toyota           | GR010      | 1060kg | 506.0kw | 2.80%   | 912MJ   | 190kph  |

![PACECHART](./IMG/OFFICIAL.png)
![STRAIGHTLINEPERFORMANCECHART](./IMG/OFFICIAL_sp.png)
![TYREPERFORMANCECHART](./IMG/OFFICIAL_tw.png)

### BoP Accuracy: 83.83%; Overall BoP Grade: B2
| Manufacturer     | Car        | Type  | RP      | QP      | Weight | Power¹  | Threshhold | PINC    | Power²   | E/Stint | AVG Vmax  | FDS     | RDLC | L/Stint | BOP-Grade | Model Accuracy | Model Points | Match%  | SimDiff |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|
| Alpine           | A424       | LMDH  | 1:26.70 | 1:23.18 | 1044kg | 516.0kw | 250.0kph   | -1.30%  | 509.30kw |  910MJ  | 269.46kph |    -    | 1.03 | 43      | ~A1       | 96.10%         | 2390         | 98.10%  | #       |
| BMW              | M-Hybrid   | LMDH  | 1:26.91 | 1:23.17 | 1044kg | 512.0kw | 250.0kph   |    -    | 512.00kw |  908MJ  | 271.20kph |    -    | 1.03 | 43      | +A2       | 100.00%        | 3339         | 92.97%  | #       |
| Cadillac         | V-Series.R | LMDH  | 1:26.71 | 1:23.09 | 1039kg | 519.0kw | 250.0kph   | -1.50%  | 511.20kw |  907MJ  | 273.42kph |    -    | 1.03 | 43      | ~A1       | 99.56%         | 5841         | 99.61%  | #       |
| Ferrari          | 499P       | LMHHU | 1:26.50 | 1:22.75 | 1060kg | 503.0kw | 250.0kph   | 1.80%   | 512.10kw |  905MJ  | 271.59kph | 190kph  | 1.05 | 43      | -B1       | 99.57%         | 7417         | 87.53%  | #       |
| Isotta Fraschini | Tipo6C     | LMHHU | 1:26.88 | 1:24.76 | 1030kg | 520.0kw | 250.0kph   |    -    | 520.00kw |  914MJ  | 275.75kph | 190kph  | 1.08 | 43      | +C2       | 100.00%        | 132          | 71.83%  | #       |
| Lamborghini      | SC63       | LMDH  | 1:27.20 | 1:24.37 | 1039kg | 519.0kw | 250.0kph   | -1.00%  | 513.80kw |  905MJ  | 269.01kph |    -    | 1.06 | 43      | +C2       | 100.00%        | 784          | 72.69%  | #       |
| Peugeot          | 9X8Evo     | LMHHU | 1:26.82 | 1:23.24 | 1051kg | 510.0kw | 250.0kph   |    -    | 510.00kw |  909MJ  | 278.63kph | 190kph  | 1.00 | 43      | +B2       | 100.00%        | 1891         | 84.22%  | #       |
| Porsche          | 963        | LMDH  | 1:26.89 | 1:23.04 | 1051kg | 512.0kw | 250.0kph   |    -    | 512.00kw |  908MJ  | 270.66kph |    -    | 1.02 | 43      | ~A1       | 98.39%         | 16118        | 100.00% | #       |
| Toyota           | GR010      | LMHHU | 1:25.85 | 1:22.24 | 1060kg | 506.0kw | 250.0kph   | 2.80%   | 520.20kw |  912MJ  | 272.01kph | 190kph  | 1.05 | 43      | -Ω1       | 99.90%         | 5196         | 47.50%  | #       |

## Power below Threshhold
| N/Nmax    | A424    | M-HYBRID | V-SERIES.R | 499P    | TIPO6C  | SC63    | 9X8EVO  | 963     | GR010   |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|
|  0.550    |  254    |  252     |  256       |  248    |  256    |  256    |  251    |  252    |  249    |
|  0.575    |  277    |  275     |  279       |  271    |  279    |  279    |  274    |  275    |  272    |
|  0.600    |  298    |  296     |  299       |  291    |  300    |  299    |  295    |  296    |  292    |
|  0.625    |  319    |  317     |  321       |  311    |  322    |  321    |  316    |  317    |  313    |
|  0.650    |  340    |  338     |  342       |  332    |  343    |  342    |  337    |  338    |  334    |
|  0.675    |  362    |  359     |  364       |  353    |  365    |  364    |  358    |  359    |  355    |
|  0.700    |  384    |  381     |  386       |  374    |  387    |  386    |  380    |  381    |  377    |
|  0.725    |  406    |  403     |  408       |  395    |  409    |  408    |  401    |  403    |  398    |
|  0.750    |  427    |  423     |  429       |  416    |  430    |  429    |  422    |  423    |  418    |
|  0.775    |  446    |  442     |  448       |  435    |  449    |  448    |  441    |  442    |  437    |
|  0.800    |  463    |  460     |  466       |  452    |  467    |  466    |  458    |  460    |  454    |
|  0.825    |  478    |  475     |  481       |  467    |  482    |  481    |  473    |  475    |  469    |
|  0.850    |  490    |  486     |  493       |  478    |  494    |  493    |  485    |  486    |  481    |
|  0.875    |  501    |  497     |  504       |  488    |  505    |  504    |  495    |  497    |  491    |
|  0.900    |  508    |  504     |  511       |  495    |  512    |  511    |  502    |  504    |  498    |
|  0.925    |  513    |  509     |  516       |  500    |  517    |  516    |  507    |  509    |  503    |
| **0.950** | **516** | **512**  | **519**    | **503** | **520** | **519** | **510** | **512** | **506** |
|  0.975    |  514    |  510     |  517       |  501    |  518    |  517    |  508    |  510    |  504    |
|  1.000    |  510    |  506     |  513       |  498    |  514    |  513    |  505    |  506    |  501    |
|  1.025    |  441    |  437     |  443       |  430    |  444    |  443    |  436    |  437    |  432    |

## Power above Threshhold
| N/Nmax    | A424       | M-HYBRID | V-SERIES.R | 499P       | TIPO6C  | SC63       | 9X8EVO  | 963     | GR010      |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|
|  0.550    |  251.14    |  252     |  252.11    |  252.03    |  256    |  253.40    |  251    |  252    |  256.08    |
|  0.575    |  274.16    |  275     |  275.12    |  275.03    |  279    |  276.44    |  274    |  275    |  279.09    |
|  0.600    |  294.17    |  296     |  295.12    |  296.03    |  300    |  296.47    |  295    |  296    |  300.10    |
|  0.625    |  315.18    |  317     |  316.13    |  317.03    |  322    |  317.50    |  316    |  317    |  322.10    |
|  0.650    |  336.19    |  338     |  337.14    |  338.04    |  343    |  338.53    |  337    |  338    |  343.11    |
|  0.675    |  357.20    |  359     |  359.15    |  359.04    |  365    |  360.57    |  358    |  359    |  365.12    |
|  0.700    |  379.22    |  381     |  380.16    |  381.04    |  387    |  382.60    |  380    |  381    |  387.13    |
|  0.725    |  400.23    |  403     |  402.17    |  403.04    |  409    |  403.64    |  401    |  403    |  409.13    |
|  0.750    |  421.24    |  423     |  422.18    |  423.04    |  430    |  424.67    |  422    |  423    |  430.14    |
|  0.775    |  440.25    |  442     |  441.19    |  442.05    |  449    |  443.70    |  441    |  442    |  449.15    |
|  0.800    |  457.26    |  460     |  459.19    |  460.05    |  467    |  461.73    |  458    |  460    |  467.15    |
|  0.825    |  472.27    |  475     |  474.20    |  475.05    |  482    |  476.75    |  473    |  475    |  482.16    |
|  0.850    |  484.28    |  486     |  485.20    |  486.05    |  494    |  487.77    |  485    |  486    |  494.16    |
|  0.875    |  494.28    |  497     |  496.21    |  497.05    |  505    |  498.79    |  495    |  497    |  505.16    |
|  0.900    |  501.29    |  504     |  503.21    |  504.05    |  512    |  505.80    |  502    |  504    |  512.17    |
|  0.925    |  506.29    |  509     |  508.21    |  509.05    |  517    |  510.81    |  507    |  509    |  517.17    |
| **0.950** | **509.29** | **512**  | **511.22** | **512.05** | **520** | **513.81** | **510** | **512** | **520.17** |
|  0.975    |  507.29    |  510     |  509.21    |  510.05    |  518    |  511.81    |  508    |  510    |  518.17    |
|  1.000    |  504.29    |  506     |  505.21    |  506.05    |  514    |  507.80    |  505    |  506    |  514.17    |
|  1.025    |  435.25    |  437     |  436.18    |  437.05    |  444    |  438.69    |  436    |  437    |  444.14    |
