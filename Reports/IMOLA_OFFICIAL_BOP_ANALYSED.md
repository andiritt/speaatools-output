# Official Imola BoP Analysed

Hey guys, here is a quick analysis on the official Imola BoP

Notes:
- Software was further updated with the help of some guys with more experience, as ballast seemed to have a too small influence and power too much of an influence. That was an error i created with the last big performance simulation overhaul last year between Le Mans and Monza
- Track Characteristics are now Semi-Automatically determined to be able to predict performances at specific tracks more accurately. BUT this also means tracks without previous knowledge as Imola will not be accurate until after I have some race data from there
- As a result of the that the performance-model simulation creates more accurate simulation models
- The Energy per stint and laps per stint calculations are currently broken, needs to be adapted to the previous two changes and I'm working on it, was just not fast enough to fix that before Imola
- I did not have time or new data to accurately test these changes to the software yet, so as always don't take this post too seriously as this is just a hobby of mine and these values could be very wrong.

- Also Peugeot not included currently due to lack of data for the rear wing version

### BoP Accuracy: 73.04%; Overall BoP Grade: C2
| Manufacturer     | Car        | Type  | RP      | QP      | Weight | Power¹ | Threshhold | PINC    | Power² | E/Stint | AVG Vmax  | FDS     | RDLC | L/Stint | BOP-Grade | Model Accuracy | Model Points | Match%  |
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|
| Alpine           | A424       | LMDH  | 1:35.57 | 1:32.71 | 1042kg | 514kw  | 0.0kph     |    -    | 514kw  |  910MJ  | 293.89kph |    -    | 1.02 | 37      | +C2       | 100.00%        | 642          | 72.12%  |
| BMW              | M-Hybrid   | LMDH  | 1:35.29 | 1:31.63 | 1035kg | 511kw  | 0.0kph     |    -    | 511kw  |  903MJ  | 290.09kph |    -    | 1.03 | 37      | -A2       | 100.00%        | 1714         | 91.61%  |
| Cadillac         | V-Series.R | LMDH  | 1:34.82 | 1:30.93 | 1030kg | 517kw  | 0.0kph     |    -    | 517kw  |  904MJ  | 295.77kph |    -    | 1.03 | 37      | -D1       | 98.95%         | 2271         | 69.85%  |
| Ferrari          | 499P       | LMHHU | 1:34.93 | 1:31.00 | 1041kg | 510kw  | 0.0kph     |    -    | 510kw  |  898MJ  | 296.45kph | 190kph  | 1.05 | 37      | -C2       | 99.93%         | 2718         | 72.98%  |
| Isotta Fraschini | Tipo6C     | LMHHU | 1:36.82 | 1:34.36 | 1058kg | 520kw  | 0.0kph     |    -    | 520kw  |  919MJ  | 293.41kph | 190kph  | 1.04 | 37      | +Ω2       | 92.36%         | 133          | -0.02%  |
| Lamborghini      | SC63       | LMDH  | 1:35.45 | 1:33.88 | 1034kg | 516kw  | 0.0kph     |    -    | 516kw  |  907MJ  | 292.82kph |    -    | 1.06 | 37      | ~A1       | 96.54%         | 418          | 100.00% |
| Porsche          | 963        | LMDH  | 1:35.48 | 1:31.50 | 1033kg | 508kw  | 0.0kph     |    -    | 508kw  |  893MJ  | 294.04kph |    -    | 1.03 | 37      | ~A1       | 99.98%         | 6168         | 100.00% |
| Toyota           | GR010      | LMHHU | 1:34.96 | 1:31.04 | 1060kg | 516kw  | 0.0kph     |    -    | 516kw  |  906MJ  | 295.62kph | 190kph  | 1.03 | 37      | -C1       | 98.53%         | 3557         | 77.78%  |

Cadillac Ferrari and Toyota seem to be very close together and have the fastest 3 cars.

After that there are BMW, Porsche, Lambo and Alpine who also seem to be pretty close.

Isotta doesn't seem to be too far back, but they certainly are the biggest question mark.

Peugeot BoP certainly seems to be not too bad, but the would need to have the fastest hypercar of all to compensate for that BoP. But doesn't seem unrealistic as they already had alot of data when they developed the rear wing.





I wanted to mention that as a first step of open sourcing the software I have made a git repository with all of the data output of the software. Any help in finding issues with output data or issues with anything else would be greatly appreciated. 

Also there is a link to a discord server for the develop,ent of this software as well as some details on the developement roadmap, explaination of what the software does etc...

Also more detail on the output BoPs can be found there. Here an example for 
Imolas official BoP:

[IMOLA GITHUB](https://github.com/andiritt/speaatools-output/blob/master/BOP/WEC2024/IMOLA/PREDEFINED/OFFICIAL_BOP.md)
If you are interested feel free to check it out.



Have a nice day;)