import arrow

from logger import txt_logger
import Run_Session
import tools
import plot_tools


ACTIVITIES_DIR_PATH = 'Takeout\Fit\Activities'
INPUT_FILE_EXTENTION = '.tcx'
GRAPH_TITLE = 'Running Stats'
GRAPH_FILENAME = 'graphs/Running_Stats' + arrow.now().format('YYYY-MM-DD') + '.html'

def main():
    print('working...')
    
    input_file_names = tools.file_names_in_dir(ACTIVITIES_DIR_PATH, INPUT_FILE_EXTENTION)
    
    run_session_list = []
    for input_file_name in input_file_names:
        input_file_path = ACTIVITIES_DIR_PATH + '\\' + input_file_name
        new_run_session = Run_Session.Run_Session(input_file_path)
        run_session_list.append(new_run_session)
    
    trace_list = plot_tools.build_trace_list(run_session_list)
    
    plot_tools.plot_all(GRAPH_TITLE, GRAPH_FILENAME, trace_list)
        
    print('done!')








if __name__ == '__main__':
    main()   