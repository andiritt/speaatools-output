| Manufacturer | Car        | Weight | Power   | PINC    | E/Stint | FDS     |
|:-|:-|:-|:-|:-|:-|:-|
| Acura        | ARX06      | 1082kg | 508.0kw | 1.00%   | 912MJ   |    -    |
| BMW          | M-Hybrid   | 1051kg | 509.0kw | -1.00%  | 904MJ   |    -    |
| Cadillac     | V-Series.R | 1044kg | 507.0kw | -1.00%  | 899MJ   |    -    |
| Lamborghini  | SC63       | 1042kg | 520.0kw |    -    | 909MJ   |    -    |
| Porsche      | 963        | 1057kg | 513.0kw | 1.00%   | 902MJ   |    -    |

![PACECHART](./IMG/ACOMETHOD.png)
![STRAIGHTLINEPERFORMANCECHART](./IMG/ACOMETHOD_sp.png)
![TYREPERFORMANCECHART](./IMG/ACOMETHOD_tw.png)

### BoP Accuracy: 89.67%; Overall BoP Grade: B1
| Manufacturer | Car        | Type | RP      | QP      | Weight | Power¹  | Threshhold | PINC    | Power²   | E/Stint | AVG Vmax  | FDS     | RDLC | L/Stint | BOP-Grade | Model Accuracy | Model Points | Match% | SimDiff |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|
| Acura        | ARX06      | LMDH | 1:37.45 | 1:32.09 | 1082kg | 508.0kw | 210.0kph   | 1.00%   | 513.10kw |  912MJ  | 306.46kph |    -    | 0.99 | 29      | -B1       | 100.00%        | 996          | 87.92% | +0.13   |
| BMW          | M-Hybrid   | LMDH | 1:37.53 | 1:32.15 | 1051kg | 509.0kw | 210.0kph   | -1.00%  | 503.90kw |  904MJ  | 306.89kph |    -    | 1.02 | 29      | ~A1       | 99.20%         | 3081         | 99.88% | +0.13   |
| Cadillac     | V-Series.R | LMDH | 1:37.42 | 1:32.18 | 1044kg | 507.0kw | 210.0kph   | -1.00%  | 501.90kw |  899MJ  | 308.86kph |    -    | 1.03 | 29      | +A2       | 99.22%         | 5358         | 94.14% | -0.20   |
| Lamborghini  | SC63       | LMDH | 1:37.99 | 1:33.62 | 1042kg | 520.0kw | 210.0kph   |    -    | 520.00kw |  909MJ  | 306.32kph |    -    | 1.06 | 30      | +C1       | 100.00%        | 784          | 77.72% | #       |
| Porsche      | 963        | LMDH | 1:37.27 | 1:31.98 | 1057kg | 513.0kw | 210.0kph   | 1.00%   | 518.10kw |  902MJ  | 308.10kph |    -    | 1.02 | 29      | -B1       | 99.87%         | 14199        | 88.68% | +0.14   |

## Power below Threshhold
| N/Nmax    | ARX06   | M-HYBRID | V-SERIES.R | SC63    | 963     |
|:-|:-|:-|:-|:-|:-|
|  0.550    |  250    |  251     |  250       |  256    |  253    |
|  0.575    |  273    |  274     |  273       |  279    |  276    |
|  0.600    |  293    |  294     |  293       |  300    |  296    |
|  0.625    |  314    |  315     |  314       |  322    |  317    |
|  0.650    |  335    |  336     |  335       |  343    |  338    |
|  0.675    |  357    |  357     |  356       |  365    |  360    |
|  0.700    |  378    |  379     |  377       |  387    |  382    |
|  0.725    |  399    |  400     |  399       |  409    |  403    |
|  0.750    |  420    |  421     |  419       |  430    |  424    |
|  0.775    |  439    |  440     |  438       |  449    |  443    |
|  0.800    |  456    |  457     |  455       |  467    |  461    |
|  0.825    |  471    |  472     |  470       |  482    |  476    |
|  0.850    |  483    |  484     |  482       |  494    |  487    |
|  0.875    |  493    |  494     |  492       |  505    |  498    |
|  0.900    |  500    |  501     |  499       |  512    |  505    |
|  0.925    |  505    |  506     |  504       |  517    |  510    |
| **0.950** | **508** | **509**  | **507**    | **520** | **513** |
|  0.975    |  506    |  507     |  505       |  518    |  511    |
|  1.000    |  503    |  504     |  502       |  514    |  507    |
|  1.025    |  434    |  435     |  433       |  444    |  438    |

## Power above Threshhold
| N/Nmax    | ARX06      | M-HYBRID   | V-SERIES.R | SC63    | 963        |
|:-|:-|:-|:-|:-|:-|
|  0.550    |  253.04    |  248.45    |  247.46    |  256    |  255.06    |
|  0.575    |  276.04    |  271.49    |  270.50    |  279    |  278.07    |
|  0.600    |  296.05    |  291.53    |  290.54    |  300    |  299.08    |
|  0.625    |  317.05    |  311.56    |  310.58    |  322    |  321.08    |
|  0.650    |  338.05    |  332.60    |  331.61    |  343    |  342.09    |
|  0.675    |  360.06    |  353.64    |  352.65    |  365    |  364.09    |
|  0.700    |  382.06    |  374.68    |  373.69    |  387    |  386.10    |
|  0.725    |  403.06    |  395.71    |  394.73    |  409    |  407.10    |
|  0.750    |  424.07    |  416.75    |  414.77    |  430    |  428.11    |
|  0.775    |  443.07    |  435.79    |  433.80    |  449    |  447.11    |
|  0.800    |  461.07    |  452.82    |  450.84    |  467    |  465.12    |
|  0.825    |  476.07    |  467.84    |  465.86    |  482    |  480.12    |
|  0.850    |  487.08    |  478.86    |  476.88    |  494    |  492.12    |
|  0.875    |  498.08    |  488.88    |  486.90    |  505    |  503.13    |
|  0.900    |  505.08    |  495.90    |  493.92    |  512    |  510.13    |
|  0.925    |  510.08    |  500.90    |  498.92    |  517    |  515.13    |
| **0.950** | **513.08** | **503.91** | **501.93** | **520** | **518.13** |
|  0.975    |  511.08    |  501.91    |  499.93    |  518    |  516.13    |
|  1.000    |  507.08    |  498.90    |  496.92    |  514    |  512.13    |
|  1.025    |  438.07    |  430.78    |  428.79    |  444    |  442.11    |
