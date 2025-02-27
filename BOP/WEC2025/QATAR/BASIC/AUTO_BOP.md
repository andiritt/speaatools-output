| Manufacturer | Car        | Weight | Power   | PINC    | E/Stint | FDS     |
|:-|:-|:-|:-|:-|:-|:-|
| Alpine       | A424       | 1037kg | 519.0kw |    -    | 919MJ   |    -    |
| Aston Martin | Valkyrie   | 1030kg | 520.0kw |    -    | 911MJ   |    -    |
| BMW          | M-Hybrid   | 1039kg | 520.0kw |    -    | 914MJ   |    -    |
| Cadillac     | V-Series.R | 1045kg | 518.0kw |    -    | 906MJ   |    -    |
| Ferrari      | 499P       | 1066kg | 514.0kw |    -    | 912MJ   | 190kph  |
| Peugeot      | 9X8Evo     | 1030kg | 509.0kw |    -    | 911MJ   | 190kph  |
| Porsche      | 963        | 1040kg | 514.0kw |    -    | 909MJ   |    -    |
| Toyota       | GR010      | 1068kg | 513.0kw |    -    | 911MJ   | 190kph  |

![PACECHART](./IMG/AUTO.png)
![STRAIGHTLINEPERFORMANCECHART](./IMG/AUTO_sp.png)
![TYREPERFORMANCECHART](./IMG/AUTO_tw.png)

### BoP Accuracy: 72.33%; Overall BoP Grade: C2
| Manufacturer | Car        | Type  | RP      | QP      | Weight | Power¹  | Threshhold | PINC    | Power²   | E/Stint | AVG Vmax  | FDS     | RDLC | L/Stint | BOP-Grade | Model Accuracy | Model Points | Match% | SimDiff |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|
| Alpine       | A424       | LMDH  | 1:41.55 | 1:39.15 | 1037kg | 519.0kw | 0.0kph     |    -    | 519.00kw |  919MJ  | 302.19kph |    -    | 1.01 | 33      | -B1       | 99.49%         | 1360         | 85.77% | -0.64   |
| Aston Martin | Valkyrie   | LMHNH | 1:44.28 | 1:41.04 | 1030kg | 520.0kw | 0.0kph     |    -    | 520.00kw |  911MJ  | 293.43kph |    -    | 1.04 | 33      | +Ω2       | 100.00%        | 312          | -7.08% | -0.87   |
| BMW          | M-Hybrid   | LMDH  | 1:41.54 | 1:38.28 | 1039kg | 520.0kw | 0.0kph     |    -    | 520.00kw |  914MJ  | 300.92kph |    -    | 1.01 | 33      | -B1       | 98.62%         | 2363         | 85.72% | -0.32   |
| Cadillac     | V-Series.R | LMDH  | 1:41.54 | 1:38.62 | 1045kg | 518.0kw | 0.0kph     |    -    | 518.00kw |  906MJ  | 295.37kph |    -    | 1.01 | 33      | -B1       | 98.50%         | 4201         | 85.51% | +0.14   |
| Ferrari      | 499P       | LMHHU | 1:41.54 | 1:38.48 | 1066kg | 514.0kw | 0.0kph     |    -    | 514.00kw |  912MJ  | 298.87kph | 190kph  | 1.02 | 33      | -B2       | 100.00%        | 4441         | 82.33% | +0.15   |
| Peugeot      | 9X8Evo     | LMHHU | 1:41.53 | 1:38.84 | 1030kg | 509.0kw | 0.0kph     |    -    | 509.00kw |  911MJ  | 301.19kph | 190kph  | 1.02 | 33      | -C1       | 100.00%        | 808          | 78.40% | +0.75   |
| Porsche      | 963        | LMDH  | 1:41.55 | 1:38.26 | 1040kg | 514.0kw | 0.0kph     |    -    | 514.00kw |  909MJ  | 298.48kph |    -    | 1.01 | 33      | -B2       | 99.87%         | 12613        | 83.84% | -0.04   |
| Toyota       | GR010      | LMHHU | 1:41.53 | 1:38.29 | 1068kg | 513.0kw | 0.0kph     |    -    | 513.00kw |  911MJ  | 295.99kph | 190kph  | 1.02 | 33      | -B2       | 99.73%         | 2956         | 84.16% | +0.85   |

## Power below Threshhold
| N/Nmax    | A424    | VALKYRIE | M-HYBRID | V-SERIES.R | 499P    | 9X8EVO  | 963     | GR010   |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|
|  0.550    |  256    |  256     |  256     |  255       |  253    |  251    |  253    |  253    |
|  0.575    |  279    |  279     |  279     |  278       |  276    |  274    |  276    |  276    |
|  0.600    |  299    |  300     |  300     |  299       |  297    |  294    |  297    |  296    |
|  0.625    |  321    |  322     |  322     |  321       |  318    |  315    |  318    |  317    |
|  0.650    |  342    |  343     |  343     |  342       |  339    |  336    |  339    |  338    |
|  0.675    |  364    |  365     |  365     |  364       |  361    |  357    |  361    |  360    |
|  0.700    |  386    |  387     |  387     |  386       |  383    |  379    |  383    |  382    |
|  0.725    |  408    |  409     |  409     |  407       |  404    |  400    |  404    |  403    |
|  0.750    |  429    |  430     |  430     |  428       |  425    |  421    |  425    |  424    |
|  0.775    |  448    |  449     |  449     |  447       |  444    |  440    |  444    |  443    |
|  0.800    |  466    |  467     |  467     |  465       |  462    |  457    |  462    |  461    |
|  0.825    |  481    |  482     |  482     |  480       |  477    |  472    |  477    |  476    |
|  0.850    |  493    |  494     |  494     |  492       |  488    |  484    |  488    |  487    |
|  0.875    |  504    |  505     |  505     |  503       |  499    |  494    |  499    |  498    |
|  0.900    |  511    |  512     |  512     |  510       |  506    |  501    |  506    |  505    |
|  0.925    |  516    |  517     |  517     |  515       |  511    |  506    |  511    |  510    |
| **0.950** | **519** | **520**  | **520**  | **518**    | **514** | **509** | **514** | **513** |
|  0.975    |  517    |  518     |  518     |  516       |  512    |  507    |  512    |  511    |
|  1.000    |  513    |  514     |  514     |  512       |  508    |  504    |  508    |  507    |
|  1.025    |  443    |  444     |  444     |  442       |  439    |  435    |  439    |  438    |

## Power above Threshhold
| N/Nmax    | A424    | VALKYRIE | M-HYBRID | V-SERIES.R | 499P    | 9X8EVO  | 963     | GR010   |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|
|  0.550    |  256    |  256     |  256     |  255       |  253    |  251    |  253    |  253    |
|  0.575    |  279    |  279     |  279     |  278       |  276    |  274    |  276    |  276    |
|  0.600    |  299    |  300     |  300     |  299       |  297    |  294    |  297    |  296    |
|  0.625    |  321    |  322     |  322     |  321       |  318    |  315    |  318    |  317    |
|  0.650    |  342    |  343     |  343     |  342       |  339    |  336    |  339    |  338    |
|  0.675    |  364    |  365     |  365     |  364       |  361    |  357    |  361    |  360    |
|  0.700    |  386    |  387     |  387     |  386       |  383    |  379    |  383    |  382    |
|  0.725    |  408    |  409     |  409     |  407       |  404    |  400    |  404    |  403    |
|  0.750    |  429    |  430     |  430     |  428       |  425    |  421    |  425    |  424    |
|  0.775    |  448    |  449     |  449     |  447       |  444    |  440    |  444    |  443    |
|  0.800    |  466    |  467     |  467     |  465       |  462    |  457    |  462    |  461    |
|  0.825    |  481    |  482     |  482     |  480       |  477    |  472    |  477    |  476    |
|  0.850    |  493    |  494     |  494     |  492       |  488    |  484    |  488    |  487    |
|  0.875    |  504    |  505     |  505     |  503       |  499    |  494    |  499    |  498    |
|  0.900    |  511    |  512     |  512     |  510       |  506    |  501    |  506    |  505    |
|  0.925    |  516    |  517     |  517     |  515       |  511    |  506    |  511    |  510    |
| **0.950** | **519** | **520**  | **520**  | **518**    | **514** | **509** | **514** | **513** |
|  0.975    |  517    |  518     |  518     |  516       |  512    |  507    |  512    |  511    |
|  1.000    |  513    |  514     |  514     |  512       |  508    |  504    |  508    |  507    |
|  1.025    |  443    |  444     |  444     |  442       |  439    |  435    |  439    |  438    |
