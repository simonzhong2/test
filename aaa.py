import pandas as pd
import random
import string


prescriber_profile=[]
for i in range(10000):
    prescriber_profile.append([''.join(random.sample(string.ascii_letters, 4)) for i in range(19)])

prescriber_profile=pd.DataFrame(prescriber_profile, columns=['hce_id_prfsnl','first_name','middle_name','last_name','gen_suffix','designation','gender','role','primary_spec','secondary_spec','tertiary_spec','primary_prof_code','primary_prof_desc','ims_id','upin','me','all_dea','npi','status_desc'])
prescriber_profile['prescriber_id']=[str(i) for i in range(10000)]
prescriber_profile['gender']=[random.choice(['F','M']) for i in range(10000)]
prescriber_profile.to_csv('D:/Canopy/Autoread/prescriber_profile.csv',index=False)