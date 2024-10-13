from typing import Any, Optional, List, Tuple, Dict, Union
from datetime import datetime
from GlyphsApp import (
    GSDocument,
    GSFontMaster,
    GSFontInfoValueLocalized,
    GSFontInfoValueSingle,
    GSMetric,
    GSInstance,
    GSGlyph,
    GSAxis,
    GSClass,
    GSFeature,
    GSFeaturePrefix,
    GSLayer,
    GSEditViewController,
)

class GSFont:
    # Properties
    parent: GSDocument
    masters: List[GSFontMaster]
    axes: List[GSAxis]
    properties: List[Union[GSFontInfoValueLocalized, GSFontInfoValueSingle]]
    stems: List[GSMetric]
    instances: List[GSInstance]
    glyphs: List[GSGlyph]
    classes: List[GSClass]
    features: List[GSFeature]
    featurePrefixes: List[GSFeaturePrefix]
    copyright: str
    copyrights: Dict[str, str]
    license: str
    licenses: Dict[str, str]
    designer: str
    designers: Dict[str, str]
    designerURL: str
    manufacturer: str
    manufacturers: Dict[str, str]
    manufacturerURL: str
    familyNames: Dict[str, str]
    trademark: str
    trademarks: Dict[str, str]
    sampleText: str
    sampleTexts: Dict[str, str]
    description: str
    descriptions: Dict[str, str]
    compatibleFullName: str
    compatibleFullNames: Dict[str, str]
    versionMajor: int
    versionMinor: int
    date: datetime
    familyName: str
    upm: int
    note: str
    kerning: Dict[str, Dict[str, float]]
    userData: Dict[str, Any]
    grid
    gridSubDivision
    gridLength
    keyboardIncrement
    keyboardIncrementBig
    keyboardIncrementHuge
    snapToObjects
    disablesNiceNames
    customParameters
    selection
    selectedLayers: List[GSLayer]
    selectedFontMaster: GSFontMaster
    masterIndex
    currentText
    tabs: List[GSEditViewController]
    fontView: GSFontViewController
    currentTab: GSEditViewController
    filepath: Optional[str]
    tool: str
    tools: List[str]
    appVersion: str

    # Initializer
    def __init__(self, path: Optional[str] = None) -> None: ...

    # Methods
    def save(self, path: Optional[str] = None) -> None: ...
    def close(self) -> None: ...
    def addGlyph(self, glyph: GSGlyph) -> None: ...
    def removeGlyph(self, glyph: GSGlyph) -> None: ...
    def getGlyph(self, name: str) -> Optional[GSGlyph]: ...
    def newGlyph(self, name: str) -> GSGlyph: ...
    def addMaster(self, master: GSFontMaster) -> None: ...
    def removeMaster(self, master: GSFontMaster) -> None: ...
    def addInstance(self, instance: GSInstance) -> None: ...
    def removeInstance(self, instance: GSInstance) -> None: ...
    def addFeature(self, feature: GSFeature) -> None: ...
    def removeFeature(self, feature: GSFeature) -> None: ...
    def addClass(self, class_: GSClass) -> None: ...
    def removeClass(self, class_: GSClass) -> None: ...
    def updateFeatures(self) -> None: ...
    def generate(
        self,
        format: int,
        path: Optional[str] = None,
        autoHint: bool = False,
        removeOverlap: bool = False,
    ) -> None: ...
    def tempPath(self) -> str: ...
    def export(
        self,
        extension: int,
        destinationPath: str,
        autoHint: bool = False,
        removeOverlap: bool = False,
        useProductionNames: bool = True,
    ) -> None: ...
    def __getitem__(self, name: str) -> GSGlyph: ...
    def __delitem__(self, name: str) -> None: ...

    # Selection methods
    def selectGlyph(self, glyph: GSGlyph) -> None: ...
    def deselectGlyph(self, glyph: GSGlyph) -> None: ...
    def selectLayer(self, layer: GSLayer) -> None: ...
    def deselectLayer(self, layer: GSLayer) -> None: ...

    # Kerning methods
    def setKerningForPair(
        self, fontMasterID: str, left: str, right: str, value: float
    ) -> None: ...
    def kerningForPair(self, fontMasterID: str, left: str, right: str) -> float: ...
    def removeKerningForPair(
        self, fontMasterID: str, left: str, right: str
    ) -> None: ...

    # Other utility methods
    def disableUpdateInterface(self) -> None: ...
    def enableUpdateInterface(self) -> None: ...
