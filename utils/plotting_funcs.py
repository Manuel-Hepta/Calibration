import numpy as np
import matplotlib.pyplot as plt

def plot_condition_classes(
    condition_data,
    variables,
    labels,
    class_order,
    class_colors,
    condition,
    ax=None,
    gap_duration=20,
    cooling_flag_col='cooling_flag_2',
    time_index_col='time_index_2',
    yscale=1000,
    title_prefix="Voltage Measurements - Condition: ",
    ylabel="Voltage (V)"
):
    """
    Plot voltage or temperature variables for a given condition with class backgrounds and cooling flags.
    Args:
        condition_data (pd.DataFrame): Data for the condition.
        variables (list): List of variable names to plot.
        labels (dict): Mapping of variable names to labels.
        class_order (list): Ordered list of class names.
        class_colors (dict): Mapping of class names to colors.
        condition (str): Condition name for title.
        ax (matplotlib.axes.Axes, optional): Axis to plot on. If None, creates new figure.
        gap_duration (int): Gap between classes in time index.
        cooling_flag_col (str): Column name for cooling flag.
        time_index_col (str): Column name for time index.
        yscale (float): Scale for y-axis (e.g., 1000 for mV to V).
        title_prefix (str): Prefix for plot title.
        ylabel (str): Y-axis label.
    """


    # Get available classes for this condition in order
    available_classes = [cls for cls in class_order if cls in condition_data['class'].unique()]

    # Create new time index with gaps between classes
    condition_data = condition_data.copy()
    condition_data[time_index_col] = 0.0
    current_time = 0
    for class_name in available_classes:
        class_data = condition_data[condition_data['class'] == class_name].copy()
        if len(class_data) > 0:
            class_data = class_data.sort_values('time_index')
            duration = len(class_data)
            new_time_indices = np.arange(current_time, current_time + duration)
            mask = condition_data['class'] == class_name
            condition_data.loc[mask, time_index_col] = new_time_indices
            current_time += duration + gap_duration
    data_sorted = condition_data.sort_values(time_index_col)
    if ax is None:
        fig, ax = plt.subplots(figsize=(2 * len(available_classes)+3, 5))
    # Plot each variable
    for var in variables:
        ax.plot(data_sorted[time_index_col], data_sorted[var] / yscale, label=labels.get(var, var))
    # Add blue shaded dashed areas for cooling_flag == 1
    cooling_flag_data = data_sorted[data_sorted[cooling_flag_col] == 1]
    if len(cooling_flag_data) > 0:
        cooling_flag_data = cooling_flag_data.copy()
        cooling_flag_data['group'] = (cooling_flag_data[time_index_col].diff() > 1).cumsum()
        for group_id, group_data in cooling_flag_data.groupby('group'):
            start_time = group_data[time_index_col].min()
            end_time = group_data[time_index_col].max()
            ax.axvspan(start_time, end_time, alpha=0.1, color='blue', edgecolor='blue', linewidth=1.5, hatch="/", label='cooling_flag' if group_id == cooling_flag_data['group'].iloc[0] else "")
    # Add background colors and labels for each class
    for class_name in available_classes:
        class_data = condition_data[condition_data['class'] == class_name]
        if len(class_data) > 0:
            class_start = class_data[time_index_col].min()
            class_end = class_data[time_index_col].max()
            ax.axvspan(class_start, class_end, alpha=0.15, color=class_colors[class_name])
            class_center = (class_start + class_end) / 2
            ax.text(class_center, ax.get_ylim()[1] * 0.99, class_name, ha='center', va='top', fontweight='bold', rotation=45, bbox=dict(boxstyle='round,pad=0.3', facecolor=class_colors[class_name], alpha=0.3))
    ax.set_title(f"{title_prefix}{condition}")
    ax.set_xlabel("Time Index (s)")
    ax.set_ylabel(ylabel)
    ax.grid(True, alpha=0.3)
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    # Print summary for this condition
    print(f"\nCondition {condition} - Data summary by class:")
    for class_name in available_classes:
        class_data = condition_data[condition_data['class'] == class_name]
        if len(class_data) > 0:
            time_range = f"{class_data[time_index_col].min():.1f} - {class_data[time_index_col].max():.1f} s"
            print(f"  {class_name}: {len(class_data)} points, time range: {time_range}")
    plt.tight_layout()
    plt.show()

def plot_all_conditions(
    all_X_clean,
    variables,
    labels,
    class_order,
    class_colors,
    conditions=None,
    gap_duration=20,
    cooling_flag_col='cooling_flag_2',
    time_index_col='time_index_2',
    yscale=1000,
    title_prefix="Voltage Measurements - Condition: ",
    ylabel="Voltage (V)"
):
    """
    Plot all conditions in all_X_clean using plot_condition_classes, with one subplot per condition.
    Args:
        all_X_clean (pd.DataFrame): DataFrame containing all conditions/classes.
        variables, labels, class_order, class_colors: see plot_condition_classes.
        conditions (list, optional): List of conditions to plot. If None, uses all unique conditions.
        Other args: passed to plot_condition_classes.
    """
    import matplotlib.pyplot as plt
    if conditions is None:
        conditions = sorted(all_X_clean['condition'].unique())
        
    fig, axes = plt.subplots(len(conditions), 1, figsize=(2 * len(class_order)+3, 5*len(conditions)))
    if len(conditions) == 1:
        axes = [axes]
    for idx, condition in enumerate(conditions):
        ax = axes[idx]
        condition_data = all_X_clean[all_X_clean['condition'] == condition].copy()
        plot_condition_classes(
            condition_data,
            variables,
            labels,
            class_order,
            class_colors,
            condition,
            ax=ax,
            gap_duration=gap_duration,
            cooling_flag_col=cooling_flag_col,
            time_index_col=time_index_col,
            yscale=yscale,
            title_prefix=title_prefix,
            ylabel=ylabel
        )
    plt.tight_layout()
    plt.show()