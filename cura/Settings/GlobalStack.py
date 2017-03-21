# Copyright (c) 2017 Ultimaker B.V.
# Cura is released under the terms of the AGPLv3 or higher.

from UM.MimeTypeDatabase import MimeType, MimeTypeDatabase
from UM.Settings.ContainerStack import ContainerStack
from UM.Settings.ContainerRegistry import ContainerRegistry

class CannotSetNextStackError(Exception):
    pass

class GlobalStack(ContainerStack):
    def __init__(self, container_id, *args, **kwargs):
        super().__init__(container_id, *args, **kwargs)

    def getProperty(self, key, property_name):
        if property_name == "value":
            resolve = super().getProperty(key, "resolve")
            if resolve:
                return resolve

        return super().getProperty(key, property_name)

    def setNextStack(self, next_stack):
        raise CannotSetNextStackError("Global stack cannot have a next stack!")

global_stack_mime = MimeType(
    name = "application/x-cura-globalstack",
    comment = "Cura Global Stack",
    suffixes = [ "global.cfg" ]
)

MimeTypeDatabase.addMimeType(global_stack_mime)
ContainerRegistry.addContainerTypeByName(GlobalStack, "global_stack", global_stack_mime.name)

class _ContainerIndexes:
    UserChanges = 0
    QualityChanges = 1
    Quality = 2
    Material = 3
    Variant = 4
    DefinitionChanges = 5
    Definition = 6

    # Simple hash map to map from index to "type" metadata entry
    IndexTypeMap = {
        UserChanges: "user",
        QualityChanges: "quality_changes",
        Quality: "quality",
        Material: "material",
        Variant: "variant",
        DefinitionChanges: "definition_changes",
        Definition: "definition",
    }
