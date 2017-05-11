from pyclassyfire import client
import os
import filecmp
data_dir = os.path.dirname(__file__)+'/test_data'
expected = {'csv': 'CompoundID,ChemOntID,ParentName\nQ595535-1,CHEMONTID:0002500,Alkanes\n',
            'json': '{"id":595535,"label":"curl_test","classification_status":"Done","invalid_entities":[],"entities":[{"identifier":"Q595535-1","smiles":"CCC","inchikey":"InChIKey=ATUOYWHBWRKTHZ-UHFFFAOYSA-N","kingdom":{"name":"Organic compounds","description":"Compounds that contain at least one carbon atom, excluding isocyanide/cyanide and their non-hydrocarbyl derivatives, thiophosgene, carbon diselenide, carbon monosulfide, carbon disulfide, carbon subsulfide, carbon monoxide, carbon dioxide, Carbon suboxide, and dicarbon monoxide.","chemont_id":"CHEMONTID:0000000","url":"http://classyfire.wishartlab.com/tax_nodes/C0000000"},"superclass":{"name":"Hydrocarbons","description":"Organic compounds made up only of carbon and hydrogen atoms.","chemont_id":"CHEMONTID:0002837","url":"http://classyfire.wishartlab.com/tax_nodes/C0002837"},"class":{"name":"Saturated hydrocarbons","description":"Hydrocarbons that contains only saturated carbon atoms, which are linked to one another through single bonds. These includes alkanes and cycloalkanes.","chemont_id":"CHEMONTID:0004474","url":"http://classyfire.wishartlab.com/tax_nodes/C0004474"},"subclass":{"name":"Alkanes","description":"Acyclic branched or unbranched hydrocarbons having the general formula CnH2n+2 , and therefore consisting entirely of hydrogen atoms and saturated carbon atoms.","chemont_id":"CHEMONTID:0002500","url":"http://classyfire.wishartlab.com/tax_nodes/C0002500"},"intermediate_nodes":[],"direct_parent":{"name":"Alkanes","description":"Acyclic branched or unbranched hydrocarbons having the general formula CnH2n+2 , and therefore consisting entirely of hydrogen atoms and saturated carbon atoms.","chemont_id":"CHEMONTID:0002500","url":"http://classyfire.wishartlab.com/tax_nodes/C0002500"},"alternative_parents":[],"molecular_framework":"Aliphatic acyclic compounds","substituents":["Acyclic alkane","Alkane","Aliphatic acyclic compound"],"description":"This compound belongs to the class of organic compounds known as alkanes. These are acyclic branched or unbranched hydrocarbons having the general formula CnH2n+2 , and therefore consisting entirely of hydrogen atoms and saturated carbon atoms.","external_descriptors":[{"source":"CHEBI","source_id":"CHEBI:32879","annotations":["alkane"]}],"predicted_chebi_terms":["chemical entity (CHEBI:24431)","hydrocarbon (CHEBI:24632)","alkane (CHEBI:18310)","organic molecule (CHEBI:72695)"],"predicted_lipidmaps_terms":[],"classification_version":"2.1"}]}',
            'sdf': 'Q595535-1\nMrv1568 12281606022D          \n\n  3  2  0  0  0  0            999 V2000\n    1.2375   -0.7145    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0\n    1.9520   -1.1270    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0\n    2.6664   -0.7145    0.0000 C   0  0  0  0  0  0  0  0  0  0  0  0\n  1  2  1  0  0  0  0\n  2  3  1  0  0  0  0\nM  END\n> <ID>\nQ595535-1\n> <InChIKey>\nInChIKey=ATUOYWHBWRKTHZ-UHFFFAOYSA-N\n> <Kingdom>\nOrganic compounds\n> <Superclass>\nHydrocarbons\n> <Class>\nSaturated hydrocarbons\n> <Subclass>\nAlkanes\n> <Intermediate Nodes>\n\n> <Direct Parent>\nAlkanes\n> <Alternative Parents>\n\n> <Molecular Framework>\nAliphatic acyclic compounds\n> <Structure-based description>\nThis compound belongs to the class of organic compounds known as alkanes. These are acyclic branched or unbranched hydrocarbons having the general formula CnH2n+2 , and therefore consisting entirely of hydrogen atoms and saturated carbon atoms.\n> <Ancestors>\nChemical entities\tOrganic compounds\tHydrocarbons\tSaturated hydrocarbons\tAlkanes\n$$$$\n'
            }


def test_structure_query():
    client.structure_query('CCC', 'smiles_test')
    client.structure_query('ATUOYWHBWRKTHZ-UHFFFAOYSA-N')


def test_get_results():
    assert client.get_results('595535', 'csv') == expected['csv']
    assert client.get_results('595535', 'json') == expected['json']
    assert client.get_results('595535', 'sdf') == expected['sdf']


def test_tabular_query():
    try:
        client.tabular_query(data_dir+'/tabulated_data.tsv', 'structure',
                             'excel-tab')
        assert filecmp.cmp(data_dir+'/tabulated_data_annotated.tsv',
                           data_dir+'/annotated.tsv')
    finally:
        os.remove(data_dir+'/tabulated_data_annotated.tsv')
