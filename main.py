import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use("Agg")   # Headless mode for saving files
import matplotlib.pyplot as plt


# 1. Load Employee Data
def load_employee_data(filename):
    """
    Load CSV dataset into a pandas DataFrame.
    """
    try:
        df = pd.read_csv(filename)
        print("Data loaded successfully.")
        return df
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return pd.DataFrame()


# 2. Plot Department Headcounts
def plot_department_counts(df):
    plt.figure(figsize=(10, 6))
    
    sns.countplot(x="Department", hue="Gender", data=df, palette="viridis")
    
    plt.title("Employee Count by Department")
    plt.xlabel("Department")
    plt.ylabel("Number of Employees")
    plt.legend(title="Gender")
    
    # Rotate labels by 45 degrees
    plt.xticks(rotation=45)
    
    output = "department_headcount.png"
    # Use bbox_inches='tight' to prevent cropping
    plt.savefig(output, bbox_inches='tight')
    print(f"Saved: {output}")


# 3. Plot Salary Distribution
def plot_salary_box(df):
    plt.figure(figsize=(10, 6))
    
    sns.boxplot(
        x="Department", 
        y="Salary", 
        data=df,
        legend=False
    )
    
    plt.title("Salary Distribution by Department")
    plt.xlabel("Department")
    plt.ylabel("Annual Salary ($)")
    
    # Rotate labels by 45 degrees
    plt.xticks(rotation=45)
    
    output = "salary_boxplot.png"
    # Use bbox_inches='tight' to prevent cropping
    plt.savefig(output, bbox_inches='tight')
    print(f"Saved: {output}")


# 4. Plot Employee Satisfaction
def plot_satisfaction_violin(df):
    plt.figure(figsize=(10, 6))
    
    sns.violinplot(
        x="Department",
        y="Satisfaction",
        hue="Gender",
        data=df,
        split=True,       
        palette="muted",
        inner="quart"      
    )
    
    plt.title("Employee Satisfaction Density (Male vs Female)")
    plt.xlabel("Department")
    plt.ylabel("Satisfaction Score (0-10)")
    plt.legend(title="Gender")
    
    # Rotate labels by 45 degrees
    plt.xticks(rotation=45)
    
    output = "satisfaction_violin.png"
    # Use bbox_inches='tight' to prevent cropping
    plt.savefig(output, bbox_inches='tight')
    print(f"Saved: {output}")


if __name__ == "__main__":
    file = "employees.csv"
    df = load_employee_data(file)

    if not df.empty:
        print(f"Total Employees: {len(df)}")

        # Who works here?
        print("\nGenerating Department Count Chart...")
        plot_department_counts(df)

        # How much do they make?
        print("\nGenerating Salary Box Plot...")
        plot_salary_box(df)

        # Are they happy?
        print("\nGenerating Satisfaction Violin Plot...")
        plot_satisfaction_violin(df)


