# import required libraries and modules
import matplotlib.pyplot as plt
import numpy as np

# specify values for stacked bars
est_type = ["Academies (1,958)", "Local authority maintained schools (523)", "Free schools (109)",
            "Special schools (91)", "Independent Schools (3)"]
below_twenty = [2.09, 0, 0, 68.13, 0]
twenty_to_forty = [0.46, 0.19, 1.83, 26.37, 0]
forty_to_sixty = [15.73, 11.85, 17.43, 4.40, 0]
sixty_to_eighty = [56.64, 65.77, 54.13, 1.10, 33.33]
eighty_plus = [25.08, 22.18, 26.61, 0, 66.67]

y = np.arange(len(est_type))
width = 0.75

# plot stacked bar chart and show
plt.bar(est_type, below_twenty, width, label="<20%")
plt.bar(est_type, twenty_to_forty, width, bottom=below_twenty, label="20-40%")
plt.bar(est_type, forty_to_sixty, width, bottom=np.array(below_twenty) + np.array(twenty_to_forty),
        label="40-60%")
plt.bar(est_type, sixty_to_eighty, width, bottom=np.array(below_twenty) + np.array(twenty_to_forty) +
        np.array(forty_to_sixty), label="60-80%")
plt.bar(est_type, eighty_plus, width, bottom=np.array(below_twenty) + np.array(twenty_to_forty) +
        np.array(forty_to_sixty) + np.array(sixty_to_eighty), label=">80%")
plt.ylim(0, 100)
plt.xticks(est_type, rotation=45, ha='right')
plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1), borderaxespad=0.)
plt.ticklabel_format(style='plain', axis='y')
plt.title("GCSE pass rate by establishment type")
plt.xlabel("Establishment Type")
plt.ylabel("Percentage")

plt.show()
