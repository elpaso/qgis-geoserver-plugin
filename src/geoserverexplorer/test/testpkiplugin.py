from geoserverexplorer.test import utils
from geoserverexplorer.test.pkicatalogtests import suite as pkiCatalogSuite
from geoserverexplorer.test.pkideletetests import suite as pkiDeleteSuite
from geoserverexplorer.test.pkidragdroptests import suite as pkiDragDropSuite
from geoserverexplorer.test.pkiguitests import suite as pkiGuiSuite
from geoserverexplorer.test.pkiowstests import suite as pkiOwsSuite

# Tests for the QGIS Tester plugin. To know more see
# https://github.com/boundlessgeo/qgis-tester-plugin

# Tests assume a standard Geoserver at localhost:8443 or GSHOSTNAME:GSPORT
# and 'Fra' for pki credentials (more in the geoserverexplorer.test.utils code)

def functionalTests():
    try:
        from qgistester.test import Test
    except:
        return []
  
    dragdropTest = Test("Verify dragging browser element into workspace")
    dragdropTest.addStep("Setting up pki auth context", lambda: utils.setUtilContext(pki=True))
    dragdropTest.addStep("Setting up catalog and explorer", utils.setUpCatalogAndExplorer)
    dragdropTest.addStep("Setting up test data project", utils.loadTestData)
    dragdropTest.addStep("Drag layer from browser 'Project home->qgis_plugin_test_pt1.shp' into\ntest_catalog->Workspaces->test_workspace")
    dragdropTest.addStep("Checking new layer", utils.checkNewLayer)
    dragdropTest.setCleanup(utils.clean)

    vectorRenderingTest = Test("Verify rendering of uploaded style")
    vectorRenderingTest.addStep("Setting up basic pki context", lambda: utils.setUtilContext(pki=True))
    vectorRenderingTest.addStep("Preparing data", utils.openAndUpload)
    vectorRenderingTest.addStep("Check that WMS layer is correctly rendered")
    vectorRenderingTest.setCleanup(utils.clean)

    return [dragdropTest, vectorRenderingTest]

def unitTests():
    _tests = []
    _tests.extend(pkiCatalogSuite())
    _tests.extend(pkiDeleteSuite())
    _tests.extend(pkiDragDropSuite())
    _tests.extend(pkiGuiSuite())
    _tests.extend(pkiOwsSuite())
    return _tests