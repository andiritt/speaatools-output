| Manufacturer     | Car        | Weight | Power   | PINC    | E/Stint | FDS     |
|:-|:-|:-|:-|:-|:-|:-|
| Alpine           | A424       | 1036kg | 480.0kw |    -    | 878MJ   |    -    |
| BMW              | M-Hybrid   | 1036kg | 480.0kw |    -    | 877MJ   |    -    |
| Cadillac         | V-Series.R | 1045kg | 480.0kw |    -    | 876MJ   |    -    |
| Ferrari          | 499P       | 1070kg | 480.0kw |    -    | 880MJ   | 190kph  |
| Isotta Fraschini | Tipo6C     | 1081kg | 520.0kw |    -    | 922MJ   | 190kph  |
| Lamborghini      | SC63       | 1062kg | 502.0kw |    -    | 899MJ   |    -    |
| Peugeot          | 9X8Evo     | 1048kg | 480.0kw |    -    | 878MJ   | 190kph  |
| Porsche          | 963        | 1048kg | 480.0kw |    -    | 877MJ   |    -    |
| Toyota           | GR010      | 1075kg | 480.0kw |    -    | 885MJ   | 190kph  |

![PACECHART](./IMG/AUTO.png)
![STRAIGHTLINEPERFORMANCECHART](./IMG/AUTO_sp.png)
![TYREPERFORMANCECHART](./IMG/AUTO_tw.png)

### BoP Accuracy: 94.85%; Overall BoP Grade: A2
| Manufacturer     | Car        | Type  | RP      | QP      | Weight | Power¹  | Threshhold | PINC    | Power²   | E/Stint | AVG Vmax  | FDS     | RDLC | L/Stint | BOP-Grade | Model Accuracy | Model Points | Match%  | SimDiff |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|
| Alpine           | A424       | LMDH  | 1:36.06 | 1:32.45 | 1036kg | 480.0kw | 0.0kph     |    -    | 480.00kw |  878MJ  | 307.58kph |    -    | 1.02 | 37      | ~A1       | 99.49%         | 1360         | 100.00% | +0.10   |
| BMW              | M-Hybrid   | LMDH  | 1:36.06 | 1:31.63 | 1036kg | 480.0kw | 0.0kph     |    -    | 480.00kw |  877MJ  | 306.29kph |    -    | 1.02 | 37      | ~A1       | 98.62%         | 2363         | 100.00% | -0.15   |
| Cadillac         | V-Series.R | LMDH  | 1:36.05 | 1:31.94 | 1045kg | 480.0kw | 0.0kph     |    -    | 480.00kw |  876MJ  | 300.74kph |    -    | 1.02 | 37      | ~A1       | 98.50%         | 4201         | 95.13%  | +0.47   |
| Ferrari          | 499P       | LMHHU | 1:36.05 | 1:31.81 | 1070kg | 480.0kw | 0.0kph     |    -    | 480.00kw |  880MJ  | 304.75kph | 190kph  | 1.02 | 37      | ~A1       | 100.00%        | 4441         | 99.03%  | -0.17   |
| Isotta Fraschini | Tipo6C     | LMHHU | 1:36.04 | 1:33.30 | 1081kg | 520.0kw | 0.0kph     |    -    | 520.00kw |  922MJ  | 306.66kph | 190kph  | 1.02 | 37      | +B2       | 98.48%         | 130          | 80.15%  | +0.16   |
| Lamborghini      | SC63       | LMDH  | 1:36.05 | 1:32.53 | 1062kg | 502.0kw | 0.0kph     |    -    | 502.00kw |  899MJ  | 303.82kph |    -    | 1.02 | 37      | ~A1       | 100.00%        | 784          | 97.72%  | -0.22   |
| Peugeot          | 9X8Evo     | LMHHU | 1:36.04 | 1:32.15 | 1048kg | 480.0kw | 0.0kph     |    -    | 480.00kw |  878MJ  | 306.70kph | 190kph  | 1.01 | 37      | +B2       | 100.00%        | 808          | 84.75%  | -0.06   |
| Porsche          | 963        | LMDH  | 1:36.04 | 1:31.58 | 1048kg | 480.0kw | 0.0kph     |    -    | 480.00kw |  877MJ  | 303.92kph |    -    | 1.01 | 37      | ~A1       | 99.87%         | 12613        | 99.42%  | -0.14   |
| Toyota           | GR010      | LMHHU | 1:36.06 | 1:31.64 | 1075kg | 480.0kw | 0.0kph     |    -    | 480.00kw |  885MJ  | 301.73kph | 190kph  | 1.01 | 37      | ~A1       | 99.73%         | 2956         | 97.46%  | +0.00   |

## Power below Threshhold
| N/Nmax    | A424    | M-HYBRID | V-SERIES.R | 499P    | TIPO6C  | SC63    | 9X8EVO  | 963     | GR010   |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|
|  0.550    |  236    |  236     |  236       |  236    |  256    |  247    |  236    |  236    |  236    |
|  0.575    |  258    |  258     |  258       |  258    |  279    |  270    |  258    |  258    |  258    |
|  0.600    |  277    |  277     |  277       |  277    |  300    |  290    |  277    |  277    |  277    |
|  0.625    |  297    |  297     |  297       |  297    |  322    |  310    |  297    |  297    |  297    |
|  0.650    |  317    |  317     |  317       |  317    |  343    |  331    |  317    |  317    |  317    |
|  0.675    |  337    |  337     |  337       |  337    |  365    |  352    |  337    |  337    |  337    |
|  0.700    |  358    |  358     |  358       |  358    |  387    |  374    |  358    |  358    |  358    |
|  0.725    |  378    |  378     |  378       |  378    |  409    |  395    |  378    |  378    |  378    |
|  0.750    |  397    |  397     |  397       |  397    |  430    |  415    |  397    |  397    |  397    |
|  0.775    |  415    |  415     |  415       |  415    |  449    |  434    |  415    |  415    |  415    |
|  0.800    |  431    |  431     |  431       |  431    |  467    |  451    |  431    |  431    |  431    |
|  0.825    |  445    |  445     |  445       |  445    |  482    |  466    |  445    |  445    |  445    |
|  0.850    |  456    |  456     |  456       |  456    |  494    |  477    |  456    |  456    |  456    |
|  0.875    |  466    |  466     |  466       |  466    |  505    |  487    |  466    |  466    |  466    |
|  0.900    |  472    |  472     |  472       |  472    |  512    |  494    |  472    |  472    |  472    |
|  0.925    |  477    |  477     |  477       |  477    |  517    |  499    |  477    |  477    |  477    |
| **0.950** | **480** | **480**  | **480**    | **480** | **520** | **502** | **480** | **480** | **480** |
|  0.975    |  478    |  478     |  478       |  478    |  518    |  500    |  478    |  478    |  478    |
|  1.000    |  475    |  475     |  475       |  475    |  514    |  497    |  475    |  475    |  475    |
|  1.025    |  410    |  410     |  410       |  410    |  444    |  429    |  410    |  410    |  410    |

## Power above Threshhold
| N/Nmax    | A424    | M-HYBRID | V-SERIES.R | 499P    | TIPO6C  | SC63    | 9X8EVO  | 963     | GR010   |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|
|  0.550    |  236    |  236     |  236       |  236    |  256    |  247    |  236    |  236    |  236    |
|  0.575    |  258    |  258     |  258       |  258    |  279    |  270    |  258    |  258    |  258    |
|  0.600    |  277    |  277     |  277       |  277    |  300    |  290    |  277    |  277    |  277    |
|  0.625    |  297    |  297     |  297       |  297    |  322    |  310    |  297    |  297    |  297    |
|  0.650    |  317    |  317     |  317       |  317    |  343    |  331    |  317    |  317    |  317    |
|  0.675    |  337    |  337     |  337       |  337    |  365    |  352    |  337    |  337    |  337    |
|  0.700    |  358    |  358     |  358       |  358    |  387    |  374    |  358    |  358    |  358    |
|  0.725    |  378    |  378     |  378       |  378    |  409    |  395    |  378    |  378    |  378    |
|  0.750    |  397    |  397     |  397       |  397    |  430    |  415    |  397    |  397    |  397    |
|  0.775    |  415    |  415     |  415       |  415    |  449    |  434    |  415    |  415    |  415    |
|  0.800    |  431    |  431     |  431       |  431    |  467    |  451    |  431    |  431    |  431    |
|  0.825    |  445    |  445     |  445       |  445    |  482    |  466    |  445    |  445    |  445    |
|  0.850    |  456    |  456     |  456       |  456    |  494    |  477    |  456    |  456    |  456    |
|  0.875    |  466    |  466     |  466       |  466    |  505    |  487    |  466    |  466    |  466    |
|  0.900    |  472    |  472     |  472       |  472    |  512    |  494    |  472    |  472    |  472    |
|  0.925    |  477    |  477     |  477       |  477    |  517    |  499    |  477    |  477    |  477    |
| **0.950** | **480** | **480**  | **480**    | **480** | **520** | **502** | **480** | **480** | **480** |
|  0.975    |  478    |  478     |  478       |  478    |  518    |  500    |  478    |  478    |  478    |
|  1.000    |  475    |  475     |  475       |  475    |  514    |  497    |  475    |  475    |  475    |
|  1.025    |  410    |  410     |  410       |  410    |  444    |  429    |  410    |  410    |  410    |
