import pandas as pd

class Json:
    def __init__(self, file):
        self._files = pd.DataFrame(columns = ["Name"            , "Location"                 , "Backup_Location"                 ] )
        self._files.loc[len(self._files)] =( ["game_settings"   , "data/game_settings.json"  , "data/game_settings_backup.json"  ] )

        self._files = self._files.set_index("Name").rename_axis(None)
        self.file = pd.read_json(self._files.at[file,"Location"],typ='series')

    def read(self, json_var):
        # throws error if doesnt exist
        return self.file[json_var]

    def write(self, json_var, new_value):
        # throws error if doesnt exist
        self.file[json_var]
        # write after checking
        self.file[json_var] = new_value

