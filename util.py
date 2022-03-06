import seaborn as sns
import matplotlib.pyplot as plt


def print_results(data, iteration):
    print("--- Runtime: %s seconds ---" % data["runtime"][iteration])
    print("--- CPU Usage: %.1f%% ---" % data["cpu_usage"][iteration])
    print("--- Memory Usage: %i GiB ---" % data["memory_usage"][iteration])
    print("--- Hard Drive Usage: %i GiB ---" % data["hard_drive_usage"][iteration])
    print("--- RSS: %i MiB ---" % data["rss"][iteration])
    print("--- VMS: %i GiB ---" % data["vms"][iteration])
    print("--- Page Faults: %i * 10^3 ---" % data["page_faults"][iteration])


def display_results(data, labels):
    fig, axs = plt.subplots(nrows=2, ncols=4)

    plt.style.use("seaborn")

    sns.barplot(x=labels, y=data["runtime"], ax=axs[0, 0]).set(title='Runtime (s)')
    sns.barplot(x=labels, y=data["cpu_usage"], ax=axs[0, 1]).set(title='CPU Usage (%)', ylim=(0, 100))
    sns.barplot(x=labels, y=data["memory_usage"], ax=axs[0, 2]).set(title='Memory Usage (GiB)')
    sns.barplot(x=labels, y=data["hard_drive_usage"], ax=axs[0, 3]).set(title='Hard Drive Usage (GiB)')

    sns.barplot(x=labels, y=data["rss"], ax=axs[1, 0]).set(title='RSS (MiB)')
    sns.barplot(x=labels, y=data["vms"], ax=axs[1, 1]).set(title='VMS (GiB)')
    sns.barplot(x=labels, y=data["page_faults"], ax=axs[1, 2]).set(title='Page Faults (10^3)')

    fig.delaxes(axs[1, 3])

    plt.show()
