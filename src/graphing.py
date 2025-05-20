import os
import json
import math
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

from plotly.subplots import make_subplots

def find_json_files(folder):
    json_files = []
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith('.json'):
                json_files.append(os.path.join(root, file))
    return json_files

def calculate_overlap(car, lower, upper):
    lb = min(car['laptimes'])
    too_fast = lb < lower
    overlap_counter = 0
    for lap in car['laptimes']:
        if lower <= lap <= upper:
            overlap_counter += 1
    overlap_percent = (overlap_counter / len(car['laptimes'])) * 100

    bop_grade = calculate_bop_grade(overlap_percent)
    if too_fast and bop_grade != "A1":
        prefixed = f"-{bop_grade}"
    elif bop_grade != "A1":
        prefixed = f"+{bop_grade}"
    else:
        prefixed = f"~{bop_grade}"
    return overlap_percent, bop_grade, prefixed

def calculate_bop_grade(overlap_percent):
    if overlap_percent > 95: return "A1"
    if overlap_percent > 90: return "A2"
    if overlap_percent > 85: return "B1"
    if overlap_percent > 80: return "B2"
    if overlap_percent > 75: return "C1"
    if overlap_percent > 70: return "C2"
    if overlap_percent > 65: return "D1"
    if overlap_percent > 60: return "D2"
    if overlap_percent > 55: return "E1"
    if overlap_percent > 50: return "E2"
    if overlap_percent > 0: return "Ω1"
    return "Ω2"

def format_time(secs):
    m = int(secs // 60)
    s = secs % 60
    return f"{m}:{s:05.2f}"

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def process_json(json_path):
    with open(json_path, "r") as f:
        data = json.load(f)
    # Table 1
    bop_table = []
    for car in data:
        bop_table.append([
            car.get("manufacturer", "-"),
            car.get("carName", "-"),
            f"{1030 + car.get('ballast', 0)}kg",
            f"{car['powerSetting']['power']:.1f}kw",
            f"{car['powerSetting']['powerIncrease']:+.2f}%" if car['powerSetting']['powerIncrease'] != 0 else "-",
            f"{car.get('stintEnergy', '-'):.0f}MJ" if car.get('stintEnergy') else "-",
            f"{car['hybridActivationLimit']}kph" if car.get('hybridActivationLimit', 0) > 0 else "-"
        ])
    bop_df = pd.DataFrame(bop_table, columns=["Manufacturer", "Car", "Weight", "Power", "PINC", "E/Stint", "FDS"])

    # Table 2
    laptime_bounds = [(min(car['laptimes']), max(car['laptimes'])) for car in data]
    lower_avg = sum(lb for lb, _ in laptime_bounds) / len(laptime_bounds)
    upper_avg = sum(ub for _, ub in laptime_bounds) / len(laptime_bounds)
    overlap_data = []
    overlaps = []
    for idx, car in enumerate(data):
        overlap_percent, _, prefixed = calculate_overlap(car, lower_avg, upper_avg)
        overlaps.append(overlap_percent)
        overlap_data.append([
            car.get("manufacturer", "-"),
            car.get("carName", "-"),
            format_time(car.get("raceLaptime", 0)),
            format_time(car.get("qualiLaptime", 0)),
            f"{car.get('topspeed', 0):.2f}kph",
            f"{car.get('raceLaptime', 0)/car.get('qualiLaptime', 1):.2f}",
            prefixed,
            f"{overlap_percent:.2f}%"
        ])
    bop_grade_total = calculate_bop_grade(sum(overlaps) / len(overlaps))
    bop_accuracy = sum(overlaps) / len(overlaps)
    bop_df2 = pd.DataFrame(overlap_data, columns=["Manufacturer", "Car", "RP", "QP", "Vavg", "RDLC", "BOP-Grade", "Match"])

    # Violin plots
    laptimes = [car['laptimes'] for car in data]
    qualilaptimes = [car['qualilaptimes'] for car in data]
    car_names = [car['carName'] for car in data]
    colors = [f"rgb({car['colorForPlotting']['R']},{car['colorForPlotting']['G']},{car['colorForPlotting']['B']})" for car in data]

    # --- Split and save each subplot as its own HTML file ---
    base = os.path.splitext(json_path)[0]

    # 1. BoP Table (top left) as markdown table
    bop_table_md = bop_df.to_markdown(index=False)

    # 2. Performance Table (top right) as markdown table
    perf_table_md = bop_df2.to_markdown(index=False)

    # 3. Race Laptimes Violin (bottom left)
    fig_race_violin = go.Figure()
    for i, laps in enumerate(laptimes):
        fig_race_violin.add_trace(go.Violin(y=laps, name=car_names[i], line_color=colors[i], box_visible=True, points=False))
    fig_race_violin.write_html(base + "_RACE_VIOLIN.html", full_html=False, include_plotlyjs='cdn')
    race_violin_html = fig_race_violin.to_html(full_html=False, include_plotlyjs='cdn')

    # 4. Quali Laptimes Violin (bottom right)
    fig_quali_violin = go.Figure()
    for i, laps in enumerate(qualilaptimes):
        fig_quali_violin.add_trace(go.Violin(y=laps, name=car_names[i], line_color=colors[i], box_visible=True, points=False))
    fig_quali_violin.write_html(base + "_QUALI_VIOLIN.html", full_html=False, include_plotlyjs='cdn')
    quali_violin_html = fig_quali_violin.to_html(full_html=False, include_plotlyjs='cdn')

    # 5. Topspeeds Violin (DETAIL left)
    fig_topspeed_violin = go.Figure()
    for i, car in enumerate(data):
        fig_topspeed_violin.add_trace(go.Violin(y=car['topspeeds'], name=car_names[i], line_color=colors[i], box_visible=True, points=False))
    fig_topspeed_violin.write_html(base + "_TOPSPEED_VIOLIN.html", full_html=False, include_plotlyjs='cdn')
    topspeed_violin_html = fig_topspeed_violin.to_html(full_html=False, include_plotlyjs='cdn')

    # 6. Laptimes Lineplot (DETAIL right)
    fig_laptime_line = go.Figure()
    for i, car in enumerate(data):
        sorted_laps = sorted(car['laptimes'], reverse=True)
        n = len(sorted_laps)
        if n > 1:
            x_vals = np.linspace(0, 100, n)
        else:
            x_vals = [100]
        fig_laptime_line.add_trace(go.Scatter(x=x_vals, y=sorted_laps, name=car_names[i], line=dict(color=colors[i])))
    fig_laptime_line.update_layout(xaxis_title="Normalised Lap Index (max=100)")
    fig_laptime_line.write_html(base + "_LAPTIME_LINE.html", full_html=False, include_plotlyjs='cdn')
    laptime_line_html = fig_laptime_line.to_html(full_html=False, include_plotlyjs='cdn')

    # Save plot images for README.md
    image_dir = os.path.join(os.path.dirname(json_path), "images")
    ensure_dir(image_dir)
    # Save static images (png) for each plot
    race_violin_img = os.path.join(image_dir, "race_violin.png")
    quali_violin_img = os.path.join(image_dir, "quali_violin.png")
    topspeed_violin_img = os.path.join(image_dir, "topspeed_violin.png")
    laptime_line_img = os.path.join(image_dir, "laptime_line.png")
    fig_race_violin.write_image(race_violin_img)
    fig_quali_violin.write_image(quali_violin_img)
    fig_topspeed_violin.write_image(topspeed_violin_img)
    fig_laptime_line.write_image(laptime_line_img)

    # Combine all plots into a markdown file in the requested order
    md_path = os.path.join(os.path.dirname(json_path), "offline.md")
    with open(md_path, "w") as mdfile:
        mdfile.write("# Combined Plots\n\n## Metadata\n\n")
        mdfile.write(f"- BoP Accuracy: {bop_accuracy:.2f}%\n- Overall BoP Grade: {bop_grade_total}\n")
        mdfile.write(f"- Track: {data[0]['track']}\n- Threshhold: {data[0]['powerSetting']['increaseThreshhold']}kph\n\n")
        mdfile.write("## BoP Table\n" + bop_table_md + "\n\n")
        mdfile.write("## Performance Table\n" + perf_table_md + "\n\n")
        mdfile.write("## Race Laptimes\n" + race_violin_html + "\n\n")
        mdfile.write("## Quali Laptimes\n" + quali_violin_html + "\n\n")
        mdfile.write("## Topspeeds\n" + topspeed_violin_html + "\n\n")
        mdfile.write("## Laptimes Lineplot\n" + laptime_line_html + "\n\n")

    # Create README.md with images instead of HTML
    readme_path = os.path.join(os.path.dirname(json_path), "README.md")
    with open(readme_path, "w") as mdfile:
        mdfile.write("# Combined Plots\n\n## Metadata\n\n")
        mdfile.write(f"- BoP Accuracy: {bop_accuracy:.2f}%\n- Overall BoP Grade: {bop_grade_total}\n")
        mdfile.write(f"- Track: {data[0]['track']}\n- Threshhold: {data[0]['powerSetting']['increaseThreshhold']}kph\n\n")
        mdfile.write("## BoP Table\n" + bop_table_md + "\n\n")
        mdfile.write("## Performance Table\n" + perf_table_md + "\n\n")
        mdfile.write("## Race Laptimes\n![Race Laptimes](images/race_violin.png)\n\n")
        mdfile.write("## Quali Laptimes\n![Quali Laptimes](images/quali_violin.png)\n\n")
        mdfile.write("## Topspeeds\n![Topspeeds](images/topspeed_violin.png)\n\n")
        mdfile.write("## Laptimes Lineplot\n![Laptimes Lineplot](images/laptime_line.png)\n\n")

def main():
    folder = "BOP"
    ensure_dir(folder)
    json_files = find_json_files(folder)
    for json_file in json_files:
        process_json(json_file)
        print(f"Processed {json_file}")

if __name__ == "__main__":
    main()