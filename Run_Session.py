import tools


# oint>
#                 </Track>
#                 <DistanceMeters>3352.710985660553</DistanceMeters>
#                 <TotalTimeSeconds>1303.219</TotalTimeSeconds>
#                 <Calories>268.0570373535156</Calories>
#                 <Intensity>Active</Intensity>
#                 <TriggerMethod>Manual</TriggerMethod>
#             </Lap>
#         </Activity>
#     </Activities>
#     <Author xsi:type="Application_t">
#         <Name>Google Fit</Name>
#         <Build>
#             <Version>
#                 <VersionMajor>0</VersionMajor>
#                 <VersionMinor>0</VersionMinor>
#                 <BuildMajor>0</BuildMajor>
#                 <BuildMinor>0</BuildMinor>
#             </Version>
#         </Build>
#         <LangID>en</LangID>
#         <PartNumber>000-00000-00</PartNumber>
#     </Author>
# </TrainingCenterDatabase>

# 
# def read_text_file(file_path):
#     with open(file_path) as text_file:  # can throw FileNotFoundError
#         result = tuple(l.rstrip() for l in text_file.readlines())
#         return result



class Run_Session:
    def __init__(self, input_file_path):
        run_vars = self.read_tcx_input(input_file_path)
        
        self.date           = run_vars['date']
        self.distance_miles = run_vars['distance_miles']
        self.time_min       = run_vars['time_min']
        self.calories       = run_vars['calories']
        try:
            self.pace       = self.time_min / self.distance_miles
        except:
            self.pace       = 0
        
        
    def read_tcx_input(self, input_file_path):
        run_vars = {'date'          : None,
                    'distance_miles': None,
                    'time_min'      : None,
                    'calories'      : None}
        
        raw_input = tools.read_text_file(input_file_path)
        
        #read backward from end to find the pos of total cals burned
        cal_line_num = len(raw_input) - 1
        while ('<Calories>' not in raw_input[cal_line_num]):
            cal_line_num -= 1
        
        run_vars['calories']       = tools.extract_float_from_str(raw_input[cal_line_num])
        run_vars['time_min']       = tools.sec_to_min ( tools.extract_float_from_str(raw_input[cal_line_num - 1]) )
        run_vars['distance_miles'] = tools.meters_to_miles ( tools.extract_float_from_str(raw_input[cal_line_num - 2]) )
        run_vars['date']           = (raw_input[cal_line_num - 5])[30:40]
        
        return run_vars
        
        
    def print_data(self):
        print('  date:', self.date)
        print('    distance_miles:', self.distance_miles)
        print('    time_min:', self.time_min)
        print('    calories:', self.calories)
        







import graph_data
if __name__ == '__main__':
    graph_data.main()   