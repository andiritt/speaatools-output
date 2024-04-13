# Sportscar  Equalization and Analysis Tools (SPE&A-Tools)

**For Transparency:**

- This analysis and the performance data are the result of a personal project I'm undertaking as a WEC enthusiast and software developer.
- Please consider this information for informational purposes only. Treat it with a critical eye and don't mistake it for official data.

**Feedback Welcome:**

- I'm constantly striving to improve the accuracy of this data.
- If you discover any errors, inconsistencies, or mismatches with official World Endurance Championship data, please don't hesitate to let me know. I appreciate your feedback!

## Table of Contents

- [Sportscar  Equalization and Analysis Tools (SPE\&A-Tools)](#sportscar--equalization-and-analysis-tools-spea-tools)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Current Usage](#current-usage)
  - [SPE\&A-Tools Development Roadmap](#spea-tools-development-roadmap)
  - [Folders](#folders)
  - [Value Explanations](#value-explanations)
  - [Plot Explanations](#plot-explanations)
  - [End Section](#end-section)


## Introduction
**Welcome to the SPE&A-Tools Data Repo!**

This repository is the first step towards fully open-sourcing the SPE&A-Tools project over the next two years. It provides fans of the World Endurance Championship with a continually expanding resource for analyzing and understanding official race data.

**Empowering WEC Fans:**

SPE&A-Tools aims to equip you with the tools you need to form informed opinions about factors influencing race outcomes. This includes the impact of Balance of Performance (BoP) and other variables.

**Transparency and Collaboration:**

By progressively releasing data and eventually the entire codebase, we hope to foster transparency and collaboration within the WEC enthusiast community.
## Current Usage

This software is used for BoP and race analysis posts on the following two forums:
 - [r/WEC](https://www.reddit.com/r/WEC/)
 - [discuit.net/WEC](https://discuit.net/WEC)

**Streamlining Communication Channels:**

While previous forums served as a platform for both development updates and data discussions, we're transitioning to a more focused approach.

- **This repository** will now be your one-stop shop for all information related to the accuracy of output data and Balance of Performance (BoP) topics.
- Upon software release, a **separate code repository** will take center stage for discussions and collaboration on the software itself.
- In **The Forums** we will now focus on high quality analysis posts relevant to those.
- **More Frequent Low Effort Analysis Reports** will be posted in the reports folder of this repository.

Also there is a discord server for contacting us directly:
[Discord](https://discord.gg/CCFctTKWnE)

**Benefits:**

This streamlined approach offers several advantages:

- **Clearer Focus:** Users can easily find the information they're looking for, whether it's about data accuracy or software development.
- **Enhanced Collaboration:** The dedicated code repository will foster a more technical environment for developers and enthusiasts.
- **Improved Efficiency:** Our communication efforts will be more targeted and productive.

**Stay Informed:**

We'll continue to provide regular updates on all platforms to keep you informed about SPE&A-Tools' progress. 
## SPE&A-Tools Development Roadmap

This roadmap outlines the key milestones for the SPE&A-Tools project:

**Ongoing Focus:**

- **Enhanced Accuracy:** We're continuously working to improve the accuracy of our pace simulation models and the BoPs (Balance of Performance) they generate. This ensures the tools provide the most reliable insights for analyzing WEC data.
- **(Optional)Additional Car Classes:** Reintroduction of lmp2s and addition of gt cars. 

**Open-Source Progress:**

- **Non-Official Data Code (Target: December 2024):** We're committed to open-sourcing all code related to non-official data by the end of 2024. This fosters transparency and encourages community collaboration.

**Full Open-Source Target:**

- **Gradual Release (January 2024 - December 2025):** We plan to progressively open-source the entire SPE&A-Tools software throughout 2024 and 2025. This process will involve careful legal considerations to ensure compliance.

## Folders
**BoP (Balance of Performance):**

This folder houses all data outputs generated by the SPE&A-Tools software. The primary source of information is in the markdown files, which conveniently incorporate relevant images for visual reference. 

**Reports:**

This section is your one-stop shop for race analysis! Dive into insightful race previews, post-race breakdowns, and even additional analyses focusing on specific race sessions.

## Value Explanations

| Field          | Description                                                | Units |
| -------------- | ---------------------------------------------------------- | ----- |
| Manufacturer   | Make of the Car                                            | -     |
| Car            | Car Model                                                  | -     |
| Type           | Car Type                                                   | -     |
| - LMHHU        | LMH Front Axle Hybrid, Tyre Spec 1                         |       |
| - LMHHE        | LMH Front Axle Hybrid, Tyre Spec 2                         |       |
| - LMDH         | LMDh Rear Axle Hybrid, Tyre Spec 1                         |       |
| - (See Note 3) | Currently unused and deprecated car types                  |       |
| RP             | Race Pace, Filtered Average Theoretical Optimum            | -     |
| QP             | Qualifying Pace, Theoretical Optimum                       | -     |
| Weight         | Car Minimum Weight                                         | kg    |
| Power          | Peak Power Output (Appendix 4b, LMH Tech. Regs;            | kW    |
|                | Article 5.1.2, LMDh Tech. Regs)                            |       |
| Power¹         | Power below BoP-speed-threshhold                           | kW    |
| Threshhold     | BoP-speed-threshhold                                       | km/h  |
| PINC           | Power increase above threshhold (%, negative for decrease) | %     |
| Power²         | Power above BoP-speed-threshhold                           | kW    |
| E/Stint        | Maximum Energy Output per Stint                            | kJ    |
| AVG Vmax       | Topspeed, Filtered Average                                 | km/h  |
| FDS            | Front Axle Hybrid Deployment Speed                         | km/h  |
| RDLC           | Relative Downforce Level Coefficient                       | -     |
|                | - Higher value: More Downforce per KG                      |       |
|                | - Lower value: Less Downforce per KG                       |       |
|                | - Value < 0.95: Too Low/Inefficient Downforce Setup        |       |
|                | - Value > 1.05: Too High/Inefficient Downforce Setup       |       |

**Additional Information:**

- **Grading System:** A1 > A2 > B1 > B2 > C1 > C2 > D1 > D2 > E1 > E2 > Ω1 > Ω2
    - Considers performance window accuracy and simulation model confidence
	- '-' -> Cars Performance window faster than intended
	- '+' -> Cars Performance window slower than intended
	- '~' -> Cars Performance window approximately matches the intended

**Simulated Performance:**

- **Model Points:** Number of unique data points used for simulation.
- **Model Accuracy:** Percentage of simulation matches with actual data.
- **Match%:** How well the simulated performance window matches the intended window.
  
**Notes:**

* <sup>1</sup> Tyre Specification 1:
    - Mandatory for all 2WD cars
    - Possible for 4WD cars homologated before 2023
    - Mandatory for 4WD cars homologated after 2022
    - Tyre Dimensions:
        - Front: 29/71-18; 13.5
        - Rear: 34/71-18; 15.0
* <sup>2</sup> Tyre Specification 2:
    - Possible for 4WD cars homologated before 2023
    - Tyre Dimensions:
        - Front: 31/71-18; 14.0
        - Rear: 31/71-18; 14.0
* <sup>3</sup> Unused Types:
    - LMHNH (LMH Non Hybrid, Tyre Spec 1)
    - LMHRRH (LMH 'Modified Roadgoing Hypercar' Rear Axle Hybrid, Tyre Spec 1)
    - LMHRFH (LMH 'Modified Roadgoing Hypercar' Front Axle Hybrid, Tyre Spec 1)
* <sup>3</sup> Deprecated Types:
    - LMP1 (Grandfathered Le Mans Prototype 1 2022)


## Plot Explanations

**Pace Probability Plot:**

- **Visualizing Lap Time Distribution:** This plot showcases the likelihood of a car achieving specific lap times throughout a race. While it doesn't directly utilize the underlying calculation values, it employs a slightly larger range for improved visualization.

**Straight Line Performance Plot:**

- **Unveiling Acceleration Differences:** This plot compares the expected straight-line performance between cars. Factors like mechanical grip and aerodynamics are relatively constant, but straight-line performance varies due to engine modes, hybrid systems, and engine types. As a result, this plot offers valuable insights into these differences. Additionally, if desired, we could incorporate mechanical grip and braking performance data into the main table alongside the Relative Downforce Level Coefficient.

**Normalized Tire Performance Plot (Work in Progress):**

- **Exploring Tire Performance Degradation Trends:** This plot provides an approximate representation of how tire performance decays over an average lifespan for a specific BoP configuration. Currently, due to limited compound-specific data, the plot reflects an average degradation across all compounds for the car. We consider this an experimental feature and welcome any feedback or suggestions for improvement. It's important to note that while the visualization sets the minimum performance at 0% for clarity, actual performance at this point may be closer to 90%. We can adjust the scale if that better reflects reality for your needs.
	
	Important Note: 
	-  **Understanding Performance Decline, Not Tire Degradation:** This plot focuses on the overall performance decline a car experiences as its tires wear, not the specific degradation of the tires themselves.
	-  **Normalized Scale:** We use a normalized scale from 0 (representing the largest decline in performance across all cars) to 100 (representing the starting performance level).

## End Section

**Transparency and Collaboration:**

We believe in open communication and collaboration. This repository serves as the central hub for all discussions related to data accuracy and BoP topics. As the software development progresses, a separate code repository will be launched to foster deeper technical discussions.

**Feedback Welcome:**

We're constantly striving to improve the accuracy and functionality of SPE&A-Tools. If you discover any mistakes, inconsistencies, or mismatches with official WEC data, please don't hesitate to let us know. Your feedback is highly appreciated!

**Disclaimer:**

This analysis and the performance data are the result of a personal project undertaken by a WEC enthusiast and software developer. Please consider this information for informational purposes only. Treat it with a critical eye and don't mistake it for official data.

**We hope you find SPE&A-Tools a valuable resource for understanding and analyzing WEC data!**
