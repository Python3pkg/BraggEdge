"""
This class will automatically retrieve the lattice parameter and the crystal structure of a given
element
"""
from python.braggedge.retrieve_metadata_table import RetrieveMetadataTable


class RetrieveMaterialMetadata(object):
    """ Retrieve the metadata for a given material """
    
    lattice = None
    crystal_structure = None
    
    def __init__(self, material=None):
        self._material = material
        self._retrieve_table()
        self._retrieve_metadata()
        
    def _retrieve_table(self):
        """retrieve the table using the url defined in the config file"""
        metadata_table = RetrieveMetadataTable()
        self.table = metadata_table.get_table()
        
    def _retrieve_metadata(self):
        """retrieve the metadata ('lattice constant','crystal structure')"""
        _metadata = self.table.loc[self._material]
        self._retrieve_lattice(_metadata)
        self._retrieve_crystal_structure(_metadata)
        
    def _retrieve_lattice(self, _metadata):
        self.lattice = float(_metadata[0])
        
    def _retrieve_crystal_structure(self, _metadata):
        _full_crystal_str = _metadata[1]
        if 'FCC' in _full_crystal_str:
            _crystal_str = 'FCC'
        elif 'BCC' in _full_crystal_str:
            _crystal_str = 'BCC'
        else:
            _crystal_str = ''
        self.crystal_structure = _crystal_str
    
    
if __name__ == "__main__":
    retrieve_material = RetrieveMaterialMetadata(material='Si')
    
        