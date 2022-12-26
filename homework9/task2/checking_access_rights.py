from pathlib import Path
from telegram import Update

file_name = "admin.config"
relative_file_directory = Path(file_name)

def checking_access_rights(update: Update) -> bool:

    verification_criterion_1 = str(update.effective_user.first_name)
    
    verification_criterion_2 = str(update.effective_user.id)
    
    with open(relative_file_directory, 'r', encoding='utf-8') as data_from_file:
        
        data_for_pars = list()
        
        for line in data_from_file:
            data_for_pars.append(line)     
        
        for count in range(0, len(data_for_pars), 1):
            data_for_pars[count] = data_for_pars[count].replace('\n', '')
        
        resalt_data = list()

        for element in data_for_pars:
                resalt_data.append(element.split(";")[0])
                resalt_data.append(element.split(";")[1])
    
    if resalt_data.count(verification_criterion_1) >=1 \
        and resalt_data.count(verification_criterion_2) >=1:
        return True
    else:
        return False