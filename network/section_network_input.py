# Below import is correct to the Language Server but fail when the interpreter tries to run it
# from timepredictionslib.timepredictionslib.helpers.file_parser import FileParser 

# Below imports are correct when run by Python interpreter
from timepredictionslib.sectionnetwork.network_data_helper import NetworkDataHelper
from timepredictionslib.sectionnetwork.sections_creator import SectionsCreator
from timepredictionslib.sectionnetwork.section_info import SectionInfo
from timepredictionslib.sectionnetwork.section_file_info import SectionFileInfo
from timepredictionslib.helpers.file_parser import FileParser

if __name__ == "__main__":
    parser = FileParser()
    pass
