| Manufacturer | Car        | Weight | Power   | PINC    | E/Stint | FDS     |
|:-|:-|:-|:-|:-|:-|:-|
| Acura        | ARX06      | 1070kg | 512.0kw |    -    | 912MJ   |    -    |
| BMW          | M-Hybrid   | 1043kg | 509.0kw | -1.00%  | 900MJ   |    -    |
| Cadillac     | V-Series.R | 1040kg | 507.0kw | -1.00%  | 903MJ   |    -    |
| Lamborghini  | SC63       | 1042kg | 517.0kw |    -    | 911MJ   |    -    |
| Porsche      | 963        | 1057kg | 513.0kw | -1.00%  | 908MJ   |    -    |

![PACECHART](./IMG/ACOMETHOD.png)
![STRAIGHTLINEPERFORMANCECHART](./IMG/ACOMETHOD_sp.png)
![TYREPERFORMANCECHART](./IMG/ACOMETHOD_tw.png)

### BoP Accuracy: 94.65%; Overall BoP Grade: A2
| Manufacturer | Car        | Type | RP      | QP      | Weight | Power¹  | Threshhold | PINC    | Power²   | E/Stint | AVG Vmax  | FDS     | RDLC | L/Stint | BOP-Grade | Model Accuracy | Model Points | Match% | SimDiff |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|
| Acura        | ARX06      | LMDH | 1:52.27 | 1:47.29 | 1070kg | 512.0kw | 210.0kph   |    -    | 512.00kw |  912MJ  | 279.41kph |    -    | 1.00 | 29      | +B1       | 100.00%        | 996          | 89.79% | #       |
| BMW          | M-Hybrid   | LMDH | 1:52.29 | 1:47.29 | 1043kg | 509.0kw | 210.0kph   | -1.00%  | 503.90kw |  900MJ  | 279.30kph |    -    | 1.03 | 29      | ~A1       | 99.20%         | 3081         | 98.25% | -0.33   |
| Cadillac     | V-Series.R | LMDH | 1:52.27 | 1:47.44 | 1040kg | 507.0kw | 210.0kph   | -1.00%  | 501.90kw |  903MJ  | 280.70kph |    -    | 1.03 | 29      | +A2       | 99.22%         | 5358         | 90.79% | +1.20   |
| Lamborghini  | SC63       | LMDH | 1:52.31 | 1:48.54 | 1042kg | 517.0kw | 210.0kph   |    -    | 517.00kw |  911MJ  | 277.46kph |    -    | 1.06 | 29      | ~A1       | 100.00%        | 784          | 98.61% | #       |
| Porsche      | 963        | LMDH | 1:52.10 | 1:47.20 | 1057kg | 513.0kw | 210.0kph   | -1.00%  | 507.90kw |  908MJ  | 278.28kph |    -    | 1.02 | 29      | ~A1       | 99.87%         | 14199        | 95.79% | +0.77   |

## Power below Threshhold
| N/Nmax    | ARX06   | M-HYBRID | V-SERIES.R | SC63    | 963     |
|:-|:-|:-|:-|:-|:-|
|  0.550    |  252    |  251     |  250       |  255    |  253    |
|  0.575    |  275    |  274     |  273       |  278    |  276    |
|  0.600    |  296    |  294     |  293       |  298    |  296    |
|  0.625    |  317    |  315     |  314       |  320    |  317    |
|  0.650    |  338    |  336     |  335       |  341    |  338    |
|  0.675    |  359    |  357     |  356       |  363    |  360    |
|  0.700    |  381    |  379     |  377       |  385    |  382    |
|  0.725    |  403    |  400     |  399       |  407    |  403    |
|  0.750    |  423    |  421     |  419       |  427    |  424    |
|  0.775    |  442    |  440     |  438       |  446    |  443    |
|  0.800    |  460    |  457     |  455       |  464    |  461    |
|  0.825    |  475    |  472     |  470       |  479    |  476    |
|  0.850    |  486    |  484     |  482       |  491    |  487    |
|  0.875    |  497    |  494     |  492       |  502    |  498    |
|  0.900    |  504    |  501     |  499       |  509    |  505    |
|  0.925    |  509    |  506     |  504       |  514    |  510    |
| **0.950** | **512** | **509**  | **507**    | **517** | **513** |
|  0.975    |  510    |  507     |  505       |  515    |  511    |
|  1.000    |  506    |  504     |  502       |  511    |  507    |
|  1.025    |  437    |  435     |  433       |  441    |  438    |

## Power above Threshhold
| N/Nmax    | ARX06   | M-HYBRID   | V-SERIES.R | SC63    | 963        |
|:-|:-|:-|:-|:-|:-|
|  0.550    |  252    |  248.45    |  247.46    |  255    |  250.43    |
|  0.575    |  275    |  271.49    |  270.50    |  278    |  273.47    |
|  0.600    |  296    |  291.53    |  290.54    |  298    |  293.50    |
|  0.625    |  317    |  311.56    |  310.58    |  320    |  314.54    |
|  0.650    |  338    |  332.60    |  331.61    |  341    |  335.57    |
|  0.675    |  359    |  353.64    |  352.65    |  363    |  356.61    |
|  0.700    |  381    |  374.68    |  373.69    |  385    |  377.65    |
|  0.725    |  403    |  395.71    |  394.73    |  407    |  399.68    |
|  0.750    |  423    |  416.75    |  414.77    |  427    |  419.72    |
|  0.775    |  442    |  435.79    |  433.80    |  446    |  438.75    |
|  0.800    |  460    |  452.82    |  450.84    |  464    |  455.78    |
|  0.825    |  475    |  467.84    |  465.86    |  479    |  470.81    |
|  0.850    |  486    |  478.86    |  476.88    |  491    |  482.83    |
|  0.875    |  497    |  488.88    |  486.90    |  502    |  492.84    |
|  0.900    |  504    |  495.90    |  493.92    |  509    |  499.86    |
|  0.925    |  509    |  500.90    |  498.92    |  514    |  504.86    |
| **0.950** | **512** | **503.91** | **501.93** | **517** | **507.87** |
|  0.975    |  510    |  501.91    |  499.93    |  515    |  505.87    |
|  1.000    |  506    |  498.90    |  496.92    |  511    |  502.86    |
|  1.025    |  437    |  430.78    |  428.79    |  441    |  433.74    |
