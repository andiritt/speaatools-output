| Manufacturer     | Car        | Weight | Power   | PINC    | E/Stint | FDS     |
|:-|:-|:-|:-|:-|:-|:-|
| Alpine           | A424       | 1034kg | 493.0kw | -2.60%  | 881MJ   |    -    |
| BMW              | M-Hybrid   | 1054kg | 509.0kw | -4.50%  | 891MJ   |    -    |
| Cadillac         | V-Series.R | 1080kg | 486.0kw | 4.60%   | 895MJ   |    -    |
| Ferrari          | 499P       | 1100kg | 480.0kw | 0.50%   | 879MJ   | 200kph  |
| Isotta Fraschini | Tipo6C     | 1091kg | 517.0kw | -1.00%  | 915MJ   | 190kph  |
| Lamborghini      | SC63       | 1057kg | 520.0kw | -2.90%  | 903MJ   |    -    |
| Peugeot          | 9X8Evo     | 1089kg | 480.0kw |    -    | 876MJ   | 190kph  |
| Porsche          | 963        | 1052kg | 485.0kw | 0.40%   | 884MJ   |    -    |
| Toyota           | GR010      | 1100kg | 480.0kw | 0.10%   | 884MJ   | 200kph  |

![PACECHART](./IMG/AUTO.png)
![STRAIGHTLINEPERFORMANCECHART](./IMG/AUTO_sp.png)
![TYREPERFORMANCECHART](./IMG/AUTO_tw.png)

### BoP Accuracy: 88.81%; Overall BoP Grade: B1
| Manufacturer     | Car        | Type  | RP      | QP      | Weight | Power¹  | Threshhold | PINC    | Power²   | E/Stint | AVG Vmax  | FDS     | RDLC | L/Stint | BOP-Grade | Model Accuracy | Model Points | Match%  | SimDiff |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|
| Alpine           | A424       | LMDH  | 1:52.51 | 1:47.66 | 1034kg | 493.0kw | 250.0kph   | -2.60%  | 480.20kw |  881MJ  | 285.75kph |    -    | 1.02 | 34      | +A2       | 100.00%        | 946          | 92.46%  | #       |
| BMW              | M-Hybrid   | LMDH  | 1:52.52 | 1:47.36 | 1054kg | 509.0kw | 250.0kph   | -4.50%  | 486.10kw |  891MJ  | 283.39kph |    -    | 1.01 | 34      | ~A1       | 100.00%        | 1998         | 96.99%  | #       |
| Cadillac         | V-Series.R | LMDH  | 1:52.52 | 1:47.67 | 1080kg | 486.0kw | 250.0kph   | 4.60%   | 508.40kw |  895MJ  | 281.30kph |    -    | 0.98 | 34      | +B1       | 98.11%         | 3991         | 89.33%  | +1.19   |
| Ferrari          | 499P       | LMHHU | 1:51.94 | 1:46.97 | 1100kg | 480.0kw | 250.0kph   | 0.50%   | 482.40kw |  879MJ  | 280.25kph | 200kph  | 0.99 | 34      | -B2       | 98.72%         | 4180         | 81.26%  | +1.92   |
| Isotta Fraschini | Tipo6C     | LMHHU | 1:52.52 | 1:49.12 | 1091kg | 517.0kw | 250.0kph   | -1.00%  | 511.80kw |  915MJ  | 283.85kph | 190kph  | 1.01 | 34      | +C2       | 97.73%         | 129          | 70.94%  | #       |
| Lamborghini      | SC63       | LMDH  | 1:52.52 | 1:48.15 | 1057kg | 520.0kw | 250.0kph   | -2.90%  | 504.90kw |  903MJ  | 285.29kph |    -    | 1.03 | 34      | ~A1       | 100.00%        | 784          | 95.76%  | #       |
| Peugeot          | 9X8Evo     | LMHHU | 1:52.53 | 1:47.92 | 1089kg | 480.0kw | 250.0kph   |    -    | 480.00kw |  876MJ  | 279.54kph | 190kph  | 0.97 | 34      | +A2       | 100.00%        | 636          | 92.93%  | #       |
| Porsche          | 963        | LMDH  | 1:52.52 | 1:47.20 | 1052kg | 485.0kw | 250.0kph   | 0.40%   | 486.90kw |  884MJ  | 283.49kph |    -    | 1.01 | 34      | ~A1       | 99.91%         | 11713        | 100.00% | +0.67   |
| Toyota           | GR010      | LMHHU | 1:51.92 | 1:46.77 | 1100kg | 480.0kw | 250.0kph   | 0.10%   | 480.50kw |  884MJ  | 279.57kph | 200kph  | 1.00 | 34      | -C1       | 99.90%         | 3123         | 79.59%  | +1.58   |

## Power below Threshhold
| N/Nmax    | A424    | M-HYBRID | V-SERIES.R | 499P    | TIPO6C  | SC63    | 9X8EVO  | 963     | GR010   |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|
|  0.550    |  243    |  251     |  239       |  236    |  255    |  256    |  236    |  239    |  236    |
|  0.575    |  265    |  274     |  261       |  258    |  278    |  279    |  258    |  261    |  258    |
|  0.600    |  285    |  294     |  281       |  277    |  298    |  300    |  277    |  280    |  277    |
|  0.625    |  305    |  315     |  301       |  297    |  320    |  322    |  297    |  300    |  297    |
|  0.650    |  325    |  336     |  321       |  317    |  341    |  343    |  317    |  320    |  317    |
|  0.675    |  346    |  357     |  341       |  337    |  363    |  365    |  337    |  341    |  337    |
|  0.700    |  367    |  379     |  362       |  358    |  385    |  387    |  358    |  362    |  358    |
|  0.725    |  388    |  400     |  383       |  378    |  407    |  409    |  378    |  382    |  378    |
|  0.750    |  407    |  421     |  402       |  397    |  427    |  430    |  397    |  401    |  397    |
|  0.775    |  426    |  440     |  420       |  415    |  446    |  449    |  415    |  419    |  415    |
|  0.800    |  443    |  457     |  436       |  431    |  464    |  467    |  431    |  436    |  431    |
|  0.825    |  457    |  472     |  451       |  445    |  479    |  482    |  445    |  450    |  445    |
|  0.850    |  468    |  484     |  462       |  456    |  491    |  494    |  456    |  461    |  456    |
|  0.875    |  478    |  494     |  472       |  466    |  502    |  505    |  466    |  471    |  466    |
|  0.900    |  485    |  501     |  478       |  472    |  509    |  512    |  472    |  477    |  472    |
|  0.925    |  490    |  506     |  483       |  477    |  514    |  517    |  477    |  482    |  477    |
| **0.950** | **493** | **509**  | **486**    | **480** | **517** | **520** | **480** | **485** | **480** |
|  0.975    |  491    |  507     |  484       |  478    |  515    |  518    |  478    |  483    |  478    |
|  1.000    |  488    |  504     |  481       |  475    |  511    |  514    |  475    |  480    |  475    |
|  1.025    |  421    |  435     |  415       |  410    |  441    |  444    |  410    |  414    |  410    |

## Power above Threshhold
| N/Nmax    | A424       | M-HYBRID   | V-SERIES.R | 499P       | TIPO6C     | SC63       | 9X8EVO  | 963        | GR010      |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|
|  0.550    |  236.09    |  239.05    |  250.18    |  237.20    |  252.41    |  248.45    |  236    |  239.46    |  236.24    |
|  0.575    |  258.10    |  261.05    |  273.19    |  259.21    |  275.45    |  271.49    |  258    |  261.50    |  258.26    |
|  0.600    |  277.11    |  281.05    |  293.21    |  278.23    |  295.48    |  291.53    |  277    |  281.54    |  277.28    |
|  0.625    |  297.11    |  301.06    |  314.22    |  298.25    |  316.51    |  312.57    |  297    |  301.58    |  297.30    |
|  0.650    |  317.12    |  321.06    |  335.23    |  318.26    |  337.55    |  333.61    |  317    |  321.62    |  317.32    |
|  0.675    |  337.13    |  341.07    |  357.25    |  338.28    |  359.58    |  354.65    |  337    |  341.66    |  337.34    |
|  0.700    |  358.14    |  362.07    |  378.26    |  359.30    |  380.62    |  375.68    |  358    |  362.70    |  358.36    |
|  0.725    |  378.14    |  383.07    |  399.28    |  380.32    |  402.65    |  396.72    |  378    |  383.74    |  378.38    |
|  0.750    |  397.15    |  402.08    |  420.29    |  399.33    |  422.69    |  416.76    |  397    |  402.78    |  397.40    |
|  0.775    |  415.16    |  420.08    |  439.31    |  417.35    |  441.72    |  435.79    |  415    |  420.81    |  415.41    |
|  0.800    |  431.16    |  436.09    |  456.32    |  433.36    |  459.75    |  453.83    |  431    |  436.84    |  431.43    |
|  0.825    |  445.17    |  451.09    |  471.33    |  447.37    |  474.77    |  468.85    |  445    |  451.87    |  445.44    |
|  0.850    |  456.17    |  462.09    |  483.34    |  458.38    |  485.79    |  479.87    |  456    |  462.89    |  456.46    |
|  0.875    |  466.18    |  472.09    |  493.35    |  468.39    |  496.81    |  489.89    |  466    |  472.91    |  466.47    |
|  0.900    |  472.18    |  478.09    |  500.35    |  474.39    |  503.82    |  496.91    |  472    |  478.92    |  472.47    |
|  0.925    |  477.18    |  483.09    |  505.35    |  479.40    |  508.83    |  501.91    |  477    |  483.93    |  477.48    |
| **0.950** | **480.18** | **486.09** | **508.36** | **482.40** | **511.83** | **504.92** | **480** | **486.94** | **480.48** |
|  0.975    |  478.18    |  484.09    |  506.35    |  480.40    |  509.83    |  502.92    |  478    |  484.94    |  478.48    |
|  1.000    |  475.18    |  481.09    |  503.35    |  477.40    |  505.82    |  499.91    |  475    |  481.93    |  475.47    |
|  1.025    |  410.16    |  415.08    |  434.30    |  412.34    |  436.71    |  430.78    |  410    |  415.80    |  410.41    |
