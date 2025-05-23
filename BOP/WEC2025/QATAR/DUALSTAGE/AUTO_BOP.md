| Manufacturer | Car        | Weight | Power   | PINC    | E/Stint | FDS     |
|:-|:-|:-|:-|:-|:-|:-|
| Toyota       | GR010      | 1083kg | 519.0kw | 0.10%   | 917MJ   | 190kph  |
| Ferrari      | 499P       | 1081kg | 519.0kw | 0.10%   | 918MJ   | 190kph  |
| Cadillac     | V-Series.R | 1052kg | 520.0kw |    -    | 908MJ   |    -    |
| Porsche      | 963        | 1055kg | 516.0kw | 0.70%   | 914MJ   |    -    |
| BMW          | M-Hybrid   | 1055kg | 519.0kw | 0.10%   | 915MJ   |    -    |
| Alpine       | A424       | 1058kg | 515.0kw | 0.90%   | 920MJ   |    -    |
| Aston Martin | Valkyrie   | 1031kg | 508.0kw | 2.30%   | 905MJ   |    -    |
| Peugeot      | 9X8Evo     | 1030kg | 520.0kw | -7.30%  | 907MJ   | 190kph  |

![PACECHART](./IMG/AUTO.png)
![STRAIGHTLINEPERFORMANCECHART](./IMG/AUTO_sp.png)
![TYREPERFORMANCECHART](./IMG/AUTO_tw.png)

### BoP Accuracy: 94.43%; Overall BoP Grade: A2
| Manufacturer | Car        | Type  | RP      | QP      | Weight | Power¹  | Threshhold | PINC    | Power²   | E/Stint | AVG Vmax  | FDS     | RDLC | L/Stint | BOP-Grade | Model Accuracy | Model Points | Match%  | SimDiff |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|
| Alpine       | A424       | LMDH  | 1:42.33 | 1:38.75 | 1058kg | 515.0kw | 210.0kph   | 0.90%   | 519.60kw |  920MJ  | 304.62kph |    -    | 1.02 | 33      | ~A1       | 96.10%         | 2390         | 96.25%  | -0.16   |
| Aston Martin | Valkyrie   | LMHNH | 1:42.33 | 1:38.29 | 1031kg | 508.0kw | 210.0kph   | 2.30%   | 519.70kw |  905MJ  | 306.39kph |    -    | 1.04 | 33      | +C2       | 100.00%        | 466          | 73.46%  | -0.00   |
| BMW          | M-Hybrid   | LMDH  | 1:42.31 | 1:38.49 | 1055kg | 519.0kw | 210.0kph   | 0.10%   | 519.50kw |  915MJ  | 306.86kph |    -    | 1.02 | 33      | ~A1       | 100.00%        | 3339         | 100.00% | -0.18   |
| Cadillac     | V-Series.R | LMDH  | 1:42.32 | 1:38.64 | 1052kg | 520.0kw | 210.0kph   |    -    | 520.00kw |  908MJ  | 309.07kph |    -    | 1.02 | 33      | ~A1       | 99.56%         | 5841         | 98.27%  | +0.27   |
| Ferrari      | 499P       | LMHHU | 1:42.30 | 1:38.43 | 1081kg | 519.0kw | 210.0kph   | 0.10%   | 519.50kw |  918MJ  | 306.74kph | 190kph  | 1.02 | 33      | ~A1       | 99.57%         | 7417         | 100.00% | +0.05   |
| Peugeot      | 9X8Evo     | LMHHU | 1:42.31 | 1:38.68 | 1030kg | 520.0kw | 210.0kph   | -7.30%  | 482.00kw |  907MJ  | 313.16kph | 190kph  | 1.03 | 33      | +B1       | 100.00%        | 1891         | 87.48%  | +0.37   |
| Porsche      | 963        | LMDH  | 1:42.30 | 1:38.35 | 1055kg | 516.0kw | 210.0kph   | 0.70%   | 519.60kw |  914MJ  | 306.83kph |    -    | 1.02 | 33      | ~A1       | 98.39%         | 16118        | 100.00% | -0.35   |
| Toyota       | GR010      | LMHHU | 1:42.30 | 1:38.54 | 1083kg | 519.0kw | 210.0kph   | 0.10%   | 519.50kw |  917MJ  | 305.50kph | 190kph  | 1.02 | 33      | ~A1       | 99.90%         | 5196         | 100.00% | +0.01   |

## Power below Threshhold
| N/Nmax    | A424    | VALKYRIE | M-HYBRID | V-SERIES.R | 499P    | 9X8EVO  | 963     | GR010   |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|
|  0.550    |  254    |  250     |  256     |  256       |  256    |  256    |  254    |  256    |
|  0.575    |  277    |  273     |  279     |  279       |  279    |  279    |  277    |  279    |
|  0.600    |  297    |  293     |  299     |  300       |  299    |  300    |  298    |  299    |
|  0.625    |  319    |  314     |  321     |  322       |  321    |  322    |  319    |  321    |
|  0.650    |  340    |  335     |  342     |  343       |  342    |  343    |  340    |  342    |
|  0.675    |  362    |  357     |  364     |  365       |  364    |  365    |  362    |  364    |
|  0.700    |  383    |  378     |  386     |  387       |  386    |  387    |  384    |  386    |
|  0.725    |  405    |  399     |  408     |  409       |  408    |  409    |  406    |  408    |
|  0.750    |  426    |  420     |  429     |  430       |  429    |  430    |  427    |  429    |
|  0.775    |  445    |  439     |  448     |  449       |  448    |  449    |  446    |  448    |
|  0.800    |  463    |  456     |  466     |  467       |  466    |  467    |  463    |  466    |
|  0.825    |  478    |  471     |  481     |  482       |  481    |  482    |  478    |  481    |
|  0.850    |  489    |  483     |  493     |  494       |  493    |  494    |  490    |  493    |
|  0.875    |  500    |  493     |  504     |  505       |  504    |  505    |  501    |  504    |
|  0.900    |  507    |  500     |  511     |  512       |  511    |  512    |  508    |  511    |
|  0.925    |  512    |  505     |  516     |  517       |  516    |  517    |  513    |  516    |
| **0.950** | **515** | **508**  | **519**  | **520**    | **519** | **520** | **516** | **519** |
|  0.975    |  513    |  506     |  517     |  518       |  517    |  518    |  514    |  517    |
|  1.000    |  509    |  503     |  513     |  514       |  513    |  514    |  510    |  513    |
|  1.025    |  440    |  434     |  443     |  444       |  443    |  444    |  441    |  443    |

## Power above Threshhold
| N/Nmax    | A424       | VALKYRIE   | M-HYBRID   | V-SERIES.R | 499P       | 9X8EVO     | 963        | GR010      |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|
|  0.550    |  256.31    |  256.34    |  256.26    |  256       |  256.26    |  237.02    |  256.30    |  256.26    |
|  0.575    |  279.34    |  279.37    |  279.28    |  279       |  279.28    |  259.02    |  279.33    |  279.28    |
|  0.600    |  299.37    |  299.39    |  299.30    |  300       |  299.30    |  278.02    |  299.35    |  299.30    |
|  0.625    |  321.39    |  321.42    |  321.32    |  322       |  321.32    |  298.02    |  321.38    |  321.32    |
|  0.650    |  342.42    |  342.45    |  342.34    |  343       |  342.34    |  318.03    |  342.40    |  342.34    |
|  0.675    |  364.45    |  364.48    |  364.36    |  365       |  364.36    |  338.03    |  364.43    |  364.36    |
|  0.700    |  386.47    |  386.51    |  386.39    |  387       |  386.39    |  359.03    |  386.46    |  386.39    |
|  0.725    |  408.50    |  408.54    |  408.41    |  409       |  408.41    |  380.03    |  408.48    |  408.41    |
|  0.750    |  429.52    |  429.57    |  429.43    |  430       |  429.43    |  399.03    |  429.51    |  429.43    |
|  0.775    |  448.55    |  448.59    |  448.45    |  449       |  448.45    |  417.03    |  448.53    |  448.45    |
|  0.800    |  466.57    |  466.61    |  466.47    |  467       |  466.47    |  433.04    |  466.55    |  466.47    |
|  0.825    |  481.59    |  481.63    |  481.48    |  482       |  481.48    |  447.04    |  481.57    |  481.48    |
|  0.850    |  493.60    |  493.65    |  493.49    |  494       |  493.49    |  458.04    |  493.58    |  493.49    |
|  0.875    |  504.62    |  504.66    |  504.50    |  505       |  504.50    |  468.04    |  504.59    |  504.50    |
|  0.900    |  511.63    |  511.67    |  511.51    |  512       |  511.51    |  474.04    |  511.60    |  511.51    |
|  0.925    |  516.63    |  516.68    |  516.52    |  517       |  516.52    |  479.04    |  516.61    |  516.52    |
| **0.950** | **519.64** | **519.68** | **519.52** | **520**    | **519.52** | **482.04** | **519.61** | **519.52** |
|  0.975    |  517.63    |  517.68    |  517.52    |  518       |  517.52    |  480.04    |  517.61    |  517.52    |
|  1.000    |  513.63    |  513.68    |  513.51    |  514       |  513.51    |  477.04    |  513.60    |  513.51    |
|  1.025    |  443.54    |  443.58    |  443.44    |  444       |  443.44    |  412.03    |  443.52    |  443.44    |
