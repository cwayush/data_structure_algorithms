import os
import matplotlib.pyplot as plt

CHARTS_DIR = "dev_tools/charts"
EXTENSIONS = {".py", ".cpp", ".java"}
IGNORE_DIRS = {".git", ".github", "dev_tools", ".venv"}

def get_category_counts():
    category_counts = {}

    for category in sorted(os.listdir('.')):
        if not os.path.isdir(category):
            continue
        if category in IGNORE_DIRS or category.startswith('.'):
            continue

        total_files = 0

        for root, dirs, files in os.walk(category):
            dirs[:] = [d for d in dirs if d not in IGNORE_DIRS and not d.startswith('.')]

            for file in files:
                if os.path.splitext(file)[1] in EXTENSIONS:
                    total_files += 1

        if total_files > 0:
            display_name = category.replace('_', ' ')
            category_counts[display_name] = total_files

    return category_counts

def create_pie_chart(counts):
    os.makedirs(CHARTS_DIR, exist_ok=True)

    plt.style.use('dark_background')

    text_color = '#E6EDF3'
    bg_color = '#0D1117'

    plt.rcParams["font.family"] = "DejaVu Sans"
    plt.rcParams.update({
        'figure.facecolor': bg_color,
        'axes.facecolor': bg_color,
        'axes.edgecolor': bg_color,
        'text.color': text_color,
    })

    fig, ax = plt.subplots(figsize=(10, 7))

    pie_data = {k: v for k, v in counts.items() if v > 0}

    labels = list(pie_data.keys())
    values = list(pie_data.values())

    total = sum(values)

    colors = [
        "#58A6FF",  # Light Blue
        "#3FB950",  # Green
        "#F85149",  # Red
        "#D2A8FF",  # Light Purple
        "#FFA657",  # Orange
        "#F2CC60",  # Yellow
        "#FF69B4",  # Hot Pink
        "#00CED1",  # Dark Turquoise (Cyan)
        "#8B4513",  # Saddle Brown
        "#9ACD32",  # YellowGreen
        "#BA55D3",  # Medium Orchid (Magenta-ish)
        "#FF4500"   # Orange Red
    ][:len(values)]

    def autopct_format(pct):
        return f"{pct:.1f}%" if pct >= 4.5 else ""

    outside_labels = [f"{(v/sum(values)*100):.1f}%" if (v/sum(values)*100) < 4.5 else "" for v in values]

    wedges, texts, autotexts = ax.pie(
        values,
        labels=outside_labels,
        autopct=autopct_format,
        startangle=140,
        colors=colors,
        radius=0.9,   
        wedgeprops=dict(linewidth=0),
        pctdistance=0.7,
        rotatelabels=True,
        labeldistance=1.05
    )

    plt.setp(texts, size=9, weight="bold", color=text_color)
    plt.setp(autotexts, size=10, weight="bold", color="black")

    # Legend labels with count
    legend_labels = [
        f"[{values[i]}] {labels[i]}"
        for i in range(len(labels))
    ]

    legend = ax.legend(
        wedges,
        legend_labels,
        title="Categories",
        loc="center left",
        bbox_to_anchor=(0.95, 0.5),
        frameon=True,
        fontsize=10,
        title_fontsize=12
    )

    # Make legend text italic
    for text in legend.get_texts():
        text.set_style('italic')

    legend.get_title().set_fontweight("bold")

    ax.set_title(
        "Category Distribution",
        pad=20,
        fontsize=15,
        fontweight="bold",
        color=text_color
    )

    plt.tight_layout()

    plt.savefig(
        os.path.join(CHARTS_DIR, 'category_pie.svg'),
        format='svg',
        facecolor=fig.get_facecolor(),
        transparent=False
    )

    plt.close(fig)


def update_readme():
    counts = get_category_counts()
    counts = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))
    if not counts:
        print("No solutions found. Please make sure files end with .py, .cpp, or .java")
        return

    create_pie_chart(counts)
    print(f"Successfully generated dark category_pie.svg chart for {sum(counts.values())} problems across {len(counts)} categories.")

if __name__ == "__main__":
    update_readme()
