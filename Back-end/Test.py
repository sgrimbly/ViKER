import unittest
from ReadWriteARM import *
from ReadWriteEER import *
from Main import EERToARM

path_read_JSONtest = '../Documentation/Phase 4/Test Cases/JSONReadWrite/Original/'
path_write_JSONtest = '../Documentation/Phase 4/Test Cases/JSONReadWrite/Generated/'

path_read_ERtoARM = '../Documentation/Phase 4/Test Cases/ERtoARM/ER/'
path_write_ERtoARM = '../Documentation/Phase 4/Test Cases/ERtoARM/Generated/'
path_target_ERtoARM = '../Documentation/Phase 4/Test Cases/ERtoARM/ARM/'

path_read_ARMtoER = '../Documentation/Phase 4/Test Cases/ARMtoER/ARM/'
path_write_ARMtoER = '../Documentation/Phase 4/Test Cases/ARMtoER/Generated/'
path_target_ARMtoER  = '../Documentation/Phase 4/Test Cases/ARMtoER/ER/'

class HelperMethods():
    '''Helper methods needed for the functionality of unit tests in this file'''
    def filesEqual(f1_path, f2_path):
        with open(f1_path) as f1, open(f2_path) as f2:
            i = 0
            for l1, l2 in zip(f1,f2):
                if(l1 != l2):
                    print("Error in line "+str(i), l1, sep=": ")
                    return False
                i += 1
            return True

class TestReadWriteJSON(unittest.TestCase):
    '''Unit tests for the ReadWriteARM class'''

    # Test using terminal with 
    # python -m unittest Test.TestReadWriteJSON

    def test_readWriteARM_case_1(self):
        test_tag = "Case1_ARM.JSON"
        relations = readARM(path_read_JSONtest+test_tag)
        writeARM(path_write_JSONtest+test_tag, relations)
        assert(HelperMethods.filesEqual(path_read_JSONtest+test_tag, path_write_JSONtest+test_tag))
        print("JSON read/write ARM test case 1 passed.")

    def test_readWriteEER_case_1(self):
        test_tag = "Case1_EER.JSON"
        entities = readEER(path_read_JSONtest+test_tag)
        writeEER(path_write_JSONtest+test_tag, entities)
        assert(HelperMethods.filesEqual(path_read_JSONtest+test_tag, path_write_JSONtest+test_tag))
        print("JSON read/write ER test case 1 passed.")

    def test_readWriteARM_case_2(self):
        test_tag = "Case2_ARM.JSON"
        relations = readARM(path_read_JSONtest+test_tag)
        writeARM(path_write_JSONtest+test_tag, relations)
        assert(HelperMethods.filesEqual(path_read_JSONtest+test_tag, path_write_JSONtest+test_tag))
        print("JSON read/write ARM test case 2 passed.")

    def test_readWriteEER_case_2(self):
        test_tag = "Case2_EER.JSON"
        entities = readEER(path_read_JSONtest+test_tag)
        writeEER(path_write_JSONtest+test_tag, entities)
        assert(HelperMethods.filesEqual(path_read_JSONtest+test_tag, path_write_JSONtest+test_tag))
        print("JSON read/write ER test case 2 passed.")

    def test_readWriteARM_case_3(self):
        test_tag = "Case3_ARM.JSON"
        relations = readARM(path_read_JSONtest+test_tag)
        writeARM(path_write_JSONtest+test_tag, relations)
        assert(HelperMethods.filesEqual(path_read_JSONtest+test_tag, path_write_JSONtest+test_tag))
        print("JSON read/write ARM test case 3 passed.")

    def test_readWriteEER_case_3(self):
        test_tag = "Case3_EER.JSON"
        entities = readEER(path_read_JSONtest+test_tag)
        writeEER(path_write_JSONtest+test_tag, entities)
        assert(HelperMethods.filesEqual(path_read_JSONtest+test_tag, path_write_JSONtest+test_tag))
        print("JSON read/write ER test case 3 passed.")

    def test_readWriteARM_case_4(self):
        test_tag = "Case4_ARM.JSON"
        relations = readARM(path_read_JSONtest+test_tag)
        writeARM(path_write_JSONtest+test_tag, relations)
        assert(HelperMethods.filesEqual(path_read_JSONtest+test_tag, path_write_JSONtest+test_tag))
        print("JSON read/write ARM test case 4 passed.")

    def test_readWriteEER_case_4(self):
        test_tag = "Case4_EER.JSON"
        entities = readEER(path_read_JSONtest+test_tag)
        writeEER(path_write_JSONtest+test_tag, entities)
        assert(HelperMethods.filesEqual(path_read_JSONtest+test_tag, path_write_JSONtest+test_tag))
        print("JSON read/write ER test case 4 passed.")

    def test_readWriteARM_case_5(self):
        test_tag = "Case5_ARM.JSON"
        relations = readARM(path_read_JSONtest+test_tag)
        writeARM(path_write_JSONtest+test_tag, relations)
        assert(HelperMethods.filesEqual(path_read_JSONtest+test_tag, path_write_JSONtest+test_tag))
        print("JSON read/write ARM test case 5 passed.")

    def test_readWriteEER_case_5(self):
        test_tag = "Case5_EER.JSON"
        entities = readEER(path_read_JSONtest+test_tag)
        writeEER(path_write_JSONtest+test_tag, entities)
        assert(HelperMethods.filesEqual(path_read_JSONtest+test_tag, path_write_JSONtest+test_tag))
        print("JSON read/write ER test case 5 passed.")
    
class TestEERToARM(unittest.TestCase):
    # Run all test cases for ER -> ARM transformations

    # Test using terminal with 
    # python -m unittest Test.TestEERToARM

    def test_EERToARM_case_1(self):
        test_case_ER = "TestCase1_EER.JSON"
        test_case_ARM = "TestCase1_ARM.JSON"
        EERToARM(path_read_ERtoARM+test_case_ER, path_write_ERtoARM+test_case_ARM)
        assert(HelperMethods.filesEqual(path_write_ERtoARM+test_case_ARM, path_target_ERtoARM+test_case_ARM))
        print("Passed ER to ARM test case 1.")

    def test_EERToARM_case_2(self):
        test_case_ER = "TestCase2_EER.JSON"
        test_case_ARM = "TestCase2_ARM.JSON"
        EERToARM(path_read_ERtoARM+test_case_ER, path_write_ERtoARM+test_case_ARM)
        assert(HelperMethods.filesEqual(path_write_ERtoARM+test_case_ARM, path_target_ERtoARM+test_case_ARM))
        print("Passed ER to ARM test case 2.")

    def test_EERToARM_case_3(self):
        test_case_ER = "TestCase3_EER.JSON"
        test_case_ARM = "TestCase3_ARM.JSON"
        EERToARM(path_read_ERtoARM+test_case_ER, path_write_ERtoARM+test_case_ARM)
        assert(HelperMethods.filesEqual(path_write_ERtoARM+test_case_ARM, path_target_ERtoARM+test_case_ARM))
        print("Passed ER to ARM test case 3.")

    def test_EERToARM_case_4(self):
        test_case_ER = "TestCase4_EER.JSON"
        test_case_ARM = "TestCase4_ARM.JSON"
        EERToARM(path_read_ERtoARM+test_case_ER, path_write_ERtoARM+test_case_ARM)
        assert(HelperMethods.filesEqual(path_write_ERtoARM+test_case_ARM, path_target_ERtoARM+test_case_ARM))
        print("Passed ER to ARM test case 4.")

    def test_EERToARM_case_5(self):
        test_case_ER = "TestCase5_EER.JSON"
        test_case_ARM = "TestCase5_ARM.JSON"
        EERToARM(path_read_ERtoARM+test_case_ER, path_write_ERtoARM+test_case_ARM)
        assert(HelperMethods.filesEqual(path_write_ERtoARM+test_case_ARM, path_target_ERtoARM+test_case_ARM))
        print("Passed ER to ARM test case 5.")

class TestARMToER(unittest.TestCase):
    # Run all test cases for ARM -> ER transformations

    # Test using terminal with 
    # python -m unittest Test.TestARMToER

    def test_EERToARM_case_1(self):
        test_case_ER = "Case1_EER.JSON"
        test_case_ARM = "Case1_ARM.JSON"
        EERToARM(path_read_ARMtoER+test_case_ARM, path_write_ARMtoER+test_case_ER)

if __name__ == '__main__':
    unittest.main()