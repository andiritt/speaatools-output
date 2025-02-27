| Manufacturer     | Car        | Weight | Power   | PINC    | E/Stint | FDS     |
|:-|:-|:-|:-|:-|:-|:-|
| Alpine           | A424       | 1038kg | 480.0kw |    -    | 880MJ   |    -    |
| BMW              | M-Hybrid   | 1040kg | 481.0kw |    -    | 880MJ   |    -    |
| Cadillac         | V-Series.R | 1050kg | 481.0kw |    -    | 877MJ   |    -    |
| Ferrari          | 499P       | 1070kg | 480.0kw |    -    | 880MJ   | 190kph  |
| Isotta Fraschini | Tipo6C     | 1087kg | 520.0kw |    -    | 920MJ   | 190kph  |
| Lamborghini      | SC63       | 1068kg | 502.0kw |    -    | 896MJ   |    -    |
| Peugeot          | 9X8Evo     | 1048kg | 480.0kw |    -    | 880MJ   | 190kph  |
| Porsche          | 963        | 1051kg | 480.0kw |    -    | 879MJ   |    -    |
| Toyota           | GR010      | 1075kg | 480.0kw |    -    | 880MJ   | 190kph  |

![PACECHART](./IMG/AUTO.png)
![STRAIGHTLINEPERFORMANCECHART](./IMG/AUTO_sp.png)
![TYREPERFORMANCECHART](./IMG/AUTO_tw.png)

### BoP Accuracy: 94.83%; Overall BoP Grade: A2
| Manufacturer     | Car        | Type  | RP      | QP      | Weight | Power¹  | Threshhold | PINC    | Power²   | E/Stint | AVG Vmax  | FDS     | RDLC | L/Stint | BOP-Grade | Model Accuracy | Model Points | Match%  | SimDiff |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|
| Alpine           | A424       | LMDH  | 1:52.46 | 1:48.91 | 1038kg | 480.0kw | 0.0kph     |    -    | 480.00kw |  880MJ  | 286.62kph |    -    | 1.01 | 33      | ~A1       | 99.49%         | 1360         | 100.00% | +0.47   |
| BMW              | M-Hybrid   | LMDH  | 1:52.45 | 1:47.92 | 1040kg | 481.0kw | 0.0kph     |    -    | 481.00kw |  880MJ  | 285.44kph |    -    | 1.01 | 33      | ~A1       | 98.62%         | 2363         | 100.00% | +0.81   |
| Cadillac         | V-Series.R | LMDH  | 1:52.45 | 1:48.32 | 1050kg | 481.0kw | 0.0kph     |    -    | 481.00kw |  877MJ  | 280.17kph |    -    | 1.01 | 33      | ~A1       | 98.50%         | 4201         | 95.14%  | +1.39   |
| Ferrari          | 499P       | LMHHU | 1:52.45 | 1:48.15 | 1070kg | 480.0kw | 0.0kph     |    -    | 480.00kw |  880MJ  | 284.19kph | 190kph  | 1.02 | 33      | ~A1       | 100.00%        | 4441         | 98.47%  | +0.67   |
| Isotta Fraschini | Tipo6C     | LMHHU | 1:52.45 | 1:49.93 | 1087kg | 520.0kw | 0.0kph     |    -    | 520.00kw |  920MJ  | 285.39kph | 190kph  | 1.01 | 33      | +C1       | 98.48%         | 130          | 79.76%  | #       |
| Lamborghini      | SC63       | LMDH  | 1:52.46 | 1:49.00 | 1068kg | 502.0kw | 0.0kph     |    -    | 502.00kw |  896MJ  | 282.74kph |    -    | 1.02 | 33      | ~A1       | 100.00%        | 784          | 97.61%  | #       |
| Peugeot          | 9X8Evo     | LMHHU | 1:52.47 | 1:48.57 | 1048kg | 480.0kw | 0.0kph     |    -    | 480.00kw |  880MJ  | 286.00kph | 190kph  | 1.00 | 33      | +B2       | 100.00%        | 808          | 84.76%  | +1.47   |
| Porsche          | 963        | LMDH  | 1:52.47 | 1:47.91 | 1051kg | 480.0kw | 0.0kph     |    -    | 480.00kw |  879MJ  | 283.12kph |    -    | 1.01 | 33      | ~A1       | 99.87%         | 12613        | 100.00% | +0.88   |
| Toyota           | GR010      | LMHHU | 1:52.46 | 1:47.96 | 1075kg | 480.0kw | 0.0kph     |    -    | 480.00kw |  880MJ  | 281.37kph | 190kph  | 1.01 | 33      | ~A1       | 99.73%         | 2956         | 97.73%  | +0.74   |

## Power below Threshhold
| N/Nmax    | A424    | M-HYBRID | V-SERIES.R | 499P    | TIPO6C  | SC63    | 9X8EVO  | 963     | GR010   |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|
|  0.550    |  236    |  237     |  237       |  236    |  256    |  247    |  236    |  236    |  236    |
|  0.575    |  258    |  259     |  259       |  258    |  279    |  270    |  258    |  258    |  258    |
|  0.600    |  277    |  278     |  278       |  277    |  300    |  290    |  277    |  277    |  277    |
|  0.625    |  297    |  298     |  298       |  297    |  322    |  310    |  297    |  297    |  297    |
|  0.650    |  317    |  318     |  318       |  317    |  343    |  331    |  317    |  317    |  317    |
|  0.675    |  337    |  338     |  338       |  337    |  365    |  352    |  337    |  337    |  337    |
|  0.700    |  358    |  359     |  359       |  358    |  387    |  374    |  358    |  358    |  358    |
|  0.725    |  378    |  379     |  379       |  378    |  409    |  395    |  378    |  378    |  378    |
|  0.750    |  397    |  398     |  398       |  397    |  430    |  415    |  397    |  397    |  397    |
|  0.775    |  415    |  416     |  416       |  415    |  449    |  434    |  415    |  415    |  415    |
|  0.800    |  431    |  432     |  432       |  431    |  467    |  451    |  431    |  431    |  431    |
|  0.825    |  445    |  446     |  446       |  445    |  482    |  466    |  445    |  445    |  445    |
|  0.850    |  456    |  457     |  457       |  456    |  494    |  477    |  456    |  456    |  456    |
|  0.875    |  466    |  467     |  467       |  466    |  505    |  487    |  466    |  466    |  466    |
|  0.900    |  472    |  473     |  473       |  472    |  512    |  494    |  472    |  472    |  472    |
|  0.925    |  477    |  478     |  478       |  477    |  517    |  499    |  477    |  477    |  477    |
| **0.950** | **480** | **481**  | **481**    | **480** | **520** | **502** | **480** | **480** | **480** |
|  0.975    |  478    |  479     |  479       |  478    |  518    |  500    |  478    |  478    |  478    |
|  1.000    |  475    |  476     |  476       |  475    |  514    |  497    |  475    |  475    |  475    |
|  1.025    |  410    |  411     |  411       |  410    |  444    |  429    |  410    |  410    |  410    |

## Power above Threshhold
| N/Nmax    | A424    | M-HYBRID | V-SERIES.R | 499P    | TIPO6C  | SC63    | 9X8EVO  | 963     | GR010   |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|
|  0.550    |  236    |  237     |  237       |  236    |  256    |  247    |  236    |  236    |  236    |
|  0.575    |  258    |  259     |  259       |  258    |  279    |  270    |  258    |  258    |  258    |
|  0.600    |  277    |  278     |  278       |  277    |  300    |  290    |  277    |  277    |  277    |
|  0.625    |  297    |  298     |  298       |  297    |  322    |  310    |  297    |  297    |  297    |
|  0.650    |  317    |  318     |  318       |  317    |  343    |  331    |  317    |  317    |  317    |
|  0.675    |  337    |  338     |  338       |  337    |  365    |  352    |  337    |  337    |  337    |
|  0.700    |  358    |  359     |  359       |  358    |  387    |  374    |  358    |  358    |  358    |
|  0.725    |  378    |  379     |  379       |  378    |  409    |  395    |  378    |  378    |  378    |
|  0.750    |  397    |  398     |  398       |  397    |  430    |  415    |  397    |  397    |  397    |
|  0.775    |  415    |  416     |  416       |  415    |  449    |  434    |  415    |  415    |  415    |
|  0.800    |  431    |  432     |  432       |  431    |  467    |  451    |  431    |  431    |  431    |
|  0.825    |  445    |  446     |  446       |  445    |  482    |  466    |  445    |  445    |  445    |
|  0.850    |  456    |  457     |  457       |  456    |  494    |  477    |  456    |  456    |  456    |
|  0.875    |  466    |  467     |  467       |  466    |  505    |  487    |  466    |  466    |  466    |
|  0.900    |  472    |  473     |  473       |  472    |  512    |  494    |  472    |  472    |  472    |
|  0.925    |  477    |  478     |  478       |  477    |  517    |  499    |  477    |  477    |  477    |
| **0.950** | **480** | **481**  | **481**    | **480** | **520** | **502** | **480** | **480** | **480** |
|  0.975    |  478    |  479     |  479       |  478    |  518    |  500    |  478    |  478    |  478    |
|  1.000    |  475    |  476     |  476       |  475    |  514    |  497    |  475    |  475    |  475    |
|  1.025    |  410    |  411     |  411       |  410    |  444    |  429    |  410    |  410    |  410    |
