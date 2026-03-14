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
        "#58A6FF",  # blue
        "#3FB950",  # green
        "#F85149",  # red
        "#D2A8FF",  # purple
        "#FFA657",  # orange
        "#79C0FF",  # light blue
        "#56D364",  # emerald
        "#FF7B72",  # coral
        "#B392F0",  # violet
        "#F2CC60",  # gold
        "#7EE787",  # mint
        "#A5D6FF"   # sky
    ][:len(values)]

    # Highlight most attempted
    explode = [0] * len(values)
    explode[values.index(max(values))] = 0.06

    def autopct_format(pct):
        return f"{pct:.1f}%" if pct > 4 else ""

    wedges, texts, autotexts = ax.pie(
        values,
        autopct=autopct_format,
        startangle=140,
        colors=colors,
        explode=explode,
        radius=0.9,   
        wedgeprops=dict(edgecolor=bg_color, linewidth=1.2),
        pctdistance=0.7
    )

    # Style percentages
    for autotext in autotexts:
        autotext.set_color("black")
        autotext.set_fontsize(10)
        autotext.set_fontweight("bold")

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
        bbox_to_anchor=(1.02, 0.5),
        frameon=False,
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

    os.makedirs(CHARTS_DIR, exist_ok=True)
    
    plt.style.use('dark_background')
    text_color = '#E0E0E0'
    bg_color = '#0D1117' 
    plt.rcParams["font.family"] = "DejaVu Sans"
    plt.rcParams.update({
        'figure.facecolor': bg_color,
        'axes.facecolor': bg_color,
        'axes.edgecolor': bg_color,
        'text.color': text_color,
    })

    fig, ax = plt.subplots(figsize=(9, 7))

    pie_data = {k: v for k, v in counts.items() if v > 0}
    values = list(pie_data.values())
    pie_labels = list(pie_data.keys())

    colors = [
        "#58A6FF", "#3FB950", "#F85149", "#D2A8FF",
        "#FFA657", "#A5D6FF", "#56D364", "#FF7B72",
        "#B392F0", "#F2CC60", "#7EE787", "#79C0FF"
    ][:len(values)]

    def my_autopct(pct):
        return ('%1.1f%%' % pct) if pct >= 4.5 else ''

    outside_labels = [('%1.1f%%' % (v/sum(values)*100)) if (v/sum(values)*100) < 4.5 else '' for v in values]

    wedges, texts, autotexts = ax.pie(
        values,
        labels=outside_labels,
        autopct=my_autopct,
        startangle=140,
        colors=colors,
        rotatelabels=True,
        labeldistance=1.05,
        wedgeprops=dict(edgecolor=bg_color)
    )

    plt.setp(texts, size=9, weight="bold", color=text_color)
    plt.setp(autotexts, size=10, weight="bold", color="black")

    ax.legend(
        wedges,
        pie_labels,
        title="Categories",
        loc="center left",
        bbox_to_anchor=(1, 0.5)
    )

    ax.set_title("Category Distribution", pad=20, fontsize=14, fontweight="bold", color=text_color)

    plt.tight_layout()
    plt.savefig(os.path.join(CHARTS_DIR, 'category_pie.svg'), format='svg', facecolor=fig.get_facecolor(), transparent=False)
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
