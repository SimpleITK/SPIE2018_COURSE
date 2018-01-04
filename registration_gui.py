import matplotlib.pyplot as plt

#
# Set of methods used for displaying the registration metric during the optimization. 
#

# Callback invoked when the StartEvent happens, sets up our new data.
def start_plot():
    global metric_values, multires_iterations, ax, fig
    fig, ax = plt.subplots(1,1, figsize=(8,4))

    metric_values = []
    multires_iterations = []
    plt.show()


# Callback invoked when the EndEvent happens, do cleanup of data and figure.
def end_plot():
    global metric_values, multires_iterations, ax, fig
    
    del metric_values
    del multires_iterations
    del ax
    del fig

# Callback invoked when the IterationEvent happens, update our data and display new figure.    
def plot_values(registration_method):
    global metric_values, multires_iterations, ax, fig
    
    metric_values.append(registration_method.GetMetricValue())  
    # Plot the similarity metric values
    ax.plot(metric_values, 'r')
    ax.plot(multires_iterations, [metric_values[index] for index in multires_iterations], 'b*')
    ax.set_xlabel('Iteration Number',fontsize=12)
    ax.set_ylabel('Metric Value',fontsize=12)
    fig.canvas.draw()
    
# Callback invoked when the sitkMultiResolutionIterationEvent happens, update the index into the 
# metric_values list. 
def update_multires_iterations():
    global metric_values, multires_iterations
    multires_iterations.append(len(metric_values))
