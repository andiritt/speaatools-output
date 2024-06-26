## BoP (Balance of Performance) Data

This folder houses all the data generated by the SPEAA-Tools software related to Balance of Performance (BoP) for various WEC races.

**Organized BoP Data:**

This section meticulously organizes the Balance of Performance (BoP) data generated by SPEAA-Tools. The structure facilitates easy navigation and understanding of the BoP variations explored for different car and track combinations.

**Top-Level Folder:**

- **Description:** This folder provides a concise overview of the car and track sets used in the simulations.

**Subfolder Breakdown (by Track):**

For each track, a dedicated subfolder is created to house the various BoP configurations explored.

**Third-Level Subfolders (BoP Variations):**

Within each track's subfolder, three subfolders categorize the different BoP approaches:

- **Basic (Auto Generated BoPs):** This subfolder contains automatically generated BoPs that aim to achieve maximum equivalence across all performance areas. It includes two files:
    
    - **AUTO_BOP.md:** This file details the BoP algorithm used for automatic generation, focusing on achieving balanced performance.
    - **ACOMETHOD.md:** This file explores a BoP method that mimics the official approach, using custom BoP values as a reference point and more subtle changes based on previous BoPs.
    
- **Dualstage (Two-Stage Auto Generated BoPs):** This subfolder delves into BoPs generated automatically with a potential performance change after a specific speed threshold. Similar to the Basic subfolder, it includes:
    
    - **AUTO_BOP.md:** Similar to the Basic AUTO_BOP.md, used for automatic generation, considering a potential performance shift at a certain speed.
    - **ACOMETHOD.md:** Similar to the Basic ACOMETHOD.md, this file explores a BoP method mimicking the official approach with a potential performance change at a speed threshold .
    
- **Predefined BoP Values:** This subfolder houses pre-defined BoP configurations that were not generated through simulation:
    
    - **CUSTOM_BOP.md:** This file documents custom BoP values defined within the software, allowing for user-specified configurations.
    - **OFFICIAL_BOP.md:** This file presents the official FIA/ACO BoP for the specific track, but only includes cars that received a BoP in the current data set.

**File Descriptions:**

- **AUTO_BOP.md and ACOMETHOD.md:** These files explain the respective BoP algorithms used for automatic generation and the method mimicking the official approach.
- **CUSTOM_BOP.md:** This file documents custom BoP values defined directly within the software.
- **OFFICIAL_BOP.md:** This file displays the official FIA/ACO BoP for the specific track, focusing on cars with assigned BoP values in the current data set.

**Key Features:**

- **Markdown Files:** These files serve as the primary source of information, presenting the data in a clear and readable format.
- **Visualizations:** Relevant images are embedded within the markdown files for better understanding of the data.
- **Separate Image Folders:** For users who prefer a more image-centric approach, separate folders containing only the data visualizations are also provided.

**Data Breakdown:**

The SPEAA-Tools software utilizes a grading system and performance windows to evaluate the effectiveness of BoP for each car in a specific race. You'll find the following data points within the markdown files:

- **Car Information:** Manufacturer, Car Model, and Car Type
- **BoP Values:** Details on the official/custom/auto generated BoP applied for the simulation.
- **Grading System:** A letter grade (A1-Ω2) reflecting how well the BoP achieved its intended performance balance. This considers both the accuracy of the performance window and the software's confidence in its simulation model.
- **Simulated Performance Model:** Details about the model used to simulate car performance, including:
    - **Model Points:** The number of data points used for the simulation.
    - **Model Accuracy:** The percentage of times the simulation matches actual car data.
    - **Match%:** How well the simulated performance window aligns with the intended window. This value can be positive (slower than intended), negative (faster than intended), or neutral (approximately matches).
- **Overall BoP Grade:** A single grade calculated as the average of all Match% values, providing a general assessment of the BoP's effectiveness for the entire race.

**Additional Information:**

- The data presented is for informational purposes only and should not be taken as official.
- We encourage users to be critical and consider the limitations of the software.
- Feedback on the data and suggestions for improvement are highly welcome.

**Accessing Reports:**

For race analysis and previews that utilize the BoP data, please visit the Reports folder in this repository. [[Link to Reports folder](https://github.com/andiritt/speaatools-output/tree/master/Reports)]