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
        input = self.read_tcx_input(input_file_path)
        
        
    def read_tcx_input(self, input_file_path):
        run_vars = {'distance_miles': None,
                    'time_min'      : None,
                    'calories'      : None}
        
        raw_input = tools.read_text_file(input_file_path)
#         print (raw_input)#```````````````````````````````````````````````````````````````````````````````````````````
        
        #read backward from end to find the pos of total cals burned
        cal_line_num = len(raw_input) - 1
        while ('<Calories>' not in raw_input[cal_line_num]):
#             print(cal_line_num)#````````````````````````````````````````````````````````````````````````
            cal_line_num -= 1
#         cal_line_num += 1
        
        run_vars['calories'] = tools.extract_float_from_str(raw_input[cal_line_num])


        print(run_vars)

#             
#         i = 1
#         for line in raw_input:
#             print(str(i) + ':  ' + line)
#             i+=1
        
#         cal_line_num = 0
#         for rev_line_num in range( len(raw_input) ):
#             line_num = len(raw_input) - rev_line_num - 1
#             if '<Calories>' in raw_input[line_num]:
#                 cal_line_num = line_num
#                 break
        
        print(cal_line_num)
        
        







import graph_data
if __name__ == '__main__':
    graph_data.main()   