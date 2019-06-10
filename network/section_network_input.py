# Below import is correct to the Language Server but fail when the interpreter tries to run it
# from samplelib.samplelib.helpers.file_parser import FileParser

# Below imports are correct when run by Python interpreter
from samplelib.sectionnetwork.network_data_helper import NetworkDataHelper
from samplelib.sectionnetwork.sections_creator import SectionsCreator
from samplelib.sectionnetwork.section_info import SectionInfo
from samplelib.sectionnetwork.section_file_info import SectionFileInfo
from samplelib.helpers.file_parser import FileParser

if __name__ == "__main__":
    parser = FileParser()
    pass
