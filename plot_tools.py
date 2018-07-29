import tools

import plotly
import plotly.graph_objs as go
import datetime as dt

from plotly import tools
import plotly.plotly as py



def str_to_dt(str_date):
    split_str_date = str_date.split('-')
    year  = int( split_str_date[0] )
    month = int( split_str_date[1] )
    day   = int( split_str_date[2] )
    return dt.date(year, month, day)


def default_trace(name, x, y):
    trace = go.Scatter( name = name,
                        x    = x,
                        y    = y,
                        mode = 'lines+markers' )
    return trace

    
def build_trace_list(run_session_list):
    date_x     = []
    distance_y = []
    time_y     = []
    calories_y = []
    pace_y     = []
    
    for run_session in run_session_list:
        date_x     .append(str_to_dt(run_session.date))
        distance_y .append(run_session.distance_miles)
        time_y     .append(run_session.time_min)
        calories_y .append(run_session.calories)
        pace_y.append(run_session.pace)
    
    trace_list = [default_trace('Distance ( Miles )'      , date_x, distance_y),
                  default_trace('Time ( Minutes )   '     , date_x, time_y),
                  default_trace('Calories Burned'         , date_x, calories_y),
                  default_trace('Pace ( Miles / Minute )' , date_x, pace_y)]
    
    return trace_list  
    
    
    
def plot_all(title, filename, trace_list):    
#     trace1 = go.Scatter(x=[1, 2, 3], y=[4, 5, 6])
#     trace2 = go.Scatter(x=[20, 30, 40], y=[50, 60, 70])
#     trace3 = go.Scatter(x=[300, 400, 500], y=[600, 700, 800])
#     trace4 = go.Scatter(x=[4000, 5000, 6000], y=[7000, 8000, 9000])
    
    fig = tools.make_subplots(rows=2, cols=2, subplot_titles=('Plot 1', 'Plot 2',
                                                              'Plot 3', 'Plot 4'))
    
    fig.append_trace(trace_list[0], 1, 1)
    fig.append_trace(trace_list[1], 1, 2)
    fig.append_trace(trace_list[2], 2, 1)
    fig.append_trace(trace_list[3], 2, 2)
    
    fig['layout'].update(height=700, width=1500, title='Multiple Subplots' +
                                                      ' with Titles')
    
    plotly.offline.plot(fig, filename=filename, auto_open=True)
#     
#     
#     
#     
#     plotly.offline.plot({
#     "data": trace_list,#[go.Scatter(x=[dt.date(2018,1,4), dt.date(2018,1,5), dt.date(2018,1,1), dt.date(2018,1,10)], y=[4, 3, 2, 1])],#, go.Scatter(x=[12, 22, 32, 24], y=[4, 32, 22, 1])],
#     "layout": go.Layout(title=title),
#     }, auto_open=True, filename = filename)

    
    
    
    
import graph_data
if __name__ == '__main__':
    graph_data.main()   